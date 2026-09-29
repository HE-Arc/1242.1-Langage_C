---
title: "3. Opérateurs"
weight: 1
---

# CHAPITRE 3 : opérateurs

## Slides
{{<slides "https://he-arc.github.io/1242.1-Langage_C-SLIDES/03_Operateurs.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.1-Langage_C-SLIDES/03_Operateurs.html?print-pdf)

## Squelette à remplir
{{<a_faire>}}
Remplir le squelette suivant au fur et à mesure du cours.
{{</a_faire>}}
<!-- SNIPPET:BEGIN source_file=chap3.c id=1242.1_Skeletons_03_chap3.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `chap3.c`**

```c
#include <stdio.h>

// CHAPTER 3

int main(void)
{
	// Experiment with modulo

	// Experiment with arithmetic operators

	// Experiment with overflow

	// Experiment with division operator

	// Conversions

	// Increment / Decrement operators

	// Experiment with comma operator

	// Experiment with logical operators

	// Experiment with bitwise operators

	// Experiment with bit shifts

	return 0;
}
```
<!-- SNIPPET:END -->

## Exemples

### 03.01 : que donne l'opérateur modulo `%` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.01_Modulo_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

#define ACTIVATE_WARNINGS_AND_ERRORS 0

int main(void)
{
	int a;

	a = 10 % 2;
	printf("%d\n", a);

	a = 10 % 3;
	printf("%d\n", a);

	a = 10 % 10;
	printf("%d\n", a);

	a = 5 % 10;
	printf("%d\n", a);

	// SEE standard page 494.
	// "The behavior is undefined in the following circumstances: [..]
	//	- The value of the second operand of the / or % operator is zero (6.5.5)."
#if ACTIVATE_WARNINGS_AND_ERRORS
	a = 10 % 0; // ERROR with VS: this is an UB according to standard.
	printf("%d\n", a);
#endif

	a = 0 % 10;
	printf("%d\n", a);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
0
1
0
5
0
```
<p class="run-info">Compiled and executed on 2026-09-25 09:40 from c153709.</p>
<!-- SNIPPET:END -->

### 03.02 : dans quel ordre les opérateurs arithmétiques sont-ils évalués ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.02_Arithmetic_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	int a = 0;

	a = (10 + 6) / (3 - 1);
	printf("%d\n", a);

	a = (10 + 6) / 3 - 1;
	printf("%d\n", a);

	a = 10 + 6 / (3 - 1);
	printf("%d\n", a);

	a = 10 + 6 / 3 - 1;
	printf("%d\n", a);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
8
4
13
11
```
<p class="run-info">Compiled and executed on 2026-09-25 09:40 from c153709.</p>
<!-- SNIPPET:END -->

### 03.03 : que se passe-t-il en cas de dépassement de capacité ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.03_Overflow_main.c run=true cflags="-Wno-error=overflow" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>
#include <math.h> // Needed for HUGE_VAL

#define ACTIVATE_WARNINGS_AND_ERRORS 0

int main(void)
{
	unsigned char a;
  // NOTE: gcc warning: overflow in conversion from 'int' to 'unsigned char' changes value from '256' to '0' [-Woverflow]
	a = 255 + 1;
	printf("%d\n", a);

	char b;
	b = 127 + 1;
	printf("%d\n", b);

	// UB, compile error with VS
#if ACTIVATE_WARNINGS_AND_ERRORS
	double testWithLiteral = 1 / 0.;
#endif

	// UB, compile error with VS
#if ACTIVATE_WARNINGS_AND_ERRORS
#define ZERO 0.0;
	double testWithMacro = 1. / ZERO;
#endif

	// OK with VS but returns infinity
	const double zero = 0.0;
	double testWithVariable = 1. / zero;
	printf("%lf\n", testWithVariable);

	double x = HUGE_VAL;
	printf("%lf %lf\n", x, -HUGE_VAL);

	double y = x / x;
	printf("%lf %lf\n", y, -HUGE_VAL / HUGE_VAL);

	double z = 1 / HUGE_VAL;
	printf("%lf\n", z);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=overflow -o main.exe main.c
main.c: In function 'main':
main.c:10:13: warning: unsigned conversion from 'int' to 'unsigned char' changes value from '256' to '0' [-Woverflow]
   10 |         a = 255 + 1;
      |             ^~~
main.c:14:13: warning: overflow in conversion from 'int' to 'char' changes value from '128' to '-128' [-Woverflow]
   14 |         b = 127 + 1;
      |             ^~~
$ ./main.exe
0
-128
inf
inf -inf
-nan(ind) -nan(ind)
0.000000
```
<p class="run-info">Compiled and executed on 2026-09-25 10:52 from c153709.</p>
<!-- SNIPPET:END -->

### 03.04 : quel est le résultat d'une division entre entiers ou entre flottants ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.04_Division_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>
#include <math.h> // Needed for HUGE_VAL

int main(void)
{
	int   i1 = 5, i2 = 2, i3;
	float f1 = 5., f2 = 2., f3;

	f3 = f1 / f2;
	printf("%f\n", f3);

	i3 = i1 / i2;
	printf("%d\n", i3);

	f3 = i1 / i2; // WARNING: converting an int into a float
	printf("%f\n", f3);

	i3 = f1 / f2; // WARNING: converting a float into an int
	printf("%d\n", i3);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
2.500000
2
2.000000
2
```
<p class="run-info">Compiled and executed on 2026-09-25 09:40 from c153709.</p>
<!-- SNIPPET:END -->

### 03.05 : quand les conversions implicites et explicites ont-elles lieu ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.05_Conversions_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	{
		int x = 5;
		int y = 2;
		int r;
		r = x / y;
		printf("%d\n", r);
	}
	{
		int x = 5;
		int y = 2;
		float r;
		r = x / y; // WARNING: converting an int into a float
		printf("%f\n", r);
	}
	{
		int x = 5;
		int y = 2;
		float r;
		r = (float)x / y;
		printf("%f\n", r);
	}
	{
		float x = 5;
		int y = 2;
		int r;
		r = x / y; // WARNING: converting a float into an int
		printf("%d\n", r);
	}
	{
		float x = 5;
		int y = 2;
		float r;
		r = x / y;
		printf("%f\n", r);
	}
	{
		int x = 5;
		int y = 2;
		float r;
		r = (float)(x / y);
		printf("%f\n", r);
	}

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
2
2.000000
2.500000
2
2.500000
2.000000
```
<p class="run-info">Compiled and executed on 2026-09-25 09:40 from c153709.</p>
<!-- SNIPPET:END -->

### 03.06 : que se passe-t-il quand on mélange les types dans un calcul ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.06_ConversionsOverflow_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
// This programs uses various operations using variables and mixing types
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	double result1, result2;
	long result3;
	unsigned int result4;
	result1 = 4. / 3;    // Division: double -> double
	result2 = 4 / 3;     // Division: int -> double
	result3 = result1;   // double -> long
	result4 = -result1;  // double -> unsigned int
	printf("double:         4. / 3  = %lg\n", result1);
	printf("double:         4  / 3  = %lg\n", result2);
	printf("long:           4. / 3  = %ld\n", result3);
	printf("unsigned int: -(4. / 3) = %u\n", result4);	// (2^32) - 1

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
double:         4. / 3  = 1.33333
double:         4  / 3  = 1
long:           4. / 3  = 1
unsigned int: -(4. / 3) = 4294967295
```
<p class="run-info">Compiled and executed on 2026-09-25 09:40 from c153709.</p>
<!-- SNIPPET:END -->

{{< attention >}}
**`result4 = -result1;`** est un comportement indéfini (UB) : convertir un **`double`** négatif en **`unsigned int`** n'est pas défini par la norme. La valeur **`4294967295`** affichée ici n'est pas garantie : un autre compilateur, une autre plateforme ou d'autres options peuvent donner un autre résultat.
{{< /attention >}}

### 03.07 : quelle différence entre `++x` et `x++` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.07_Increment_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	{
		int x = 6, y;
		y = ++x;
		printf("%d\n", y);
	}
	{
		int x = 6, y;
		y = x++;
		printf("%d\n", y);
	}
	{
		int x = 6, y;
		y = --x;
		printf("%d\n", y);
	}
	{
		int x = 6, y;
		y = x--;
		printf("%d\n", y);
	}

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
7
6
5
6
```
<p class="run-info">Compiled and executed on 2026-09-25 09:40 from c153709.</p>
<!-- SNIPPET:END -->

### 03.08 : comment isoler des bits avec l'opérateur `&` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.08_Bitwise_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	unsigned char x = 0xAA; // 1010 1010

	printf("%X\n", x); 
	printf("%X\n", x & 0xFF); 
	printf("%X\n", x & 0x01); 
	printf("%X\n", x & 0x03);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
AA
AA
0
2
```
<p class="run-info">Compiled and executed on 2026-09-25 09:40 from c153709.</p>
<!-- SNIPPET:END -->

### 03.96 : que se passe-t-il quand on convertit une valeur trop grande pour un `char` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.96_CastAndOverflow_main.c run=true cflags="-Wno-error=overflow" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	// Cast 128 into a char (8 bits) => overflow
	printf("c1 = %d\n", (char)128);
	char c1 = 128;
	printf("c1 = %d\n", c1);

	// Cast 128.99 into a char (8 bits)
	// Undefined Behavior
	// SEE: https://stackoverflow.com/questions/14774540/implicitly-casting-a-float-constant

	// 1) Undefined Behavior
	// Here, the value is first stored in a variable.
	// So the compiler will just cast at runtime and that will overflow.
	double d2 = 128.99;
	char c2 = (char) d2;
	printf("d2 = %lf\n", d2);
	printf("c2 = %d\n", (char) c2);

	// 2) Undefined Behavior
	// Here, the compiler converts the constant 128.99 itself, at compile time.
	// 128 is not representable on a char, and the C standard does not say what to do then.
	// So the result depends on the compiler version:
	// - gcc <= 14 clamps the value to the maximum value possible, that is 127.
	// - gcc >= 15 gives the same result as the runtime conversion above, that is -128.
	// Same source code, different outputs: this is what Undefined Behavior means.
	double d3 = (char) 128.99;
	char c3 = (char) d3;
	printf("d3 = %lf\n", d3);
	printf("c3 = %d\n", (char) c3);
	printf("c3 = %d\n", (char) 128.99);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=overflow -o main.exe main.c
main.c: In function 'main':
main.c:7:19: warning: overflow in conversion from 'int' to 'char' changes value from '128' to '-128' [-Woverflow]
    7 |         char c1 = 128;
      |                   ^~~
$ ./main.exe
c1 = -128
c1 = -128
d2 = 128.990000
c2 = -128
d3 = -128.000000
c3 = -128
c3 = -128
```
<p class="run-info">Compiled and executed on 2026-09-25 13:04 from c153709.</p>
<!-- SNIPPET:END -->

### 03.98 : comment utiliser l'opérateur conditionnel `? :` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.98_Conditional_main.c run=true cflags="-Wno-unused-variable" -->
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

	// It obviously also works without parenthesis
	max = (a > b) ? a : b;
	printf("Max: %d\n", max);

	// Q: can we nest ternary operator?
	// A: yes. A ternary operator needs expression as operands.
	//    So, as a ternary operator is an expression, it can contain
	//    other ternary operators
	int value = 100;
	int quarter = value > 50 ? (value > 75 ? 4 : 3) : (value <= 25 ? 1 : 2);

	// It even works without parenthesis, but it is less readible
	int quarter2 = value > 50 ? value > 75 ? 4 : 3 : value <= 25 ? 1 : 2;

	// Q: why cannot we use blocks inside conditional operator?
	// A:
	//   ISO C standard
	//     6.5.15 Conditional operator
	//       "...the result is the value of the second or third operand	(whichever is evaluated), converted to the type described below..."
	//       ==>> blocks do not return values, expressions do.

	//  - VS: error C2059:  syntax error: '{'
	//  - GCC: error: expected expression before '{' token
	int i = 1;

#if ACTIVATE_WARNINGS_AND_ERRORS
	(i++ == 1) ? {printf("Hello\n"); } : {printf("World\n"); };
#endif

	//  - VS: error C2059:  syntax error: '{'
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
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-unused-variable -o main.exe main.c
$ ./main.exe
Min / max: 3 / 9
Max: 9
Hello
r: 1
l2r: 3
r2l: 1
Associativity: right-to-left
```
<p class="run-info">Compiled and executed on 2026-09-25 10:52 from c153709.</p>
<!-- SNIPPET:END -->

### 03.99 : comment fonctionne l'opérateur virgule ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.99_Comma_main.c run=true cflags="-Wno-error=unused-value -Wno-unused-variable" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	// The comma operator ',' is a binary operator with the lowest priority.
	// It uses two steps:
	// 1) it evaluates the first part (before the comma) and ignores the result;
	// 2) it evaluates the second part (after the comma) and returns the result (with the associated type!)

	float a = 5.2; // Warning	C4305 'initializing': truncation from 'double' to 'float'

	// Corner case (With VS): no warning because 5.5 can be exactly represented as a float
	float a_bis = 5.5;

	double b = 10.1;

	a = b; // Warning C4244 '=': conversion from 'double' to 'float', possible loss of data
	
	// , has the lowest priority, so it is the same as doing:
	// 1) a = a
	// 2) evalute b
	// => no problem here.
	a = a, b;

	// Here, we enforce the comma operator evaluation first using ().
	// So it is the same as:
	// 1) (a, b)
	//		1.1) evaluate a
	//		1.2) evaluate b and return the result AND its type
	// So the final type of (a, b) is the type of b, that is double
	// 2) then we do a = (a, b), and this affects a double to a float.
	a = (a, b); // Warning C4244 '=': conversion from 'double' to 'float', possible loss of data

	// QUESTION: what happens if we do:
	a, b = b, a; // OK, double affected to double

	// QUESTION: what happens if we do:
	a, b = a, b; // OK, float affected to double

	// QUESTION: what happens if we do:
	b, a = b, a; // Warning C4244 '=': conversion from 'double' to 'float', possible loss of data

	// QUESTION: what happens if we do:
	b, a = a, b; // OK, float affected to float.

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=unused-value -Wno-unused-variable -o main.exe main.c
main.c: In function 'main':
main.c:23:14: warning: right-hand operand of comma expression has no effect [-Wunused-value]
   23 |         a = a, b;
      |              ^
main.c:32:15: warning: left-hand operand of comma expression has no effect [-Wunused-value]
   32 |         a = (a, b); // Warning C4244 '=': conversion from 'double' to 'float', possible loss of data
      |               ^
main.c:35:10: warning: left-hand operand of comma expression has no effect [-Wunused-value]
   35 |         a, b = b, a; // OK, double affected to double
      |          ^
main.c:35:17: warning: right-hand operand of comma expression has no effect [-Wunused-value]
   35 |         a, b = b, a; // OK, double affected to double
      |                 ^
main.c:38:10: warning: left-hand operand of comma expression has no effect [-Wunused-value]
   38 |         a, b = a, b; // OK, float affected to double
      |          ^
main.c:38:17: warning: right-hand operand of comma expression has no effect [-Wunused-value]
   38 |         a, b = a, b; // OK, float affected to double
      |                 ^
main.c:41:10: warning: left-hand operand of comma expression has no effect [-Wunused-value]
   41 |         b, a = b, a; // Warning C4244 '=': conversion from 'double' to 'float', possible loss of data
      |          ^
main.c:41:17: warning: right-hand operand of comma expression has no effect [-Wunused-value]
   41 |         b, a = b, a; // Warning C4244 '=': conversion from 'double' to 'float', possible loss of data
      |                 ^
main.c:44:10: warning: left-hand operand of comma expression has no effect [-Wunused-value]
   44 |         b, a = a, b; // OK, float affected to float.
      |          ^
main.c:44:17: warning: right-hand operand of comma expression has no effect [-Wunused-value]
   44 |         b, a = a, b; // OK, float affected to float.
      |                 ^
$ ./main.exe
```
<p class="run-info">Compiled and executed on 2026-09-25 10:52 from c153709.</p>
<!-- SNIPPET:END -->

## Exercices

### Exercice 1 : assignation / affectation
A) Réécrire les instructions suivantes en utilisant des opérateurs d'affectation composés.

```c
memory = memory + 1;	
word = word * 8;	
currency = currency - 1;	
a = a % b;	
part = part / nb_persons;	
```

B) Quelles sont les valeurs des variables **`x`**, **`y`** et **`z`** ?

```c
int x = 10;
int y, z;
x *= y = z = 4;
```

### Exercice 2 : opérateurs arithmétiques

A) Addition et division : quelle est la valeur de la variable **`x`** ?

```c
int n = 5, p = 9;
float x;

x = p / n ;	
x = (float) p / n ;	
x = (p + 0.5) / n ;	
x = (int) (p + 0.5) / n ; 	
```

B) Modulo : quelle est la valeur de la variable **`a`** ?

```c
int a;
a = 10 % 10; 
a =  5 % 10; 
a = 10 %  0; 
a =  0 % 10; 
```

### Exercice 3 : opérateurs d’incrémentation

Quelles sont les valeurs des variables **`x`**, **`y`** et **`z`** ?

```c
int x = 2, y = 1, z = 3;
z += -x++ + ++y;
```

### Exercice 4 : opérateurs de comparaison et logique
A) Évaluer les expressions suivantes :

**`3 <= 2-1`**

**`3 * (4 > 4) + 2.5`**

**`(4 == 5.1) / 2 + 1`**

**`true && false || true`**

**`3 + (n > n - 1)`**

**`!true && false || !false`**

**RAPPEL :** il faut inclure **`<stdbool.h>`** pour utiliser les valeurs **`true`** et **`false`**.

B) Assigner à une variable booléenne b. La valeur est vraie si la variable **`x`** est comprise entre 5 et 10, fausse sinon.

{{<katex>}}
b =
\begin{cases}
vrai  & \quad \text{si $x \in [5..10]$}\\ 
faux  & \quad \text{sinon}
\end{cases}
{{</katex>}}

C) Assignez à une variable booléenne b. La valeur est vraie si la variable x n’est pas comprise entre 5 et 10, fausse sinon.

{{<katex>}}
b =
\begin{cases}
vrai  & \quad \text{si $x \notin [5..10]$}\\ 
faux  & \quad \text{sinon}
\end{cases}
{{</katex>}}

### Exercice 5 : divers opérateurs

A) Que vaut **`q`** :

```c
int n = 5, p = 9;
int q;
float x;
q = n < p ;	/* 1 */
q = n == p ;	/* 2 */
q = p % n + (p > n) ;	/* 3 */
```

B) Quels résultats fournit le programme suivant :

```c
int n = 10, p = 5, q = 10, r ;
r = n == (p = q) ;
n = p = q = 5;
n += p += q ;
```

C) Donner les résultats des calculs suivants et en préciser le type :

a) **`3.5 * 6`**

b) **`243 * -83`**

c) **`(int)(20.35 * 24)`**

d) **`(int)85.35 * 2`**

e) **`'w' - 2024`**

f) **`(char)(23 / 9)`**

D) Quel doit être le type de **`var`** pour que les affectations suivantes ne provoquent pas d'erreur d'arrondi :

a) **`var = 12 + 'g';`**

b) **`var = (1 < 3);`**

c) **`var = 13 - 274.3;`**

d) **`var += 2.5;`**

e) **`var = 255 + 1;`**

f) **`var = 2 / 7.;`**

E) Donner la valeur de la variable **`x`** (de type **`int`**) après chaque instruction de la séquence de programme suivante (pour chaque instruction, la valeur de **`x`** est celle calculée à l'instruction précédente).
Indiquer également s'il y a des comportements indéfinis (UB) :

```c
x = 2;
x = 3 + (3 > x);
x += x -= 2;
x = (++x - 6) * 3;
x *= (5 > x) * (3 + 23);
```

F) Dans les expressions suivantes, repérer les parenthèses inutiles.

a) **`a = (x * w) + 3;`**

b) **`f *= 15 - (3 + f);`**

c) **`g = (g++ + g) * 3;`**

d) **`m = k > (b || 1);`**

e) **`h = (n += 12);`**

f) **`b *= (20 + 3);`**

### Exercice 6 : opérateurs bit à bit

A) Écrire un programme qui met i) les deux bits de poids forts à 1 et ii) les deux bits de poids faible à 0.

**Exemple :**
 
```c
unsigned char x = 0xAA; // 1010 1010
```
devient **11**1010**00**

B) Écrire un programme qui affiche le contenu des bits 3, 4 et 5 de la variable **`x`**. 10**011**010 doit afficher 3.
 
C) Soit la déclaration de variable suivante :

```c
unsigned int x=0x03020100;
```

Écrire un programme qui décompose la variable **`x`** en 4 variables **`b0`**, **`b1`**, **`b2`**, **`b3`** contenant les 4 bytes de **`x`**.

### Exercice 7 : débordement

A) Décrire ce qui se passe lorsque la valeur d'une variable dépasse sa valeur maximale admise dans le programme suivant :

```c
printf("INT_MAX: %d  INT_MAX+1: %d\n", INT_MAX,INT_MAX+1);
printf("DBL_MAX: %g\n",      DBL_MAX);
printf("DBL_MAX+1000: %g\n", DBL_MAX+1000);
printf("DBL_MAX*2   : %g\n", DBL_MAX*2);

printf("q = 1/0: %f  \n", 1/0);
float q  =  1.0f/0;
printf("q = 1.0f/0: %f  \n", q);
printf("1/q       : %f  \n", 1/q);
printf("q/q       : %f  \n", q/q);

printf("sqrt(-1)  : %f  \n", sqrt(-1));
```

## Défis

### **`i = i++`**

Les expressions suivantes sont-elles correctes en C ?
Pourquoi ?

```c
i = ++i;
i = i++;
j = ++i + i++;
i = (++i, i++);
```

{{<details "Explications" >}}
Pour le comprendre, il faut savoir ce qu'est un point de séquence en C (voir la FAQ [Qu’est-ce qu’un point de séquence en C ?]({{< relref "/docs/cours/faq/#quest-ce-quun-point-de-s%c3%a9quence-en-c-" >}})).

En particulier, entre 2 points de séquence, il n'y a aucune garantie sur l'ordre dans lequel les effets de bord (modifications de variables) seront effectués.
Par conséquent, toute expression qui modifie 2 fois la même variable entre 2 points de séquence est un comportement indéfini (UB) en C.

Avec l'option **`-Wall`**, **GCC** signale ces expressions par un warning **`-Wsequence-point`** (voir la compilation de l'exemple complet ci-dessous).

{{<a_noter>}}
L'opérateur **`,`** (virgule, ou comma en anglais) introduit un point de séquence entre chaque **`,`**.
Donc le code suivant n'est pas un UB :
  
  ```c
  j = (++i, i++);
  ```
{{</a_noter>}}

Voici un exemple complet :

<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_03.97_SequencePointsAndUB_main.c run=true cflags="-Wno-error=sequence-point" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int sum(int a, int b)
{
  return a + b;
}

int main(void)
{
  int i = 0;
  int j = ++i; // OK

  // Undefined Behavior (UB)
  // Same variable (i) is modified multiple times (or modified and read) without a sequence point.
  // GCC warns: operation on 'i' may be undefined [-Wsequence-point]
  i = ++i;          // UB: modify i and assign to i without sequence point
  i = i++;          // UB: idem
  j = ++i + i++;    // UB: no sequence point between operands of +

  // OK
  // Comma operator: there IS a sequence point between its two operands.
  // We end up modifying i only once after the last sequence point.
  j = ++i;          // OK: single modification, trivial
  j = (++i, i++);   // OK: comma sequences ++i before i++; assign to j (not to i)

  // Undefined Behavior (UB)
  i = (++i, i++);   // UB: after the comma, i is modified twice without a sequence point
  
  // Undefined Behavior (UB)
  // There is NO sequence point after closing parenthesis and + has none between its operands.
  j = (++i, i++) + ++i;  // UB: read/modify i again on the right operand with no sequencing

  // Undefined Behavior (UB)
  // There is NO sequence point between the evaluations of function-call arguments.
  j = sum(i, ++i);  // UB: read i and modify i without sequencing
  j = sum(i, i++);  // UB: idem

  // With the UBs above, the output is meaningless.
  printf("i = %d, j = %d\n", i, j);

  return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=sequence-point -o main.exe main.c
main.c: In function 'main':
main.c:16:5: warning: operation on 'i' may be undefined [-Wsequence-point]
   16 |   i = ++i;          // UB: modify i and assign to i without sequence point
      |   ~~^~~~~
main.c:17:5: warning: operation on 'i' may be undefined [-Wsequence-point]
   17 |   i = i++;          // UB: idem
      |   ~~^~~~~
main.c:18:7: warning: operation on 'i' may be undefined [-Wsequence-point]
   18 |   j = ++i + i++;    // UB: no sequence point between operands of +
      |       ^~~
main.c:27:5: warning: operation on 'i' may be undefined [-Wsequence-point]
   27 |   i = (++i, i++);   // UB: after the comma, i is modified twice without a sequence point
      |   ~~^~~~~~~~~~~~
main.c:31:20: warning: operation on 'i' may be undefined [-Wsequence-point]
   31 |   j = (++i, i++) + ++i;  // UB: read/modify i again on the right operand with no sequencing
      |                    ^~~
main.c:35:14: warning: operation on 'i' may be undefined [-Wsequence-point]
   35 |   j = sum(i, ++i);  // UB: read i and modify i without sequencing
      |              ^~~
main.c:36:15: warning: operation on 'i' may be undefined [-Wsequence-point]
   36 |   j = sum(i, i++);  // UB: idem
      |              ~^~
$ ./main.exe
i = 13, j = 25
```
<p class="run-info">Compiled and executed on 2026-09-25 10:52 from c153709.</p>
<!-- SNIPPET:END -->
{{</details>}}