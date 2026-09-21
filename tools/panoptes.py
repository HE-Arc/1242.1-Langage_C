"""Regenerate snippet blocks on change and run `hugo server`.

    python tools/panoptes.py [hugo server arguments...]

The site opens in the default browser once the server is up.

Snippet sources (tools/hugo_preprocessor.toml) and content/**/*.md are polled;
a changed source regenerates only the pages including it, a changed page is
regenerated alone. Compilation results are cached per snippet content, so a
page edit never recompiles an unchanged example.
"""
import shutil
import subprocess
import sys
import time
from pathlib import Path

import hugo_preprocessor as hp

POLL_SECONDS = 0.5
SETTLE_SECONDS = 0.3
SOURCE_EXTENSIONS = (".c", ".h", ".cpp")


def log(message):
    print(f"[panoptes] {message}", flush=True)


def snapshot(source_roots, content_root):
    files = {}
    for root in source_roots:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in SOURCE_EXTENSIONS:
                files[path] = path.stat().st_mtime_ns
    for path in content_root.rglob("*.md"):
        files[path] = path.stat().st_mtime_ns
    return files


def changed_paths(before, after):
    return {path for path in before.keys() | after.keys() if before.get(path) != after.get(path)}


def settled_snapshot(source_roots, content_root, current):
    """Wait until no file has changed for SETTLE_SECONDS (editors write in bursts)."""
    while True:
        time.sleep(SETTLE_SECONDS)
        again = snapshot(source_roots, content_root)
        if again == current:
            return current
        current = again


def regenerate(repo_root, content_root, run_cache, changed=None):
    """Regenerate the pages affected by `changed` (every page when None)."""
    try:
        includes, snippets, snippet_files, invalid = hp.scan_and_load(repo_root, content_root, strict=False)
    except Exception as e:
        log(f"error: {e}")
        return []

    if changed is None:
        affected = list(dict.fromkeys(inc["md_file"] for inc in includes))
    else:
        changed_sources = {path.name for path in changed if path.suffix.lower() in SOURCE_EXTENSIONS}
        affected = list(dict.fromkeys(
            inc["md_file"] for inc in includes
            if inc["md_file"] in changed or inc["source_file"] in changed_sources
        ))

    written = []
    for md in affected:
        if md in invalid:
            continue
        try:
            if hp.replace_includes_in_markdown(md, snippets, snippet_files, run_cache):
                written.append(md)
                log(f"updated {md.relative_to(repo_root)}")
        except Exception as e:
            log(f"error: {md.relative_to(repo_root)}: {e}")
    return written


def main():
    hugo = shutil.which("hugo")
    if hugo is None:
        log("hugo not found in PATH")
        return 1

    repo_root, content_root = hp.repo_paths()
    source_roots = hp.configured_snippet_paths(repo_root)
    run_cache = {}

    log("initial pass")
    regenerate(repo_root, content_root, run_cache)
    baseline = snapshot(source_roots, content_root)
    for root in source_roots:
        log(f"watching {root}")
    log(f"watching {content_root}")

    server = subprocess.Popen([hugo, "server", "--openBrowser", *sys.argv[1:]], cwd=repo_root)
    try:
        while server.poll() is None:
            time.sleep(POLL_SECONDS)
            current = snapshot(source_roots, content_root)
            changed = changed_paths(baseline, current)
            if not changed:
                continue

            current = settled_snapshot(source_roots, content_root, current)
            changed = changed_paths(baseline, current)
            for path in sorted(changed):
                log(f"changed {path.name}")

            written = regenerate(repo_root, content_root, run_cache, changed)
            baseline = current
            for md in written:
                baseline[md] = md.stat().st_mtime_ns
    except KeyboardInterrupt:
        pass
    finally:
        if server.poll() is None:
            server.terminate()
            try:
                server.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server.kill()
    return server.returncode or 0


if __name__ == "__main__":
    raise SystemExit(main())
