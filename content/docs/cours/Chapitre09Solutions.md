---
title: "Chapitre 9 : solutions"
draft: false
weight: 21
---
# Chapitre 9 : solutions

## Solutions
[1242.1.09_Pointeurs_Corrections.pdf](/pdf/1242.1.09_Pointeurs_Corrections.pdf)

### `1242.1_09.01_Pointers - Exercice 6`
```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int read_positive_integer(const char *message)
{
	int status = 0;
	const int nbExpectedValues = 1;
	// Variables to store User input values
	int value;
	do
	{
		printf("%s", message);
		status = scanf("%d", &value);
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}
	} while (status != nbExpectedValues || value < 0);

	return value;
}

int main(void)
{
	int A[100], B[50];  // A needs to hold 50+50 elements
	int n, m;
	
	n = read_positive_integer("Number of values for A (max.50): ");

	for (int i = 0; i < n; i++)
	{
		int value;

		// Might use snprintf to construct the char * and pass it to read_positive_integer instead. Not worth the effort IMHO
		printf("Element %d: ", i);
		value = read_positive_integer("");
		*(A+i) = value;
	}

	m = read_positive_integer("Number of values for B (max.50): ");

	for (int i = 0; i < m; i++)
	{
		int value;

		// Might use snprintf to construct the char * and pass it to read_positive_integer instead. Not worth the effort IMHO
		printf("Element %d: ", i);
		value = read_positive_integer("");
		*(B+i) = value;
	}

	printf("A:\n");
	for (int i = 0; i < n; i++)
	{
		printf("%d ", *(A + i));
	}
	
	printf("\nB:\n");
	for (int i = 0; i < m; i++)
	{
		printf("%d ", *(B + i));
	}
	printf("\n");

	// Copy A values after B values
	for (int i = 0; i < m; i++)
	{
		*(A + n + i) = *(B + i);
	}

	n += m;

	printf("Final results:\n");
	for (int i = 0; i < n; i++)
	{
		printf("%d ", *(A + i));
	}
	printf("\n");

	return 0;
}
```

### `1242.1_09.01_Pointers - Exercice9`
```c
#include <stdio.h>
#include <stdlib.h>

int read_size(float *ptr)
{
	return sizeof(ptr);
}

int main(void)
{
	float array[20];
	printf("Size[byte] of array: %2d\n", sizeof(array));
	printf("Size[byte] of read_size(array): %2d\n", read_size(array));

	return 0;
}
```

### `1242.1_09.01_Pointers - Exercice 10`
```c
#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
	int a = 5, b = 10;

	printf("Before: a: %d, b: %d\n", a, b);
	swap(&a, &b);
	printf("After:  a: %d, b: %d\n", a, b);

	return 0;
}

void swap(int *a, int *b)
{
	int tmp;

	tmp = *a;
	*a = *b;
	*b = tmp;
}
```

## Solutions Auto-évaluations
### `ch09_ex06_CopyArrays`
```c
#include <stdio.h>

// TODO: add functions prototypes here
void ch09_ex06_CopyArrays();

#ifndef IGNORE_MAIN
int main(void)
{
  // TODO: add functions calls here
  ch09_ex06_CopyArrays();
}
#endif

// TODO: add functions definitions here
void ch09_ex06_CopyArrays()
{
  int A[100];
  int B[50];

  int status = -1;
  int n = -1;
  int m = -1;
  
  do
  {
    printf("Number of values for A (max.50): ");
    status = scanf(" %d", &n);
    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }
  } while (status != 1 || n < 0);

  for (int i = 0; i < n; i++)
  {
    printf("Element %d: ", i);
    scanf(" %d", &A[i]);
  }

  do
  {
    printf("Number of values for B (max.50): ");
    status = scanf(" %d", &m);
    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }
  } while (status != 1 || m < 0);

  for (int i = 0; i < m; i++)
  {
    printf("Element %d: ", i);
    scanf(" %d", &B[i]);
  }

  printf("A:\n");
  for (int i = 0; i < n; i++)
  {
    printf("%d ", A[i]);
  }

  printf("\nB:\n");
  for (int i = 0; i < m; i++)
  {
    printf("%d ", B[i]);
  }

  for (int i = 0; i < m; i++)
  {
    A[n+i] = B[i];
  }

  printf("\nFinal results:\n");
  for (int i = 0; i < n+m; i++)
  {
    printf("%d ", A[i]);
  }
  printf("\n");
}
```

### `ch09_ex10_Swap`
```c
#include <stdio.h>

// TODO: add functions prototypes here
void ch09_ex10_Swap(int *a, int *b);

#ifndef IGNORE_MAIN
int main(void)
{
	// TODO: add function calls here
  int a = 5;
  int b = 10;

  printf("Before: a: %d, b: %d\n", a, b);
  ch09_ex10_Swap(&a, &b);
  printf("After:  a: %d, b: %d\n", a, b);

}
#endif

// TODO: add functions definitions here
void ch09_ex10_Swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}
```
