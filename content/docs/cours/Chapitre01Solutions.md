---
title: "Chapitre 1 : solutions"
draft: false
weight: 21
---
# Chapitre 1 : solutions

## Exemples
### `1242.1_01.01_Hello_World`
```c
#include <stdio.h>

int main(void)
{
	printf("Hello World\n");

	return 0;
}
```

### `1242.1_01.01b_Add`
```c
#include <stdio.h>

int main(void)
{
	int a = 10;
	int b = 5;
	printf(" %d" , a+b);
	return 0;
}
```

## Solutions exercices

### `1242.1_01.01_HelloWorld`

```c
#include <stdio.h>
#include <math.h>   // include math functions and M_PI constant
#include <stdlib.h>

// SEE: https://stackoverflow.com/questions/29264462/m-pi-not-available-with-gcc-std-c11-but-with-std-gnu11
#ifndef M_PI
#define M_PI           3.14159265358979323846
#endif

void chap_01_ex1_printHelloWorld(void);
void chap_01_ex2_printMathCalc(void);
void chap_01_ex3_someCalculus(void);
void chap_01_ex4_multipleTable3(int);

int main(void)
{
	chap_01_ex1_printHelloWorld();
	chap_01_ex2_printMathCalc();
	chap_01_ex3_someCalculus();
	chap_01_ex4_multipleTable3(37);

	return 0;
}

void chap_01_ex1_printHelloWorld(void)
{
	printf("hello, ");
	printf("world");
	printf("\n");
}

void chap_01_ex2_printMathCalc(void)
{
	int a = 37;
	int b = 12;
	printf("The result of %d * %d = %d\n", a, b, a * b);
}

void chap_01_ex3_someCalculus(void)
{
	double A;
	double B;
	double res;

	// Input for A and B
	printf("Input a value for A: ");
	scanf(" %lf", &A);
	printf("input a value for B: ");
	scanf(" %lf", &B);

	// a) a^b
	res = pow(A, B);
	printf("\n a) %f power %f = %G \n", A, B, res);

	// b) Hypothenuse
	res = sqrt(pow(A, 2) + pow(B, 2));
	printf("\n b) The hypotenuse of the right triangle is %f \n", res);

	// c) tangent of A
	// NOTE: we consider that A is in degrees
	// WARNING: trigonometric functions use radians
	res = sin(A) / cos(A);
	res = sin(A * M_PI / 180) / cos(A * M_PI / 180); // to use degrees instead
	printf("\n c) The tangent of A is %f \n", res);

	// d) Rounding down A/B
	res = floor(A / B);
	printf("\n d) The rounded down value of A/B is %f \n", res);

	// e) Rounding down A/B with 3 decimals
	res = floor(1000.0 * (A / B)) / 1000.0;
	printf("\n e) The rounded down value of A/B with 3 decimals is %f \n\n", res);
}

void chap_01_ex4_multipleTable3(int refNumber)
{
	int n = 37;
	for (int i = 0; i <= 12; i++)
	{
		printf("%d * %d = %d\n", refNumber, i, n * i);
	}
}
```

## Solutions Auto-évaluations

### `ch01_ex01_PrintHelloWorld`

```c
#include <stdio.h>

void ch01_ex01_PrintHelloWorld(void);

#ifndef IGNORE_MAIN
int main(void)
{
	ch01_ex01_PrintHelloWorld();

	return 0;
}
#endif

void ch01_ex01_PrintHelloWorld(void)
{
  // TODO
	// START REMOVE LINES
  printf("hello, ");
	printf("world");
	printf("\n");
	// END REMOVE LINES
}
```	

### `ch01_ex02_PrintMathCalc`

```c
#include <stdio.h>

void ch01_ex02_PrintMathCalc(void);

#ifndef IGNORE_MAIN
int main(void)
{
	ch01_ex02_PrintMathCalc();

	return 0;
}
#endif

void ch01_ex02_PrintMathCalc(void)
{
	// TODO
	// START REMOVE LINES
	int a = 37;
	int b = 12;

	printf("The result of %d * %d = %d\n", a, b, a * b);
	// END REMOVE LINES
}
```	

### `ch01_ex03_SomeCalculus`

```c
#include <stdio.h>
#include <math.h>   // include math functions and M_PI constant

// SEE FAQ "Pourquoi faut-il définir M_PI nous-même ?"
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

void ch01_ex03_SomeCalculus(double, double);

#ifndef IGNORE_MAIN
int main(void)
{
	double A;
	double B;

	// Input for A and B
	printf("Input a value for A: ");
	scanf(" %lf", &A);
	printf("input a value for B: ");
	scanf(" %lf", &B);

	ch01_ex03_SomeCalculus(A, B);

	return 0;
}
#endif

void ch01_ex03_SomeCalculus(double A, double B)
{
	double res = 0;

	// a) a^b
	// TODO
	// START REMOVE LINES
	res = pow(A, B);
	// END REMOVE LINES
	printf("\n a) %f power %f = %G \n", A, B, res);

	// b) Hypothenuse
	// TODO
	// START REMOVE LINES
	res = sqrt(pow(A, 2) + pow(B, 2));
	// END REMOVE LINES
	printf("\n b) The hypotenuse of the right triangle is %f \n", res);

	// c) tangent of A
	// NOTE: we consider that A is in degrees
	// WARNING: trigonometric functions use radians
	// TODO
	// START REMOVE LINES
	res = sin(A) / cos(A);
	res = sin(A * M_PI / 180) / cos(A * M_PI / 180); // to use degrees instead
	// END REMOVE LINES
	printf("\n c) The tangent of A is %f \n", res);

	// d) Rounding down A/B
	// TODO
	// START REMOVE LINES
	res = floor(A / B);
	// END REMOVE LINES
	printf("\n d) The rounded down value of A/B is %f \n", res);

	// e) Rounding down A/B with 3 decimals
	// TODO
	// START REMOVE LINES
	res = floor(1000.0 * (A / B)) / 1000.0;
	// END REMOVE LINES
	printf("\n e) The rounded down value of A/B with 3 decimals is %f \n\n", res);
}
```
