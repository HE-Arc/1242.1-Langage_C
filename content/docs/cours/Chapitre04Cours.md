---
title: "4 - Entrées-sorties"
weight: 1
---

# CHAPITRE 4 : entrées-sorties
## Cours
[1242.1.04_Entrees-Sorties](/pdf/1242.1.04_Entrees-Sorties.pdf)

## Squelette à remplir

```c
#include <stdio.h>

// CHAPTER 4

int main(void)
{
	// Experiment with printf and different types and formats

	// Experiment with %[L][.P]

	// Experiment with escape characters

	// Experiment with scanf and different types and formats

	// Experiment with scanf and separators

	// Experiment with scanf for 2 or more characters

	// Experiment with scanf and return status

	// Experiment with scanf and buffer (last example in the course)

	return 0;
}
```

## Quiz
[QUIZ SUR LES ENTRÉES - SORTIES (~10')](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=761445)

# EXERCICES

## Exercice 1
Créer un programme C avec l'instruction **`printf`**, qui produit l'affichage suivant :

```
Initials: __
Code: __


Birthdate: __/__/__
Number: __\__
Text: "____"
```

{{< hint danger >}}
**ATTENTION :** l'affichage doit se terminer par un retour à la ligne.
{{< /hint >}}

## Exercice 2
Créer un programme C demandant à l'utilisateur d'entrer 3 lettres.
Le programme doit fournir en résultat les codes ASCII des 3 lettres saisies.
L'utilisateur doit pouvoir entrer les lettres soit l'une à la suite de l'autre, soit en les séparant par un retour de chariot **`<CR>`**.

**L'affichage doit se présenter ainsi :**

```


Please enter 3 letters:
a b c

Here are the corresponding ASCII codes:
a--------->97
b--------->98
c--------->99
```

{{< hint danger >}}
**ATTENTION :** l'affichage doit commencer par 2 retours à la ligne et se terminer par un retour à la ligne.
{{< /hint >}}

## Exercice 3
Écrire un programme qui calcule la surface d'un cercle lorsqu'on introduit la valeur du rayon.
Le résultat sera affiché avec 2 chiffres significatifs (après le point).

**L'affichage doit se présenter ainsi :**

```
Circle radius: 1
pi = 3.141593
Circle surface = 3.14
```

{{< hint danger >}}
**ATTENTION :** l'affichage doit se terminer par un retour à la ligne.
{{< /hint >}}

## [TRÈS AVANCÉ] Exercice 4
Faire un programme qui récupère en continu les caractères saisis au clavier (sans **`<enter>`**) pour déplacer un symbole **`*`** à travers l’écran.
Si le symbole dépasse un des bords, il réapparait de l’autre coté.
Pour effacer l’écran, on peut utiliser une commande système **`cls`** par exemple.
