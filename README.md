# 1242.1 Langage C : site du cours

Site statique Hugo publié sur https://he-arc.github.io/1242.1-Langage_C/. Le contenu est dans `content/docs/cours/`, une page `ChapitreNNCours.md` et une page `ChapitreNNSolutions.md` par chapitre.

## Prérequis

- Hugo *extended*.
- Python 3.11 ou plus récent (le préprocesseur utilise `tomllib`).
- `gcc` dans le `PATH` (MSYS2 UCRT64), utilisé pour compiler et exécuter les exemples marqués `run=true`.
- Le repo `1242.1-Langage_C-Profs` cloné à côté de celui-ci : les chemins de `tools/hugo_preprocessor.toml` sont relatifs (`../1242.1-Langage_C-Profs/...`).

## Travail au quotidien : `panoptes`

```
python tools/panoptes.py [arguments de hugo server]
```

`panoptes` fait une passe complète du préprocesseur, puis lance `hugo server` avec les arguments fournis (par exemple `-D` pour voir les pages en `draft`). Tant que le serveur tourne, il surveille :

- les sources de snippets listées dans `tools/hugo_preprocessor.toml` (`.c`, `.h`, `.cpp`) ;
- les pages `content/**/*.md`.

Quand un fichier change, seules les pages concernées sont régénérées : une source modifiée régénère les pages qui l'incluent, une page modifiée est régénérée seule. Les résultats de compilation sont mis en cache par contenu de snippet, donc éditer une page ne recompile pas un exemple inchangé. Hugo recharge ensuite le navigateur comme d'habitude. `Ctrl+C` arrête le serveur et la surveillance.

## Le préprocesseur seul

```
python tools/hugo_preprocessor.py            # scan + replace
python tools/hugo_preprocessor.py scan       # vérifie les inclusions et les snippets, n'écrit rien
python tools/hugo_preprocessor.py clean      # ramène les blocs générés à leurs placeholders
python tools/hugo_preprocessor.py replace    # remplace les placeholders par le code
```

Les blocs générés sont **commités** : le CI ne lance pas le préprocesseur. La ligne `run-info` (date et commit) d'un bloc n'est réécrite que si le code, la commande ou la sortie ont changé, donc relancer le script sans modification ne touche aucun fichier.

## Inclure un snippet dans une page

Dans un fichier `.md`, un placeholder sur sa propre ligne :

```
<!-- SNIPPET:INCLUDE source_file=hello.c id=1242.1_Exemples_01.01_Hello_World_hello.c -->
```

Paramètres :

| Paramètre | Rôle |
|---|---|
| `source_file` | nom du fichier affiché dans le libellé `**Code source : `hello.c`**`, généré par le script, à ne pas écrire à la main |
| `id` | identifiant du snippet, voir ci-dessous |
| `run=true` | compile et exécute le snippet avec `gcc -Wall -Wextra -Wpedantic -Werror -std=c23`, puis ajoute un libellé `**Compilation et exécution**` et un bloc `terminal` avec la commande et la sortie |
| `stdin="..."` | entrée standard fournie au programme pour `run=true` ; `\n` sépare les lignes, `\"` et `\\` s'échappent |

Forme générale avec exécution et entrée clavier (identifiant à adapter) :

```
<!-- SNIPPET:INCLUDE source_file=main.c id=1242.1_Exemples_NN.MM_Dossier_main.c run=true stdin="12\n34\n" -->
```

Le script remplace le placeholder par un bloc délimité par `<!-- SNIPPET:BEGIN ... -->` et `<!-- SNIPPET:END -->`. Ne pas éditer l'intérieur de ce bloc : il est régénéré. Pour changer un paramètre, modifier la ligne `SNIPPET:BEGIN` qui reprend les paramètres de l'inclusion.

Conventions de page (voir `CLAUDE.md`) : slides, squelette à remplir, exemples, exercices. Les exemples vont sur la page de cours, jamais sur la page de solutions.

## Marquer un snippet dans un fichier `.c`

Dans le repo Profs, entourer le fichier entier ou une région :

```c
//@ SNIPPET:BEGIN 1242.1_Exemples_01.01_Hello_World_hello.c
#include <stdio.h>

int main(void)
{
	printf("hello, world\n");

	return 0;
}
//@ SNIPPET:END 1242.1_Exemples_01.01_Hello_World_hello.c
```

- Les deux balises sont sur leur propre ligne, avec le même identifiant.
- Identifiant : `1242.1_<Exemples|Exercices|Skeletons>_<chapitre.numéro>_<dossier>_<fichier>`. Il doit être unique dans tous les dossiers scannés.
- Dossiers scannés : `tools/hugo_preprocessor.toml`, section `[snippets]`. Par défaut `Exemples`, `Exercices` et `Skeletons` du repo Profs, plus `static/snippets` de ce repo pour les rares sources qui n'ont pas leur place dans Profs.
- Le repo Profs fait foi : corriger le code là-bas, puis relancer `panoptes` ou le préprocesseur ici.
- Un snippet inclus avec `run=true` doit compiler sans warning avec la commande ci-dessus, se terminer seul en moins de 5 secondes et ne lire que l'entrée fournie par `stdin`.
