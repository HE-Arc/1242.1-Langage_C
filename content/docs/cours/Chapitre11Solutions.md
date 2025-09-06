---
title: "Chapitre 11 : solutions"
draft: false
weight: 31
---
# Chapitre 11 : solutions

## Exemples
### `01_MainParameters`
```c
// Author: FRT
// Date: 01.02.06

#include <stdio.h>

int main(int argc, char *argv[], char *env[])
{
	int i;
	int return_value;

	printf("Argc = %d\n\n", argc);

	printf("\nCommand line %d parameters are:\n\n", argc);
	for (i = 0; i < argc; i++)
	{
		printf("  argv[%d] : %s\n", i, argv[i]);
	}

	printf("\nCommand line %d parameters are:\n\n", argc);
	i = 0;
	while (argv[i] != NULL)
	{
		printf("  argv[%d] : %s\n", i, argv[i]);
		i++;
	}

	printf("\nEnvironment variables are:\n\n");
	i = 0;
	while (env[i] != NULL)
	{
		printf("   env[%d] : %s\n", i, env[i]);
		i++;
	}

	if (argc > 3)
	{
		sscanf(argv[2], "%d", &return_value); // convert from string to integer
	}
	else
	{
		return_value = 0;
	}
	printf("--> returned value %d\n", return_value);

	return return_value;
}
```

### `04_SimpleFunctionPointer`
```c
#include <stdio.h>

void f1(void);
void f2(void);
void f3(void);
void f4(int);

int main(int argc, char *argv[])
{
	void (*ptr_fct_void)(void);
	void (*ptr_fct_int)(int);

	ptr_fct_void = f1;
	(*ptr_fct_void)();

	ptr_fct_void = f2;
	(*ptr_fct_void)();

	ptr_fct_void = f3;
	ptr_fct_void();

	ptr_fct_int = f4;
	(*ptr_fct_int)(3);
	(*ptr_fct_int)(2);

	printf("F1 %p\n", f1);
	printf("F2 %p\n", f2);
	printf("F3 %p\n", f3);
	printf("Please enter needed function (enter its address):\n");
	scanf("%p", &ptr_fct_void);
	(*ptr_fct_void)();

	return 0;
}

void f1(void)
{
	printf("Executing %s \n", __func__);
}

void f2(void)
{
	printf("Executing %s \n", __func__);
}

void f3(void)
{
	printf("Executing %s \n", __func__);
}

void f4(int j)
{
	printf("Executing %s \n", __func__);
}
```

### `05_ArrayFunctionPointer`
```c
#include <stdio.h>
#include <stdlib.h>

void  f1(void);
void  f2(void);
void  f3(void);
void  f4(void);

typedef void (*fptrTy)();

int main(int argc, char* argv[])
{
	void (*ftab1[4])();
  // Or with a typedef:
	fptrTy ftab2[4]; // Declaration of an array of pointers

	ftab1[0] = f1;
	ftab1[1] = f2;
	ftab1[2] = f3;
	ftab1[3] = f4;
  // Or with a typedef:
	ftab2[0] = f1;
	ftab2[1] = f2;
	ftab2[2] = f3;
	ftab2[3] = f4;

	int i;
	for (i = 0; i < 4; i++)
	{
		(*ftab1[i])();
	}
  // Or with a typedef:
	for (i = 0; i < 4; i++)
	{
		(*ftab2[i])();
	}
  // NOTE: the results are strictly the same  

	return 0;
}

void f1(void)
{
	printf("Executing %s \n", __func__);
}

void f2(void)
{
	printf("Executing %s \n", __func__);
}

void f3(void)
{
	printf("Executing %s \n", __func__);
}

void f4(void)
{
	printf("Executing %s \n", __func__);
}
```

# `06_VoidPointerArithmetic`
```c
#include <stdio.h>

int f1(void)
{
  return 99;
}

int f2(void)
{
  return 199;
}

int main(void)
{
  int tab[4] = {1, 2, 3, 4};
	void *p1 = tab + 1;
  void *p2 = tab + 3;

  // error: pointer of type 'void *' used in subtraction
  // int i = p2 - p1;

  int (*f1_ptr)(void) = f1;
  int (*f2_ptr)(void) = f2;

  // error: pointer to a function used in subtraction
  // int j = f2 - f1;

	return 0;
}
```

## Solutions
[1242.1.11_Fonctions_II_Corrections.pdf](/pdf/1242.1.11_Fonctions_II_Corrections.pdf)
### `Exercice 1`
```c
#include <stdio.h>

void swap(int *val1, int *val2)
{
  int temp = *val1;
  *val1 = *val2;
  *val2 = temp;
}

int main(void)
{
  int var1 = 3, var2 = 5;
  printf("var1: %d    var2: %d\n", var1, var2);
  swap(&var1, &var2);
  printf("swap(&var1, &var2)\n");
  printf("var1: %d    var2: %d\n", var1, var2);

  return 0;
}
```

### `Exercice 2`
```c
#include <stdio.h>

void raz(int *px)
{
	*px = 0;
}

void test_et_raz(int *px)
{
	if (*px != 0)
	{
		raz(px);
	}
}

int main(void)
{
	int x = 19;
	test_et_raz(&x);
	printf("x: %d\n", x);

	return 0;
}
```

### `Exercice 3`
```c
#include <stdio.h>

void reset_pointer(int **pptr)
{
	*pptr = NULL;
}

int main(void)
{
	int x = 1;
	int *ptr = &x;
	// printf("ptr:%p\n", ptr);
	reset_pointer(&ptr);
	printf("ptr: %p\n", ptr);

	return 0;
}
```

### `Exercice 4`
```c
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int read_size(void)
{
  int N;
  printf("Please enter array size: ");
  scanf("%d", &N);
  return N;
}

int *allocate_array(int n)
{
  int *adr = (int *)malloc(n * sizeof(int));
  return adr;
}

void fill_array(int *t, int n)
{
  int i;
  srand((unsigned int)time(NULL));
  for (i = 0; i < n; i++)
  {
    //*t++ = 32+rand()%(127-32);
    t[i] = 32 + rand() % (127 - 32);
  }
}

void print_array(int *t, int n)
{
  int i;
  for (i = 0; i < n; i++)
  {
    printf("%d ", *t++);
  }
  printf("\n");
}

void free_array(int **t)
{
  free(*t);
  *t = NULL;
}

int main(void)
{
  int *ptr_tab = NULL;
  int N;
  N = read_size();
  ptr_tab = allocate_array(N);
  fill_array(ptr_tab, N);
  print_array(ptr_tab, N);
  printf("%p %d bytes\n", ptr_tab, (int)sizeof(ptr_tab));
  free_array(&ptr_tab);
  printf("%p %d bytes\n", ptr_tab, (int)sizeof(ptr_tab));
  // Note: the variable ptr_tab still exists here v(4 bytes)

  return 0;
}
```

### `Exercice 5`
```c
/* Langage C
   Serie 11.1, exercice 5: Arguments du programme

   pour tester ce programme, il faut l'executer en ligne de commande ou
   a partir d'un script (p.ex. batch):
                                                " EX11_1_5.exe F "

   *Dans CodeBlocks :*
     Saisir le parametre dans Project/Set program's arguments...
   *Dans Visual Studio 2019 (en Anglais) :*
     1) Clic droit sur le projet
     2) Aller dans Properties
     3) Dans l'onglet Debugging, modifier le parametre "Command Arguments"
     NOTE : meme si on change un parametre dans l'onglet Debugging, ceci fonctionne en Release aussi.
*/
#include <stdio.h>

int main(int argc, char *argv[])
{
  if (argc == 1)
    printf("Hello world!\n");
  else
    switch (argv[1][0]) // on prend le premier caractere du premier argument
    {
    case 'E':
    case 'e':
      printf("Hello World!\n");
      break;
    case 'F':
    case 'f':
      printf("Salut tout le monde!\n");
      break;
    case 'D':
    case 'd':
      printf("Salu Tzame!\n");
      break;
    case 'I':
    case 'i':
      printf("Ciao Mondo!\n");
      break;
    default:
      printf("Langue non supportee, Achetez la version PREMIUM!");
      return -1;
    }

  return 0;
}
```

### `Exercice 6`
```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NB_INTERVALS 1000

double compute_integral(double (*ptrFonc)(double x), double a, double b);
double fx_eq_1(double x) { return 1; }
double fx_eq_x(double x) { return x; }

int main(void)
{
  double result;

  result = compute_integral(sin, 0, 0.5);
  printf("\nIntegral of sin(x) in [0..0.5] = %f\n", result);

  result = compute_integral(exp, 0, 3);
  printf("\nIntegral of exp(x) in [0...3] = %f\n", result);

  result = compute_integral(log10, 1, 10);
  printf("\nIntegral of log10(x) in [1...10] = %f\n", result);

  result = compute_integral(fx_eq_1, 2, 5);
  printf("\nIntegral of f(x)=1 in [2...5] = %f\n", result);

  result = compute_integral(fx_eq_x, 0, 4);
  printf("\nIntegral of f(x)=x in [0...4] = %f\n\n", result);

  return 0;
}

double compute_integral(double (*ptrFonc)(double x), double a, double b)
{
  double x, surface_rectangle, sum_rectangles = 0.0;

  for (int i = 0; i < NB_INTERVALS; i++)
  {
    x = a + (b - a) * ((double)i / NB_INTERVALS);
    surface_rectangle = (*ptrFonc)(x) * ((b - a) / NB_INTERVALS);
    sum_rectangles += surface_rectangle;
  }
  return sum_rectangles;
}
```

### `Exercice 7`
```c
#include <stdio.h>
#include <stdlib.h> // For EXIT_SUCCESS

int times_2(int x);
int times_4(int x);
void edit_array(int *t, int n, int (*f) (int));
void print_array(char text[], int t[], int n);

int main(void)
{
	int tab[] = { 1 , 2 , 3 , 4 };
	int size = sizeof(tab) / sizeof(int);
	print_array("Initial array:", tab, size);

	edit_array(tab, size, times_2);
	print_array("Function x2:", tab, size);

	edit_array(tab, size, times_4);
	print_array("Function x4:", tab, size);

	int (*ptr_times) (int) = times_2;

	edit_array(tab, size, ptr_times);
	print_array("Function pointer x2:", tab, size);

	ptr_times = times_4;
	edit_array(tab, size, ptr_times);
	print_array("Function pointer x4:", tab, size);

	int (*tab_ptr_times[2]) (int) = { times_2,times_4 };
	for (int i = 0; i < 2; i++)
	{
		edit_array(tab, size, tab_ptr_times[i]);
		print_array("Function pointers array:", tab, size);
	}

	return EXIT_SUCCESS;
}

int times_2(int x)
{
	return 2 * x;
}

int times_4(int x)
{
	return 4 * x;
}

void edit_array(int *t, int n, int(*fonction)(int))
{
	for (int i = 0; i < n; i++)
		t[i] = (*fonction)(t[i]);
}

void print_array(char texte[], int t[], int n)
{
	printf("%40s ", texte);
	for (int i = 0; i < n; i++)
	{
		printf("%5d ", t[i]);
	}
	printf("\n");
}
```

### `Exercice 8`
```c
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

/**
void qsort (void* base,                             // array (data)
            size_t num,                             // Nb values
            size_t size,                            // Nb bytes per value
            int (*compar)(const void*,const void*)  // callback
            );
**/

int comp_increasing(const void *a, const void *b);
int comp_decreasing(const void *a, const void *b);

void print_array(char *text, double *t, short n);

int main(void)
{
  static double tab[] = {4.6, 4.8, 4.79, -6.1, 0, -6.11, 4.79, -6.09, 4.81, 0};
  short n = sizeof tab / sizeof(*tab);

  printf("Nb values in array: %d\n\n", n);

  print_array("Initial array: ", tab, n);

  qsort(tab, n, sizeof(*tab), comp_increasing);
  print_array("\n\nArray in increasing order: ", tab, n);

  qsort(tab, n, sizeof(*tab), comp_decreasing);
  print_array("\n\nArray in decreasing order: ", tab, n);

  return 0;
}

void print_array(char *texte, double *t, short n)
{
  int i;
  printf("%s\n", texte);
  for (i = 0; i < n; i++)
  {
    printf("%+4.2lf | ", t[i]);
  }
  printf("\n");
}

int comp_increasing(const void *pa, const void *pb)
{
  double a = *(double *)pa;
  double b = *(double *)pb;
  if (a > b)
  {
    return 1;
  }
  else if (a < b)
  {
    return -1;
  }
  else
  {
    return 0;
  }
}

int comp_decreasing(const void *pa, const void *pb)
{
  if (*(double *)pa < *(double *)pb)
  {
    return 1;
  }
  else if (*(double *)pa > *(double *)pb)
  {
    return -1;
  }
  else
  {
    return 0;
  }
}
```

## Solutions Auto-évaluations
### `ch11_ex02_Reset`
```c
#include <stdio.h>

// TODO: add functions prototypes here
void ch11_ex02_Reset(int *n);
void ch11_ex02_TestAndReset(int *n);

#ifndef IGNORE_MAIN
int main(void)
{
	// TODO: add function calls here
	int n = 0;
	ch11_ex02_TestAndReset(&n);
}
#endif

// TODO: add functions definitions here
void ch11_ex02_Reset(int *n)
{
	*n = 0;
}

void ch11_ex02_TestAndReset(int *n)
{
	if (*n != 0)
	{
		ch11_ex02_Reset(n);
	}
}
```

### `ch11_ex03_ResetPointer`
```c
#include <stdio.h>

// TODO: add functions prototypes here
void ch11_ex03_ResetPointer(int **ptr);

#ifndef IGNORE_MAIN
int main(void)
{
	// TODO: add function calls here
  int n = 0;
  int *ptr = &n;
  ch11_ex03_ResetPointer(&ptr);
}
#endif

// TODO: add functions definitions here
void ch11_ex03_ResetPointer(int **ptr)
{
	*ptr = NULL;
}
```

### `ch11_ex07_FunctionsPointers`
```c
#include <stdio.h>

// TODO: add functions prototypes here
void ch11_ex07_EditArray(int tab[], int size, int (*func_ptr)(int));
int ch11_ex07_Times2(int n);
int ch11_ex07_Times4(int n);
void ch11_ex07_FunctionsPointers(void);
void ch11_ex07_PrintArray(const char *text, int t[], int n);

#ifndef IGNORE_MAIN
int main(void)
{
  // TODO: add function calls here
  ch11_ex07_FunctionsPointers();
}
#endif

// TODO: add functions definitions here
void ch11_ex07_FunctionsPointers(void)
{  
  int tab[] = {1, 2, 3, 4};
  int size = sizeof(tab) / sizeof(int);
  ch11_ex07_PrintArray("Initial array:", tab, size);

  // TODO: call ch11_ex07_EditArray() with functions directly
  ch11_ex07_EditArray(tab, size, ch11_ex07_Times2);
  ch11_ex07_PrintArray("Function x2:", tab, size);

  // TODO: call ch11_ex07_EditArray() with functions directly
  ch11_ex07_EditArray(tab, size, ch11_ex07_Times4);
  ch11_ex07_PrintArray("Function x4:", tab, size);

  // TODO: define a function pointer to ch11_ex07_Times2
  int (*func_ptr)(int n) = ch11_ex07_Times2;

  // TODO: call ch11_ex07_EditArray() with a function pointer
  ch11_ex07_EditArray(tab, size, func_ptr);
  ch11_ex07_PrintArray("Function pointer x2:", tab, size);

  // TODO: define a function pointer to ch11_ex07_Times4
  func_ptr = ch11_ex07_Times4;

  // TODO: call ch11_ex07_EditArray() with a function pointer
  ch11_ex07_EditArray(tab, size, func_ptr);
  ch11_ex07_PrintArray("Function pointer x4:", tab, size);

  // TODO: define an array containing 2 functions pointers
  int (*func_ptr_tab[2])(int n) = {ch11_ex07_Times2, ch11_ex07_Times4};

  for (int i = 0; i < 2; i++)
  {
    // TODO: call ch11_ex07_EditArray with elements of the defined functions pointers array
    ch11_ex07_EditArray(tab, size, func_ptr_tab[i]);
    ch11_ex07_PrintArray("Function pointers array:", tab, size);
  }
}

void ch11_ex07_PrintArray(const char *text, int t[], int n)
{
  printf("%40s ", text);
  for (int i = 0; i < n; i++)
  {
    printf("%5d ", t[i]);
  }
  printf("\n");
}

void ch11_ex07_EditArray(int tab[], int size, int (*func_ptr)(int n))
{
  for (int i = 0; i < size; ++i)
  {
    tab[i] = func_ptr(tab[i]);
  }
}

int ch11_ex07_Times2(int n)
{
  return 2 * n;
}

int ch11_ex07_Times4(int n)
{
  return 4 * n;
}
```
