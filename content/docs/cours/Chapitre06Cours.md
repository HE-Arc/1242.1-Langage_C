---
title: "6 - Fonctions I"
weight: 1
---

# CHAPITRE 6 : fonctions I
## Cours
[1242.1.06_Fonctions_I](/pdf/1242.1.06_Fonctions_I.pdf)

## Squelette à remplir

```c
#include <stdio.h>

// CHAPTER 6

int main(void)
{

	// Experiment with f(int x) example

	// Experiment with int sum(int, int) example

	// Create and experiment with f being declared before main, and defined after main.

	// Experiment with inc(int) and show(int) functions (as seen in course)

	// Write and experiment following functions declaring them first, then defining them (after main)
	// - int sum(int lowerBound, int upperBound);
	// - double mean(int lowerBound, int upperBound);

	// Experiment with print_stars example (global variables are dangerous)

	return 0;
}
```

## Quiz
[QUIZ SUR LES FONCTIONS I (10')](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=761640)


# EXERCICES

## Exercice 1

Qu’affiche le programme suivant :

```c
#include <stdio.h>

int fct(int);

int main(void)
{
  int n, p = 5;
  n = fct(p);
  printf("p = %d, n = %d\n", p, n);
  
  return 0 ;
}

int fct(int r)
{
  return 2*r;
}
```

## Exercice 2

Écrire un petit programme appelant successivement 3 fonctions `f1`, `f2` et `f3`, après les avoir convenablement déclarées au moyen de prototypes.
La fonction `f1` affiche "bonjour" (elle ne possède aucun argument, ni valeur de retour).
La fonction `f2` affiche "bonjour" autant de fois que la valeur reçue en argument (`int`) et qui ne renvoie aucune valeur.
La fonction `f3` fait la même chose que `f2`, mais, en plus, renvoie la valeur (`int`) `0`.

{{< hint danger >}}
**IMPORTANT :** l’appel de fonction **`printf("Bonjour");`** ne doit apparaitre qu’une seule fois dans le programme.
{{< /hint >}}

## Exercice 3

Quels résultats fournit le programme ci-dessous :

```c
#include <stdio.h>

int n = 10, q = 2; // Variables globales !!!

int fct(int);
void f(void);

int main(void)
{
  int n = 0, p = 5;
  n = fct(p);
  printf("A : dans main, n = %d, p = %d, q = %d\n", n, p, q);
  f();
  
  return 0 ;
}

int fct(int p)
{
  int q;
  q = 2 * p + n;
  printf("B : dans fct, n = %d, p = %d, q = %d\n", n, p, q);
  
  return q;
}

void f(void)
{
  int p = q * n;
  printf("C : dans f, n = %d, p = %d, q = %d\n", n, p, q);
}
```

## Exercice 4
Écrire un programme qui calcule le carré des nombres inférieurs ou égal à la valeur saisie au clavier.
Pour ce faire il faut :
1. Déclarer (puis définir) la fonction **`ch06_ex04_Square()`** qui reçoit une valeur entière et retourne son carré.
2. Déclarer (puis définir) la fonction **`ch06_ex04_Squares()`** qui reçoit une valeur entière et retourne un booléen.
Cette valeur entère doit être comprise entre 1 et 1000.
En cas de saisie incorrecte, la fonction retourne **`false`**.
Dans le cas contraire, la fonction affiche tous les carrés des nombres inférieurs ou égal à la valeur saisie et retourne **`true`**.

{{< hint danger >}}
**ATTENTION :** il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** il faut respecter strictement les noms de fonctions donnés.
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** il faut terminer l'affichage de chaque carré par un espace.
{{< /hint >}}

**Exemple :** un appel à la fonction **`ch06_ex04_Squares()`** avec la valeur 5 doit afficher :
```code
1 4 9 16 25 
```

## Exercice 5 (non évalué)
Écrire un programme qui saisit, au clavier, un nombre compris entre deux valeurs et affiche la table de multiplication du nombre saisi.
Le programme `main()` n’est constitué que de deux appels à des fonctions, comme ce qui suit :

```c
int main(void)
{
	const int MIN_TABLE = 1;
	const int MAX_TABLE = 12;
	
	int number;
	number = ch06_ex05_Read(MIN_TABLE, MAX_TABLE);
	ch06_ex05_MultiplicationTable(number);

	return 0;
}
```

Il faut donc :
1. écrire la fonction **`ch06_ex05_Read()`** qui reçoit 2 paramètres entiers : une valeur min et une valeur max entre lesquelles le nombre saisi au clavier doit être compris, bornes min et max incluses.
2. écrire la fonction **`ch06_ex05_MultiplicationTable()`** qui affiche la table de multiplication demandée selon l'exemple ci-dessous.

**Exemple :**
```code
Please enter the multiplication table (in [1..12]): 0
Please enter the multiplication table (in [1..12]): 13
Please enter the multiplication table (in [1..12]): a
Please enter the multiplication table (in [1..12]): 5

MULTIPLICATION TABLE FOR 5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
```

## Exercice 6
Écrire un programme qui effectue des opérations mathématiques simples : +,-,*,/.
Ce programme sera constitué de 2 fonctions :
1. La fonction **`ch06_ex06_Calculator()`** qui ne prend pas de paramètre et ne retourne rien.
Elle demande à l’utilisateur de saisir une expression mathématique simple (2 opérandes et un opérateur), effectue les calculs associés en appelant la fonction **`ch06_ex06_Compute()`** (voir ci-dessous) et affiche le résultat.
2. La fonction **`ch06_ex06_Compute()`** qui reçoit 3 paramètres : 2 nombres à virgule flottante (**`double`**) et un caractère.
Les deux nombres flottants sont les opérandes de l’opération.
Le caractère indique l’opérateur soit **`+`**, **`-`**, **`*`**, **`/`**.
La fonction retourne un résultat correspondant à l'une des 4 opérations appliquées à ses deux opérandes.
On tiendra compte des risques de division par zéro.
Dans ce cas, la fonction retourne zéro.

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** le résultat sera affiché avec 4 décimales.
{{< /hint >}}

**Exemple 1 :**
```code
$ .\ch06_ex06_Calculator.exe
Enter an expression <nb op nb> : 2 + 4
Result = 6.0000
```

**Exemple 2 :**
```code
$ .\ch06_ex06_Calculator.exe
Enter an expression <nb op nb> : 1.1 * 9.9
Result = 10.8900
```

**Exemple 3 :**
```code
$ .\ch06_ex06_Calculator.exe
Enter an expression <nb op nb> : 2 z 3
Enter an expression <nb op nb> : a s d
Enter an expression <nb op nb> : a + s
Enter an expression <nb op nb> : 10 / 0
Result = 0.0000
```

## Exercice 7
Écrire un programme qui calcule la somme des entiers compris entre 2 entiers (inclus).
Il faut en particulier écrire la fonction **`ch06_ex07_SumN()`** qui prend 2 entiers en paramètre, et retourne un entier.

**Exemple 1 :** un appel à la fonction **`ch06_ex07_SumN(1, 5)`** doit retourner 15.

**Exemple 2 :** un appel à la fonction **`ch06_ex07_SumN(5, 1)`** doit retourner 15.

**Exemple 3 :** un appel à la fonction **`ch06_ex07_SumN(1, 1)`** doit retourner 1.

**Exemple 4 :** un appel à la fonction **`ch06_ex07_SumN(1, 100)`** doit retourner 5050.

## Exercice 8
Écrire un programme qui inverse les chiffres composants un nombre entier.
Il faut en particulier écrire la fonction **`ch06_ex08_Invert()`** qui prend 1 entier positif en paramètre, et retourne un entier.
En cas d'erreur, la fonction retourne -1.

**Exemple 1 :** un appel à la fonction **`ch06_ex08_Invert(1234)`** doit retourner 4321.

**Exemple 2 :** un appel à la fonction **`ch06_ex08_Invert(-12)`** doit retourner -1.
