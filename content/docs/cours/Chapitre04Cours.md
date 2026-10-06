---
title: "4. Entrées-sorties"
weight: 1
---

# CHAPITRE 4 : entrées-sorties

{{< attention >}}
**`scanf` : pour apprendre, pas pour un vrai programme.**

Dans ce chapitre, nous utilisons **`scanf`** pour des raisons pédagogiques (format, tampon, valeur de retour, etc.). Mais **`scanf`** est déconseillé pour des raisons de sécurité. Dans un vrai programme, on lit la ligne entière avec **`fgets`**, puis on l'analyse avec **`sscanf`**, ou **`strtol`** pour détecter aussi un nombre hors limites.

**`printf`** ne pose cependant pas ce problème.
{{< /attention >}}

## Slides
{{<slides "https://he-arc.github.io/1242.1-Langage_C-SLIDES/04_Entrees-Sorties.html">}}

[Version imprimable (faire CTRL+P)](https://he-arc.github.io/1242.1-Langage_C-SLIDES/04_Entrees-Sorties.html?print-pdf)

{{< a_noter >}}
Les slides ne présentent que les formats les plus utilisés. Quelques compléments.

**Réels : le cas du `float`**
- Les slides utilisent **`double`** et **`%lf`** partout. Un **`float`** ne se justifie que dans des cas particuliers (mémoire limitée, calcul graphique, etc.).
- Avec **`printf`**, **`%f`** et **`%lf`** sont équivalents : un **`float`** passé à **`printf`** est converti en **`double`**.
- Avec **`scanf`**, il faut **`%f`** pour un **`float`** et **`%lf`** pour un **`double`** : **`scanf`** reçoit une adresse et doit savoir s'il écrit 4 octets (**`float`**) ou 8 (**`double`**). Voir l'exemple 04.98.

**Hexadécimal**
- **`%X`** affiche les lettres en majuscules : **`printf("%x %X", 255, 255);`** affiche **`ff FF`**.
- La norme prévoit **`%x`** pour un **`unsigned int`**. Avec un **`int`** positif, le résultat est le même.
- Avec un **`int`** négatif, c'est en principe un comportement indéfini (UB). En pratique, on obtient la représentation en complément à 2 : **`printf("%x", -1);`** affiche **`ffffffff`**.

Tous les formats : [cppreference → fprintf](https://en.cppreference.com/w/c/io/fprintf).
{{< /a_noter >}}

## Squelette à remplir
{{<a_faire>}}
Remplir le squelette suivant au fur et à mesure du cours.
{{</a_faire>}}
<!-- SNIPPET:BEGIN source_file=chap4.c id=1242.1_Skeletons_04_chap4.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `chap4.c`**

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
<!-- SNIPPET:END -->

## Exemples

### 04.01 : comment lire des caractères, des entiers et des mots avec `scanf` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.01_InputOutput_main.c run=true stdin="S\nG\n28/11/70" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	int year, month, day;
	char name1, name2;

	printf("First letter in your first name: ");
	scanf(" %c", &name1);
	printf("First letter in your last name: ");
	scanf(" %c", &name2);

	printf("Your birthdate (dd/mm/yy): ");
	scanf(" %d/%d/%d", &day, &month, &year);

	printf("\nYour initials are %c.%c.\n", name1, name2);
	printf("You are born on %d/%d/%d\n", day, month, year);

	printf("\nASCII CODE: %c=%d, %c=%d\n", name1, name1, name2, name2);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
First letter in your first name: S
First letter in your last name: G
Your birthdate (dd/mm/yy): 28/11/70

Your initials are S.G.
You are born on 28/11/70

ASCII CODE: S=83, G=71
```
<p class="run-info">Compiled and executed on 2026-10-01 13:34 from f00c4b5.</p>
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=main_with_strings.c id=1242.1_Exemples_04.01_InputOutput_main_with_strings.c run=true stdin="Ada\nLovelace" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main_with_strings.c`**

```c
#include <stdio.h>

int main(void)
{
	// Messages are "const char *" because they are not supposed to be modified
	const char *enter_your_first_name_msg = "Enter your first name: ";
	const char *enter_your_last_name_msg = "Enter your last name: ";
	// first_name and last_name are arrays of characters because they are supposed to be modified
	char first_name[80];
	char last_name[80];

	// WARNING: this will not work if the name has a space in it
	// %79s: at most 79 characters + '\0' in 80
	printf("%s", enter_your_first_name_msg);
	scanf("%79s", first_name);
	printf("%s", enter_your_last_name_msg);
	scanf("%79s", last_name);

	printf("Your name is %s %s\n", first_name, last_name);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main_with_strings.exe main_with_strings.c
$ ./main_with_strings.exe
Enter your first name: Ada
Enter your last name: Lovelace
Your name is Ada Lovelace
```
<p class="run-info">Compiled and executed on 2026-10-01 13:30 from f00c4b5.</p>
<!-- SNIPPET:END -->

### 04.02 : comment lire une ligne et valider une saisie ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.02_Input_main.c run=true stdin="hello, world\n12:ss:12\n12:12:12" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	char line[80];	// string variable

	// NOTE: after display, sets the cursor to the next line
	puts("Write a line of text:");
	fgets(line, sizeof(line), stdin);
	puts("The line variable has the following value:");
	puts(line);

	const int nbExpectedValues = 3;
	int  h, m, s;
	int  status;

	do // input with validation
	{
		printf("\nPlease enter hour (h:m:s): ");
		status = scanf(" %d:%d:%d", &h, &m, &s);
		if (status == EOF)
		{
			return 1; // input closed
		}

		// Do NOT use fflush(stdin): undefined behavior (fflush is only for output streams).
		// Empty the buffer "manually" instead.
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);

			// BIIIP to let user know when there is a problem
			if (status != nbExpectedValues)
			{
				printf("\a");
			}
		}
	} while (status != nbExpectedValues);	// status == 3, then we read 3 inputs so we are ok

	printf("\nInput hour is: %d:%d:%d\n", h, m, s);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
Write a line of text:
hello, world
The line variable has the following value:
hello, world


Please enter hour (h:m:s): 12:ss:12
␇
Please enter hour (h:m:s): 12:12:12

Input hour is: 12:12:12
```
<p class="run-info">Compiled and executed on 2026-10-06 14:18 from 5aa5850.</p>
<!-- SNIPPET:END -->

### 04.03 : comment lire caractère par caractère et vider le tampon d'entrée ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.03_PrintfScanf_main.c run=true stdin="abc.\nhello\n12:34:56" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
	char line[80];	// String variable

	printf("Input and output characters with getchar/putchar. Use '.' to quit.\n\n");
	int ch; // int, not char: getchar() may return EOF
	while ((ch = getchar()) != '.' && ch != EOF)
	{
		putchar(ch);
	}

	putchar('\n');

	// Do NOT use fflush(stdin): undefined behavior (fflush is only for output streams).
	// Empty the buffer "manually" instead.
	{
		int c;
		do
		{
			c = getchar();
		} while (c != '\n' && c != EOF);
	}

	// NOTE: after display, sets the cursor to the next line
	puts("Write a line of text:");
	// gets may read too many characters
	// gets(ligne);

	// fgets also reads the character "\n"
	fgets(line, sizeof(line), stdin);

	printf("Print all characters in line after fgets:\n");
	int i;
	for (i = 0; i < (int) strlen(line); i++)
	{
		printf("  %d : %d\n", i, line[i]);
	}

	// Find a character
	char *p = strchr(line, '\n');
	if (p != NULL)
	{
		*p = 0; // We found an end of line
	}
	else // If we did not find "\n", then we must flush the stdin buffer
	{
		int c;
		do
		{
			c = getchar();
		} while (c != '\n' && c != EOF);
	}

	printf("Print all characters in line after fgets,\n");
	printf("but after having deleted character \\n :\n");
	for (i = 0; i < (int) strlen(line); i++)
	{
		printf("  %d : %d\n", i, line[i]);
	}

	puts("The line variable has the following value:");
	puts(line);

	const int nbExpectedValues = 3;
	int  h, m, s;
	int  status;

	do // input with validation
	{
		printf("\nPlease enter hour (h:m:s): ");
		status = scanf(" %d:%d:%d", &h, &m, &s);
		if (status == EOF)
		{
			return 1; // input closed
		}

		// Do NOT use fflush(stdin): undefined behavior (fflush is only for output streams).
		// Empty the buffer "manually" instead.
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);

			// BIIIP to let user know when there is a problem
			if (status != nbExpectedValues)
			{
				printf("\a");
			}
		}
	} while (status != nbExpectedValues);	// status == 3, then we read 3 inputs so we are ok

	printf("\nInput hour is: %d:%d:%d\n", h, m, s);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
Input and output characters with getchar/putchar. Use '.' to quit.

abc.
abc
Write a line of text:
hello
Print all characters in line after fgets:
  0 : 104
  1 : 101
  2 : 108
  3 : 108
  4 : 111
  5 : 10
Print all characters in line after fgets,
but after having deleted character \n :
  0 : 104
  1 : 101
  2 : 108
  3 : 108
  4 : 111
The line variable has the following value:
hello

Please enter hour (h:m:s): 12:34:56

Input hour is: 12:34:56
```
<p class="run-info">Compiled and executed on 2026-10-06 14:18 from 5aa5850.</p>
<!-- SNIPPET:END -->

### 04.04 : que se passe-t-il quand le format ne correspond pas au type ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.04_IOErrors_main.c run=true cflags="-Wno-error=format" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

// NOTE: many gcc warnings associated with wrong format.
int main(void)
{
	char a = 65;
	printf("char:    %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", a, a, a, a);

	int  b = 65;
	printf("int :    %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", b, b, b, b);

	float c = 65.f;
	printf("float:   %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", c, c, c, c);

	double d = 65.;
	printf("double:  %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", d, d, d, d);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=format -o main.exe main.c
main.c: In function 'main':
main.c:7:55: warning: format '%f' expects argument of type 'double', but argument 4 has type 'int' [-Wformat=]
    7 |         printf("char:    %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", a, a, a, a);
      |                                                   ~~~~^                        ~
      |                                                       |                        |
      |                                                       double                   int
      |                                                   %8.3d
main.c:7:68: warning: format '%lf' expects argument of type 'double', but argument 5 has type 'int' [-Wformat=]
    7 |         printf("char:    %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", a, a, a, a);
      |                                                               ~~~~~^              ~
      |                                                                    |              |
      |                                                                    double         int
      |                                                               %8.3d
main.c:10:55: warning: format '%f' expects argument of type 'double', but argument 4 has type 'int' [-Wformat=]
   10 |         printf("int :    %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", b, b, b, b);
      |                                                   ~~~~^                        ~
      |                                                       |                        |
      |                                                       double                   int
      |                                                   %8.3d
main.c:10:68: warning: format '%lf' expects argument of type 'double', but argument 5 has type 'int' [-Wformat=]
   10 |         printf("int :    %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", b, b, b, b);
      |                                                               ~~~~~^              ~
      |                                                                    |              |
      |                                                                    double         int
      |                                                               %8.3d
main.c:13:33: warning: format '%c' expects argument of type 'int', but argument 2 has type 'double' [-Wformat=]
   13 |         printf("float:   %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", c, c, c, c);
      |                               ~~^                                        ~
      |                                 |                                        |
      |                                 int                                      double
      |                               %2f
main.c:13:44: warning: format '%d' expects argument of type 'int', but argument 3 has type 'double' [-Wformat=]
   13 |         printf("float:   %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", c, c, c, c);
      |                                         ~~~^                                ~
      |                                            |                                |
      |                                            int                              double
      |                                         %11f
main.c:16:33: warning: format '%c' expects argument of type 'int', but argument 2 has type 'double' [-Wformat=]
   16 |         printf("double:  %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", d, d, d, d);
      |                               ~~^                                        ~
      |                                 |                                        |
      |                                 int                                      double
      |                               %2f
main.c:16:44: warning: format '%d' expects argument of type 'int', but argument 3 has type 'double' [-Wformat=]
   16 |         printf("double:  %%c: %2c  %%d: %11d %%f: %8.3f %%lf: %8.3lf\n", d, d, d, d);
      |                                         ~~~^                                ~
      |                                            |                                |
      |                                            int                              double
      |                                         %11f
$ ./main.exe
char:    %c:  A  %d:          65 %f:    0.000 %lf:    0.000
int :    %c:  A  %d:          65 %f:    0.000 %lf:    0.000
float:   %c:  ␀  %d:           0 %f:   65.000 %lf:   65.000
double:  %c:  ␀  %d:           0 %f:   65.000 %lf:   65.000
```
<p class="run-info">Compiled and executed on 2026-10-01 12:15 from f00c4b5.</p>
<!-- SNIPPET:END -->

{{< attention >}}
Passer à **`printf`** un argument dont le type ne correspond pas au format est un comportement indéfini (UB). Les valeurs affichées ici ne sont pas garanties : un autre compilateur, une autre plateforme ou d'autres options peuvent donner un autre résultat.
{{< /attention >}}

### 04.93 : quelle différence entre un fichier ouvert en mode texte et en mode binaire ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.93_PrintfWithNewLineAsCharacter_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
  FILE *f1 = fopen("text_mode.txt", "w");
  FILE *f2 = fopen("binary_mode.txt", "wb");
  if (f1 == NULL || f2 == NULL)
  {
    printf("Cannot open the files\n");
    return 1;
  }

  fputc('A', f1);
  fputc(0x0A, f1);
  fputc('B', f1);
  
  fputc('A', f2);
  fputc(0x0A, f2);
  fputc('B', f2);

  fclose(f1);
  fclose(f2);

  return 0;
}
```
<!-- SNIPPET:END -->

### 04.94 : comment `scanf` lit-il un entier en octal ou en hexadécimal ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.94_IODecimalsOctalsAndHexadecimals_main.c run=true stdin="032\n0x32" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
  int value = 0;

  // Reads a decimal value
  // Entering 032 will be interpreted as 32
  scanf("%d", &value);
  printf("Value: %d\n", value);

  // Reads an octal or hexadecimal value
  // Entering 032 will be interpreted as 26
  // Entering 0x32 will be interpreted as 50
  scanf("%i", &value);
  printf("Value: %d\n", value);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
032
Value: 32
0x32
Value: 50
```
<p class="run-info">Compiled and executed on 2026-10-06 14:15 from 5aa5850.</p>
<!-- SNIPPET:END -->

### 04.95 : comment `getch`, `scanf` et `fgets` consomment-ils le tampon ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.95_BufferExamples_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
	char first, letter, word[32], sentence[128];

	printf("Please enter a phrase: \n");

	first = getch();
	scanf("%c", &letter);

	scanf("%31s", word);

	fgets(sentence, 128, stdin);

	printf("first = %c\n", first);
	printf("letter = %c\n", letter);
	printf("word = %s\n", word);
	printf("sentence = %s\n", sentence);

	return 0;
}
```
<!-- SNIPPET:END -->

### 04.96 : pourquoi `printf("%lf", 42)` n'affiche-t-il pas `42.000000` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.96_printf_lf_with_int_main.c run=true cflags="-Wno-error=format" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

void myPrintingFunction(double valueToPrint)
{
	printf("%lf\n", valueToPrint);
}

int main(void)
{
	int valueToPrint = 42;

	// From ISO C Standard:
	//	" If a conversion specification is invalid, the behavior is undefined.
	//    If any argument is not the correct type for the corresponding conversion
	//		specification, the behavior is undefined."
	// => so the following line has an undefined behavior because
	//    we pass %lf as the conversion specification and valueToPrint is an int
	// NOTE: printf accepts a variable number of parameters, with variable types.
	// => so it does not know in advance the type of the parameter and thus
	//    cannot cast them to the expected type.
	printf("%lf\n", valueToPrint); // Prints 0.000000 with gcc and MSVC on Windows (UB: may differ elsewhere)

	// Here, we still pass an int.
	// But myPrintingFunction expects a double so the int parameter is first converted
	// into a double and then used in printf.
	// => In that case, it works.
	myPrintingFunction(valueToPrint); // Prints 42.000000

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=format -o main.exe main.c
main.c: In function 'main':
main.c:21:19: warning: format '%lf' expects argument of type 'double', but argument 2 has type 'int' [-Wformat=]
   21 |         printf("%lf\n", valueToPrint); // Prints 0.000000 with gcc and MSVC on Windows (UB: may differ elsewhere)
      |                 ~~^     ~~~~~~~~~~~~
      |                   |     |
      |                   |     int
      |                   double
      |                 %d
$ ./main.exe
0.000000
42.000000
```
<p class="run-info">Compiled and executed on 2026-10-06 14:15 from 5aa5850.</p>
<!-- SNIPPET:END -->

### 04.97 : quelle différence entre `scanf` et `scanf_s` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.97_scanf_vs_scanf_s_main.c run=true stdin="x y\na b c d" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
// scanf_s comes from Annex K of the C standard (bounds-checking interfaces), which is optional:
// glibc (Linux) does not provide it; on Windows, gcc uses the one from Microsoft's UCRT.
// scanf_s is NOT a drop-in replacement for scanf: %c, %s and %[ need an extra buffer size argument.
// For this course, use scanf.

#include <stdio.h>

int main(void)
{
	// Reading 1 character
	char c1 = 'a', c1_s = 'a';
	printf("Please enter 2 characters: ");
	scanf(" %c", &c1);

	// scanf_s(" %c", &c1_s); // UB: the buffer size is missing, and gcc does not warn about it
	scanf_s(" %c", &c1_s, 1);
	printf("Read characters are %c and %c.\n", c1, c1_s);

	// Reading several characters: one buffer size after each variable address
	char c2, c3;
	printf("Please enter 4 characters: ");
	scanf(" %c %c", &c2, &c3);

	char c2_s, c3_s;
	// scanf_s(" %c %c", &c2_s, &c3_s); // UB: idem
	scanf_s(" %c %c", &c2_s, 1, &c3_s, 1);

	printf("Read characters are %c, %c, %c and %c.\n", c2, c3, c2_s, c3_s);

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -o main.exe main.c
$ ./main.exe
Please enter 2 characters: x y
Read characters are x and y.
Please enter 4 characters: a b c d
Read characters are a, b, c and d.
```
<p class="run-info">Compiled and executed on 2026-10-01 12:28 from f00c4b5.</p>
<!-- SNIPPET:END -->

### 04.98 : comment afficher et lire des `float` et des `double` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.98_IOFloatsAndDoubles_main.c run=true stdin="1.5 2.5 3.5 4.5 5.5\n1.5 2.5 3.5 4.5 5.5\n2.25" cflags="-Wno-error=format" -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	float smallFloat = 1.0f;
	float bigFloat = 12345678900.0f;
	double smallDouble = (double)smallFloat;
	double bigDouble = (double)bigFloat;

	// PRINTF

	// Several supported formats for floats: %f, %e, %E, %g and %G
	printf("PRINTF FOR FLOATS\n");
	printf("\t%f\n\t%e\n\t%E\n\t%g\n\t%G\n", smallFloat, smallFloat, smallFloat, smallFloat, smallFloat);
	printf("\t%f\n\t%e\n\t%E\n\t%g\n\t%G\n", bigFloat, bigFloat, bigFloat, bigFloat, bigFloat);

	// Same format for doubles "augmented" with 'l' (since C99)
	// NOTE: for printf, formats like %f (et al.) can be used interchangeably with %lf (et al.)
	// ==>> DO NOT DO THIS!
	printf("PRINTF FOR DOUBLES\n");
	printf("\t%lf\n\t%le\n\t%lE\n\t%lg\n\t%lG\n", smallDouble, smallDouble, smallDouble, smallDouble, smallDouble);
	printf("\t%lf\n\t%le\n\t%lE\n\t%lg\n\t%lG\n", bigDouble, bigDouble, bigDouble, bigDouble, bigDouble);

	// SCANF
	// Same formats as for printf but we additionally need to specify whether we are reading a float or a double with 'l' in the format
	float fa = 0, fb = 0, fc = 0, fd = 0, fe = 0;
	printf("SCANF FOR FLOATS\n");
	scanf(" %f %e %E %g %G", &fa, &fb, &fc, &fd, &fe); // <<== DO NOT FORGET THE '&'
	printf("\t%f\n\t%e\n\t%E\n\t%g\n\t%G\n", fa, fb, fc, fd, fe);

	double da = 0, db = 0, dc = 0, dd = 0, de = 0;
	printf("SCANF FOR DOUBLES\n");
	scanf(" %lf %le %lE %lg %lG", &da, &db, &dc, &dd, &de); // <<== DO NOT FORGET THE '&'
	printf("\t%lf\n\t%le\n\t%lE\n\t%lg\n\t%lG\n", da, db, dc, dd, de);

	// COMMON MISTAKES
	// Reading a float into a double
	printf("MISTAKE: reading a float into a double\n");
	scanf(" %f", &da);
	printf("\t%f\n", da);

	// Reading a double into a float: see example 04.99

	return 0;
}
```

**Compilation et exécution**

```terminal
$ gcc -Wall -Wextra -Wpedantic -Werror -std=c23 -Wno-error=format -o main.exe main.c
main.c: In function 'main':
main.c:39:18: warning: format '%f' expects argument of type 'float *', but argument 2 has type 'double *' [-Wformat=]
   39 |         scanf(" %f", &da);
      |                 ~^   ~~~
      |                  |   |
      |                  |   double *
      |                  float *
      |                 %lf
$ ./main.exe
PRINTF FOR FLOATS
	1.000000
	1.000000e+00
	1.000000E+00
	1
	1
	12345678848.000000
	1.234568e+10
	1.234568E+10
	1.23457e+10
	1.23457E+10
PRINTF FOR DOUBLES
	1.000000
	1.000000e+00
	1.000000E+00
	1
	1
	12345678848.000000
	1.234568e+10
	1.234568E+10
	1.23457e+10
	1.23457E+10
SCANF FOR FLOATS
1.5 2.5 3.5 4.5 5.5
	1.500000
	2.500000e+00
	3.500000E+00
	4.5
	5.5
SCANF FOR DOUBLES
1.5 2.5 3.5 4.5 5.5
	1.500000
	2.500000e+00
	3.500000E+00
	4.5
	5.5
MISTAKE: reading a float into a double
2.25
	1.500000
```
<p class="run-info">Compiled and executed on 2026-10-06 14:29 from 5aa5850.</p>
<!-- SNIPPET:END -->

### 04.99 : que se passe-t-il si on lit un `double` dans un `float` ?
<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exemples_04.99_ScanfDoubleIntoFloat_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <stdio.h>

int main(void)
{
	float fa = 0, fb = 0, fc = 0;

	// MISTAKE: reading a double (%lf) into a float
	// scanf writes 8 bytes where there are only 4 => undefined behavior:
	// a neighbor variable (fa or fc) may be changed, or the stack may be corrupted.
	// NOTE (MSVC): must be run in Release mode. In Debug mode, MSVC adds extra bytes "around" the local variables
	// for run-time checks and reports "Run-Time Check Failure #2 - Stack around the variable 'fa' was corrupted."
	printf("Enter a real number: ");
	scanf(" %lf", &fb);
	printf("\t%f\n\t%f\n\t%f\n", fa, fb, fc);

	return 0;
}
```
<!-- SNIPPET:END -->

{{< attention >}}
Lire un **`double`** (**`%lf`**) dans un **`float`** écrit 8 octets là où il n'y en a que 4 : c'est un comportement indéfini (UB), qui peut modifier une autre variable ou corrompre la pile. Le résultat change d'une exécution à l'autre, selon l'environnement : c'est pourquoi cet exemple n'est pas exécuté ici.
{{< /attention >}}

## Exercices

### Exercice 1 : `printf`
Créer un programme C avec l'instruction **`printf`**, qui produit l'affichage suivant :

```terminal
Initials: __
Code: __


Birthdate: __/__/__
Number: __\__
Text: "____"
```

{{< attention >}}
L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

### Exercice 2 : codes ASCII
Créer un programme C demandant à l'utilisateur d'entrer 3 lettres.
Le programme doit fournir en résultat les codes ASCII des 3 lettres saisies.
L'utilisateur doit pouvoir entrer les lettres soit l'une à la suite de l'autre, soit en les séparant par un retour à la ligne.

**L'affichage doit se présenter ainsi :**

```terminal
Please enter 3 letters:
a b c

Here are the corresponding ASCII codes:
a--------->97
b--------->98
c--------->99
```

{{< attention >}}
L'affichage doit commencer par 2 retours à la ligne et se terminer par un retour à la ligne.
{{< /attention >}}

### Exercice 3 : surface d'un cercle
Écrire un programme qui calcule la surface d'un cercle lorsqu'on introduit la valeur du rayon.
Le résultat sera affiché avec 2 chiffres après le point.

**L'affichage doit se présenter ainsi :**

```terminal
Circle radius: 1
pi = 3.141593
Circle surface = 3.14
```

{{< attention >}}
L'affichage doit se terminer par un retour à la ligne.
{{< /attention >}}

<br>

### Exercice 4 : déplacer un symbole 🌶️
{{< notion_avancee >}}
Faire un programme qui récupère en continu les caractères saisis au clavier (sans **`<enter>`**) pour déplacer un symbole **`*`** à travers l’écran.
Si le symbole dépasse un des bords, il réapparait de l’autre coté.
Pour effacer l’écran, on peut utiliser une commande système **`cls`** par exemple.
{{< /notion_avancee >}}
