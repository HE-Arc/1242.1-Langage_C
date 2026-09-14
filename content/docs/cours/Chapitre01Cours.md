---
title: "1. Introduction"
weight: 1
---

# CHAPITRE 1 : INTRODUCTION

## Slides
{{<slides "https://he-arc.github.io/1242.1-Langage_C-SLIDES/01_Introduction.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.1-Langage_C-SLIDES/01_Introduction.html?print-pdf)

## Squelette
{{<a_faire>}}
Remplir le squelette suivant au fur et à mesure du cours.
{{</a_faire>}}
<!-- SNIPPET:BEGIN source_file=chap1.c id=1242.1_Skeletons_01_chap1.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `chap1.c`**

```c
// CHAPTER 1

int main(void)
{

	return 0;
}
```
<!-- SNIPPET:END -->


## Exemples

### 01.01 : comment compiler et exécuter un programme C ?
<!-- SNIPPET:BEGIN source_file=hello.c id=1242.1_Exemples_01.01_Hello_World_hello.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `hello.c`**

```c
#include <stdio.h>

int main(void)
{
	printf("hello, world\n");

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o hello.exe hello.c
$ ./hello.exe
hello, world
```
<p class="run-info">Compiled and executed on 2026-09-14 13:09 from b493ffe.</p>
<!-- SNIPPET:END -->

### 01.01b : comment déclarer des variables et afficher le résultat d'un calcul ?
<!-- SNIPPET:BEGIN source_file=add.c id=1242.1_Exemples_01.01b_Add_add.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `add.c`**

```c
#include <stdio.h>

int main(void)
{
	int a = 10;
	int b = 5;
	printf("%d\n", a + b);
	
	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o add.exe add.c
$ ./add.exe
15
```
<p class="run-info">Compiled and executed on 2026-09-14 18:38 from a060919.</p>
<!-- SNIPPET:END -->

## Exercices

### Contexte
Soit le programme **`Hello_World`** pour  voir les éléments d'un programme écrit en C :

<!-- SNIPPET:BEGIN source_file=hello.c id=1242.1_Exemples_01.01_Hello_World_hello.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `hello.c`**

```c
#include <stdio.h>

int main(void)
{
	printf("hello, world\n");

	return 0;
}
```
<!-- SNIPPET:END -->

### Discussion
La fonction **`main`** ne reçoit pas de données, donc la liste des paramètres est vide (**`void`**).

Le programme ne contient pas de variables, donc le bloc de déclarations est vide.

La fonction **`main`** contient 2 instructions détaillées dans ce qui suit.

#### 1) L'appel de la fonction **`printf`** avec l'argument **`"hello, world\n"`**

Affiche la chaîne de caractères **`"hello, world"`** terminée par **`\n`** (retour à la ligne).

{{< notion_avancee >}}
**```\n``` et retour à la ligne**

En C, le caractère spécial **```\n```** sert à aller à la ligne.

Sous Unix/Linux/macOS, **```\n```** correspond à un seul caractère ASCII : LF (Line Feed, code 10).

Sous Windows, **```\n```** est traduit automatiquement en 2 caractères : CR + LF (Carriage Return + Line Feed, codes 13 et 10).

✅ Il faut donc utiliser **```\n```** pour «aller à la ligne» de façon portable.
La bibliothèque standard se chargera de traduire en fonction du système.

{{< /notion_avancee >}}

L'argument de la fonction **`printf`** est une chaîne de caractères indiquée entre les guillemets.
Une telle suite de caractères est appelée chaîne de caractères constante.
La suite de symboles **`\n`** à la fin de la chaîne de caractères **`"hello, world\n"`** est la notation C pour le **passage à la ligne** ("new line" en Anglais).
En C, il existe plusieurs couples de symboles qui contrôlent l'affichage ou l'impression de texte.
Ces séquences d'échappement sont toujours précédées par le caractère d'échappement **`\`**.
Ces notions seront abordées en détails lors du chapitre 4 sur les entrées-sorties.
La fonction **`printf`** fait partie de la bibliothèque de fonctions standard **`stdio`** qui gère les entrées et les sorties de données.

La première ligne du programme :
```c
#include <stdio.h>
```
demande donc au précompilateur d'inclure le fichier en-tête **`stdio.h`** dans le texte du programme.
Le fichier **`stdio.h`** contient les informations nécessaires pour pouvoir utiliser les fonctions de la bibliothèque standard **`stdio`**.

#### 2) L'instruction **`return`** avec la valeur de retour 0 (zéro)
Cette instruction met fin à la fonction **`main`** et retourne 0 au programme appelant (ici, le système d'exploitation).

### Exercice 1
Modifier le programme **`Hello_World`** pour obtenir le même résultat sur l'écran en utilisant plusieurs fois la fonction **`printf`**.

{{< attention >}}
L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

### Exercice 2
À partir des exemples du cours, écrire un programme qui affiche :
```terminal
The result of 37 * 12 = 444
```

{{< attention >}}
L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

### Exercice 3
Modifier le programme suivant de façon à ce qu'il affiche :
1. la valeur du calcul {{<katex>}}A^B{{</katex>}}. Il faut utiliser la fonction **`pow`**.
2. l'hypoténuse d'un triangle rectangle de côtés A et B.
3. la tangente de A en n'utilisant que les fonctions **`sin`** et **`cos`** (qui prennent des radians en argument). On considère que A est un angle exprimé en degrés. Il faut donc faire la conversion en radians.
4. la valeur arrondie (en moins) de {{<katex>}}A/B{{</katex>}}
5. la valeur arrondie (en moins) à trois positions derrière la virgule de {{<katex>}}A/B{{</katex>}}.

```c
#include <stdio.h>
#include <math.h>   // include math functions and M_PI constant

// SEE FAQ "Pourquoi faut-il définir M_PI nous-même ?"
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

int main(void)
{
  double A;
  double B;
  double res = 0.0;

  // Input for A and B
  printf("Input a value for A: ");
  scanf(" %lf", &A);
  printf("input a value for B: ");
  scanf(" %lf", &B);

  // a) a^b
  // TODO
  // res = ...
  printf("\n a) %f power %f = %G \n", A, B, res);

  // b) Hypothenuse
  // TODO
  // res = ...
  printf("\n b) The hypotenuse of the right triangle is %f \n", res);

  // c) tangent of A
  // WARNING: trigonometric functions use radians
  // TODO
  // res = ...
  printf("\n c) The tangent of A is %f \n", res);

  // d) Rounding down A/B
  // TODO
  // res = ...
  printf("\n d) The rounded down value of A/B is %f \n", res);

  // e) Rounding down A/B with 3 decimals
  // TODO
  // res = ...
  printf("\n e) The rounded down value of A/B with 3 decimals is %f \n\n", res);

  return 0;
}
```

### Les fonctions arithmétiques standard
Les **[fonctions arithmétiques standard](https://en.cppreference.com/w/c/numeric/math)** sont prédéfinies dans la bibliothèque mathématique.
Pour pouvoir les utiliser, le programme doit contenir la ligne :

```c
#include <stdlib.h>
```
pour les fonctions les plus simples comme **`abs`**, **`labs`**, **`div`**, **`rand`**.

Sinon, il faut utiliser la ligne :
```c
#include <math.h>
```

### Type des données
Les arguments et les résultats des fonctions arithmétiques de **`math.h`** sont de type **`double`**.

### Quelques fonctions arithmétiques de **`math.h`**

| FONCTION C | EXPLICATION | LANG. ALGORITHMIQUE |
| ---------- | ----------- | ------------------- |
| **`exp(X)`** | fonction exponentielle | {{<katex>}}e^{X}{{</katex>}} | 
| **`log(X)`** | logarithme naturel | {{<katex>}}ln(X), X>0{{</katex>}}  | 
| **`log10(X)`** | logarithme à base 10 | {{<katex>}}log_{10}(X), X>0{{</katex>}}  | 
| **`pow(X,Y)`** | X exposant Y | {{<katex>}}X^{Y}{{</katex>}}  | 
| **`sqrt(X)`** | racine carrée de X | {{<katex>}}X \geq 0{{</katex>}}  | 
| **`fabs(X)`** | valeur absolue de X | {{<katex>}}\lvert X \rvert{{</katex>}}  | 
| **`floor(X)`** | arrondir en moins | | 
| **`ceil(X)`** | arrondir en plus | | 
| **`fmod(X,Y)`** | reste de la division de X par Y à quotient entier, même signe que X | pour Y différent de 0 |
| **`fmod(16.5, 4.1)`** | vaut 0.1000 |  | 
| **`sin(X) cos(X) tan(X)`**  |  sinus, cosinus, tangente de X  |  | 
| **`asin(X) acos(X) atan(X)`** | arcsin(X), arccos(X), arctan(X)  |  | 
| **`sinh(X) cosh(X) tanh(X)`** | sinus, cosinus, tangente hyperboliques de X  |  | 

**Remarque :** la liste des fonctions ne cite que les fonctions les plus courantes. Pour la liste complète et les constantes prédéfinies, voir les **[fonctions arithmétiques standard](https://en.cppreference.com/w/c/numeric/math)**.

<!--
{{< notion_avancee >}}
### Exercice 4
1. Écrire un programme qui affiche la table de multiplication de 37 selon le format suivant :
```
37 * 0 = 0
37 * 1 = 37
37 * 2 = 74
. . .
37 * 12 = 444
```
{{< /notion_avancee >}}
-->