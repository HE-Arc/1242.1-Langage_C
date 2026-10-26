---
title: "6. Fonctions I"
weight: 1
---

# CHAPITRE 6 : fonctions
## Slides
{{<slides "https://he-arc.github.io/1242.1-Langage_C-SLIDES/06_Fonctions_I.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.1-Langage_C-SLIDES/06_Fonctions_I.html?print-pdf)

## Squelette à remplir
{{<a_faire>}}
Remplir le squelette suivant au fur et à mesure du cours.
{{</a_faire>}}
<!-- SNIPPET:BEGIN source_file=chap6.c id=1242.1_Skeletons_06_chap6.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `chap6.c`**

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

	// Experiment with increment(int) (pass by value) and with a static local variable (f1)

	return 0;
}
```
<!-- SNIPPET:END -->

## Exemples

### 06.01 : comment appeler une fonction qui ne retourne rien ?
<!-- SNIPPET:BEGIN source_file=Function.c id=1242.1_Exemples_06.01_Function_Function.c run=true stdin="42" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Function.c`**

```c
#include <stdio.h>

// Prototype
void prn_message(int k);

int main(void)
{
	int N;
	int status = 0;
	const int nbExpectedValues = 1;
	do
	{
		printf("Please enter an integer: ");
		status = scanf("%d", &N);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			printf("\a");
		}
	} while (status != nbExpectedValues);

	// Function call like a procedure
	prn_message(N);

	return 0;
}

void prn_message(int k)
{
	printf("\nYou entered the value %d\n\n", k);
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o Function.exe Function.c
$ ./Function.exe
Please enter an integer: 42

You entered the value 42
```
<p class="run-info">Compiled and executed on 2026-10-26 15:39 from 81a5010.</p>
<!-- SNIPPET:END -->

### 06.02 : comment déclarer une fonction avant `main` et la définir après ?
<!-- SNIPPET:BEGIN source_file=Sum2.c id=1242.1_Exemples_06.02_Sum2_Sum2.c run=true stdin="1 10" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Sum2.c`**

```c
#include <stdio.h>

// Prototype/Declaration
int sum(int lowerBound, int upperBound);	// With a comma!!!
double mean(int lowerBound, int upperBound);

int main(void)
{
	int lower, upper, status;
	int total;
	const int nbExpectedValues = 2;
	do
	{
		printf("Please enter lower bound and upper bound (in that order): ");
		status = scanf("%d %d", &lower, &upper);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}
	} while (status != nbExpectedValues);

	// Call sum function
	// NOTE that effective/actual parameters and formal parameters may have different names
	total = sum(lower, upper);
	printf("The sum from %d to %d = %d\n", lower, upper, total);
	// We can even make the call of a function in the call of another function
	printf("The mean value is = %lf\n", mean(lower, upper));

	return 0;
}

// Definition
int sum(int lowerBound, int upperBound) // Header
{ // Body
	int sum = 0;

	for (int n = lowerBound; n <= upperBound; ++n)
	{
		sum += n;
	}

	return sum;
}

// Definition
double mean(int lowerBound, int upperBound)
{
	// Check for errors
	if (lowerBound > upperBound)
	{
		return 0; // 0.0 will be identified as an error
	}

	// NOTE the cast
	double mean = sum(lowerBound, upperBound) / ((double)upperBound - lowerBound + 1);
	
	return mean;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o Sum2.exe Sum2.c
$ ./Sum2.exe
Please enter lower bound and upper bound (in that order): 1 10
The sum from 1 to 10 = 55
The mean value is = 5.500000
```
<p class="run-info">Compiled and executed on 2026-10-26 15:39 from 81a5010.</p>
<!-- SNIPPET:END -->

### 06.03 : où sont rangées en mémoire les variables globales, locales et dynamiques ?
<!-- SNIPPET:BEGIN source_file=AllocationHeapStack.c id=1242.1_Exemples_06.03_AllocationHeapStack_AllocationHeapStack.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `AllocationHeapStack.c`**

```c
#include <stdio.h>
#include <stdlib.h>

char g1;
char g2;
char g1i = 9;
char g2i = 10;

void f1(char p1)
{
	printf("p1f1: %p\n", (void *) &p1);
	char l1f1;
	printf("l1f1: %p\n", (void *) &l1f1);
	char l2f1;
	printf("l2f1: %p\n", (void *) &l2f1);
	char l3f1;
	printf("l3f1: %p\n", (void *) &l3f1);
	char l4f1;
	printf("l4f1: %p\n", (void *) &l4f1);
}

void f2(void)
{
	char l1f2;
	printf("l1f2: %p\n", (void *) &l1f2);
	char l2f2;
	printf("l2f2: %p\n", (void *) &l2f2);
	char l3f2;
	printf("l3f2: %p\n", (void *) &l3f2);
	char l4f2;
	printf("l4f2: %p\n", (void *) &l4f2);
}

int main(void)
{
	printf("g1:  %p\n", (void *) &g1);
	printf("g2:  %p\n", (void *) &g2);
	printf("g1i: %p\n", (void *) &g1i);
	printf("g2i: %p\n", (void *) &g2i);

	char l1m;
	printf("l1m: %p\n", (void *) &l1m);
	char l2m;
	printf("l2m: %p\n", (void *) &l2m);
	char l3m;
	printf("l3m: %p\n", (void *) &l3m);
	char l4m;
	printf("l4m: %p\n", (void *) &l4m);

	f1('x');

	char *px;
	printf("px: %p\n", (void *) &px);

	px = malloc(1);
	printf("dyn1: %p\n", (void *) px);
	px = malloc(1);
	printf("dyn2: %p\n", (void *) px);
	px = malloc(1);
	printf("dyn3: %p\n", (void *) px);
	px = malloc(1);
	printf("dyn4: %p\n", (void *) px);
	px = malloc(1);
	printf("dyn5: %p\n", (void *) px);

	f2();

	return 0;
}
```
<!-- SNIPPET:END -->

{{< a_noter >}}
Les adresses affichées changent d'une exécution à l'autre : l'exemple n'est donc pas exécuté ici.
Comparer les adresses des variables globales, locales (`main`, `f1`, `f2`) et allouées avec `malloc` (voir chapitre 10) avec le schéma des slides.
{{< /a_noter >}}

## Exercices

### Exercice 1 : valeur retournée
Qu’affiche le programme suivant :

<!-- SNIPPET:BEGIN source_file=Exercice1.c id=1242.1_Exercices_06.01_FonctionsI_Exercice1.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice1.c`**

```c
#include <stdio.h>

int fct(int);

int main(void)
{
	int n, p = 5;
	n = fct(p);
	printf("p = %d, n = %d\n", p, n);

	return 0;
}

int fct(int r)
{
	return 2 * r;
}
```
<!-- SNIPPET:END -->

### Exercice 2 : trois fonctions qui disent bonjour

Écrire un petit programme appelant successivement 3 fonctions `f1`, `f2` et `f3`, après les avoir convenablement déclarées au moyen de prototypes.
La fonction `f1` affiche "bonjour" (elle ne possède aucun argument, ni valeur de retour).
La fonction `f2` affiche "bonjour" autant de fois que la valeur reçue en argument (`int`) et qui ne renvoie aucune valeur.
La fonction `f3` fait la même chose que `f2`, mais, en plus, renvoie la valeur (`int`) `0`.

{{< hint danger >}}
**IMPORTANT :** l’appel de fonction **`printf("Bonjour");`** ne doit apparaitre qu’une seule fois dans le programme.
{{< /hint >}}

### Exercice 3 : variables globales et locales
Quels résultats fournit le programme ci-dessous :

<!-- SNIPPET:BEGIN source_file=Exercice3_ReverseEngineering.c id=1242.1_Exercices_06.01_FonctionsI_Exercice3_ReverseEngineering.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice3_ReverseEngineering.c`**

```c
#include <stdio.h>

int n = 10, q = 2; // Global variables!
int fct(int);
void f(void);

int main(void)
{
	int n = 0, p = 5;
	n = fct(p);
	printf("A : dans main, n = %d, p = %d, q = %d\n", n, p, q);
	f();

	return 0;
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
<!-- SNIPPET:END -->

### Exercice 4 : carrés
Écrire un programme qui calcule le carré des nombres inférieurs ou égal à la valeur saisie au clavier.
Pour ce faire il faut :
1. Déclarer (puis définir) la fonction **`ch06_ex04_Square()`** qui reçoit une valeur entière et retourne son carré.
2. Déclarer (puis définir) la fonction **`ch06_ex04_Squares()`** qui reçoit une valeur entière et retourne un booléen.
Cette valeur entère doit être comprise entre 1 et 1000.
En cas de saisie incorrecte, la fonction retourne **`false`**.
Dans le cas contraire, la fonction affiche tous les carrés des nombres inférieurs ou égal à la valeur saisie et retourne **`true`**.

{{< attention >}}
- Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
- Il faut respecter strictement les noms de fonctions donnés.
- Il faut terminer l'affichage de chaque carré par un espace.
- L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

**Exemple :** un appel à la fonction **`ch06_ex04_Squares()`** avec la valeur 5 doit afficher :
```terminal
1 4 9 16 25 
```

### Exercice 5 : table de multiplication (non évalué)
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
```terminal
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

### Exercice 6 : calculatrice
Écrire un programme qui effectue des opérations mathématiques simples : +,-,*,/.
Ce programme sera constitué d'une seule fonction (en plus de `main()`), à savoir :
1. la fonction **`ch06_ex06_Compute()`** qui reçoit 3 paramètres (dans cet ordre) : 2 nombres à virgule flottante (**`double`**) et un caractère.
Les deux nombres flottants sont les opérandes de l’opération.
Le caractère indique l’opérateur soit **`+`**, **`-`**, **`*`**, **`/`**.
La fonction retourne un résultat correspondant à l'une des 4 opérations appliquées à ses deux opérandes.
On tiendra compte des risques de division par zéro.
Dans ce cas, la fonction retourne zéro.

{{< a_noter >}}
Dans les exemples suivantes, les entrées-sorties sont données à titre indicatif.
Il n'est pas nécessaire de reproduire exactement le même formatage.
{{< /a_noter >}}

**Exemple 1 :**
```terminal
$ .\ch06_ex06_Calculator.exe
Enter an expression <nb op nb> : 2 + 4
Result = 6.0000
```

**Exemple 2 :**
```terminal
$ .\ch06_ex06_Calculator.exe
Enter an expression <nb op nb> : 1.1 * 9.9
Result = 10.8900
```

**Exemple 3 :**
```terminal
$ .\ch06_ex06_Calculator.exe
Enter an expression <nb op nb> : 2 z 3
Enter an expression <nb op nb> : a s d
Enter an expression <nb op nb> : a + s
Enter an expression <nb op nb> : 10 / 0
Result = 0.0000
```

### Exercice 7 : somme des entiers entre deux bornes
Écrire un programme qui calcule la somme des entiers compris entre 2 entiers (inclus).
Il faut en particulier écrire la fonction **`ch06_ex07_SumN()`** qui prend 2 entiers en paramètre, et retourne un entier.

**Exemple 1 :** un appel à la fonction **`ch06_ex07_SumN(1, 5)`** doit retourner 15.

**Exemple 2 :** un appel à la fonction **`ch06_ex07_SumN(5, 1)`** doit retourner 15.

**Exemple 3 :** un appel à la fonction **`ch06_ex07_SumN(1, 1)`** doit retourner 1.

**Exemple 4 :** un appel à la fonction **`ch06_ex07_SumN(1, 100)`** doit retourner 5050.

### Exercice 8 : inverser les chiffres d’un nombre
Écrire un programme qui inverse les chiffres composants un nombre entier.
Il faut en particulier écrire la fonction **`ch06_ex08_Invert()`** qui prend 1 entier positif en paramètre, et retourne un entier.
En cas d'erreur, la fonction retourne -1.

**Exemple 1 :** un appel à la fonction **`ch06_ex08_Invert(1234)`** doit retourner 4321.

**Exemple 2 :** un appel à la fonction **`ch06_ex08_Invert(-12)`** doit retourner -1.

## Défis

### Fonctions mal déclarées ou sans `return`
Dans le programme suivant, compilé en C23 avec les options du cours, quels appels ou déclarations sont refusés par `gcc`, et pourquoi ?
- `func2` ne contient pas d’instruction `return` ;
- `func3(void)` est appelée avec un paramètre ;
- `func4()` est déclarée sans paramètre et appelée avec un paramètre ;
- `func5` est déclarée sans type de retour.

{{<details "Explications" >}}
Tous sont refusés :
- `func2` : utiliser la valeur d’une fonction non `void` terminée sans `return` est un comportement indéfini (UB) ; `gcc` l’avertit (`-Wreturn-type`), ce qui devient une erreur avec `-Werror`.
- `func3(99)` : le prototype `int func3(void)` interdit tout paramètre.
- `func4(99)` : depuis C23, `int func4();` équivaut à `int func4(void);`. Pre C23, `()` signifiait « paramètres non précisés » et l’appel était accepté.
- `func5` : le type de retour implicite `int` n’existe plus depuis C99.

L’exemple complet n’active les appels fautifs qu’avec `-DACTIVATE_ERRORS` :
<!-- SNIPPET:BEGIN source_file=FunctionDefaultInt.c id=1242.1_Exemples_06.99_FunctionDefaultInt_FunctionDefaultInt.c run=true cflags="-DACTIVATE_ERRORS" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `FunctionDefaultInt.c`**

```c
#include <stdio.h>

// Prototypes
int func1(int a);
int func2(int a);
int func3(void);
int func4(); // C23: same as int func4(void)
#ifdef ACTIVATE_ERRORS
func5(void); // Pre C23: implicit int
#endif

int main(void)
{
	printf("func1(99) = %d\n", func1(99));
	printf("func3() = %d\n", func3());
	printf("func4() = %d\n", func4());

#ifdef ACTIVATE_ERRORS
	printf("func2(99) = %d\n", func2(99)); // UB: func2 has no return statement
	printf("func3(99) = %d\n", func3(99)); // too many arguments
	printf("func4(99) = %d\n", func4(99)); // C23: too many arguments
	printf("func5() = %d\n", func5());
#endif

	return 0;
}

int func1(int a)
{
	return a;
}

int func2(int a)
{
	printf("a = %d\n", a);
#ifndef ACTIVATE_ERRORS
	return a;
#endif
}

int func3(void)
{
	return 3;
}

int func4()
{
	return 4;
}

#ifdef ACTIVATE_ERRORS
func5(void)
{
	return 5;
}
#endif
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -DACTIVATE_ERRORS -o FunctionDefaultInt.exe FunctionDefaultInt.c
FunctionDefaultInt.c:9:1: error: data definition has no type or storage class [-Werror]
    9 | func5(void); // Pre C23: implicit int
      | ^~~~~
FunctionDefaultInt.c:9:1: error: type defaults to 'int' in declaration of 'func5' [-Wimplicit-int]
FunctionDefaultInt.c: In function 'main':
FunctionDefaultInt.c:20:36: error: too many arguments to function 'func3'; expected 0, have 1
   20 |         printf("func3(99) = %d\n", func3(99)); // too many arguments
      |                                    ^~~~~ ~~
FunctionDefaultInt.c:6:5: note: declared here
    6 | int func3(void);
      |     ^~~~~
FunctionDefaultInt.c:21:36: error: too many arguments to function 'func4'; expected 0, have 1
   21 |         printf("func4(99) = %d\n", func4(99)); // C23: too many arguments
      |                                    ^~~~~ ~~
FunctionDefaultInt.c:7:5: note: declared here
    7 | int func4(); // C23: same as int func4(void)
      |     ^~~~~
FunctionDefaultInt.c: At top level:
FunctionDefaultInt.c:52:1: error: return type defaults to 'int' [-Wimplicit-int]
   52 | func5(void)
      | ^~~~~
FunctionDefaultInt.c: In function 'func2':
FunctionDefaultInt.c:39:1: error: control reaches end of non-void function [-Werror=return-type]
   39 | }
      | ^
cc1.exe: all warnings being treated as errors
```
<p class="run-info">Compiled and executed on 2026-10-26 15:39 from 81a5010.</p>
<!-- SNIPPET:END -->
{{</details>}}
