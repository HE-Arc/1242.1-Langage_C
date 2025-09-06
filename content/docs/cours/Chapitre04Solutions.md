---
title: "Chapitre 4 : solutions"
draft: false
weight: 21
---
# Chapitre 4 : solutions

## Exemples
### `1242.1_04.01_InputOutput`
```c
// This is important when using Visual Studio.
// This is done automagically when using CMake.
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{
	int year, month, day;
	char name1, name2;
	int status = 0;

	printf("First letter in your first name: ");
	status = scanf(" %c", &name1);
	printf("First letter in your last name: ");
	status = scanf(" %c", &name2);

	printf("Your birthdate (jj/mm/aa): ");
	status = scanf(" %d/%d/%d", &day, &month, &year);

	printf("\nYour initials are %c.%c.\n", name1, name2);
	printf("You are born on %d/%d/%d\n", day, month, year);

	printf("\nASCII CODE: %c=%d, %c=%d\n", name1, name1, name2, name2);

	return 0;
}
```

### `1242.1_04.02_Input`
```c
#include <stdio.h>

int main(void)
{
	char line[80];	// string variable

	// NOTE: after display, sets the cursor to the next line
	puts("Write a line of text:");
	gets(line);
	puts("The line variable has the following value:");
	puts(line);

	const int nbExpectedValues = 3;
	int  h, m, s;
	int  status;

	do // input with validation
	{
		printf("\nPlease enter hour (h:m:s): ");
		status = scanf(" %d:%d:%d", &h, &m, &s);

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

### `1242.1_04.03_PrintfScanf`
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
	char line[80];	// String variable

	printf("Input and output characters with getchar/putchar. Use '.' to quit.\n\n");
	char ch;
	do
	{
		ch = getchar();
		putchar(ch);
	} while (ch != '.');

	putchar('\n');

	// fflush does not always work.
	// It is strongly advised NOT to use it
	// fflush(stdin);
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
	for (i = 0; i < strlen(line); i++)
	{
		printf("  %d : %d\n", i, line[i]);
	}

	// Find a character
	char *p = strchr(line, '\n');
	if (p != NULL)
	{
		*p = 0; // We found a end of line
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
	printf("but after having deleted charactere \\n :\n");
	for (i = 0; i < strlen(line); i++)
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

### `1242.1_04.04_IOErrors`
```c
#include <stdio.h>

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

### `1242.1_04.96_printf_lf_with_int`
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
	//	" If a conversion speciﬁcation is invalid, the behavior is undeﬁned.
	//    If any argument is not the correct type for the corresponding conversion
	//		speciﬁcation, the behavior is undeﬁned."
	// => so the following line has an undefined behavior because
	//    we pass %lf as the conversion specification and valueToPrint is an int
	// NOTE: printf accepts a variable number of parameters, with variable types.
	// => so it does not know in advance the type of the parameter and thus
	//    cannot cast them to the expected type.
	printf("%lf\n", valueToPrint); // Prints 0.000000 with VS

	// Here, we still pass an int.
	// But myPrintingFunction expects a double so the int parameter is first converted
	// into a double and then used in printf.
	// => In that case, it works.
	myPrintingFunction(valueToPrint); // Prints 42.000000

	return 0;
}
```

### `1242.1_04.97_scanf_vs_scanf_s`
```c
// This example shows main differences between scanf and scanf_s
// NOTE that Visual Studio will complain when using scanf alone.

// IMPORTANT: scanf_s is NOT a direct replacement for scanf. Some parameters may be different.
// SEE documentation: https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/scanf-s-scanf-s-l-wscanf-s-wscanf-s-l?view=vs-2019

// If you want to force Visual Studio to use scanf, define the following
#define _CRT_SECURE_NO_WARNINGS 1
// For this course, we recommend to use scanf instead of scanf_s and to define the following macro

#include <stdio.h>

int main(void)
{
	// According to the documentation:
	// "scanf_s and wscanf_s require you to specify buffer sizes for some parameters.
	//  Specify the sizes for all c, C, s, S, or string control set [] parameters.
	//  The buffer size in characters is passed as an additional parameter."
	// So for %c in particular, you need to specify the size of the buffer, that is 1

	// Reading 1 character
	char c1 = 'a', c1_s = 'a';
	printf("Please enter 2 characters: ");
	scanf(" %c", &c1);
	// Visual Studio:
	//			warning C4473: 'scanf_s' : not enough arguments passed for format string
	//			message: placeholders and their parameters expect 2 variadic arguments, but 1 were provided
	//			message: the missing variadic argument 2 is required by format string '%c'
	//			message: this argument is used as a buffer size

	// scanf_s("%c", &c1_s);

	// NOTE: when reading 1 character only, you get a warning but the result is still consistent.
	// However, this is risky and should not be used.
	// ==>> So specify buffer size instead
	scanf_s(" %c", &c1_s, 1);
	printf("Read characters are %c and %c.\n", c1, c1_s);

	// Reading several characters with scanf and scanf_s
	char c2, c3;
	printf("Please enter 4 characters: ");
	scanf(" %c %c", &c2, &c3);

	char c2_s, c3_s;
	// The following will NOT work properly
	// scanf_s(" %c %c", &c2_s, &c3_s);

	// Instead, specify buffer size after each variable address
	scanf_s(" %c %c", &c2_s, 1, &c3_s, 1);

	printf("Read characters are %c, %c, %c and %c.\n", c2, c3, c2_s, c3_s);

	return 0;
}
```

### `1242.1_04.98_IOFloatsAndDoubles`
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
	float fa, fb, fc, fd, fe = 0;
	printf("SCANF FOR FLOATS\n");
	scanf(" %f %e %E %g %G", &fa, &fb, &fc, &fd, &fe); // <<== DO NOT FORGET THE '&'
	printf("\t%f\n\t%e\n\t%E\n\t%g\n\t%G\n", fa, fb, fc, fd, fe);

	double da, db, dc, dd, de = 0;
	printf("SCANF FOR DOUBLES\n");
	scanf(" %lf %le %lE %lg %lG", &da, &db, &dc, &dd, &de); // <<== DO NOT FORGET THE '&'
	printf("\t%lf\n\t%le\n\t%lE\n\t%lg\n\t%lG\n", da, db, dd, dd, de);

	// COMMON MISTAKES
	// Reading a float into a double
	printf("MISTAKE: reading a float into a double\n");
	scanf(" %f", &da);
	printf("\t%f\n", da);

	// Reading a double into a float => writing in wrong memory locations
	// NOTE: must be ran in Release mode. In Debug mode, VS will add extras "around" the local variables in memory for
	// run-time checks
	printf("MISTAKE: reading a double into a float\n");
	fa = 0, fb = 0, fc = 0;
	scanf(" %lf", &fb);
	// Here, fc may be changed too
	printf("\t%f\n\t%f\n\t%f\n", fa, fb, fc);

	// In Debug mode, VS says "Run-Time Check Failure #2 - Stack around the variable 'fa' was corrupted. occurred"
	return 0;
}
```

### `1242.1_04.99_ScanfBufferOverflow`
```c
#include <stdio.h>

// IMPORTANT for Visual Studio: execute in RELEASE Mode to avoid additional debug padding around stack variables
int main(void)
{
	// IMPORTANT for Visual Studio: variables order on the stack is not guaranteed.
	// If we do char a[9] instead, then a and b will be in different order on the stack.
	char a[8] = "abcdefg";
	char b[8] = "abcdefg";
	printf("a is at address: %p\n", a);
	printf("b is at address: %p\n", b);

	printf("a = %s\n", a);
	printf("b = %s\n", b);
	scanf("%s", b); // Enter "abcdefg!!!!"
	printf("a = %s\n", a);
	printf("b = %s\n", b);

	return 0;
}
```

## Solutions exercices
[1242.1.04_Entrees-Sorties_Correction.pdf](/pdf/1242.1.04_Entrees-Sorties_Correction.pdf)

### `1242.1_04.01_InputOutput`
```c
// This is important when using Visual Studio.
// This is done automagically when using CMake.
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>  // printf, scanf

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

int main(void)
{
	// EXERCISE 1
	printf("Initials: __\n");
	printf("Code: __\n");
	printf("\n\n");
	printf("Birthdate: __/__/__\n");
	printf("Number: __\\__\n");
	printf("Text: \"____\"\n");

	// EXERCISE 2
	char letter1, letter2, letter3;
	int status = 0;

	int nbExpectedValues = 3;
	do
	{
		printf("\n\nPlease enter 3 letters:\n");
		status = scanf("%c %c %c", &letter1, &letter2, &letter3);

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

	printf("\nHere are the corresponding ASCII codes:\n");
	printf("%c--------->%d\n%c--------->%d\n%c--------->%d\n",
		letter1, letter1, letter2, letter2, letter3, letter3);

	// EXERCISE 3
	double radius, surface;

	nbExpectedValues = 1;
	do
	{
		printf("Circle radius: ");
		status = scanf("%lf", &radius);

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

	surface = radius * radius * M_PI;
	printf("pi = %f\n", M_PI);
	printf("Circle surface = %.2f\n", surface);

	return 0;
}
```

### `1242.1_04.01_InputOutput_StarGame`
```c
#include <conio.h>    // For getch()
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h> // for CONSOLE_SCREEN_BUFFER_INFO

#define VERSION_1

#ifdef VERSION_1
void getTerminalSize(short int *rows, short int *columns)
{
	CONSOLE_SCREEN_BUFFER_INFO csbi;

	GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi);
	*columns = csbi.srWindow.Right - csbi.srWindow.Left + 1;
	*rows = csbi.srWindow.Bottom - csbi.srWindow.Top + 1;

	// For debug purposes
	// printf("columns: %d\n", columns);
	// printf("rows: %d\n", rows);
}

int main(void)
{
	short maxLines, maxColumns = 0;
	short line = 15, column = 30;

	char direction;
	bool finished = false;
	while (!finished)
	{
		getTerminalSize(&maxLines, &maxColumns); // get terminal size

		for (int l = 0; l < line; l++)
			printf("\n");
		for (int c = 0; c < column; c++)
			printf(" ");
		printf("*");
		direction = getch(); // wait until a character is entered
		switch (direction)
		{
		case 'w':
			line--;
			system("cls");
			break;
		case 's':
			line++;
			system("cls");
			break;
		case 'a':
			column--;
			system("cls");
			break;
		case 'd':
			column++;
			system("cls");
			break;
		default: finished = true;
		}
		line = line < 0 ? maxLines : line % maxLines;
		column = column < 0 ? maxColumns : column % maxColumns;
	}

	return 0;
}
#endif

#ifdef VERSION_2
void HideCursor(void)
{
	// See windows.h library : https://docs.microsoft.com/en-us/windows/console/console-functions
	CONSOLE_CURSOR_INFO cci;

	GetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cci); // Read cursor info
	cci.bVisible = FALSE;   // Hide cursor
	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cci); // Write cursor info
}

void getTerminalSize(int *rows, int *columns)
{
	CONSOLE_SCREEN_BUFFER_INFO csbi;

	GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi);
	*columns = csbi.srWindow.Right - csbi.srWindow.Left + 1;
	*rows = csbi.srWindow.Bottom - csbi.srWindow.Top + 1;
}

int main(void)
{
	int LineCounter, SpaceCounter, LineMax, SpaceMax, i;
	unsigned char Input, Stop = FALSE;

	HideCursor();
	getTerminalSize(&LineMax, &SpaceMax);

	LineMax--;                  // Last line for info
	LineCounter = LineMax / 2;    // Begin in center
	SpaceCounter = SpaceMax / 2;

	while (Stop == FALSE)
	{
		system("CLS");
		for (i = 0; i < LineCounter; i++) printf("\n");
		for (i = 0; i < SpaceCounter; i++) printf(" ");
		printf("*");

		for (i = 0; i < LineMax - LineCounter; i++) printf("\n");
		printf("Space: %3d Line: %d", SpaceCounter, LineCounter);

		Input = getch();
		if (Input == 0xE0) Input = getch(); // arrow acquisition

		switch (Input)
		{
		case 0x50:         // down
		case 's':
			LineCounter++;
			break;

		case 0x48:         // up
		case 'w':
			LineCounter--;
			break;

		case 0x4d:         // right
		case 'd':
			SpaceCounter++;
			break;

		case 0x4b:         // left
		case 'a':
			SpaceCounter--;
			break;

		default:
			Stop = TRUE;
		}
		LineCounter = LineCounter < 0 ? LineMax - 1 : LineCounter % LineMax;
		SpaceCounter = SpaceCounter < 0 ? SpaceMax - 1 : SpaceCounter % SpaceMax;
	}
	return 0;
}
#endif

#ifdef VERSION_3
// WARNING: this is not dynamically resized with the size of the window
#define MAXLINES 50
#define MAXCOLUMNS 60
int main(void)
{
	short line = 15, column = 30;
	int anumber = -123;
	anumber >>= 2;

	char direction;
	bool finished = false;
	while (!finished)
	{
		for (int l = 0; l < line; l++)
			printf("\n");
		for (int c = 0; c < column; c++)
			printf(" ");
		printf("*");
		direction = getch(); // Wait for a character to be entered
		switch (direction)
		{
		case 'w':
			line--;
			system("cls");
			break;
		case 's':
			line++;
			system("cls");
			break;
		case 'a':
			column--;
			system("cls");
			break;
		case 'd':
			column++;
			system("cls");
			break;
		default:
			finished = true;
		}
		line = line < 0 ? MAXLINES : line % MAXLINES;
		column = column < 0 ? MAXCOLUMNS : column % MAXCOLUMNS;
	}

	return 0;
}
#endif
```

## Solutions auto-évaluations
### `ch04_ex01_Printf`
```c
#include <stdio.h>

void ch04_ex01_Printf(void);

#ifndef IGNORE_MAIN
int main(void)
{
  ch04_ex01_Printf();

  return 0;
}
#endif

void ch04_ex01_Printf(void)
{
	// TODO
	// START REMOVE LINES
	printf("Initials: __\n");
	printf("Code: __\n");
	printf("\n\n");
	printf("Birthdate: __/__/__\n");
	printf("Number: __\\__\n");
	printf("Text: \"____\"\n");
	// END REMOVE LINES
}
```

### `ch04_ex02_ScanfPrintf`
```c
#include <stdio.h>

void ch04_ex02_ScanfPrintf(void);

#ifndef IGNORE_MAIN
int main(void)
{
  ch04_ex02_ScanfPrintf();

  return 0;
}
#endif

void ch04_ex02_ScanfPrintf(void)
{
	// TODO
	// START REMOVE LINES  
  char letter1, letter2, letter3;
  int status = 0;

  int nbExpectedValues = 3;
  do
  {
    printf("\n\nPlease enter 3 letters:\n");
    status = scanf("%c %c %c", &letter1, &letter2, &letter3);

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

  printf("\nHere are the corresponding ASCII codes:\n");
  printf("%c--------->%d\n%c--------->%d\n%c--------->%d\n",
         letter1, letter1, letter2, letter2, letter3, letter3);
  // END REMOVE LINES
}
```

### `ch04_ex03_Circle`
```c
#include <stdio.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

void ch04_ex03_Circle(void);

#ifndef IGNORE_MAIN
int main(void)
{
  ch04_ex03_Circle();

  return 0;
}
#endif

void ch04_ex03_Circle(void)
{
	// TODO
	// START REMOVE LINES  
  double radius, surface;

  int nbExpectedValues = 1;

  int status = -1;

  do
  {
    printf("Circle radius: ");
    status = scanf("%lf", &radius);

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

  surface = radius * radius * M_PI;

  printf("pi = %f\n", M_PI);
  printf("Circle surface = %.2f\n", surface);
  // END REMOVE LINES
}
```


