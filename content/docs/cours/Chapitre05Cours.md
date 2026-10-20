---
title: "5. Structures de contrôle"
weight: 1
---

# CHAPITRE 5 : structures de contrôle

## Slides
{{<slides "https://he-arc.github.io/1242.1-Langage_C-SLIDES/05_StructuresDeControle.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.1-Langage_C-SLIDES/05_StructuresDeControle.html?print-pdf)

## Squelette à remplir
{{<a_faire>}}
Remplir le squelette suivant au fur et à mesure du cours.
{{</a_faire>}}
<!-- SNIPPET:BEGIN source_file=chap5.c id=1242.1_Skeletons_05_chap5.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `chap5.c`**

```c
#include <stdio.h>

// CHAPTER 5

int main(void)
{
	// Experiment with if () {...} else {...}
	// => read an integer, then check whether it is divisible by 13 (for example)

	// Experiment with the ternary operator (see example 05.98)

	// Experiment with switch
	// =>  For example, read 2 values and an operation (in +, -, * and /) and perform the calculation.

	// Experiment with while(){...}
	// => Read 2 integers M and N, then compute modulo
	// => Copy examples from chapter 5 then check the answers
	// => Read an integer N, then compute the summation from 1 to N

	// Experiment with do{...}while()
	// => Read an integer between 0 and 10 until the input is valid (see example 04.02)
	// => Continuously read values and sum them. Stop when the user enters 0.

	// Experiment with for(;;){...}
	// => (SEE example chapter 5) Read an integer N, then display the iteration number.
	// => (SEE example chapter 5) Copy loop examples then check your answers.
	// => (SEE example chapter 5) Read an integer N, then display the list of powers of 2, from 1 to N.

	// Experiment with return, exit(), break and continue inside for loops

	return 0;
}
```
<!-- SNIPPET:END -->

## Exemples

### 05.01 : comment tester si un nombre est divisible par 13 avec `if` / `else` ?
<!-- SNIPPET:BEGIN source_file=if_else_Divi13.c id=1242.1_Exemples_05.01_if_else_Divi13_if_else_Divi13.c run=true stdin="39" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `if_else_Divi13.c`**

```c
#include <stdio.h>
#include <stdlib.h>

// A number N is a multiple of M, iff when dividing N by M, the remainder is 0
int main(void)
{
	int number = 0;
	int remainder = 0;
	int status = 0;
	const int nbExpectedValues = 1;

	do
	{
		printf("Number: ");
		status = scanf("%d", &number);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			printf("Please enter an integer.\n");
		}
	} while (status != nbExpectedValues);

	if (number < 0)
	{
		// If the number is < 0
		// then we test for its positive counterpart only
		number = -number;
	}
	remainder = number % 13;

	if (remainder == 0)
	{
		printf("This number is divisible by 13.\n");
		printf("Result: %d / 13 = %d\n", number, number / 13);
	}
	else
	{
		printf("This number is NOT divisible by 13.\n");
		printf("The closest (lowest) multiple is %d.\n", number - remainder);
	}

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o if_else_Divi13.exe if_else_Divi13.c
$ ./if_else_Divi13.exe
Number: 39
This number is divisible by 13.
Result: 39 / 13 = 3
```
<p class="run-info">Compiled and executed on 2026-10-19 20:41 from 0114261.</p>
<!-- SNIPPET:END -->

### 05.02 : comment résoudre un système de deux équations linéaires avec `if` / `else` ?
<!-- SNIPPET:BEGIN source_file=if_else_Equalin.c id=1242.1_Exemples_05.02_if_else_Equalin_if_else_Equalin.c run=true stdin="1, 1, 3\n1, -1, 1" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `if_else_Equalin.c`**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	double a11, a12, a21, a22, c1, c2;
	double det, det1, det2, x, y;
	int status = 0;

	const int nbExpectedValues = 3;

	printf("This program solves a system of 2 linear equations of the form:\n");
	printf("    a11x + a12y = c1 \nAND a21x + a22y = c2\n");
	printf("Please enter equations system coefficients (with commas):\n");
	do
	{
		printf("a11, a12, c1   = ");
		status = scanf("%lf, %lf, %lf", &a11, &a12, &c1);

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

	do
	{
		printf("a21, a22, c2   = ");
		status = scanf("%lf, %lf, %lf", &a21, &a22, &c2);

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

	// Determinant
	det = a11 * a22 - a21 * a12;
	// There is a solution iff det != 0
	if (det != 0)
	{
		// Codeterminants
		det1 = c1 * a22 - c2 * a12;
		det2 = a11 * c2 - a21 * c1;

		// Solutions
		x = det1 / det;
		y = det2 / det;

		printf("x = %lf, y = %lf\n", x, y);
	}
	else
	{
		printf("These equations do NOT have a unique solution.\n");
	}

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o if_else_Equalin.exe if_else_Equalin.c
$ ./if_else_Equalin.exe
This program solves a system of 2 linear equations of the form:
    a11x + a12y = c1 
AND a21x + a22y = c2
Please enter equations system coefficients (with commas):
a11, a12, c1   = 1, 1, 3
a21, a22, c2   = 1, -1, 1
x = 2.000000, y = 1.000000
```
<p class="run-info">Compiled and executed on 2026-10-19 20:41 from 0114261.</p>
<!-- SNIPPET:END -->

### 05.03 : comment choisir une opération avec `switch` ?
<!-- SNIPPET:BEGIN source_file=switch_Operat.c id=1242.1_Exemples_05.03_switch_Operat_switch_Operat.c run=true stdin="3 * 4" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `switch_Operat.c`**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  double par1, par2, result;
  char operation;
  int status = 0;

  printf("This program allows to apply +,-,* and / on numbers.\n");

  const int nbExpectedValues = 3;

  do
  {
    printf("Please enter operation: ");
    status = scanf(" %lf %c %lf", &par1, &operation, &par2);

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

  switch (operation)
  {
  case '+':
    result = par1 + par2;
    break;
  case '-':
    result = par1 - par2;
    break;
  case '*':
    result = par1 * par2;
    break;
  case '/':
    if (par2 == 0)
    {
      printf("Division by zero\n");
      return 1;
    }
    result = par1 / par2;
    break;
  default:
    printf("Unknown operation: %c\n", operation);
    return 1;
  }

  printf("Result: %lf %c %lf = %lf\n", par1, operation, par2, result);

  return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o switch_Operat.exe switch_Operat.c
$ ./switch_Operat.exe
This program allows to apply +,-,* and / on numbers.
Please enter operation: 3 * 4
Result: 3.000000 * 4.000000 = 12.000000
```
<p class="run-info">Compiled and executed on 2026-10-19 19:16 from 0114261.</p>
<!-- SNIPPET:END -->

### 05.04 : comment calculer la somme de 1 à N avec `while` ?
<!-- SNIPPET:BEGIN source_file=while_Sum.c id=1242.1_Exemples_05.04_while_Sum_while_Sum.c run=true stdin="10" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `while_Sum.c`**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int sum = 0, counter = 1, N;
	int status = 0;

	printf("This program computes the sum from 1 to N.\n");

	const int nbExpectedValues = 1;
	do
	{
		printf("Please enter N: ");
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

	while (counter <= N)
	{
		sum += counter;
		++counter;
	}
	printf("Result: %d\n", sum);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o while_Sum.exe while_Sum.c
$ ./while_Sum.exe
This program computes the sum from 1 to N.
Please enter N: 10
Result: 55
```
<p class="run-info">Compiled and executed on 2026-10-19 20:41 from 0114261.</p>
<!-- SNIPPET:END -->

### 05.04b : qu'affiche un `while` selon la place du `++` ?
<!-- SNIPPET:BEGIN source_file=while_loops.c id=1242.1_Exemples_05.04b_while_loops_while_loops.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `while_loops.c`**

```c
#include <stdio.h>

int main(void)
{
  // Example A
  printf("\nExemple A\n");
  {
    int i = 0;

    while (i++ < 3)
    {
      printf(" %d ", i);
    }

    printf(" et %d ", i);
  }
  
  // Example B
  printf("\nExemple B\n");
  {
    int i = 0;

    while (++i < 3)
    {
      printf(" %d ", i);
    }
    printf(" et %d ", i);
  }

  // Example C
  printf("\nExemple C\n");
  {
    int i = 0;
    while (i < 3)
    {
      printf(" %d ", i++);
    }
    printf(" et %d ", i);
  }

  // Example D
  printf("\nExemple D\n");
  {
    int i = 0;

    while (i < 3)
    {
      printf(" %d ", ++i);
    }
    printf(" et %d ", i);
  }

  return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o while_loops.exe while_loops.c
$ ./while_loops.exe

Exemple A
 1  2  3  et 4 
Exemple B
 1  2  et 3 
Exemple C
 0  1  2  et 3 
Exemple D
 1  2  3  et 3
```
<p class="run-info">Compiled and executed on 2026-10-18 18:13 from 0114261.</p>
<!-- SNIPPET:END -->

### 05.05 : comment additionner des valeurs jusqu'à la saisie de 0 avec `do...while` ?
<!-- SNIPPET:BEGIN source_file=do_while_Addition.c id=1242.1_Exemples_05.05_do_while_Addition_do_while_Addition.c run=true stdin="1.5\n2\n0" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `do_while_Addition.c`**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	double sum = 0;
	int status = 0;

	printf("This program computes the sum of a list of reals (terminated by 0)\n");

	double value = 0;
	do
	{
		const int nbExpectedValues = 1;
		do
		{
			printf("add: ");
			status = scanf("%lf", &value);

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

		sum += value;
	} while (value != 0);

	printf("Sum = %lf\n", sum);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o do_while_Addition.exe do_while_Addition.c
$ ./do_while_Addition.exe
This program computes the sum of a list of reals (terminated by 0)
add: 1.5
add: 2
add: 0
Sum = 3.500000
```
<p class="run-info">Compiled and executed on 2026-10-19 20:41 from 0114261.</p>
<!-- SNIPPET:END -->

### 05.06 : comment afficher les puissances de 2 avec `for` ?
<!-- SNIPPET:BEGIN source_file=for_power2.c id=1242.1_Exemples_05.06_for_Power2_for_power2.c run=true stdin="100" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `for_power2.c`**

```c
#include <stdio.h>

int main(void)
{
	int result, N, exponent = 0;
	int status = 0;

	printf("This program displays the powers of 2 up to N\n");

	const int nbExpectedValues = 1;
	do
	{
		printf("Please enter N: ");
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

	for (result = 1; result <= N; result *= 2)
	{
		printf("2^%d = %d\n", exponent, result);
		++exponent;
	}

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o for_power2.exe for_power2.c
$ ./for_power2.exe
This program displays the powers of 2 up to N
Please enter N: 100
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
```
<p class="run-info">Compiled and executed on 2026-10-19 19:16 from 0114261.</p>
<!-- SNIPPET:END -->

### 05.07 : que vaut l'indice d'une boucle `for` à chaque tour, et après ?
<!-- SNIPPET:BEGIN source_file=for_loop_examples.c id=1242.1_Exemples_05.07_for_loop_examples_for_loop_examples.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `for_loop_examples.c`**

```c
#include <stdio.h>

int main(void)
{
	int n;
	for (n = 0; n < 2; ++n)
	{
		printf("Iteration:%d\n", n);
	}

	printf("Fin:%d", n);

	int i, j, c, k;

	printf("\n");
	for (i = 0; i < 5; i++)
		printf("%d,", i);

	printf("\n");
	for (j = 4; j <= 12; j = j + 2)
		printf("%d,", j);

	printf("\n");
	for (c = 'a'; c < 'f'; c += 1)
		printf("%c,", c);

	printf("\n");
	for (k = 5; k > 0; k--)
		printf("%d,", k);

	printf("\n");
	for (int i = 0, j = 0; i < 10; i++, j = i * i)
	{
		printf("x = %2d, x^2 = %2d\n", i, j);
	}

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o for_loop_examples.exe for_loop_examples.c
$ ./for_loop_examples.exe
Iteration:0
Iteration:1
Fin:2
0,1,2,3,4,
4,6,8,10,12,
a,b,c,d,e,
5,4,3,2,1,
x =  0, x^2 =  0
x =  1, x^2 =  1
x =  2, x^2 =  4
x =  3, x^2 =  9
x =  4, x^2 = 16
x =  5, x^2 = 25
x =  6, x^2 = 36
x =  7, x^2 = 49
x =  8, x^2 = 64
x =  9, x^2 = 81
```
<p class="run-info">Compiled and executed on 2026-10-18 18:13 from 0114261.</p>
<!-- SNIPPET:END -->

### 05.98 : comment utiliser l'opérateur conditionnel `? :` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_05.98_Conditional_main.c run=true cflags="-Wno-error=unused-variable" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
// Conditional operator
#include <stdio.h>

#define ACTIVATE_WARNINGS_AND_ERRORS 0

int main(void)
{
	// Example from Slides
	int a = 3, b = 9, max, min;

	max = ((a > b) ? a : b);
	min = ((a > b) ? b : a);

	printf("Min / max: %d / %d\n", min, max);

	// It obviously also works without parentheses
	max = (a > b) ? a : b;
	printf("Max: %d\n", max);

	// Q: can we nest ternary operator?
	// A: yes. A ternary operator needs expression as operands.
	//    So, as a ternary operator is an expression, it can contain
	//    other ternary operators
	int value = 100;
	int quarter = value > 50 ? (value > 75 ? 4 : 3) : (value <= 25 ? 1 : 2);

	// It even works without parentheses, but it is less readable
	int quarter2 = value > 50 ? value > 75 ? 4 : 3 : value <= 25 ? 1 : 2;

	// Q: why cannot we use blocks inside conditional operator?
	// A:
	//   ISO C standard
	//     6.5.15 Conditional operator
	//       "...the result is the value of the second or third operand	(whichever is evaluated), converted to the type described below..."
	//       ==>> blocks do not return values, expressions do.

	//  - MSVC: error C2059:  syntax error: '{'
	//  - GCC: error: expected expression before '{' token
	int i = 1;

#if ACTIVATE_WARNINGS_AND_ERRORS
	(i++ == 1) ? {printf("Hello\n"); } : {printf("World\n"); };
#endif

	//  - MSVC: error C2059:  syntax error: '{'
	//  - GCC (with -Wpedantic): 	warning: ISO C forbids braced-groups within expressions [-Wpedantic]
	//    but prints "Hello"
	//    ==>> GCC extension.
#if ACTIVATE_WARNINGS_AND_ERRORS
	(i++ == 1) ? ({ printf("Hello\n"); }) : ({ printf("World\n"); });
#endif

	// OK: a function call is an expression
	(i++ == 1) ? printf("Hello\n") : printf("World\n");

	// Q: does ternary operator have right-to-left or left-to-right associativity?
	// A: right-to-left
	int r = 1 ? 1 : 2 ? 3 : 4; // ??
	int l2r = (1 ? 1 : 2) ? 3 : 4; // 3
	int r2l = 1 ? 1 : (2 ? 3 : 4); // 1

	printf("r: %d\n", r);
	printf("l2r: %d\n", l2r);
	printf("r2l: %d\n", r2l);

	if (r == r2l)
	{
		printf("Associativity: right-to-left\n");
	}
	else
	{
		printf("Associativity: left-to-right\n");
	}

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=unused-variable -o main.exe main.c
main.c: In function 'main':
main.c:28:13: warning: unused variable 'quarter2' [-Wunused-variable]
   28 |         int quarter2 = value > 50 ? value > 75 ? 4 : 3 : value <= 25 ? 1 : 2;
      |             ^~~~~~~~
main.c:25:13: warning: unused variable 'quarter' [-Wunused-variable]
   25 |         int quarter = value > 50 ? (value > 75 ? 4 : 3) : (value <= 25 ? 1 : 2);
      |             ^~~~~~~
$ ./main.exe
Min / max: 3 / 9
Max: 9
Hello
r: 1
l2r: 3
r2l: 1
Associativity: right-to-left
```
<p class="run-info">Compiled and executed on 2026-10-19 20:41 from 0114261.</p>
<!-- SNIPPET:END -->

## Exercices

{{< a_noter >}}
Pour des raisons historiques, la numérotation des exercices n'est pas continue.
{{< /a_noter >}}

### Exercice 1 : instructions `if` erronées
1) Parmi les instructions suivantes, indiquer celles qui sont fausses et dire pourquoi :

```c
//a)
if (number < 1) ++number;
//b) 
if (x < limit) 
    x *= 2 
else if (x >= limit)
    x /=2;
//c) 
if (offer > demand)
    price *= 0.95;
else
    price *= 1.07;
//d) 
if (value >= 0);
    printf("positive value");
//e) 
if (color = red)
{
    color= green;
    printf("green\n");
}
```

2) Réécrire les instructions a), b) et c) avec l’opérateur ternaire **`?`** et **corriger les éventuelles erreurs**.

### Exercice 2 : minuscule ou majuscule
Écrire un programme qui détermine si le caractère qu'on tape est une minuscule (code ASCII compris entre 97 et 122) ou une majuscule (code compris entre 65 et 90).

{{< attention >}}
- Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
- L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

**Exemple 1**
```terminal
$ .\ch05_ex02_LowercaseUppercase.exe
Type a letter: u
lowercase
```

**Exemple 2**
```terminal
$ .\ch05_ex02_LowercaseUppercase.exe
Type a letter: F
UPPERCASE
```

**Exemple 3**
```terminal
$ .\ch05_ex02_LowercaseUppercase.exe
Type a letter: !
The character you entered is not a letter.
```

### Exercice 3 : signe d'un produit
Écrire un programme qui lit deux valeurs entières (a et b) au clavier et qui affiche le signe du produit (positif, négatif ou zéro) de a et b **sans faire la multiplication**.

{{< attention >}}
- Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
- L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

**Exemple 1**
```terminal
$ .\ch05_ex03_MultiplicationSign.exe
Please enter 2 integers: 1 2
1 * 2 > 0
```

**Exemple 2**
```terminal
$ .\ch05_ex03_MultiplicationSign.exe
Please enter 2 integers: 0 0
0 * 0 = 0
```

**Exemple 3**
```terminal
$ .\ch05_ex03_MultiplicationSign.exe
Please enter 2 integers: a b
Please enter 2 integers: b 1
Please enter 2 integers: -1 3
-1 * 3 < 0
```

### Exercice 4 : ordre décroissant
Écrire un programme qui affiche dans l'ordre décroissant trois nombres introduits au clavier par l'utilisateur.
Il s’agit d’échanger le contenu des variables de manière à mettre la plus grande valeur dans la première variable, la médiane dans la seconde et la plus petite dans la troisième.

{{< attention >}}
- Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
- L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

**Exemple 1**
```terminal
$ .\ch05_ex04_DecreasingOutput.exe
Please enter 3 integers separated by commas: 1,2,3
The 3 integers sorted in decreasing order: 3, 2, 1
```

**Exemple 2**
```terminal
$ .\ch05_ex04_DecreasingOutput.exe
Please enter 3 integers separated by commas: 1,-2,0
The 3 integers sorted in decreasing order: 1, 0, -2
```

**Exemple 3**
```terminal
$ .\ch05_ex04_DecreasingOutput.exe
Please enter 3 integers separated by commas: a,1,2
Please enter 3 integers separated by commas: 1, -9, c
Please enter 3 integers separated by commas: 0,0,0
The 3 integers sorted in decreasing order: 0, 0, 0
```

### Exercice 5 : signe d'une somme
Écrire un programme qui lit deux valeurs entières (a et b) au clavier et qui affiche le signe (positif, négatif ou zéro) de la somme de a et b sans faire l'addition. Au besoin, vous pouvez utiliser la fonction abs de la bibliothèque <stdlib.h>.

### Exercice 6 : maximum de trois valeurs
Écrire un programme qui lit trois valeurs entières (a, b et c) au clavier et qui affiche la plus grande des trois valeurs, en utilisant :
1. if - else et une variable d'aide max
2. if - else if - ... - else sans variable d'aide
3. les opérateurs ternaires et une variable d'aide max
4. les opérateurs ternaires sans variable d'aide

### Exercice 7 : équation du second degré
Écrire un programme qui calcule la ou les solutions réelles d'une équation du second degré de la forme suivante :

<center>
{{<katex>}}ax^{2}  + bx + c = 0{{</katex>}}
</center>

en utilisant la formule suivante :

<center>
{{<katex>}}x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}{{</katex>}}
</center>

Considérer aussi les cas où l'utilisateur entre :
- une valeur nulle pour a; 
- des valeurs nulles pour a et b; 
- des valeurs nulles pour a, b et c.
 
Afficher les résultats et les messages nécessaires sur l'écran.

{{< attention >}}
- Il faut afficher les réels avec 4 chiffres après la virgule.
- Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
- L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

**Exemple 1**
```terminal
$ .\ch05_ex07_SecondOrderEquation.exe
Compute solutions of an equation of the form ax^2 + bx + c = 0 
Please enter coefficients a, b, and c: 0 0 0
Any real is solution of this equation.
```

**Exemple 2**
```terminal
$ .\ch05_ex07_SecondOrderEquation.exe
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 1 1 
This equation has no real solution.
```

**Exemple 3**
```terminal
$ .\ch05_ex07_SecondOrderEquation.exe
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 1 -2
The real solutions of this equation are:
x1 = 1.0000
x2 = -2.0000
```

**Exemple 4**
```terminal
$ .\ch05_ex07_SecondOrderEquation.exe
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: a 1 2
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 b -2
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 2 -1 -2
The real solutions of this equation are:
x1 = 1.2808
x2 = -0.7808
```

### Exercice 21 : de `if` à `switch`
Remplacer l'instruction **`if`** suivante par une instruction **`switch`** équivalente et créer un programme pour vérifier cette transformation (le type de x est **`int`** ou **`char`**) :
```c
if (x == 0)
    printf("Error\n");
else
    printf("100/%d = %lf\n", x, 100./x);
```

### Exercice 22 : conversion de devises
Écrire un programme qui effectue la conversion en francs suisses d’une somme donnée en won (W), dollars ($), yens (Y) ou livres sterling (P).
Pour la saisie, utiliser l'instruction suivante :
```c
scanf(" %lf %c", &amount, &currency); // amount is a double
```

Pour les taux de changes, il faut utiliser les constantes suivantes :
```c
const double WON2CHF = 0.00070;
const double USD2CHF = 0.99;
const double YEN2CHF = 0.0067;
const double POUND2CHF = 1.13;
```

{{< attention >}}
- Il faut afficher les réels avec 3 décimales.
- Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
- L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

**Exemple 1**
```terminal
$ .\ch05_ex22_CurrencyConverter.exe
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 W
Swiss francs: 0.086
```

**Exemple 2**
```terminal
$ .\ch05_ex22_CurrencyConverter.exe
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 $
Swiss francs: 121.770
```

**Exemple 3**
```terminal
$ .\ch05_ex22_CurrencyConverter.exe
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: -123 Y
The input amount is negative!!
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 Y
Swiss francs: 0.824
```

**Exemple 4**
```terminal
$ .\ch05_ex22_CurrencyConverter.exe
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 L
Unsupported currency!!
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 123 P
Swiss francs: 138.990
```

**Exemple 5**
```terminal
$ .\ch05_ex22_CurrencyConverter.exe
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: d W
The input format is not correct!!
USAGE: non-negative value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount to convert: 122 W
Swiss francs: 0.085
```

### Exercice 23 : nombre de jours d'un mois
Écrire un programme qui demande à l'utilisateur le numéro d'un mois (1 pour janvier, 2 pour février, ...) et lui affiche le nombre de jours correspondant (31 jours en janvier, 28 en février, ...).

{{< attention >}}
- Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
- L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

**Exemple 1**
```terminal
$ .\ch05_ex23_DaysInMonth.exe
Please enter the number of the month (january=1, ... , december=12): 1
The 1th month has 31 days.
```

**Exemple 2**
```terminal
$ .\ch05_ex23_DaysInMonth.exe
Please enter the number of the month (january=1, ... , december=12): 12
The 12th month has 31 days.
```

**Exemple 3**
```terminal
$ .\ch05_ex23_DaysInMonth.exe
Please enter the number of the month (january=1, ... , december=12): 13
Please enter the number of the month (january=1, ... , december=12): 7
The 7th month has 31 days.
```

**Exemple 4**
```terminal
$ .\ch05_ex23_DaysInMonth.exe
Please enter the number of the month (january=1, ... , december=12): a
Please enter the number of the month (january=1, ... , december=12): b
Please enter the number of the month (january=1, ... , december=12): 0
Please enter the number of the month (january=1, ... , december=12): 8
The 8th month has 31 days.
```

### Exercice 24 : `switch` et `toupper`
Expliquer ce que fait le programme ci-dessous. Donner quelques exemples d'utilisation.

```c
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char choice;
    switch(choice = toupper(getchar()))
    {
    case 'R' : printf("RED");
    break;
    case 'V' : printf("GREEN");
    break;
    case 'B' : printf("BLUE");
    break;
    default : printf("Error");
    }
return 0 ;
}
```

### Exercice 31 : que font ces boucles ?
Expliquer ce que font les boucles suivantes :

**a)**
```c
    n = 1;
    while (n < 40) 
    {
      printf("value %d\n", n);
      n *= 2;
    }
```

**b)**
 ```c
   int count = 0;
   do
   {
     printf("%d ", count);
     ++count;
   }
   while (count% 8 != 0);
   ```

**c)** 
 ```c
    while (n == 0);
   ```

**d)** 
```c
   for (x = 0; x < 1000; ++x)
     printf("%d ", x);
   ```

**e)** 
```c
   for (money = 100; money < 10000; money *= 2.0)
     printf("Fortune = %f\n", money);
   ```

### Exercice 32 : somme, produit et moyenne
a) Écrire un programme qui lit N nombres entiers au clavier et qui affiche leur somme, leur produit et leur moyenne.
Choisissez un type approprié pour les valeurs à afficher.
Le nombre N est à entrer au clavier.
Il faut utiliser la boucle la plus appropriée.

{{< attention >}}
- Il faut afficher les réels avec 4 décimales.
- Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
- L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

b) Répéter l'introduction du nombre N jusqu'à ce que N ait une valeur entre 1 et 15.

**Exemple**
 ```terminal
 $ .\ch05_ex32_SumProductMean.exe
Number of values to read: 16
Number of values to read: 0
Number of values to read: -1
Number of values to read: 3
1. number: a
1. number: 1
2. number: b
2. number: 2
3. number: c
3. number: 3
Sum = 6
Product = 6
Mean = 2.0000
```

### Exercice 33 : factorielle
Calculer la factorielle {{<katex>}}N!{{</katex>}} d'un entier naturel N telle que :

<center>
{{<katex>}}N! = 1*2*3*...*(N-1)*N{{</katex>}}
</center>

et

<center>
{{<katex>}}0! = 1{{</katex>}}
</center>

{{< attention >}}
- Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
- L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

**Exemple 1**
```terminal
$ .\ch05_ex33_Factorial.exe
Please enter a positive integer N: 6
6! = 720
```

**Exemple 2**
```terminal
$ .\ch05_ex33_Factorial.exe
Please enter a positive integer N: -1
Please enter a positive integer N: a
Please enter a positive integer N: 6
6! = 720
```

### 🌶️ Exercice 34 : racine carrée
{{< notion_avancee >}}
a) Calculer la racine carrée x d'un nombre réel positif A par approximations successives en utilisant la relation de récurrence suivante :

<center>
{{<katex>}}X_{j+1} = (X_{j} + A/X_{j}) / 2{{</katex>}}
</center>

avec

<center>
{{<katex>}}X_{1} = A{{</katex>}}
</center>

L’utilisateur doit entrer la précision ɛ du calcul souhaitée.
Le programme doit s’arrêter lorsque {{<katex>}}|X_{j+1} - X_{j}| < \varepsilon{{</katex>}}.

b) Assurez-vous lors de l'introduction des données que la valeur pour A et ɛ sont des réels positifs.

c) Affichez lors du calcul toutes les approximations calculées : 
```
 The first square root approximation of ... is ...
 The second square root approximation of ... is ...
 The third square root approximation of ... is ...
 ...
 ```
{{< /notion_avancee >}}

### Exercice 35 : triangle d'étoiles
Afficher un triangle isocèle formé d'étoiles de N lignes (N est fourni au clavier) :

```terminal
line count: 8
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
```
### Exercice 36 : table de multiplication
Afficher la table des produits pour N variant de 1 à 10 :

```terminal
X*Y   I   0   1   2   3   4   5   6   7   8   9  10
---------------------------------------------------
 0    I   0   0   0   0   0   0   0   0   0   0   0
 1    I   0   1   2   3   4   5   6   7   8   9  10
 2    I   0   2   4   6   8  10  12  14  16  18  20
 3    I   0   3   6   9  12  15  18  21  24  27  30
 4    I   0   4   8  12  16  20  24  28  32  36  40
 5    I   0   5  10  15  20  25  30  35  40  45  50
 6    I   0   6  12  18  24  30  36  42  48  54  60
 7    I   0   7  14  21  28  35  42  49  56  63  70
 8    I   0   8  16  24  32  40  48  56  64  72  80
 9    I   0   9  18  27  36  45  54  63  72  81  90
10    I   0  10  20  30  40  50  60  70  80  90 100
```


Les colonnes sont alignées grâce au format %3d.

### Exercice 37 : FizzBuzz
Faire un programme affichant le résultat d'une partie de FizzBuzz (sans erreur) pour les nombres de 1 à 100.

Description du jeu:

_Les joueurs sont assis en cercle. Un joueur commence et dit le nombre "1" puis son voisin 
incrémente le nombre et le dit (donc "2"), puis … Cependant chaque fois que le nombre est 
divisible par 3, le joueur doit dire Fizz au lieu du nombre, et si le nombre est divisible par 5, il doit dire Buzz. Les nombres divisibles par 3 et par 5 deviendront Fizz Buzz. Le joueur qui se trompe est éliminé._

Un début de partie donnera donc les résultats suivants :
 ```
 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, 
 Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz
 ```

**AVANCÉ (optionnel) :** adapter le programme pour jouer au "BEUZEU".

### Exercice 41 : `switch` dans deux boucles
Qu'affiche ce programme :

```c
  #include <stdio.h>
  int main(void)
  {
    int i, j, x = 0 ;
    for (i = 0 ; i < 5 ; ++i)
    for (j = 0; j < i; ++j)
    {
      switch(i + j - 1)
      {
      case -1 :
      case 0  : x += 1;
                break;
      case 1  :
      case 2  :
      case 3  : x += 2;
                break;
      default : x += 3;
      }
   printf("%d ", x);
   }
   printf("\nx = %d\n", x);
   return 0;
}
```

### Exercice 42 : `switch` sans tous ses `break`
Qu'affiche ce programme : 

```c
  #include <stdio.h>
  
int main(void)
  {
    int i, j, x = 0;
    for (i = 0 ; i < 5 ; ++i)
      for (j = 0; j < i; ++j)
      {
        switch(i + j - 1)
        {
          case -1 :
          case 0  : x += 1;
                   break;
          case 1  :
          case 2  :
          case 3  : x += 2;
          default : x += 3;
       }
       printf("%d ", x);
   }
   printf("\nx = %d\n", x);
   return 0;
}
```

## Défis

### Opérateur ternaire et blocs

Le code suivant est-il correct en C ?

```c
int i = 1;

(i++ == 1) ? {printf("Hello\n"); } : {printf("World\n"); };
```

{{<details "Explications" >}}
Les blocs ne retournent pas de valeur, donc ne sont pas des expressions.
Ainsi, ils ne conviennent pas pour l'opérateur ternaire.

Il faut noter cependant que les fonctions retournent des valeurs (même si c'est `void`).
L'exemple suivant fonctionne donc parfaitement :

```c
int i = 1;
(i++ == 1) ? printf("Hello\n") : printf("World\n");
```
{{</details>}}

### Label de `case` dynamique (avec un appel de fonction)

Dans un `switch`, puis-je écrire un `case` dont la valeur provient d’un appel à une fonction qui retourne un `int` ?

Par exemple :

```c
int f(void) { return 2; }

int main(void)
{
    int x = 1;

    switch (x) {
        case f(): // ?
        printf("ok\n");
        break;
    }

    return 0;
}
```

{{<details "Explications" >}}
Non.
En effet, la norme dit :

> **6.8.4.2 The `switch` statement**
>
> The expression of each `case` label shall be an integer constant expression [...]

Donc les étiquettes `case` doivent être **des expressions constantes entières**, donc connues à la compilation.
Un appel de fonction est évalué **à l’exécution**, et est donc interdit dans une étiquette de `case`.

En particulier, GCC affiche l'erreur suivante (l'exemple complet n'active le `switch` fautif qu'avec `-DACTIVATE_ERRORS`) :

<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_05.97_CaseLabelFunctionCall_main.c run=true cflags="-DACTIVATE_ERRORS" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int f(void)
{
	return 2;
}

int main(void)
{
	int x = 2;

#ifdef ACTIVATE_ERRORS
	switch (x)
	{
	case f(): // ?
		printf("ok\n");
		break;
	}
#endif

	printf("x = %d\n", x);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -DACTIVATE_ERRORS -o main.exe main.c
main.c: In function 'main':
main.c:15:9: error: case label does not reduce to an integer constant
   15 |         case f(): // ?
      |         ^~~~
```
<p class="run-info">Compiled and executed on 2026-10-18 18:13 from 0114261.</p>
<!-- SNIPPET:END -->
{{</details>}}
