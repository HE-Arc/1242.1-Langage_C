from datetime import datetime
from pathlib import Path
import queue
import re
import subprocess
import tempfile
import threading
import time
import tomllib
from xml.parsers.expat import errors
import argparse


INCLUDE_RE = re.compile(r'^\s*<!--\s*SNIPPET:INCLUDE\s+(.*?)\s*-->\s*$')

SNIPPET_BEGIN_RE = re.compile(r'^\s*//@\s*SNIPPET:BEGIN\s+([A-Za-z0-9_.-]+)\s*$')
SNIPPET_END_RE   = re.compile(r'^\s*//@\s*SNIPPET:END\s+([A-Za-z0-9_.-]+)\s*$')

SNIPPET_BLOCK_BEGIN_RE = re.compile(r'^\s*<!--\s*SNIPPET:BEGIN\s+(.*?)\s*-->\s*$')

SNIPPET_BLOCK_END_RE = re.compile(r'^\s*<!--\s*SNIPPET:END\s*-->\s*$')

# key=value pairs; the value is either a double-quoted string (with backslash
# escapes) or a bare token without spaces.
DIRECTIVE_PARAM_RE = re.compile(r'\s*([A-Za-z_]+)=(?:"((?:[^"\\]|\\.)*)"|([^\s"]+))')

SNIPPET_ID_RE = re.compile(r'^[A-Za-z0-9_.-]+$')

DIRECTIVE_KEYS = {"source_file", "id", "run", "stdin"}

GCC_FLAGS = ["-Wall", "-Wextra", "-std=c17"]
RUN_TIMEOUT_SECONDS = 5
# Silence on stdout/stderr after which the program is assumed to be waiting for input.
INPUT_QUIET_SECONDS = 0.3
RUN_FENCE_LANG = "terminal"
SOURCE_LABEL_FORMAT = "**Code source : `{source_file}`**"
RUN_LABEL = "**Compilation et exécution**"
RUN_INFO_FORMAT = '<p class="run-info">Compiled and executed on {date} from {commit}.</p>'

# Linked next to the example so that stdout is unbuffered even when piped,
# which lets the runner interleave echoed input with the program's output as
# a real terminal would. The example's own translation unit is untouched, so
# its diagnostics are exactly those of the displayed command.
UNBUFFERED_STDOUT_C = """#include <stdio.h>

__attribute__((constructor)) static void hugo_preprocessor_unbuffer_stdout(void)
{
	setvbuf(stdout, NULL, _IONBF, 0);
}
"""
UNBUFFERED_STDOUT_NAME = "hugo_preprocessor_unbuffered_stdout"


def decode_directive_string(value: str) -> str:
    escapes = {"n": "\n", "t": "\t", '"': '"', "\\": "\\"}
    out = []
    i = 0
    while i < len(value):
        c = value[i]
        if c == "\\" and i + 1 < len(value) and value[i + 1] in escapes:
            out.append(escapes[value[i + 1]])
            i += 2
            continue
        out.append(c)
        i += 1
    return "".join(out)


def encode_directive_string(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\t", "\\t")
    )


def parse_directive_params(text: str, where: str) -> dict:
    """Parse the `key=value ...` part of an INCLUDE or generated BEGIN directive."""
    raw = {}
    pos = 0
    while pos < len(text):
        m = DIRECTIVE_PARAM_RE.match(text, pos)
        if not m:
            raise RuntimeError(f"{where}: malformed snippet directive near '{text[pos:]}'")
        key = m.group(1)
        if key not in DIRECTIVE_KEYS:
            raise RuntimeError(f"{where}: unknown snippet directive parameter '{key}'")
        if key in raw:
            raise RuntimeError(f"{where}: duplicate snippet directive parameter '{key}'")
        quoted, bare = m.group(2), m.group(3)
        raw[key] = decode_directive_string(quoted) if quoted is not None else bare
        pos = m.end()

    for key in ("source_file", "id"):
        if key not in raw:
            raise RuntimeError(f"{where}: snippet directive is missing '{key}'")
    if not SNIPPET_ID_RE.match(raw["id"]):
        raise RuntimeError(f"{where}: invalid snippet id '{raw['id']}'")

    run = None
    if "run" in raw:
        if raw["run"] not in ("true", "false"):
            raise RuntimeError(f"{where}: 'run' must be true or false, got '{raw['run']}'")
        run = raw["run"] == "true"

    return {
        "source_file": raw["source_file"],
        "id": raw["id"],
        "run": run,
        "stdin": raw.get("stdin"),
    }


def format_directive_params(params: dict) -> str:
    parts = [f"source_file={params['source_file']}", f"id={params['id']}"]
    if params.get("run") is not None:
        parts.append(f"run={'true' if params['run'] else 'false'}")
    if params.get("stdin") is not None:
        parts.append(f'stdin="{encode_directive_string(params["stdin"])}"')
    return " ".join(parts)


def scan_markdown_for_includes(content_root: Path):
    includes = []

    for md_file in content_root.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8", errors="replace")
        lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")

        for lineno, line in enumerate(lines, start=1):
            m = INCLUDE_RE.match(line)
            if not m:
                continue

            params = parse_directive_params(m.group(1), f"{md_file}:{lineno}")

            includes.append({
                "md_file": md_file,
                "line": lineno,
                **params,
            })

    return includes

def load_snippet_paths(config_path: Path, repo_root: Path) -> list[Path]:
    data = tomllib.loads(config_path.read_text(encoding="utf-8"))

    if "snippets" not in data or "paths" not in data["snippets"]:
        raise RuntimeError("Invalid config: missing [snippets].paths")

    paths = []
    for p in data["snippets"]["paths"]:
        path = (repo_root / p).resolve()
        if not path.exists():
            raise RuntimeError(f"Snippet path does not exist: {path}")
        paths.append(path)

    return paths


def scan_files_for_snippets(paths):
    snippets = {}
    snippet_files = {}

    for root in paths:
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in (".c", ".h", ".cpp"):
                continue

            text = path.read_text(encoding="utf-8", errors="replace")
            lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")

            current_id = None
            buffer = []

            for lineno, line in enumerate(lines, start=1):
                m_begin = SNIPPET_BEGIN_RE.match(line)
                if m_begin:
                    if current_id is not None:
                        raise RuntimeError(
                            f"{path}:{lineno}: nested SNIPPET:BEGIN"
                        )
                    current_id = m_begin.group(1)
                    buffer = []
                    continue

                m_end = SNIPPET_END_RE.match(line)
                if m_end:
                    if current_id is None:
                        raise RuntimeError(
                            f"{path}:{lineno}: SNIPPET:END without BEGIN"
                        )
                    if m_end.group(1) != current_id:
                        raise RuntimeError(
                            f"{path}:{lineno}: SNIPPET:END id mismatch"
                        )

                    snippets.setdefault(path.name, {})[current_id] = "\n".join(buffer).rstrip()
                    snippet_files.setdefault(path.name, {})[current_id] = path
                    current_id = None
                    buffer = []
                    continue

                if current_id is not None:
                    buffer.append(line)

            if current_id is not None:
                raise RuntimeError(
                    f"{path}: EOF: missing SNIPPET:END for '{current_id}'"
                )

    return snippets, snippet_files


def git_head_for_file(path: Path) -> str:
    """Short HEAD hash of the repository containing the file."""
    try:
        head = subprocess.run(["git", "-C", str(path.parent), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True)
    except FileNotFoundError:
        return "unknown"
    commit = head.stdout.strip()
    return commit if head.returncode == 0 and commit else "unknown"

def check_includes_against_snippets(includes, snippets):
    errors = 0

    for inc in includes:
        src = inc["source_file"]
        sid = inc["id"]
        md_file = inc["md_file"]
        line = inc["line"]

        if src not in snippets:
            print(
                f"{md_file}:{line}: error: undefined snippet file '{src}'"
            )
            errors += 1
            continue

        if sid not in snippets[src]:
            print(
                f"{md_file}:{line}: error: undefined snippet '{sid}' in file '{src}'"
            )
            errors += 1
            continue

        if inc["run"] and Path(src).suffix.lower() != ".c":
            print(
                f"{md_file}:{line}: error: run=true requires a .c source file, got '{src}'"
            )
            errors += 1

    return errors


def normalize_process_output(text) -> str:
    if text is None:
        return ""
    if isinstance(text, bytes):
        text = text.decode("utf-8", errors="replace")
    return text.replace("\r\n", "\n").replace("\r", "\n").rstrip()


def run_with_echoed_input(exe_path: Path, cwd: Path, stdin_text, timeout: float) -> tuple[str, bool]:
    """Run the binary and return (transcript, timed_out).

    stdout and stderr are merged. Input lines are fed one at a time, each one
    as soon as the program has been silent for INPUT_QUIET_SECONDS (i.e. is
    presumably waiting on a read), and echoed into the transcript like a
    terminal would.
    """
    pending = []
    if stdin_text:
        if not stdin_text.endswith("\n"):
            stdin_text += "\n"
        pending = stdin_text.splitlines(keepends=True)

    proc = subprocess.Popen(
        [str(exe_path)],
        cwd=cwd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    chunks = queue.Queue()

    def pump_output():
        while True:
            data = proc.stdout.read1(4096)
            if not data:
                break
            chunks.put(data)
        chunks.put(None)

    threading.Thread(target=pump_output, daemon=True).start()

    def feed_next_line():
        nonlocal pending
        line = pending.pop(0)
        transcript.append(line.encode("utf-8"))
        try:
            proc.stdin.write(line.encode("utf-8"))
            proc.stdin.flush()
        except OSError:
            pending = []
        if not pending:
            try:
                proc.stdin.close()
            except OSError:
                pass

    transcript = []
    if not pending:
        proc.stdin.close()

    deadline = time.monotonic() + timeout
    timed_out = False
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            timed_out = True
            break
        wait = min(remaining, INPUT_QUIET_SECONDS) if pending else remaining
        try:
            data = chunks.get(timeout=wait)
        except queue.Empty:
            if pending:
                feed_next_line()
                continue
            timed_out = True
            break
        if data is None:
            break
        transcript.append(data)

    if timed_out:
        proc.kill()
    proc.wait()

    while True:
        try:
            data = chunks.get(timeout=0.2)
        except queue.Empty:
            break
        if data is None:
            break
        transcript.append(data)

    return b"".join(transcript).decode("utf-8", errors="replace"), timed_out


def compile_and_run_snippet(source_file: str, code: str, stdin_text) -> str:
    """Compile and run the snippet in a temporary directory, return the console transcript."""
    exe_name = f"{Path(source_file).stem}.exe"
    transcript = [f"$ gcc {' '.join(GCC_FLAGS)} -o {exe_name} {source_file}"]

    with tempfile.TemporaryDirectory(prefix="hugo_preprocessor_", ignore_cleanup_errors=True) as tmp:
        tmp_dir = Path(tmp)
        (tmp_dir / source_file).write_text(code + "\n", encoding="utf-8", newline="\n")

        support_c = f"{UNBUFFERED_STDOUT_NAME}.c"
        support_o = f"{UNBUFFERED_STDOUT_NAME}.o"
        (tmp_dir / support_c).write_text(UNBUFFERED_STDOUT_C, encoding="utf-8", newline="\n")

        try:
            support = subprocess.run(
                ["gcc", "-c", "-o", support_o, support_c],
                cwd=tmp_dir,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
        except FileNotFoundError:
            raise RuntimeError("gcc not found in PATH: required for run=true directives")
        if support.returncode != 0:
            raise RuntimeError(f"failed to build runner support object:\n{support.stderr}")

        compilation = subprocess.run(
            ["gcc", *GCC_FLAGS, "-fdiagnostics-color=never", "-o", exe_name, source_file, support_o],
            cwd=tmp_dir,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        compile_output = normalize_process_output(compilation.stdout + compilation.stderr)
        if compile_output:
            transcript.append(compile_output)

        if compilation.returncode != 0:
            return "\n".join(transcript)

        transcript.append(f"$ ./{exe_name}")
        run_output, timed_out = run_with_echoed_input(
            tmp_dir / exe_name, tmp_dir, stdin_text, RUN_TIMEOUT_SECONDS
        )
        run_output = normalize_process_output(run_output)
        if timed_out:
            timeout_note = f"[timeout: execution killed after {RUN_TIMEOUT_SECONDS} s]"
            run_output = f"{run_output}\n{timeout_note}" if run_output else timeout_note

        if run_output:
            transcript.append(run_output)

    return "\n".join(transcript)


def replace_includes_in_markdown(md_path, snippets, snippet_files, run_cache):
    original = md_path.read_text(encoding="utf-8", errors="replace")
    lines = original.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    # Step 1: normalize
    lines = normalize_generated_blocks_to_includes(lines, md_path)

    out = []
    modified = False

    for lineno, line in enumerate(lines, start=1):
        m = INCLUDE_RE.match(line)
        if not m:
            out.append(line)
            continue

        params = parse_directive_params(m.group(1), f"{md_path}:{lineno}")
        source_file = params["source_file"]
        snippet_id = params["id"]

        content = snippets[source_file][snippet_id]

        block = [
            f"<!-- SNIPPET:BEGIN {format_directive_params(params)} -->",
            "<!--",
            "  GENERATED FILE — DO NOT EDIT.",
            "  This block is automatically regenerated.",
            "-->",
            SOURCE_LABEL_FORMAT.format(source_file=source_file),
            "",
            "```c",
            content,
            "```",
        ]

        if params["run"]:
            cache_key = (source_file, snippet_id, params["stdin"])
            if cache_key not in run_cache:
                print(f"run: {source_file} ({snippet_id})")
                run_cache[cache_key] = compile_and_run_snippet(source_file, content, params["stdin"])
            run_info = RUN_INFO_FORMAT.format(
                date=datetime.now().strftime("%Y-%m-%d %H:%M"),
                commit=git_head_for_file(snippet_files[source_file][snippet_id]),
            )
            block.extend([
                "",
                RUN_LABEL,
                "",
                f"```{RUN_FENCE_LANG}",
                run_cache[cache_key],
                "```",
                run_info,
            ])

        block.append("<!-- SNIPPET:END -->")

        out.extend(block)
        modified = True

    new_text = "\n".join(out)

    # Force LF output, only write if changed
    normalized_original = original.replace("\r\n", "\n").replace("\r", "\n")
    if new_text != normalized_original:
        md_path.write_text(new_text, encoding="utf-8", newline="\n")
        return True

    return False

def remove_generated_snippet_blocks(lines):
    out = []
    inside = False

    for line in lines:
        if SNIPPET_BLOCK_BEGIN_RE.match(line):
            inside = True
            continue

        if inside:
            if SNIPPET_BLOCK_END_RE.match(line):
                inside = False
            continue

        out.append(line)

    if inside:
        raise RuntimeError("Unclosed SNIPPET:BEGIN block in markdown")

    return out

def normalize_generated_blocks_to_includes(lines, md_path=None):
    out = []
    i = 0

    while i < len(lines):
        line = lines[i]
        m = SNIPPET_BLOCK_BEGIN_RE.match(line)
        if not m:
            out.append(line)
            i += 1
            continue

        params = parse_directive_params(m.group(1), f"{md_path}:{i + 1}")

        # Skip until END
        j = i + 1
        while j < len(lines) and not SNIPPET_BLOCK_END_RE.match(lines[j]):
            j += 1
        if j >= len(lines):
            raise RuntimeError("Unclosed SNIPPET:BEGIN block in markdown (missing SNIPPET:END)")

        out.append(f"<!-- SNIPPET:INCLUDE {format_directive_params(params)} -->")
        i = j + 1

    return out


def main():
    import argparse

    repo_root = Path(__file__).resolve().parent.parent
    content_root = repo_root / "content"

    parser = argparse.ArgumentParser(prog="hugo_preprocessor.py")
    parser.add_argument(
        "command",
        nargs="?",
        choices=["scan", "clean", "replace"],
        help="scan | clean | replace (default: clean + scan + replace)",
    )
    args = parser.parse_args()

    if not content_root.exists():
        raise RuntimeError(f"content/ directory not found at {content_root}")

    def do_clean():
        modified = 0
        for md_file in content_root.rglob("*.md"):
            original = md_file.read_text(encoding="utf-8", errors="replace")
            norm = original.replace("\r\n", "\n").replace("\r", "\n")
            lines = norm.split("\n")

            new_lines = normalize_generated_blocks_to_includes(lines, md_file)
            new_text = "\n".join(new_lines)

            if new_text != norm:
                md_file.write_text(new_text, encoding="utf-8", newline="\n")
                modified += 1

        print(f"\nMarkdown files cleaned: {modified}")

    def do_scan_and_load():
        includes = scan_markdown_for_includes(content_root)

        config_path = repo_root / "tools" / "hugo_preprocessor.toml"
        snippet_paths = load_snippet_paths(config_path, repo_root)
        snippet_paths = [p.resolve() for p in snippet_paths if p.exists()]
        c_snippets, c_snippet_files = scan_files_for_snippets(snippet_paths)

        errors = check_includes_against_snippets(includes, c_snippets)
        if errors > 0:
            print(f"\n{errors} error(s) generated.")
            raise SystemExit(1)

        return includes, c_snippets, c_snippet_files

    def do_replace(includes, c_snippets, c_snippet_files):
        modified = 0
        seen = set()
        run_cache = {}
        for inc in includes:
            md = inc["md_file"]
            if md in seen:
                continue
            seen.add(md)
            if replace_includes_in_markdown(md, c_snippets, c_snippet_files, run_cache):
                modified += 1

        print(f"\nMarkdown files updated: {modified}")

    # ---------- dispatch ----------
    if args.command is None:
        # Default: clean -> scan -> replace
        do_clean()
        includes, c_snippets, c_snippet_files = do_scan_and_load()
        do_replace(includes, c_snippets, c_snippet_files)
        return

    if args.command == "clean":
        do_clean()
        return

    if args.command == "scan":
        includes, c_snippets, _ = do_scan_and_load()
        print(f"\nIncludes found: {len(includes)}")
        print(f"Snippet files indexed: {len(c_snippets)}")
        return

    if args.command == "replace":
        includes, c_snippets, c_snippet_files = do_scan_and_load()
        do_replace(includes, c_snippets, c_snippet_files)
        return


if __name__ == "__main__":
    main()
