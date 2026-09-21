---
title: "2. Types et variables"
weight: 1
---

# CHAPITRE 2 : types et variables

## Slides
{{<slides "https://he-arc.github.io/1242.1-Langage_C-SLIDES/02_TypesEtVariables.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.1-Langage_C-SLIDES/02_TypesEtVariables?print-pdf)

### Visualisation : entiers et flottants en mémoire
Cliquez sur les bits, changez la valeur, ou suivez un scénario pas à pas.

{{<viz "https://he-arc.github.io/1242.1-Langage_C-VIZ/ints-floats/">}}

## Squelette à remplir
{{<a_faire>}}
Remplir le squelette suivant au fur et à mesure du cours.
{{</a_faire>}}
<!-- SNIPPET:BEGIN source_file=chap2.c id=1242.1_Skeletons_02_chap2.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `chap2.c`**

```c
#include <stdio.h>

// CHAPTER 2

int main(void)
{
	// Experiment with identifiers.


	// Check size in bytes of most common types.
	// Example: printf("char          : %zu bits\n", 8 * sizeof(char));


	// Experiment with assignements


	// Experiment with blocks and variables


	// Write swap instructions


	// Declare constants with const keyword and #define preprocessor directives
	

	return 0;
}
```
<!-- SNIPPET:END -->

{{< a_noter>}}
 **```%zu```** est le spécificateur de format pour des valeurs de type **```size_t```**.
{{< /a_noter>}}

## Exemples

### 02.01 : quelle est la taille en bits des types de base ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_02.01_Prog_typeSize_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	int* p;
	enum vowel{ a, e, i, o, u, y } vow;

	printf("_Bool         : %d bits\n", 8 * (int) sizeof(_Bool));
	printf("char          : %d bits\n", 8 * (int) sizeof(char));
	printf("unsigned char : %d bits\n", 8 * (int) sizeof(unsigned char));
	printf("\n");
	printf("short (int)   : %d bits\n", 8 * (int) sizeof(short int));
	printf("short         : %d bits\n", 8 * (int) sizeof(short));
	printf("unsigned short: %d bits\n", 8 * (int) sizeof(unsigned short));
	printf("\n");
	printf("int           : %d bits\n", 8 * (int) sizeof(int));
	printf("unsigned int  : %d bits\n", 8 * (int) sizeof(unsigned int));
	printf("\n");
	printf("long          : %d bits\n", 8 * (int) sizeof(long));
	printf("unsigned long : %d bits\n", 8 * (int) sizeof(unsigned long));
	printf("\n");
	printf("float         : %d bits\n", 8 * (int) sizeof(float));
	printf("double        : %d bits\n", 8 * (int) sizeof(double));
	printf("long double   : %d bits\n", 8 * (int) sizeof(long double));
	printf("\n");
	printf("enum          : %d bits\n", 8 * (int) sizeof(vow));
	printf("pointer       : %d bits\n", 8 * (int) sizeof(p));
	printf("\n");

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
_Bool         : 8 bits
char          : 8 bits
unsigned char : 8 bits

short (int)   : 16 bits
short         : 16 bits
unsigned short: 16 bits

int           : 32 bits
unsigned int  : 32 bits

long          : 32 bits
unsigned long : 32 bits

float         : 32 bits
double        : 64 bits
long double   : 128 bits

enum          : 32 bits
pointer       : 64 bits
```
<p class="run-info">Compiled and executed on 2026-09-21 19:44 from 18f0dd4.</p>
<!-- SNIPPET:END -->

### 02.02 : comment échanger le contenu de deux variables ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_02.02_SwapAB_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	int a = 10;
	int b = 5;
	int temp;

	// Before swapping variables values
	printf("BEFORE swap\n");
	printf("Variable a: %d \n", a); //  Variable a: 10
	printf("Variable b: %d \n", b); //  Variable b: 5

	/// Add here the instructions to SWAP the variables values
	/// Hint: 2 instructions are executed sequentially (one after the other)
	temp = a;
	a = b;
	b = temp;

	// After swapping varialbes values
	printf("\nAFTER swap\n");
	printf("Variable a: %d \n", a); //  Variable a: 5
	printf("Variable b: %d \n", b); //  Variable b: 10

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
BEFORE swap
Variable a: 10 
Variable b: 5 

AFTER swap
Variable a: 5 
Variable b: 10
```
<p class="run-info">Compiled and executed on 2026-09-21 19:44 from 18f0dd4.</p>
<!-- SNIPPET:END -->

### 02.03 : à quoi ressemblent un entier et un flottant en mémoire, bit à bit ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_02.03_BinaryConversion_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

// Assumes little endian
void printBits(int size, void *ptr)
{
	unsigned char *b = (unsigned char*)ptr;

	for (int i = size - 1; i >= 0; --i)
	{
		for (int j = 7; j >= 0; --j)
		{
			// Take the i-th byte
			unsigned char byte = b[i];
			// Use a mask to keep the (j+1)-th bit.
			// 10000000 to keep 8th bit (j == 7)
			// 01000000 to keep 7th bit
			// ...
			// 00000001 to keep 1st bit (j == 0)
			unsigned char mask = 1 << j;
			byte = byte & mask;
			// Then offset byte so that the (j+1)-th bit is in the first position.
			// So the char will always be 0 or 1 depending on the value of the (j+1)-th bit
			byte >>= j;
			printf("%u", byte);
		}
	}

	puts("");
}

int main(void)
{
	char          c = 1;
	int           i = 1;
	float         f = 1.f;
	double        d = 1.;
	printf("char   c = 1  : "); printBits(sizeof(c), &c);
	printf("int    i = 1  : "); printBits(sizeof(i), &i);
	printf("float  f = 1.f: "); printBits(sizeof(f), &f);
	printf("double d = 1. : "); printBits(sizeof(d), &d);

	c = -1;
	i = -1;
	f = -1.f;
	d = -1.;
	printf("char   c = -1  : "); printBits(sizeof(c), &c);
	printf("int    i = -1  : "); printBits(sizeof(i), &i);
	printf("float  f = -1.f: "); printBits(sizeof(f), &f);
	printf("double d = -1. : "); printBits(sizeof(d), &d);

	c = '1';
	printf("char c = '1' : "); printBits(sizeof(c), &c);
	c = 49;
	printf("char c = 49  : "); printBits(sizeof(c), &c);

	printf("\nPrint values 1, 2 and 4 (float):\n");
	f = 1.f;
	printBits(sizeof(f), &f); // 0 0111 1111  00000000000000000000000 exp=127 (-127) => e=0 1*2^0 = 1
	f = 2.f;
	printBits(sizeof(f), &f); // 0 1000 0000  00000000000000000000000 exp=128 (-127) => e=1 1*2^1 = 2
	f = 4.f;
	printBits(sizeof(f), &f); // 0 1000 0001  00000000000000000000000 exp=129 (-127) => e=2 1*2^2 = 4

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
char   c = 1  : 00000001
int    i = 1  : 00000000000000000000000000000001
float  f = 1.f: 00111111100000000000000000000000
double d = 1. : 0011111111110000000000000000000000000000000000000000000000000000
char   c = -1  : 11111111
int    i = -1  : 11111111111111111111111111111111
float  f = -1.f: 10111111100000000000000000000000
double d = -1. : 1011111111110000000000000000000000000000000000000000000000000000
char c = '1' : 00110001
char c = 49  : 00110001

Print values 1, 2 and 4 (float):
00111111100000000000000000000000
01000000000000000000000000000000
01000000100000000000000000000000
```
<p class="run-info">Compiled and executed on 2026-09-21 19:44 from 18f0dd4.</p>
<!-- SNIPPET:END -->

### 02.04 : que fait la séquence d'échappement `` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_02.04_BIIIP_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

// WARNING: \a is interpreted by the terminal.
// So it might bip, or display a bell, or do nothing.
// It depends on the terminal.

int main(void)
{
	// BIIIP using a char
	char c = '\7';
	printf("%c", c);

	c = '\a';
	printf("%c", c);

	// BIIIP using a string
	const char* s = "\7";
	printf("%s", s);

  // BIIIP using an escape sequence
	c = '\a';
	printf("%c", c);

	c = '\a';
	printf("%c", c);

	// BIIIP using a string with an escape sequence
	s = "\a";
	printf("%s", s);

	return 0;
}
```
<!-- SNIPPET:END -->

### 02.05 : comment fonctionnent les booléens en C (`_Bool`, `bool`) ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_02.05_Booleans_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>
// To use bool instead of _Bool
// Added in C99: https://en.wikipedia.org/wiki/C99
#include <stdbool.h>

int main(void)
{
	int oldBool = 42;
	if (oldBool == 0)
	{
		printf("%s", "oldBool is FALSE\n");
	}
	// Any other value is considered true
	else
	{
		printf("%s", "oldBool is TRUE\n");
	}

	// _Bool is a keyword of the language
	_Bool newBool = 42;
	if (newBool == 0)
	{
		printf("%s", "newBool is FALSE\n");
	}
	// Any other value is considered true
	else
	{
		printf("%s", "newBool is TRUE\n");
	}

	bool betterBool = true;
	if (betterBool == false)
	{
		printf("%s", "betterBool is FALSE\n");
	}
	else
	{
		printf("%s", "betterBool is TRUE\n");
	}

	// Test output
	{
		_Bool test = 3; //!=0 so considered true
		printf("%d\n", test);
		test = (2 * 3) < 7;
		printf("%d\n", test);
	}
	{
		bool test = true;
		printf("%d\n", test);
		test = (2 * 3) < 7;
		printf("%d\n", test);
	}

	_Bool x = true;
	bool y = true;
	char z = true;

	printf("x = %d\n", x);
	printf("y = %d\n", y);
	printf("z = %d\n", z);
	printf("(x == true) = %d\n", x == true);
	printf("Memory space: \n");
	printf("x: %d\n", (int) sizeof(x));
	printf("y: %d\n", (int) sizeof(y));
	printf("z: %d\n", (int) sizeof(z));
	printf("(x == true): %d\n", (int) sizeof(x == true));

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
oldBool is TRUE
newBool is TRUE
betterBool is TRUE
1
1
1
1
x = 1
y = 1
z = 1
(x == true) = 1
Memory space: 
x: 1
y: 1
z: 1
(x == true): 4
```
<p class="run-info">Compiled and executed on 2026-09-21 19:44 from 18f0dd4.</p>
<!-- SNIPPET:END -->

### 02.06 : comment comparer deux `double` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_02.06_DoubleComparison_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>
#include <math.h>
#include <float.h>

int main(void)
{
  double d1 = 0.3;
  double d2 = 0.1 + 0.1 + 0.1;
  if (d1 == d2)
  {
    printf("d1 is equal to d2\n");
  }
  else
  {
    printf("d1 is NOT equal to d2\n");
  }

  if (fabs(d1 - d2) < DBL_EPSILON)
  {
    printf("d1 is approximately equal to d2\n");
  }
  else
  {
    printf("d1 is NOT approximately equal to d2\n");
  }

  return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
d1 is NOT equal to d2
d1 is approximately equal to d2
```
<p class="run-info">Compiled and executed on 2026-09-21 19:44 from 18f0dd4.</p>
<!-- SNIPPET:END -->

# EXERCICES

## Exercice 1 
Parmi les noms de variables suivants, indiquer ceux qui sont corrects :

```
nombre		Auto			Dollar$			Ligne4
17h20		ARC_EN_CIEL	RouGE7			vert/jaune
"poisson"	Pourcent		descriptiondinterface1
n			ZoRRo			arbre()			Lumière!
```

## Exercice 2
Vérifier si les déclarations de variables ci-dessous sont conformes aux règles du C.

```
{
  int a, b=2, c;
  float 4roues, Deux_Roues, tricycle;
  double PIBSuisse_;
  real  PIB_USA_en_$;
  char c;
}
```

Si ce n'est pas le cas, dire pourquoi.

## Exercice 3
Écrire la définition des variables pour un programme qui utilise les valeurs suivantes :
- la valeur de {{<katex>}}\pi{{</katex>}}
- un numéro de téléphone à 10 chiffres
- le sexe d'une personne (Homme / Femme)
- le taux de change de l'Euro en francs suisse
- le numéro du mois actuel (4 pour avril, 5 pour mai, ...)
- l'initiale de votre premier prénom
- la valeur boursière de la société Apple (>150'000'000'000 de $)
 
Justifier les choix faits.

## Exercice 4
Écrire la définition des variables pour le programme suivants :

```c
#include <stdio.h>

int main(void)
{
  // Definitions

  // Instructions
  pi = 3.14; // Not needed if we use const double pi = 3.14
  birthYear = 1963;
  month = 10;
  day = 10;
  letter = 'b';

  return 0 ;
}
```

## Exercice 5 
Représenter les nombres binaires suivants en notation décimale et hexadécimale.

{{<katex>}}01010001_{2} = {{</katex>}}
&nbsp;

{{<katex>}}00011110_{2} = {{</katex>}}

{{<katex>}}00111100_{2} = {{</katex>}}
&nbsp;

{{<katex>}}01111000_{2} = {{</katex>}}
&nbsp;

## Exercice 6
Représenter les nombres décimaux suivants en notation binaire et hexadécimale.

{{<katex>}}33_{10} = {{</katex>}}
&nbsp;

{{<katex>}}255_{10} = {{</katex>}}
&nbsp;

{{<katex>}}101_{10} = {{</katex>}}
&nbsp;

## Exercice 7
En représentation binaire, comment savoir si un nombre est pair ou impair ?

## Exercice 8  
Combien de valeurs peut-on dénombrer avec des mots de 8, 16, 32 et 64 bits ?

## Exercice 9
Soient 3 octets arrivant sur un bus de 8 bits, quel est leur code ascii associé et quel est le mot formé ? (exercice avec calculatrice et table ascii)

{{<katex>}}00111010_{2} = {{</katex>}}
&nbsp;

{{<katex>}}00101101_{2} = {{</katex>}}
&nbsp;

{{<katex>}}00101001_{2} = {{</katex>}}
&nbsp;

## Exercice 10
Soient 3 nombres hexadécimaux, quel est leur code ascii associé et quel est le mot formé ? (avec calculatrice)

{{<katex>}}31_{16}{{</katex>}}
&nbsp;

{{<katex>}}32_{16}{{</katex>}}
&nbsp;

{{<katex>}}32_{16}{{</katex>}}
&nbsp;

## Exercice 11

Compléter le programme suivant pour qu’il échange le contenu des variables {{<katex>}}variable1{{</katex>}} et {{<katex>}}variable2{{</katex>}}.

```c
#include <stdio.h>

int main(void)
{
  int variable1 = 10;
  int variable2 = 5;

  // Before swapping the variables content
  printf("Variable 1: %d \n", variable1); // Variable 1: 10
  printf("Variable 2: %d \n", variable2); // Variable 2: 5

  // Swap variables content

  ...

  // After swapping the variables content
  printf("Variable 1: %d \n", variable1); // Variable 1: 5
  printf("Variable 2: %d \n", variable2); // Variable 2: 10
}
```

{{< notion_avancee >}}
## Exercice 12
Écrire le code permettant d’échanger les valeurs contenues dans les deux variables a et b sans utiliser d’autre variable.
{{< /notion_avancee >}}

{{< notion_avancee >}}
## Exercice 13
Quelle est la valeur du nombre de type **`float`** dans la variable **`chouia`** dont le contenu mémoire est représenté ci-dessous ?

```c
float chouia    /* = ??? */    ;
```
{{< /notion_avancee >}}

{{< figure src="/images/chouia.png#center" >}}

## Exercice 21
Écrire un programme C qui convertit une température saisie par l’utilisateur en 
degrés Celsius, en degrés Fahrenheit et l’affiche :

```
Enter a temperature in Celsius: 12
12 degres Celsius correspond to a 53.6 degres Fahrenheit
```

Indication : {{<katex>}} T_F = 32 + 1.8*T_C {{</katex>}}

## Exercice 22
Écrire un programme C qui effectue un calcul d'intérêts et de capital pour un compte en banque.
Il demande à l'utilisateur d'introduire:
- Le capital initial sur le compte (francs et centimes)
- Le taux d'intérêt (annuel) du compte en pourcent
- La durée du dépôt (on ne peut retirer l'argent qu'au terme d'une année complète)
puis il calculera le montant disponible lors du retrait et l'affichera en francs et 
centimes selon la formule {{<katex>}}asset = initAmount * (1 + rate)^{duration}{{</katex>}}

```
What is your initial asset? 1000
What is your yearly interest rate (in pourcent)?: 2.5
Duration in years? 30

After 30 years, your assets (with interest) will be     2097.57 SFr
```

{{< notion_avancee >}}
## Exercice 23
Améliorer l'affichage pour avoir des séparateurs après les milliers, et millions, et 
arrondir le montant à 5 centimes. La valeur 1876435.264901 affichera par exemple **1'876'435.30 SFr**
{{< /notion_avancee >}}

{{< notion_avancee >}}
## Exercice 24
Implémenter le codage d’un nombre réel donné par l’utilisateur, en virgule flottante selon IEEE754
- Calcul du bit signe (facile)
- Calcul de l’exposant (moyen)
- Calcul de la mantisse (difficile?)
- Vérification avec les bits du nombre mémorisé dans une variable float (difficile)
{{< /notion_avancee >}}

# Défis

## Comparaison de flottants
Qu'affiche le programme suivant ? Pourquoi ? Quelle est la bonne manière de comparer des **`double`** ?

```c
#include <stdio.h>

int main(void)
{
  double d1 = 0.3;
  double d2 = 0.1 + 0.1 + 0.1;
  if (d1 == d2)
  {
    printf("d1 is equal to d2\n");
  }
  else
  {
    printf("d1 is NOT equal to d2\n");
  }
  

  return 0;
}
```

Pour voir ce qui se passe bit par bit, suivez le scénario « 0.1 + 0.2 en double » :

{{<viz "https://he-arc.github.io/1242.1-Langage_C-VIZ/ints-floats/?scenario=double-sum">}}

{{<details "Explications" >}}
Le programme affiche **`d1 is NOT equal to d2`**.
En effet, en représentation binaire, 0.1 est une valeur périodique (comme 1/3 en décimal).
Donc, 0.1 ne peut pas être représentée exactement en binaire.
Par conséquent, la somme de 3 fois 0.1 n'est pas exactement égale à 0.3.
La bonne manière de comparer des **`double`** est de vérifier que la différence entre les deux valeurs est inférieure à une petite valeur epsilon (typiquement la plus petite valeur représentable par un **`double`** : **`DBL_EPSILON`**).

<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_02.06_DoubleComparison_main.c run=true -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>
#include <math.h>
#include <float.h>

int main(void)
{
  double d1 = 0.3;
  double d2 = 0.1 + 0.1 + 0.1;
  if (d1 == d2)
  {
    printf("d1 is equal to d2\n");
  }
  else
  {
    printf("d1 is NOT equal to d2\n");
  }

  if (fabs(d1 - d2) < DBL_EPSILON)
  {
    printf("d1 is approximately equal to d2\n");
  }
  else
  {
    printf("d1 is NOT approximately equal to d2\n");
  }

  return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
d1 is NOT equal to d2
d1 is approximately equal to d2
```
<p class="run-info">Compiled and executed on 2026-09-21 19:44 from 18f0dd4.</p>
<!-- SNIPPET:END -->
{{</details>}}

## Cast de **`double`** en **`char`**

Qu'affiche le programme suivant ? Pourquoi ?

```c
#include <stdio.h>

int main(void)
{
	// Cast 128 into a char (8 bits) => overflow
	printf("c1 = %d\n", (char)128);
	char c1 = 128;
	printf("c1 = %d\n", c1);

	// 1)
	double d2 = 128.99;
	char c2 = (char) d2;
	printf("d2 = %lf\n", d2);
	printf("c2 = %d\n", (char) c2);

	// 2)
	double d3 = (char) 128.99;
	char c3 = (char) d3;
	printf("d3 = %lf\n", d3);
	printf("c3 = %d\n", (char) c3);
	printf("c3 = %d\n", (char) 128.99);

	return 0;
}
```

{{< details "Explications" >}}
Le code cast un **`double`** (128.99) en **`char`**.
Comme la valeur maximale représentable par un **`char`** est 127, il devrait y avoir débordement (overflow).
On s'attend donc à avoir -128 au final.

Cependant, le programme affiche :

```
c1 = -128
c1 = -128
d2 = 128.990000
c2 = -128
d3 = 127.000000
c3 = 127
c3 = 127
```

La norme dit :

> **6.3.1.4 Real floating and integer**
> 
> When a finite value of real floating type is converted to an integer type other than _Bool, the fractional part is discarded (i.e., the value is truncated toward zero).
> **If the value of the integral part cannot be represented by the integer type, the behavior is undefined.**

Donc, quand un **`double`** est casté en **`char`**, seule la partie entière est conservée.
Si elle ne peut pas être représentée dans le type entier demandé (ici **`char`**), alors c'est un **comportement indéfini**.

Dans l'exemple de code donné, les parties 1) et 2) sont donc des comportements indéfinis.
Et le compilateur (ici GCC) va faire les choses différemment.

Dans le cas 1), comme la valeur est stockée dans une variable, le cast se fera à l'exécution.
Il prend donc la valeur stockée dans la variable (128.99), ne garde que la partie entière (128), et la cast en **`char`**.
Si **`char`** est signé (plage [-128,127]), 128 n’est pas représentable : la conversion a un comportement indéfini.
Dans ce cas particulier, l’exécution affiche -128, mais elle pourrait tout aussi bien afficher 0, 127, 42, ou provoquer un crash.
Si **`char`** est non signé (plage [0,255]), la conversion est bien définie et donne 128.

Dans le cas 2), le compilateur voit directement que la partie entière de la constante 128.99 ne pourra pas être représentée sur un **`char`** et prend des mesures, donc directement durant la compilation.
En particulier, il décide d'utiliser la valeur maximale représentable par un **`char`**, et donc on récupère 127.

**👉 Ne jamais se fier au résultat d’un cast hors bornes. En C, c’est un comportement indéfini.**

{{< /details >}}
