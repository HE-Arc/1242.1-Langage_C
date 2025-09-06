---
title: "Chapitre 6 : solutions"
draft: false
weight: 21
---
# Chapitre 6 : solutions

## Exemples
### `1242.1_06.01_Function`
```c
#include <stdio.h>

// Prototype
void prn_message(int k);

int main(void)
{
	printf("%s compiled on %s at %s\n", __FILE__, __DATE__, __TIME__);

	int N;
	int status = 0;
	const int nbExpectedValues = 1;
	do
	{
		printf("Please enter an integer: ");
		status = scanf("%d", &N);

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

	// Function call like a procedure
	prn_message(N);

	return 0;
}

void prn_message(int k)
{
	printf("\nYou entered the value %d\n\n", k);
}
```

### `1242.1_06.02_Sum2`
```c
#include <stdio.h>

// Prototype/Declaration
int sum(int lowerBound, int upperBound);	// With a comma!!!
double mean(int lowerBound, int upperBound);

int main(void)
{
	int lower, upper, status;
	int total;
	const int nbExpectedValues = 2;
	do
	{
		printf("Please enter lower bound and upper bound (in that order): ");
		status = scanf("%d %d", &lower, &upper);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}
	} while (status != 2);

	// Call sum function
	// NOTE that effective/actual parameters and formal parameters may have different names
	total = sum(lower, upper);
	printf("The sum from %d to %d = %d\n", lower, upper, total);
	// We can even make the call of a function in the call of another function
	printf("The mean value is = %lf\n", mean(lower, upper));

	return 0;
}

// Definition
int sum(int lowerBound, int upperBound) // Header
{ // Body
	int sum = 0;

	for (int n = lowerBound; n <= upperBound; ++n)
	{
		sum += n;
	}

	return sum;
}

// Definition
double mean(int lowerBound, int upperBound)
{
	// Check for errors
	if (lowerBound > upperBound)
	{
		return 0; // 0.0 will be identified as an error
	}

	// NOTE the cast
	double mean = sum(lowerBound, upperBound) / ((double)upperBound - lowerBound + 1);
	
	return mean;
}
```

### `1242.1_06.99_FunctionDefaultInt`
```c
#include <stdio.h>

// Prototype/Declaration
int func1(int);
int func2(int);
int func3(void);
int func4();
func5(void);

int main(void)
{
	// OK
	int res = func1(42);
	printf("RESULT: %d\n", res);
	// UB: func2 has no return statement
	res = func2(42);
	printf("RESULT: %d\n", res);
	// WARNING
	res = func3(42);
	printf("RESULT: %d\n", res);
	// OK ^^'
	res = func4(42);
	printf("RESULT: %d\n", res);
	// OK. Default return type is int
	res = func5();
	printf("RESULT: %d\n", res);
}

// Definition
int func1(int a)
{
	printf("CALLING: ");
	printf(__func__);
	printf("\n");

	return 42;
}

int func2(int a)
{
	printf("CALLING: ");
	printf(__func__);
	printf("\n");

	// OUPS
}

int func3(void)
{
	printf("CALLING: ");
	printf(__func__);
	printf("\n");

	return 42;
}

int func4()
{
	printf("CALLING: ");
	printf(__func__);
	printf("\n");

	return 42;
}

func5()
{
	printf("CALLING: ");
	printf(__func__);
	printf("\n");

	return 42;
}
```

## Solutions
[1242.1.06_Fonctions_I_Correction](/pdf/1242.1.06_Fonctions_I_Correction.pdf)

### `1242.1_06.01_FonctionsI Exercice1`
```c
#include <stdio.h>

int fct(int);

int main(void)
{
	int n, p = 5;
	n = fct(p);
	printf("p = %d, n = %d\n", p, n);

	return 0;
}

int fct(int r)
{
	return 2 * r;
}
```

### `1242.1_06.01_FonctionsI Exercice2_Hello`
```c
#include <stdio.h>

void f1(void);
void f2(int);
int f3(int);

// NOTE: keep French to stick to instructions
int main(void)
{
	printf("f1 :\n");
	f1();
	printf("\nf2 :\n");
	f2(3);
	printf("\nf3 :\n");
	int j = f3(3);

	return 0;
}

void f1(void)
{
	printf("bonjour\n");
}

void f2(int n)
{
	int i;
	for (i = 0; i < n; i++)
	{
		f1();
	}
}

int f3(int n)
{
	f2(n);
	return 0;
}
```

### `1242.1_06.01_FonctionsI Exercice3_ReverseEngineering`
```c
#include <stdio.h>

int n = 10, q = 2; // Global variables!
int fct(int);
void f(void);

// NOTE: keep French to stick to instructions
int main(void)
{
	int n = 0, p = 5;
	n = fct(p);
	printf("A : dans main, n = %d, p = %d, q = %d\n", n, p, q);
	f();

	return 0;
}

int fct(int p)
{
	int q;
	q = 2 * p + n;
	printf("B : dans fct, n = %d, p = %d, q = %d\n", n, p, q);

	return q;
}

void f(void)
{
	int p = q * n;
	printf("C : dans f, n = %d, p = %d, q = %d\n", n, p, q);
}
```

### `1242.1_06.01_FonctionsI Exercice4_Squares`
```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int squares(int n);

int main(void)
{
	const int nbExpectedValues = 1;
	int status = 0;
	int userLimitValue = 1000;

// #define OPTION

	do
	{
		printf("Please enter a positive integer in [1..1000]: ");
		status = scanf(" %d", &userLimitValue);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}
		if (status != nbExpectedValues || userLimitValue < 1 || userLimitValue > 1000)
		{
			// printf("\a");
		}

	} while (status != 1 || userLimitValue < 1 || userLimitValue > 1000);

#ifndef OPTION
	for (int number = 1; number <= userLimitValue; number += 1)
	{
		printf("%d^2 = %d\n", number, squares(number));
	}
#else
	int currentValue = 1;
	int currentSquare = 1;
	while (currentSquare <= userLimitValue)
	{
		printf("%d^2 = %d\n", currentValue, currentSquare);
		currentSquare = squares(++currentValue);
	}
#endif

	printf("\n");

	return 0;
}

int squares(int n)
{
	return n * n;
}
```

### `1242.1_06.01_FonctionsI Exercice5_MultiplicationsTable`
```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

#define MIN_TABLE 1
#define MAX_TABLE 12

int read(int lowerLimit, int upperLimit);
void multiplicationTable(int n);

int main(void)
{
	int number;
	number = read(MIN_TABLE, MAX_TABLE);
	multiplicationTable(number);

	return 0;
}

int read(int lowerLimit, int upperLimit)
{
	const int nbExpectedValues = 1;
	int status = 0;
	int input = 0;
	do
	{
		printf("Please enter the multiplication table (in [%d..%d]): ", lowerLimit, upperLimit);
		status = scanf(" %d", &input);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}
		if (status != nbExpectedValues || input < lowerLimit || input > upperLimit)
		{
			// printf("\a");
		}

	} while (status != nbExpectedValues || input < lowerLimit || input > upperLimit);

	return input;
}

void multiplicationTable(int n)
{
	int count;
	printf("\nMULTIPLICATION TABLE FOR %d\n", n);
	for (count = 1; count <= 10; ++count)
	{
		printf("%0d X %0d = %0d\n", n, count, n * count);
	}
}
```

### `1242.1_06.01_FonctionsI Exercice6_Calculator`
```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdbool.h>

double compute(double, double, char);

int main(void)
{
	double nb1, nb2, result;
	char operation;

	const int nbExpectedValues = 3;
	int status = 0;
	bool knownOperation = false;
	do
	{
		printf("Enter an expression <nb op nb> : ");
		status = scanf(" %lf %c %lf", &nb1, &operation, &nb2);
		knownOperation = (operation == '+') || (operation == '-') || (operation == '*') || (operation == '/');
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}
		if (status != nbExpectedValues || knownOperation == false)
		{
			// printf("\a");
		}

	} while (status != nbExpectedValues || knownOperation == false);

	result = compute(nb1, nb2, operation);
	printf("Result = %.4lf\n", result);

	return 0;
}

double compute(double n1, double n2, char op)
{
	switch (op)
	{
	case '+':
		return (n1 + n2);  // No need for break here as we return
	case '-':
		return (n1 - n2);
	case '*':
		return (n1 * n2);
	case '/':
		return (n2 != 0) ? (n1 / n2) : 0;
	default:
		return 0; // We choose 0 as a default value
	}
}
```

## Solutions Auto-évaluations
### `ch06_ex04_Squares`
```c
#include <stdio.h>

// TODO: add functions prototypes here
// START REMOVE LINES
int ch06_ex04_Square(int n);
void ch06_ex04_Squares(void);

// #define OPTION

// END REMOVE LINES

#ifndef IGNORE_MAIN
int main(void)
{
  // TODO: call functions here
  // START REMOVE LINES
  ch06_ex04_Squares();

  return 0;
  // END REMOVE LINES
}
#endif

// TODO: add functions definitions here
// START REMOVE LINES
int ch06_ex04_Square(int n)
{
  return n * n;
}

void ch06_ex04_Squares(void)
{
  const int nbExpectedValues = 1;
  int status = 0;
  int userLimitValue = 1000;

  do
  {
    printf("Please enter a positive integer in [1..1000]: ");
    status = scanf(" %d", &userLimitValue);

    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }
    if (status != nbExpectedValues || userLimitValue < 1 || userLimitValue > 1000)
    {
      // printf("\a");
    }

  } while (status != 1 || userLimitValue < 1 || userLimitValue > 1000);

#ifndef OPTION
  for (int number = 1; number <= userLimitValue; number += 1)
  {
    printf("%d^2 = %d\n", number, ch06_ex04_Square(number));
  }
#else
  int currentValue = 1;
  int currentSquare = 1;
  while (currentSquare <= userLimitValue)
  {
    printf("%d^2 = %d\n", currentValue, currentSquare);
    currentSquare = ch06_ex04_Square(++currentValue);
  }
#endif

  printf("\n");
}
// END REMOVE LINES
```

### `ch06_ex05_MultiplicationTable`
```c
#include <stdio.h>

// TODO: add functions prototypes here
// START REMOVE LINES
int ch06_ex05_Read(int, int);
void ch06_ex05_MultiplicationTable(int);
// END REMOVE LINES

#ifndef IGNORE_MAIN
int main(void)
{
	// TODO: call functions here
	// START REMOVE LINES
	const int MIN_TABLE = 1;
	const int MAX_TABLE = 10;
	
	int number;
	number = ch06_ex05_Read(MIN_TABLE, MAX_TABLE);
	ch06_ex05_MultiplicationTable(number);

	return 0;
	// END REMOVE LINES
}
#endif

// TODO: add functions definitions here
// START REMOVE LINES
int ch06_ex05_Read(int lowerLimit, int upperLimit)
{
	const int nbExpectedValues = 1;
	int status = 0;
	int input = 0;
	do
	{
		printf("Please enter the multiplication table (in [%d..%d]): ", lowerLimit, upperLimit);
		status = scanf(" %d", &input);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}
		if (status != nbExpectedValues || input < lowerLimit || input > upperLimit)
		{
			// printf("\a");
		}

	} while (status != nbExpectedValues || input < lowerLimit || input > upperLimit);

	return input;
}

void ch06_ex05_MultiplicationTable(int n)
{
	int count;
	printf("\nMULTIPLICATION TABLE FOR %d\n", n);
	for (count = 1; count <= 10; ++count)
	{
		printf("%0d X %0d = %0d\n", n, count, n * count);
	}
}
// END REMOVE LINES
```

### `ch06_ex06_Calculator`
```c
#include <stdio.h>
#include <stdbool.h> // bool, true, false

// TODO: add functions prototypes here
// START REMOVE LINES
double ch06_ex06_Compute(double, double, char);
void ch06_ex06_Calculator(void);
// END REMOVE LINES

#ifndef IGNORE_MAIN
int main(void)
{
  // TODO: call functions here
  // START REMOVE LINES
  ch06_ex06_Calculator();

  return 0;
  // END REMOVE LINES
}
#endif

// TODO: add functions definitions here
// START REMOVE LINES
void ch06_ex06_Calculator(void)
{
  double nb1, nb2, result;
  char operation;

  const int nbExpectedValues = 3;
  int status = 0;
  bool knownOperation = false;
  do
  {
    printf("Enter an expression <nb op nb> : ");
    status = scanf(" %lf %c %lf", &nb1, &operation, &nb2);
    knownOperation = (operation == '+') || (operation == '-') || (operation == '*') || (operation == '/');
    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }
    if (status != nbExpectedValues || knownOperation == false)
    {
      // printf("\a");
    }

  } while (status != nbExpectedValues || knownOperation == false);

  result = ch06_ex06_Compute(nb1, nb2, operation);
  printf("Result = %.4lf\n", result);
}

double ch06_ex06_Compute(double n1, double n2, char op)
{
  switch (op)
  {
  case '+':
    return (n1 + n2); // No need for break here as we return
  case '-':
    return (n1 - n2);
  case '*':
    return (n1 * n2);
  case '/':
    return (n2 != 0) ? (n1 / n2) : 0;
  default:
    return 0; // We choose 0 as a default value
  }
}
// END REMOVE LINES
```


