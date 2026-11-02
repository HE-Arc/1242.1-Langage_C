---
title: "7. Compilation et modularisation"
weight: 1
---

# CHAPITRE 7 : compilation et modularisation
## Slides
{{<slides "https://he-arc.github.io/1242.1-Langage_C-SLIDES/07_Compilation.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.1-Langage_C-SLIDES/07_Compilation.html?print-pdf)

## Étude de cas : ARGOS
Chaque exercice ARGOS est un module :
- `ex_NNNN_Nom.h` : le prototype de la fonction ;
- `ex_NNNN_Nom.c` : sa définition, à écrire ;
- `main.c` : un bac à sable qui appelle la fonction.

Exemple avec l'exercice `ex_0017_Factorial` : les mêmes sources donnent deux exécutables.

{{< plantuml src="diagrams/07_argos_compilation.puml" id="argos-compilation" />}}

- `main.exe` : `main.c` et le module `ex_0017_Factorial`, compilés à la main depuis le dossier de l'exercice :
  ```terminal
  $ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c ex_0017_Factorial.c
  ```
- `ex_0017_TEST.exe` : construit par `argos check`, avec le test, le module `ex_0017_Factorial` et des bibliothèques statiques. Le test a son propre `main` : `main.c` n'est pas utilisé.

## Exemples

### 07.01 : que fait le préprocesseur avec les macros et la compilation conditionnelle ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_07.01_Preprocessor_main.c run=true cflags="-Wno-error=sequence-point" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>
#include <stdlib.h>

#define PI 3.1466666

#define MAX_WRONG(x,y) x>y?x:y
#define MAX(x,y) ((x)>(y)?(x):(y))

#define SQUARE_WRONG(x) x*x
#define SQUARE(x) ((x)*(x))

// Displays informations when in Debug mode
void myNiceFunction(void)
{
	// NOTE:
	//	(since C99) __func__ is a const char *. It is NOT a macro.
	//  __FILE__ is a macro containing a string
	//  __LINE__ is a macro containing an integer
#ifdef DEBUG
	printf("Calling %s, in %s:%d\n", __func__, __FILE__, __LINE__);
#endif

	// DO SOMETHING GREAT HERE
}

int main(void)
{
	// Conditional-compilation
#ifdef MY_UNDEF_MACRO
	printf("Defined!\n");
#else
	printf("Undefined!\n");
#endif

	// Checking OS
	// SEE https://stackoverflow.com/questions/142508/how-do-i-check-os-with-a-preprocessor-directive
#ifdef _WIN32
	printf("Windows\n");
#elif __linux__
	printf("Linux\n");
#elif __APPLE__
	printf("Mac OSX\n");
#else
	printf("Unknown\n");
#endif

	// Using MACROS ==> see preprocessed source code.
	printf("PI: %lf\n", PI);
	printf("MAX WRONG: %d\n", 2 * MAX_WRONG(4, 6));
	printf("MAX: %d\n", 2 * MAX(4, 6));

	printf("SQUARE WRONG: %d\n", 2 * SQUARE_WRONG(3+2));
	printf("SQUARE: %d\n", 2 * SQUARE(3 + 2));

	// IMPORTANT: no side-effects in parameters of a macro!!!
	int x = 1;
	printf("SQUARE: %d\n", SQUARE(++x));
	// expands to ((++x) * (++x))
	// => several modifications of x between 2 sequence points
	// => UB

	myNiceFunction();

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=sequence-point -o main.exe main.c
main.c: In function 'main':
main.c:57:39: warning: operation on 'x' may be undefined [-Wsequence-point]
   57 |         printf("SQUARE: %d\n", SQUARE(++x));
      |                                       ^
main.c:10:21: note: in definition of macro 'SQUARE'
   10 | #define SQUARE(x) ((x)*(x))
      |                     ^
$ ./main.exe
Undefined!
Windows
PI: 3.146667
MAX WRONG: 4
MAX: 12
SQUARE WRONG: 14
SQUARE: 50
SQUARE: 9
```
<p class="run-info">Compiled and executed on 2026-11-02 22:10 from c162b8e.</p>
<!-- SNIPPET:END -->

{{< attention >}}
**`SQUARE(++x)`** devient **`((++x)*(++x))`** : **`x`** est modifié deux fois sans point de séquence, c'est un comportement indéfini (UB). gcc le signale (**`-Wsequence-point`**) et la valeur affichée n'est pas garantie. Jamais d'effet de bord dans l'argument d'une macro.
{{< /attention >}}

### 07.02 : à quoi ressemble un programme en assembleur ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_07.02_Assembly_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
int main(void)
{
	int myVariable = 42;

	if (myVariable == 43)
	{
		myVariable -= 1;
	}
	else
	{
		myVariable += 1;
	}

	// Test with switch
	int value = 1;
	switch (value)
	{
	case 1: value = 10; break;
	case 2: value = 100; break;
	case 3: value = 1000; break;
	case 4: value = 10000; break;
	case 5: value = 100000; break;
	default: value = 0;
	}

	return value;
}
```
<!-- SNIPPET:END -->

L'option **`-S`** arrête gcc après la compilation : **`gcc -S main.c`** produit le fichier assembleur **`main.s`**.

### 07.03 : comment découper un programme en modules ?
<!-- SNIPPET:BEGIN source_file=hello.h id=1242.1_Exemples_07.03_Modules_avec_CMake_hello.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `hello.h`**

```c
#ifndef HELLO_H
#define HELLO_H

void printHello(void);

#endif
```
<!-- SNIPPET:END -->
<!-- SNIPPET:BEGIN source_file=hello.c id=1242.1_Exemples_07.03_Modules_avec_CMake_hello.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `hello.c`**

```c
#include <stdio.h>
#include "hello.h"

void printHello(void)
{
	printf("Hello ");
}
```
<!-- SNIPPET:END -->
<!-- SNIPPET:BEGIN source_file=world.h id=1242.1_Exemples_07.03_Modules_avec_CMake_world.h -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `world.h`**

```c
#ifndef WORLD_H
#define WORLD_H

void printWorld(void);

#endif
```
<!-- SNIPPET:END -->
<!-- SNIPPET:BEGIN source_file=world.c id=1242.1_Exemples_07.03_Modules_avec_CMake_world.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `world.c`**

```c
#include <stdio.h>
#include "world.h"

void printWorld(void)
{
	printf("world\n");
}
```
<!-- SNIPPET:END -->
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_07.03_Modules_avec_CMake_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include "hello.h"
#include "world.h"

int main(void)
{
	printHello();
	printWorld();

	return 0;
}
```
<!-- SNIPPET:END -->

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c hello.c world.c
$ ./main.exe
Hello world
```

### 07.99 : quel compilateur et quelle norme C sont utilisés ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_07.99_Preprocessor_Current_Compiler_Version_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
#ifdef _MSC_VER
  printf("Current compiler is Visual Studio ");

  // Now print which specific version of the compiler we are running
  // SEE: https://docs.microsoft.com/en-us/cpp/preprocessor/predefined-macros?view=msvc-160
  switch (_MSC_VER)
  {
  case 800:
  case 900:
  case 1000:
  case 1020:
  case 1100:
  case 1200:
  case 1300:
  case 1310:
  case 1400:
  case 1500:
  case 1600:
  case 1700:
  case 1800:
    printf("2013 and prior\n");
    break;
  case 1900:
    printf("2015\n");
    break;
  case 1910:
  case 1911:
  case 1912:
  case 1913:
  case 1914:
  case 1915:
  case 1916:
    printf("2017\n");
    break;
  case 1920:
  case 1921:
  case 1922:
  case 1923:
  case 1924:
  case 1925:
  case 1926:
  case 1927:
  case 1928:
    printf("2019\n");
    break;
  default:
    printf("Unrecognized version for Visual Studio: %d\n", _MSC_VER);
  }
#elif __GNUC__
  printf("Current compiler is GCC %d.%d.%d\n", __GNUC__, __GNUC_MINOR__, __GNUC_PATCHLEVEL__);

#ifdef __STDC_VERSION__
  printf("C standard is %ld \n", __STDC_VERSION__);
#endif
#endif

  return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
Current compiler is GCC 15.2.0
C standard is 202311
```
<p class="run-info">Compiled and executed on 2026-11-02 22:10 from c162b8e.</p>
<!-- SNIPPET:END -->

## Défis

### Macro `SQUARE` sans parenthèses
Que fait le programme suivant ? Pourquoi ? Que faut-il modifier pour qu'il fonctionne correctement ?

<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_07.98_MacroWithoutParentheses_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

#define SQUARE(x) x * x

int main(void)
{
  int a = 5;
  int b = SQUARE(a + 1);
  printf("b = %d\n", b);

  return 0;
}
```
<!-- SNIPPET:END -->

{{< details "Explications" >}}
Le programme affiche **`b = 11`** et non **`b = 36`**. Le préprocesseur remplace le texte sans tenir compte des priorités : **`SQUARE(a + 1)`** devient **`a + 1 * a + 1`**, soit **`5 + 5 + 1`**.

Il faut entourer de parenthèses chaque argument et l'expression entière de la macro :

<!-- SNIPPET:BEGIN source_file=main_fixed.c id=1242.1_Exemples_07.98_MacroWithoutParentheses_main_fixed.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main_fixed.c`**

```c
#include <stdio.h>

#define SQUARE(x) ((x) * (x))

int main(void)
{
  int a = 5;
  int b = SQUARE(a + 1);
  printf("b = %d\n", b);

  return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main_fixed.exe main_fixed.c
$ ./main_fixed.exe
b = 36
```
<p class="run-info">Compiled and executed on 2026-11-02 22:16 from c162b8e.</p>
<!-- SNIPPET:END -->

**`SQUARE(a + 1)`** devient alors **`((a + 1) * (a + 1))`**.
{{< /details >}}
