---
title: "Chapitre 4 : solutions"
draft: true
weight: 21
---
# Chapitre 4 : solutions

## Solutions exercices

{{< pdf src="/pdfs/1242.1.04_Entrees-Sorties_Correction.pdf" >}}

### `1242.1_04.01_InputOutput`

<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exercices_04.01_InputOutput_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

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
<!-- SNIPPET:END -->

### `1242.1_04.01_InputOutput_StarGame`

<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exercices_04.01_InputOutput_StarGame_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
#include <conio.h>    // For getch()
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h> // for CONSOLE_SCREEN_BUFFER_INFO

#define VERSION_2

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
<!-- SNIPPET:END -->

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


