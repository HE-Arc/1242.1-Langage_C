---
title: "8. Tableaux et structures"
weight: 1
---

# CHAPITRE 8 : Tableaux et structures

## Slides
{{<slides "https://he-arc.github.io/1242.1-Langage_C-SLIDES/08_TableauxStructures.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.1-Langage_C-SLIDES/08_TableauxStructures.html?print-pdf)

## Squelette à remplir
{{<a_faire>}}
Remplir le squelette suivant au fur et à mesure du cours.
{{</a_faire>}}
<!-- SNIPPET:BEGIN source_file=chap8.c id=1242.1_Skeletons_08_chap8.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `chap8.c`**

```c
#include <stdio.h>

// CHAPTER 8

int main(void)
{
	// 1) Array declaration
	// Use a #define to create a new array (and output its size)
	// Use a const int to create a new array (and output its size)
	// Use an int read using scanf to create a new array (and output its size)

	// 2) Array initialization
	// Use constant size
	// Use a variable-sized array
	// Do NOT specify size but initialize array with constant values.

	// 3) copy values from one array to another one

	// 4) print values outside array boundaries
	// => what happens when we try to print values with negative indices

	// 5) create an array with constant values
	// => what happens when you try to change a value after initialization

	// 6) How to know the number of elements in an array, in a type-independent way?

	// 7) Create, initialize and access values in a multi-dimensional array

	// 8) Experiment with strings in C

	// 9) Print a C string created and initialized with another C string
	// 10) Print a C string created and initialized with an array of chars
	// => What happens if array does not explicitly ends with \0?

	// 11) Experiment with C string manipulation with string.h library

	// 12) Declare a struct type, initialize a variable of this type, access its members and copy it

	// 13) Use typedef to give the struct type a shorter name




	return 0;
}
```
<!-- SNIPPET:END -->

## Exemples

### 08.01 : comment déclarer un tableau et fixer sa taille ?
<!-- SNIPPET:BEGIN source_file=01_ArraysDeclarations.c id=1242.1_Exemples_08.01_Arrays_Structures_01_ArraysDeclarations.c run=true stdin="5" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `01_ArraysDeclarations.c`**

```c
#include <stdio.h>

#define NMAX 32

int main(void)
{
	double price[NMAX];
	printf("Array \"price\" has a size of %d\n", (int)(sizeof(price) / sizeof(double)));

	// Variable-length arrays (VLA) are not supported by MSVC
#ifndef _MSC_VER
	const int nMAX = 43;
	double price2[nMAX]; // MSVC: error C2057: expected constant expression
	printf("Array \"price2\" has a size of %d\n", (int)(sizeof(price2) / sizeof(double)));

	int nmax;
	printf("Please enter \"price3\" array size: ");
	scanf("%d", &nmax); // TODO: should use safe scanf here
	double price3[nmax]; // MSVC: error C2057: expected constant expression
	printf("Array \"price3\" has a size of %d\n", (int)(sizeof(price3) / sizeof(double)));
#endif

#ifdef __GNUC__
	// NOTE: nMAX6 is actually not a constant.
	// => price6 is a VLA and thus cannot be initialized like that.
	// const int nMAX6 = 3;
	// double price6[nMAX6] = {1, 2, 3};
#endif

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o 01_ArraysDeclarations.exe 01_ArraysDeclarations.c
$ ./01_ArraysDeclarations.exe
Array "price" has a size of 32
Array "price2" has a size of 43
Please enter "price3" array size: 5
Array "price3" has a size of 5
```
<p class="run-info">Compiled and executed on 2026-11-09 21:32 from 3e403c3.</p>
<!-- SNIPPET:END -->

{{< a_noter >}}
**`price2`** et **`price3`** sont des tableaux de taille variable (VLA) : leur taille n'est connue qu'à l'exécution, même avec un **`const int`**. Un VLA ne peut pas être initialisé à sa déclaration (voir l'exemple 08.98).
{{< /a_noter >}}

### 08.02 : comment initialiser un tableau ?
<!-- SNIPPET:BEGIN source_file=02_ArraysInitialisations.c id=1242.1_Exemples_08.01_Arrays_Structures_02_ArraysInitialisations.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `02_ArraysInitialisations.c`**

```c
#include <stdio.h>

int main(void)
{
	// ALL elements are initialized
	int tablo[5] = { -12, 9, 5, 47, 66 };

	// SOME elements are initialized.
	// The others are set to 0.
	// SEE norm 6.7.9/19
	int tab[5] = { 1, 4, 9 };
	tab[3] = 11;

	// Size is automatically set to 4 because of initialisation
	double data[] = { 1.3, 2.6, -8.4, 0.1 };

	// Better, when possible, to enforce the size directly
	double data2[4] = { 1.3, 2.6, -8.4, 0.1 };

	// TOO FEW init values => the remaining values are set to the default value
	int tab2[4] = { 1, 2, 3 };

	// TOO MANY init values => error
	// int tab3[4] = { 1, 2, 3, 4, 5 };

	// TOO FEW init values => the remaining values are set to the default value
	char tab4[4] = { 'a', 'b', 'c' };

	// TOO MANY init values => error
	// char tab5[4] = { 'a', 'b', 'c', 'd', 'e' };

	// TOO FEW init values using literals => the remaining values are set to the default value
	char word[25] = "world";
	printf("%s\n", word); // Prints "world": the 19 remaining chars are '\0'

	// TOO MANY init values using literals => "OK"
	// SEE norm 6.7.9/14
	// NOTE: gcc warning: initializer-string for array of 'char' truncates NUL terminator [-Wunterminated-string-initialization]
	char word2[5] = "world";
	// word2 has no room for '\0': it is not a C string, printing it with %s is undefined behavior

	return 0;
}
```
<!-- SNIPPET:END -->

Cet exemple sert à lire les différentes initialisations, pas à être exécuté : avec la commande du cours, gcc le refuse (variables déclarées mais jamais utilisées, tableau **`word2`** trop petit pour le **`'\0'`** final).

### 08.03 : que peut-on faire avec un tableau dont la taille est lue au clavier ?
<!-- SNIPPET:BEGIN source_file=03_ArraysRemarks.c id=1242.1_Exemples_08.01_Arrays_Structures_03_ArraysRemarks.c run=true stdin="3\n2.5\n4" cflags="-Wno-error=unused-variable" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `03_ArraysRemarks.c`**

```c
#include <stdio.h>

// Prototypes
int input_size(void);
double input_value(void);

int main(void)
{
	// Variable-length arrays (VLA) are not supported by MSVC
#ifndef _MSC_VER
	int size = input_size();
	int tablo[size];

	// [Error with GCC] error: variable-sized object may not be initialized
	// double val[size] = { 1.1, 2.2, 3.3 };
#endif

	double x = 1.23;
	double values[3] = { 2.4, 1.2, x };

	// Can we initialize an array with values known at runtime?
	// Variable-length arrays (VLA) are not supported by MSVC
#ifndef _MSC_VER
	double value2 = input_value();

	// OK: constant-size array
	double array2[] = { 1.1, 2.2, value2 };

	int size3 = input_size();
	// [Error with GCC] error: variable-sized object may not be initialized
	// double array3[size3] = { 1.1, 2.2, value2 };
#endif

	int nbElements = sizeof(values) / sizeof(double);
	// Set all values in an array
	for (int i = 0; i < nbElements; ++i)
	{
		values[i] = i / 10.;
	}

	// Print all values in an array
	for (int i = 0; i < nbElements; ++i)
	{
		printf("%lf ", values[i]);
	}
	printf("\n");

	// Copy values from one to array to the other
	double values2[3];
	for (int i = 0; i < nbElements; ++i)
	{
		values2[i] = values[i];
		printf("%lf ", values2[i]);
	}
	printf("\n");

	return 0;
}

int input_size(void)
{
	int size;
	printf("Please enter array size: ");
	scanf("%d", &size); // TODO: use safe scanf here
	return size;
}

double input_value(void)
{
	// Handling User input errors:
	// 1) Print what is expected
	// 2) Read input from User
	// 3) Empty the stdin buffer
	// 4) Repeat until we got what we expected
	int status = 0;
	const int nbExpectedValues = 1;
	// Variables to store User input values
	double value;
	do
	{
		printf("Input value: ");
		status = scanf("%lf", &value);

		// IMPORTANT: fflush(stdin) does not always work!
		// It is strongly advised NOT to use it
		// fflush(stdin);
		// Instead, empty the buffer "manually"
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		// BIIIP to let user know when there is a problem
		if (status != nbExpectedValues)
		{
			printf("\a");
		}
	} while (status != nbExpectedValues);

	return value;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=unused-variable -o 03_ArraysRemarks.exe 03_ArraysRemarks.c
03_ArraysRemarks.c: In function 'main':
03_ArraysRemarks.c:29:13: warning: unused variable 'size3' [-Wunused-variable]
   29 |         int size3 = input_size();
      |             ^~~~~
03_ArraysRemarks.c:27:16: warning: unused variable 'array2' [-Wunused-variable]
   27 |         double array2[] = { 1.1, 2.2, value2 };
      |                ^~~~~~
03_ArraysRemarks.c:12:13: warning: unused variable 'tablo' [-Wunused-variable]
   12 |         int tablo[size];
      |             ^~~~~
$ ./03_ArraysRemarks.exe
Please enter array size: 3
Input value: 2.5
Please enter array size: 4
0.000000 0.100000 0.200000 
0.000000 0.100000 0.200000
```
<p class="run-info">Compiled and executed on 2026-11-09 21:32 from 3e403c3.</p>
<!-- SNIPPET:END -->

### 08.04 : que se passe-t-il quand on lit hors des limites d'un tableau ?
<!-- SNIPPET:BEGIN source_file=04_SideEffects.c id=1242.1_Exemples_08.01_Arrays_Structures_04_SideEffects.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `04_SideEffects.c`**

```c
#include <stdio.h>

int main(void)
{
	int daysInMonth[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };

	// Out of range access
	// daysInMonth[12], daysInMonth[13] and daysInMonth[14] print garbage
	for (int i = -3; i < 15; i++)
	{
		printf("daysInMonth[%d] = %d\n", i + 1, daysInMonth[i]);
	}

	return 0;
}
```
<!-- SNIPPET:END -->

{{< attention >}}
Lire un élément hors des limites d'un tableau (**`daysInMonth[-3]`**, **`daysInMonth[12]`**…) est un comportement indéfini (UB). Le compilateur ne dit rien et le programme affiche ce qui se trouve en mémoire à côté du tableau : le résultat change d'une exécution à l'autre, c'est pourquoi cet exemple n'est pas exécuté ici.
{{< /attention >}}

### 08.05 : peut-on modifier un tableau de constantes ?
L'affectation fautive n'est compilée qu'avec **`-DACTIVATE_ERRORS`** : gcc la refuse.

<!-- SNIPPET:BEGIN source_file=05_ArrayOfConsts.c id=1242.1_Exemples_08.01_Arrays_Structures_05_ArrayOfConsts.c run=true cflags="-DACTIVATE_ERRORS" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `05_ArrayOfConsts.c`**

```c
#include <stdio.h>

int main(void)
{
	const double sinus[91] = { 0.000, 0.017, 0.035, 0.052, 0.070, 0.087 };

	printf("sinus[4] = %lf\n", sinus[4]);
#ifdef ACTIVATE_ERRORS
	// Elements of a const array are read-only
	sinus[0] = 1.0;
#endif
	printf("sinus[0] = %lf\n", sinus[0]);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -DACTIVATE_ERRORS -o 05_ArrayOfConsts.exe 05_ArrayOfConsts.c
05_ArrayOfConsts.c: In function 'main':
05_ArrayOfConsts.c:10:18: error: assignment of read-only location 'sinus[0]'
   10 |         sinus[0] = 1.0;
      |                  ^
```
<p class="run-info">Compiled and executed on 2026-11-09 21:32 from 3e403c3.</p>
<!-- SNIPPET:END -->

### 08.06 : comment connaître le nombre d'éléments d'un tableau ?
<!-- SNIPPET:BEGIN source_file=06_Size.c id=1242.1_Exemples_08.01_Arrays_Structures_06_Size.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `06_Size.c`**

```c
#include <stdio.h>

int main(void)
{
	int data[100] = { 1, 2, 3, 4, 5, 6, 7 };
	char vowels[] = { 'a', 'e', 'i', 'o', 'u', 'y' };

	// Total size
	printf("Total size of array \"data\" = %d\n", (int)sizeof(data));
	// Nb Elements in array data
	int nbElementsInData = (int)sizeof(data) / sizeof(int);
	printf("Number of elements in array \"data\" = %d\n", nbElementsInData);

	// Nb Elements in array vowels
	int nbElementsInVowels = (int)sizeof(vowels) / sizeof(char);
	printf("Number of elements in array \"vowels\" = %d\n", nbElementsInVowels);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o 06_Size.exe 06_Size.c
$ ./06_Size.exe
Total size of array "data" = 400
Number of elements in array "data" = 100
Number of elements in array "vowels" = 6
```
<p class="run-info">Compiled and executed on 2026-11-09 21:32 from 3e403c3.</p>
<!-- SNIPPET:END -->

### 08.07 : pourquoi faut-il passer la taille d'un tableau à une fonction ?
<!-- SNIPPET:BEGIN source_file=07_ArraysParam.c id=1242.1_Exemples_08.01_Arrays_Structures_07_ArraysParam.c run=true cflags="-Wno-error=sizeof-array-argument" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `07_ArraysParam.c`**

```c
#include <stdio.h>

// NOTE: arrays cannot be passed by values so they decay into pointers when passed to functions
void display(int tab[], int nb)
{
	int i;
	// IMPORTANT: int tab[] here is treated as a pointer (an address). So sizeof(tab) returns the size of a pointer.
	//  ==>> ALWAYS pass an additional parameter giving the number of elements in the array
	printf("Array size as seen OUTSIDE the function is %d elements\n", nb);
	// NOTE: gcc warning: 'sizeof' on array function parameter 'tab' will return size of 'int *' [-Wsizeof-array-argument]
	printf("Array size as seen INSIDE the function is %d elements\n", (int)(sizeof(tab) / sizeof(int)));
	for (i = 0; i < nb; i++)
	{
		printf("%d\n", tab[i]);
	}
}

int main(void)
{
	int tablo[10] = { 1,2,3 };
	display(tablo, sizeof(tablo) / sizeof(int));

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=sizeof-array-argument -o 07_ArraysParam.exe 07_ArraysParam.c
07_ArraysParam.c: In function 'display':
07_ArraysParam.c:11:87: warning: 'sizeof' on array function parameter 'tab' will return size of 'int *' [-Wsizeof-array-argument]
   11 |         printf("Array size as seen INSIDE the function is %d elements\n", (int)(sizeof(tab) / sizeof(int)));
      |                                                                                       ^
07_ArraysParam.c:4:18: note: declared here
    4 | void display(int tab[], int nb)
      |              ~~~~^~~~~
$ ./07_ArraysParam.exe
Array size as seen OUTSIDE the function is 10 elements
Array size as seen INSIDE the function is 2 elements
1
2
3
0
0
0
0
0
0
0
```
<p class="run-info">Compiled and executed on 2026-11-09 21:32 from 3e403c3.</p>
<!-- SNIPPET:END -->

{{< a_noter >}}
Dans la fonction, **`tab`** n'est plus un tableau mais une adresse : **`sizeof(tab)`** donne la taille d'une adresse (8 octets ici), pas celle du tableau. gcc le signale, et la commande du cours en fait une erreur.
{{< /a_noter >}}

### 08.08 : comment déclarer et parcourir un tableau à plusieurs dimensions ?
<!-- SNIPPET:BEGIN source_file=08_Multi.c id=1242.1_Exemples_08.01_Arrays_Structures_08_Multi.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `08_Multi.c`**

```c
#include <stdio.h>

int main(void)
{
	int value[20][40];
	double volume[10][10][10];
	int matrix[2][4] = { {10,20,30,40}, {15,25,35,45} };

	printf("\"value\" size is %d\n", (int)(sizeof(value) / sizeof(int)));
	printf("\"volume\" size is %d\n", (int)(sizeof(volume) / sizeof(double)));
	printf("\"matrix\" size is %d\n\n", (int)(sizeof(matrix) / sizeof(int)));

	for (int i = 0; i < 2; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			printf("matrix[%d][%d] = %d\n", i, j, matrix[i][j]);
		}
	}

	printf("matrix[%d][%d] = %d\n", 1, 0, matrix[1][0]);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o 08_Multi.exe 08_Multi.c
$ ./08_Multi.exe
"value" size is 800
"volume" size is 1000
"matrix" size is 8

matrix[0][0] = 10
matrix[0][1] = 20
matrix[0][2] = 30
matrix[0][3] = 40
matrix[1][0] = 15
matrix[1][1] = 25
matrix[1][2] = 35
matrix[1][3] = 45
matrix[1][0] = 15
```
<p class="run-info">Compiled and executed on 2026-11-09 21:32 from 3e403c3.</p>
<!-- SNIPPET:END -->

### 08.09 : comment copier une structure ?
<!-- SNIPPET:BEGIN source_file=09_StructureCopy.c id=1242.1_Exemples_08.01_Arrays_Structures_09_StructureCopy.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `09_StructureCopy.c`**

```c
#include <stdio.h>
#include <string.h>

struct User
{
	char login[16];
	int id;
};

int main(void)
{
	int current_id = 42;
	struct User user1 = { "toto", current_id++ };
	struct User user2 = { .id = current_id++, .login = "titi" };
	struct User user3;

	printf("INITIALISATION\n");
	printf("user1 {id, login}: {%d, %s}\n", user1.id, user1.login);
	printf("user2 {id, login}: {%d, %s}\n", user2.id, user2.login);
	printf("user3 {id, login}: {%d, %s}\n", user3.id, user3.login);// NOTE: prints garbage

	strcpy(user1.login, "tata");

	printf("strcpy from literal\n");
	printf("user1 {id, login}: {%d, %s}\n", user1.id, user1.login);
	printf("user2 {id, login}: {%d, %s}\n", user2.id, user2.login);
	printf("user3 {id, login}: {%d, %s}\n", user3.id, user3.login);// NOTE: prints garbage

	strcpy(user3.login, user1.login);

	printf("strcpy from other structure\n");
	printf("user1 {id, login}: {%d, %s}\n", user1.id, user1.login);
	printf("user2 {id, login}: {%d, %s}\n", user2.id, user2.login);
	printf("user3 {id, login}: {%d, %s}\n", user3.id, user3.login);

	user3 = user2;

	printf("Full structure assignment\n");
	printf("user1 {id, login}: {%d, %s}\n", user1.id, user1.login);
	printf("user2 {id, login}: {%d, %s}\n", user2.id, user2.login);
	printf("user3 {id, login}: {%d, %s}\n", user3.id, user3.login);

	return 0;
}
```
<!-- SNIPPET:END -->

{{< attention >}}
**`user3`** est affichée avant d'avoir reçu une valeur : lire une variable locale non initialisée est un comportement indéfini (UB). Les deux premiers affichages de **`user3`** changent d'une exécution à l'autre, c'est pourquoi cet exemple n'est pas exécuté ici.
{{< /attention >}}

### 08.10 : où sont rangées les variables en mémoire, et que se passe-t-il quand une chaîne déborde ?
<!-- SNIPPET:BEGIN source_file=10_MemoryAllocationStringInt.c id=1242.1_Exemples_08.01_Arrays_Structures_10_MemoryAllocationStringInt.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `10_MemoryAllocationStringInt.c`**

```c
#include <stdio.h>
#include <string.h>

/* Allocation de:

    k       vaut 30 a la fin de la boucle
    a=1     0x0001
    b
    c= -1 = 0xFFFF
    t1="abcd"
    t2="xyz"
    En memoire on a :
    x y z \0 a b c d \0 0xFFFF **** 1000 00021 ******
    t1       t2         c      b    a    k

    strcpy(t2,"1234567890");

    En memoire on a :
    1 2 3 4 5 6 7 8 0x90FF **** 1000 00021 ******
    t1      t2      c      b    a    k
*/

int main(void)
{
  int k;
  int a = 1;
  int b;
  int c = -1;
  char t1[] = "abcd";
  char t2[] = "xvy";

  printf("&a:%p(%d)\n&b:%p(%d)\n&c:%p(%d)\nt1:%p(%d)\nt2:%p(%d)\n", (void *)&a, (int)&a, (void *)&b, (int)&b, (void *)&c, (int)&c, (void *)t1, (int)t1, (void *)t2, (int)t2);
  printf("-----------------------\n");

  for (k = 0; k < 30; k++)
  {
    printf("%p(%d) %c %d\n", (void *)&t2[k], (int)&t2[k], t2[k], (int)t2[k]);
  }
  printf("-----------------------\n");

  // NOTE: gcc warning: '__builtin_memcpy' writing 11 bytes into a region of size 4 overflows the destination
  strcpy(t2, "1234567890");

  for (k = 0; k < 30; k++)
  {
    printf("%p(%d) %c %d\n", (void *)&t2[k], (int)&t2[k], t2[k], (int)t2[k]);
  }
  printf("-----------------------\n");

  printf("\n%s", t1);

  return 0;
}
```
<!-- SNIPPET:END -->

{{< attention >}}
**`strcpy`** copie 11 caractères dans **`t2`**, qui n'en contient que 4, et les boucles lisent 30 caractères à partir de **`t2`** : ce sont des comportements indéfinis (UB), qui écrasent ou lisent les variables voisines. Les adresses affichées changent d'une exécution à l'autre, c'est pourquoi cet exemple n'est pas exécuté ici. Avec la commande du cours, gcc refuse d'ailleurs ce programme (débordement de **`strcpy`**, adresses converties en **`int`**).
{{< /attention >}}

### 08.11 : comment afficher et lire une chaîne de caractères ?
<!-- SNIPPET:BEGIN source_file=11_StringsInitializations.c id=1242.1_Exemples_08.01_Arrays_Structures_11_StringsInitializations.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `11_StringsInitializations.c`**

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
	char fileName[16] = "test.c";
	printf("%s", fileName);

	char word[] = {'H','e','l','l','o'};
	printf("%s", word);

	char chaine[256];
	char mini[4];
	scanf("%s", chaine);
	scanf("%s", mini);
	printf("%s\n", chaine);
	printf("%s\n", mini);

	return 0;
}
```
<!-- SNIPPET:END -->

{{< attention >}}
**`word`** n'a pas de **`'\0'`** final : **`printf("%s", word)`** continue à lire la mémoire après le tableau. Et avec la saisie **`Vive HE-Arc`**, **`scanf`** écrit 7 caractères dans **`mini`**, qui n'en contient que 4. Ce sont deux comportements indéfinis (UB) : le résultat dépend du compilateur et de la disposition des variables en mémoire, c'est pourquoi cet exemple n'est pas exécuté ici.
{{< /attention >}}

### 08.12 : que se passe-t-il quand on copie une chaîne dans un tableau trop petit ?
<!-- SNIPPET:BEGIN source_file=12_RevueCStrings.c id=1242.1_Exemples_08.01_Arrays_Structures_12_RevueCStrings.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `12_RevueCStrings.c`**

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
	char letter   = 'a';
	char chaine[] = "a";

	char temp [] = "";
	char text [] = "Blablabla";

	int i = 0;
	
	for (; i < strlen(text)+1 ; i++)
	{
		temp[i] = text[i];
	}

	return 0;
}
```
<!-- SNIPPET:END -->

{{< attention >}}
**`temp`** ne contient qu'un seul caractère (le **`'\0'`**) : la boucle écrit 10 caractères, dont 9 hors du tableau. C'est un comportement indéfini (UB), qui écrase la mémoire voisine.
{{< /attention >}}

### 08.96 : un tableau est-il initialisé à zéro par défaut ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_08.96_ArrayInitializationToZero_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

// Global or static array => elements automatically initialized to 0
int global_array[4];

void print_array(int arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		printf("%d ", arr[i]);
	}
	printf("\n");
}

void print_string_as_ascii(char arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		printf("%d ", arr[i]);
	}
	printf("\n");
}

int main(void)
{
	// Not initialized by default
	int local_array[4];
	print_array(local_array, sizeof(local_array)/sizeof(local_array[0]));
	// Some elements initialized => all the others initialized to default value (here 0)
	int local_array1[4] = {99};
	print_array(local_array1, sizeof(local_array1)/sizeof(local_array1[0]));
	int local_array2[4] = {[1] = 99, [3] = 99};
	print_array(local_array2, sizeof(local_array2)/sizeof(local_array2[0]));

	// Empty braces: all elements initialized to 0 (standard since C23)
	int local_array22[4] = {};
	print_array(local_array22, sizeof(local_array22)/sizeof(local_array22[0]));

	// Global or static array => elements automatically initialized to 0
	static int static_array[4];
	print_array(static_array, sizeof(static_array)/sizeof(static_array[0]));

	char str[10] = {'Z'};
	print_string_as_ascii(str, sizeof(str)/sizeof(str[0]));

	printf("%c", 12["Hello, World!\n"]);

	return 0;
}
```
<!-- SNIPPET:END -->

{{< attention >}}
**`local_array`** n'est pas initialisé : ses valeurs sont indéterminées et les afficher est un comportement indéfini (UB). Cet exemple n'est donc pas exécuté ici.
{{< /attention >}}

### 08.97 : comment `scanf("%s")` peut-il écraser d'autres variables ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_08.97_ScanfBufferOverflow_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// IMPORTANT for MSVC: execute in RELEASE mode to avoid additional debug padding around stack variables
int main(void)
{
	// IMPORTANT: variables order on the stack is not guaranteed.
	// If we do char a[9] instead, then a and b will be in different order on the stack.
	bool access_granted = false;
	char expected_password[10] = "admin1234";
	char actual_password[10] = "000000000";

	printf("Values before overflow:\n");
	printf("\taccess_granted: %d\n", access_granted);
	printf("\texpected_password: %s\n", expected_password);
	printf("\tactual_password: %s\n", actual_password);

	printf("Please enter password: ");
	// Enter "9999999999999999999999" will rewrite the stack
	scanf("%s", actual_password);

	printf("Values after overflow:\n");
	printf("\taccess_granted: %d\n", access_granted);
	printf("\texpected_password: %s\n", expected_password);
	printf("\tactual_password: %s\n", actual_password);

	// String are different, but access_granted has been changed to true...
	if (strcmp(actual_password, expected_password) == 0) // If password is correct
	{
		access_granted = true;
	}

	if (access_granted == true)
	{
		printf("CONGRATS: you gained control of the server!\n");
	}
	else
	{
		printf("SORRY: you do not have enough privileges!\n");
	}

	return 0;
}
```
<!-- SNIPPET:END -->

{{< attention >}}
**`scanf("%s")`** ne connaît pas la taille du tableau : une saisie de plus de 9 caractères déborde de **`actual_password`** et écrase les variables voisines. C'est un comportement indéfini (UB), dont le résultat dépend de la disposition des variables en mémoire : cet exemple n'est pas exécuté ici.
{{< /attention >}}

### 08.98 : un `const int` suffit-il pour fixer la taille d'un tableau ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_08.98_VLAs_main.c run=true cflags="-Wno-error=unused-variable" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

// If not using MSVC
#ifndef _MSC_VER
// If C version is C11 or newer, VLAs are optional.
// => So explicitly check for their support
#if __STDC_VERSION__ >= 201100L
#ifndef __STDC_NO_VLA__
#define VLAS_SUPPORTED
#endif
// Else if C version is C99, VLAs are supported.
#elif __STDC_VERSION__ >= 199900L
#define VLAS_SUPPORTED
#endif
#endif

// OK with MSVC and GCC
#define DEF_ARRAY_SIZE 10
int array1[DEF_ARRAY_SIZE];

// NOTE: const in C means "read-only", not that it is a constant.
// => So const_array_size is still considered as a variable.
// MSVC: error C2057: expected constant expression
// GCC: error: variably modified 'array2' at file scope
const int const_array_size = 10;
// int array2[const_array_size];

void function(void)
{
	// Compile error with MSVC
	// MSVC: error C2057: expected constant expression
#ifdef VLAS_SUPPORTED
	// OK with GCC
	int array3[const_array_size];
	// NOTE: const in C means "read-only", not that it is a constant.
 	// GCC: error: variable-sized object may not be initialized
 	// int array4[const_array_size] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

	 // But the following is OK
	 int array5[10] =  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
#endif
}

int main(void)
{
	#ifdef VLAS_SUPPORTED
	printf("VLAs are supported on this compiler\n");
	#endif

	function();
	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=unused-variable -o main.exe main.c
main.c: In function 'function':
main.c:40:14: warning: unused variable 'array5' [-Wunused-variable]
   40 |          int array5[10] =  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
      |              ^~~~~~
main.c:34:13: warning: unused variable 'array3' [-Wunused-variable]
   34 |         int array3[const_array_size];
      |             ^~~~~~
$ ./main.exe
VLAs are supported on this compiler
```
<p class="run-info">Compiled and executed on 2026-11-09 21:32 from 3e403c3.</p>
<!-- SNIPPET:END -->

### 08.99 : que se passe-t-il quand la saisie dépasse la taille de la chaîne ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_08.99_StringOverflow_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

// Run it with the debugger and see what happens
int main(void)
{
	char string[4] = "123";
	printf("%s\n", string);

	scanf("%s", string);
	printf("%s\n", string);

	return 0;
}
```
<!-- SNIPPET:END -->

{{< attention >}}
**`string`** contient au plus 3 caractères et le **`'\0'`** : une saisie plus longue écrit hors du tableau, ce qui est un comportement indéfini (UB). Cet exemple n'est pas exécuté ici.
{{< /attention >}}

## Exercices

{{< a_noter >}}
Pour des raisons historiques, la numérotation des exercices n'est pas continue.
{{< /a_noter >}}

### Exercice 1
Parmi les définitions suivantes, indiquer celles qui sont erronées et expliquer pourquoi :
```c
unsigned int matrice[3, 3];
int vecteur[6];
char ordinateur[] = 'IBM PC';
float mesure[2][1000];
int des[3] [3] [3];
char nom[8] = "François";
char mois[14] = "juin";
```

### Exercice 2
Lesquelles des chaînes suivantes sont initialisées correctement ?
Corrigez les déclarations fausses et indiquer pour chaque chaîne de caractères le nombre d'octets réservés en mémoire.
```c
char a[] = "un\ndeux\ntrois\n";
char b[12] = "un deux trois";
char c[] = 'abcdefg';
char d[10] = 'x';
char e[5] = "cinq";
char f[] = "Cette " "phrase " "est coupée";
char g[2] = {'a', '\0'};
char h[4] = {'a', 'b', 'c'};
char i[4] = "'o'";
```
### Exercice 3
À la suite des déclarations et instructions suivantes, placer le contenu mémoire des tableaux suivants (valeur décimale ou caractère) :

```c
double values[] = {1.2, -2.3, 0.};
short int IDEtudiant[5] = { 1234, 4576, 7345, 9999};
int serie[5];
for (int i=0; i < 5; i++)
serie[i]= 2 * i + 1;
char texte[]="Alea jacta est";
struct XY { char x; double y } var1 ={'5',5.f};
struct XY tabStruct[3] = {{'5',5.f}, {'6',6.f}, {'7',7.f} };
```

**Exemple :**
```c
char L[5]={ 'a', 't'};
```
donne :

| **`L[0]`** | **`L[1]`** | **`L[2]`** | **`L[3]`** | **`L[4]`** |
| ---- | ---- | ---- | ---- | ---- | 
| `'a'`| `'t'`| `0`  | `0`  | `0`  |

{{< a_noter >}}
Chaque élément représente 1 byte.
{{< /a_noter >}}

### Exercice 21_1
Écrire une fonction **`ch08_ex21_1_CompareArray()`** qui compare deux tableaux d'entiers de même taille et renvoie **`true`** si les tableaux sont identiques, et **`false`** sinon.
**`ch08_ex21_1_CompareArray()`** prend 3 paramètres en entrée : les 2 tableaux d'entiers et leur taille, dans cet ordre.

**Exemples**

Pour les tableaux suivants :
```c
int array1[] = {1, 2, 3, 4, 4};
int array2[] = {1, 2, 3, 4, 5};
```

**`ch08_ex21_1_CompareArray(array1, array2, 0)`** renvoie **`true`**.
**`ch08_ex21_1_CompareArray(array1, array2, 4)`** renvoie **`true`**.
**`ch08_ex21_1_CompareArray(array1, array2, 5)`** renvoie **`false`**.

### Exercice 21_2
Écrire une fonction **`ch08_ex21_2_PrintArray()`** qui affiche à l'écran un tableau d'entiers, et ne retourne rien.
**`ch08_ex21_2_PrintArray()`** prend donc 2 paramètres en entrée : 1 tableau d'entiers et sa taille.

**Exemples**

Pour le tableau suivant :
```c
int array[] = {1, 2, 3, 4, 5};
```

**`ch08_ex21_2_PrintArray(array, 0)`** n'affiche rien.
**`ch08_ex21_2_PrintArray(array, 4)`** affiche **`1 2 3 4`**.
**`ch08_ex21_2_PrintArray(array, 5)`** affiche **`1 2 3 4 5`**.

{{<attention>}}
Chaque élément du tableau est suivi d'un espace, **sauf le dernier**. De plus, **il ne faut pas** terminer l'affichage par un **`\n`**.
{{</attention>}}

### Exercice 21_3
Écrire une fonction **`ch08_ex21_3_FillArray()`** qui remplit un tableau d'entiers passé en paramètre avec des valeurs saisies au clavier par l'utilisateur.
On s'arrête quand l'utilisateur entre une valeur négative.
La fonction **`ch08_ex21_3_FillArray()`** retourne le nombre de valeurs correctes saisies.

{{< attention >}}
Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
{{< /attention >}}

**Exemples**

**`ch08_ex21_3_FillArray(array, -1)`** ne fait rien.

**`ch08_ex21_3_FillArray(array, 0)`** ne fait rien.

Pour le tableau :
```c
int array[] = {-2, -2, -2, -2};
```
alors **`ch08_ex21_3_FillArray(array, 4)`** avec les saisies au clavier
```
a
b
1
-1
```
change le tableau en :
```c
{1, -2, -2, -2};
```

Pour le tableau :
```c
int array[] = {-2, -2, -2, -2};
```
alors **`ch08_ex21_3_FillArray(array, 4)`** avec les saisies au clavier
```
2
2
-2
```
change le tableau en :
```c
{2, 2, -2, -2};
```

Pour le tableau :
```c
int array[] = {-2, -2, -2, -2};
```
alors **`ch08_ex21_3_FillArray(array, 4)`** avec les saisies au clavier
```
3
3
-2
```
change le tableau en :
```c
{3, 3, -2, -2};
```

### Exercice 21
En vous aidant des exercices précédents, écrire une fonction **`ch08_ex21_ArraySum()`** qui :
1. déclare un tableau pouvant contenir 50 entiers maximum
2. demande à l’utilisateur le nombre de valeurs **`n`** à saisir (maximum 50)
3. remplit le tableau avec n valeurs entrées au clavier
4. affiche les n premiers éléments du tableau
5. affiche la somme des valeurs saisies se trouvant dans le tableau

{{< attention >}}
Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
{{< /attention >}}

**Exemple 1**
```c
$ .\ch08_ex21_ArraySum.exe
Nb values (max.50): a
Nb values (max.50): b
Nb values (max.50): -2
Nb values (max.50): -1
Nb values (max.50): 0
array:

Total sum: 0
```

**Exemple 2**
```c
.\ch08_ex21_ArraySum.exe
Nb values (max.50): 4
Value 0? -2
Value 1? -1
Value 2? 0
Value 3? 1
array:
-2 -1 0 1
Total sum: -2
```

### Exercice 22
Écrire une fonction qui :
1. déclare un tableau pouvant contenir 50 entiers maximum
2. demande à l’utilisateur le nombre de valeurs n
3. remplit le tableau avec n valeurs entrées au clavier
4. copie toutes les valeurs strictement positives dans un 2ème tableau
5. copie toutes les valeurs strictement négatives dans un 3ème tableau
6. Affiche les tableaux

### Exercice 23
Écrire une fonction **`ch08_ex23_Array2DSum()`** qui :
1. déclare un tableau d'entiers (taille maximale : 50 lignes et 50 colonnes).
2. lit les tailles (nombre de lignes et nombre de colonnes) au clavier
3. remplit le tableau avec des valeurs entrées au clavier
4. affiche la somme de tous ses éléments

{{< attention >}}
Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
{{< /attention >}}

**Exemple 1 :**
```c
$ .\ch08_ex23_Array2DSum.exe
Nb lines (max.50): a
Nb lines (max.50): -1
Nb lines (max.50): 2
Nb columns (max.50): a
Nb columns (max.50): -1
Nb columns (max.50): 2
array[0][0]: 1
array[0][1]: 2
array[1][0]: 3
array[1][1]: 4
Total sum: 10
```

**Exemple 2 :**
```c
$ .\ch08_ex23_Array2DSum.exe
Nb lines (max.50): 0
Nb columns (max.50): 9
Total sum: 0
```

**Exemple 3 :**
```c
$ .\ch08_ex23_Array2DSum.exe
Nb lines (max.50): 9
Nb columns (max.50): 0
Total sum: 0
```

**Exemple 4 :**
```c
$ .\ch08_ex23_Array2DSum.exe
Nb lines (max.50): 0
Nb columns (max.50): 0
Total sum: 0
```

### Exercice 24
Écrire une fonction **`ch08_ex24_DotProduct()`** qui calcule le produit vectoriel de 2 vecteurs d'entiers {{<katex>}}\vec{u}{{</katex>}} et {{<katex>}}\vec{v}{{</katex>}}.
Les vecteurs sont passés en paramètres sous forme de tableaux d'entiers, avec leur taille, dans cet ordre.

{{< a_noter >}}

{{<katex>}}\vec{u} = (3, 2, -4){{</katex>}} et {{<katex>}}\vec{v} = (2, -3, 5){{</katex>}} alors 

{{<katex>}}
\vec{u}\cdot\vec{v} = \begin{pmatrix} x_{u} & y_{u} & z_{u} \end{pmatrix} \begin{pmatrix} x_{v}\\ y_{v}\\ z_{v} \end{pmatrix} \newline
\vec{u}\cdot\vec{v} = \begin{pmatrix} 3 & 2 & -4 \end{pmatrix} \begin{pmatrix} 2 \\ -3 \\ 5 \end{pmatrix} \newline
\vec{u}\cdot\vec{v} = 3 * 2 + 2 * (-3) + (-4) * 5 = -20
{{</katex>}}

{{< /a_noter >}}

**Exemple :**
Avec les tableaux suivants :
```c
int u[] = {3, 2, -4};
int v[] = {2, -3, 5};
```
alors **`ch08_ex24_DotProduct(u, v, 3)`** renvoie **`-20`**.

### Exercice 25
Écrire un programme qui détermine la plus grande et la plus petite valeur dans un tableau d'entiers.
Afficher ensuite la valeur et la position du maximum et du minimum.

**Note :** si le tableau contient plusieurs maxima ou minima, le programme retiendra la position du premier maximum ou minimum rencontré.

{{< notion_avancee >}}
### Exercice 26
Écrire une fonction qui calcule le produit matriciel de 2 matrices d'entiers {{<katex>}}A{{</katex>}} et {{<katex>}}B{{</katex>}} passées en paramètres.
{{< /notion_avancee >}}
### Exercice 31
Écrire une fonction qui lit 5 mots, séparés par des espaces et qui les affiche ensuite dans une ligne, mais dans l'ordre inverse.
Les mots sont mémorisés dans 5 variables **`M1`**, …, **`M5`**.

### Exercice 32
Écrire une fonction qui lit une ligne de texte (taille max. 50 caractères) et puis un caractère.
Elle doit indiquer si le caractère se trouve dans le texte.
Si oui, elle doit afficher à quelle position il se trouve (indice de la première occurrence).

{{< attention >}}
IL ne faut pas utiliser des fonctions de **`<string.h>`**.
{{< /attention >}}

### Exercice 33
Écrire une fonction qui lit une ligne de texte (taille maximale : 200 caractères), la mémorise dans une variable **`texte`** et affiche ensuite :
a) la longueur **`lChaine`** de la chaîne.
b) le nombre de **'e'** contenus dans le texte.
c) toute la phrase à rebours, sans changer le contenu de la variable **`texte`**.
d) toute la phrase à rebours, après avoir inversé l'ordre des caractères dans **`texte`**.

{{< a_noter >}}
Il faut utiliser la fonction **`fgets()`** pour lire une ligne de texte comportant des espaces.
{{< /a_noter >}}

{{< notion_avancee >}}
### Exercice 34
Écrire une fonction qui lit une ligne de texte (taille maximale : 128 caractères), puis qui supprime tous les espaces dans la chaine et tasse les éléments restants.

{{< a_noter >}}
Commencer par faire l’exercice sur papier en raisonnant d’abord avec 2 chaines de caractères, puis avec une seule.
{{< /a_noter >}}

{{< /notion_avancee >}}

{{< notion_avancee >}}
### Exercice 35
Écrire une fonction qui lit une ligne de texte (taille maximale : 128 caractères), y récupère un chiffre (positif ou négatif), le mémorise dans une variable de type long et l’affiche.

{{< a_noter >}}
On supportera les formats simples comme "1748", "+1748" et "-1748".
{{< /a_noter >}}
{{< /notion_avancee >}}

### Exercice 41
Définir une structure **`Time`** capable de mémoriser le temps d’un marathon (hh:mm:ss).

1. Écrire une fonction **`ch08_ex41_InitTime()`** qui prend 3 entiers (heures, minutes, secondes) passés en paramètres et retourne une structure **`Time`**.
2. Écrire une fonction **`ch08_ex41_PrintTime()`** qui prend une structure **`Time`** en paramètre et affiche le temps associé.
3. Écrire une fonction **`ch08_ex41_Time()`** qui créé une structure **`Time`** contenant 5 heures, 3 minutes et 17 secondes en utilisant la fonction **`ch08_ex41_InitTime()`** et l’affiche en utilisant la fonction **`ch08_ex41_PrintTime()`**.

**Exemple :**
```c
  Time t = ch08_ex41_InitTime(5, 3, 17);
  ch08_ex41_PrintTime(t);
  ```

affichera **`05:03:17`** si on a stocké 5 heures 03 minutes et 17 secondes dans **`t1`**.

{{< a_noter >}}
Il faut utiliser un **`typedef`** en définissant la structure.
{{< /a_noter >}}

### Exercice 42
Écrire un programme pour gérer des nombres complexes.
En particulier :
1. définir le type **`Complex`** avec 2 membres de type réel : **`real`** et **`imaginary`**
2. ajouter le code à **`scanf`** pour que la saisie d'un nombres complexe ne se fasse qu'au format (r,i) et encapsuler ce code dans une fonction **`ch08_ex42_InputComplex()`** qui retourne une structure **`Complex`**.
3. ajouter les fonctions **`ch08_ex42_SumComplex()`** et **`ch08_ex42_DiffComplex()`** appelées pour calculer la somme, et la différence de deux nombres complexes stockés dans une structure **`Complex`**. Ces fonctions prennent 2 paramètres de type **`Complex`** et retournent un **`Complex`**.

**`sum_complex()`** : {{<katex>}}(a_1 + i b_1)+( a_2 + i b_2) = (a_1+a_2) + i (b_1+b_2){{</katex>}}

**`diff_complex()`** : {{<katex>}}(a_1 + i b_1)-( a_2 + i b_2) = (a_1-a_2) + i (b_1-b_2){{</katex>}}

4. implémenter une fonction **`ch08_ex42_PrintComplex()`** qui affiche un nombre complexe sous la forme suivante : **`5.00 + -3.00i`**.
5. écrire une fonction **`ch08_ex42_Complex()`** qui lit deux nombres complexes, calcule leur somme et leur différence et affiche les résultats.

{{< a_noter >}}
Il faut utiliser les fonctions écrites dans les points précédents.
{{< /a_noter >}}

{{< attention >}}
Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
{{< /attention >}}

**Exemple :**
```c
$ .\ch08_ex42_Complex.exe
Please enter a complex number (r,i): a
Please enter a complex number (r,i): -1
Please enter a complex number (r,i): (1,1)
Please enter a complex number (r,i): (2,3) 

Sum = 3.00 + 4.00i

Diff = -1.00 + -2.00i
```

{{< attention >}}
Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?]({{< relref "/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-" >}})).
{{< /attention >}}

### Exercice 43
1. Créer un type **`Person`** pour une personne, caractérisée par son nom (20 caractères maximum), son prénom (20 caractères maximum) et son année de naissance.
2. Dans une fonction **`ch08_ex43_Person()`**, déclarer un tableau de 10 personnes et l'initialiser avec les données des sept personnes suivantes :
```c
"Knuth", "Donald", 1938
"Kernighan", "Brian", 1942
"Ritchie", "Dennis", 1941
"Thompson", "Ken", 1943
"Minsky", "Marvin", 1927
"Dijkstra", "Edsger", 1930
"Stroustrup", "Bjarne", 1950
```
3. Dans la fonction **`ch08_ex43_Person()`**, afficher toutes les personnes âgées de moins de 80 ans.

{{< attention >}}
Il faut considérer que nous sommes en 2020.
{{< /attention >}}

4. Trouver les personnes dont le nom est en tête/en fin de classement selon l’ordre alphanumérique (le plus proche de « AAA » / le proche de « ZZZ » ).

{{< attention >}}
Il faut utiliser la fonction **`strcmp()`** pour comparer les noms.
{{< /attention >}}

5. Qui sont ces personnes et qu’ont-elles fait ?

**Exemple :**
```c
7 Persons
Persons less than 80 years old:
Brian Kernighan 78 years
Dennis Ritchie 79 years
Ken Thompson 77 years
Bjarne Stroustrup 70 years

Alphabetic order:
The first is: Dijkstra
The last is: Thompson
```
