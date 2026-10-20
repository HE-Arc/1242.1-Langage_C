---
title: "Chapitre 5 : solutions"
draft: true
weight: 21
---
# Chapitre 5 : solutions

## Solutions exercices

{{< pdf src="/pdfs/1242.1.05.01_StructuresDeControle_Correction.pdf" >}}

{{< pdf src="/pdfs/1242.1.05.02_StructuresDeControle_Correction.pdf" >}}

{{< pdf src="/pdfs/1242.1.05.03_StructuresDeControle_Correction.pdf" >}}

{{< pdf src="/pdfs/1242.1.05.04_StructuresDeControle_Correction.pdf" >}}

### `1242.1_05.01_FlowControl`

<!-- SNIPPET:BEGIN source_file=Exercice1_Corrections.c id=1242.1_Exercices_05.01_FlowControl_Exercice1_Corrections.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice1_Corrections.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{
	const int red = 0x00FF0000;
	const int green = 0x0000FF00;
	int color = 0x00FF0000;
	int number = 0, x = 1, limit = 2, value = -3, offer = 100, demand = 200;
	double price = 12.45;

	// a) CORRECTED
	if (number < 1)
	{
		++number;
	}

	// b) CORRECTED
	if (x < limit)
	{
		x *= 2;
	}
	else
	{
		x /= 2;
	}

	// c) CORRECTED
	if (offer > demand)
	{
		price *= 0.95;
	}
	else
	{
		price *= 1.07;
	}

	// d) CORRECTED
	if (value >= 0)
	{
		printf("positive value");
	}

	// e) CORRECTED
	if (color == red)
	{
		color = green;
		printf("green\n");
	}

	// II
	number = number < 1 ? number + 1 : number;
	x = x < limit ? x * 2 : x / 2;
	price *= (offer > demand) ? 0.95 : 1.07;

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice2_UpperLower.c id=1242.1_Exercices_05.01_FlowControl_Exercice2_UpperLower.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice2_UpperLower.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{
	char letter;
	int status = 0;
	int nbExpectedValues = 1;
	do
	{
		printf("Type a letter: ");
		status = scanf("%c", &letter);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues);

	if ((letter >= 'A') && (letter <= 'Z'))
	{
		printf("UPPERCASE\n");
	}
	else if ((letter >= 'a') && (letter <= 'z'))
	{
		printf("lowercase\n");
	}
	else
	{
		printf("The character you entered is not a letter.\n");
	}

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice3_MultiplicationSign.c id=1242.1_Exercices_05.01_FlowControl_Exercice3_MultiplicationSign.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice3_MultiplicationSign.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{
	int a, b;
	int status = 0;

	int nbExpectedValues = 2;
	do
	{
		printf("Please enter 2 integers: ");
		status = scanf("%d %d", &a, &b);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues);

	if ((a == 0) || (b == 0))
	{
		printf("%d * %d = 0\n", a, b);
	}
	else if ((a > 0 && b > 0) || (a < 0 && b < 0))
	{
		printf("%d * %d > 0\n", a, b);
	}
	else
	{
		printf("%d * %d < 0\n", a, b);
	}

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice4_DecreasingOutput.c id=1242.1_Exercices_05.01_FlowControl_Exercice4_DecreasingOutput.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice4_DecreasingOutput.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{
	int a, b, c, x;
	int status = 0;
	
	int nbExpectedValues = 3;
	do
	{
		printf("Please enter 3 integers separated by commas: ");
		status = scanf("%d , %d , %d", &a, &b, &c);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues);


	if (a < b)
	{
		x = a;
		a = b;
		b = x;    // Swap a and b
	}
	if (b < c)
	{
		x = b;
		b = c;
		c = x;    // Swap b and c
	}
	if (a < b)
	{
		x = a;
		a = b;
		b = x;    // ANOTHER Swap a and b
	}

	printf("The 3 integers sorted in decreasing order: %d, %d, %d\n", a, b, c);

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice5_SumSign.c id=1242.1_Exercices_05.01_FlowControl_Exercice5_SumSign.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice5_SumSign.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <math.h>
#include <stdio.h>

int main(void)
{
	int a, b;
	int status = 0;

	int nbExpectedValues = 2;
	do
	{
		printf("Please enter 2 integers: ");
		status = scanf("%d %d", &a, &b);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues);

	if (
		(a == 0 && b == 0) ||
		(a > 0 && b < 0 && abs(a) == abs(b)) ||
		(a < 0 && b > 0 && abs(a) == abs(b))
		)
	{
		printf("%d + %d = 0\n", a, b);
	}
	else if (
		(a >= 0 && b >= 0) ||
		(a <= 0 && b >= 0 && abs(a) <= abs(b)) ||
		(a >= 0 && b <= 0 && abs(a) >= abs(b))
		)
	{
		printf("%d + %d > 0\n", a, b);
	}
	else
	{
		printf("%d + %d < 0\n", a, b);
	}

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice6_OutputMax3.c id=1242.1_Exercices_05.01_FlowControl_Exercice6_OutputMax3.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice6_OutputMax3.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

#define VERSION_D

int main(void)
{
	int a, b, c;
	int status = 0;

	int nbExpectedValues = 3;
	do
	{
		printf("Please enter 3 integers:");
		status = scanf("%d %d %d", &a, &b, &c);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues);

#ifdef VERSION_A
  int max;
	if (a > b)
	{
		max = a;
	}
	else
	{
		max = b;
	}
	if (c > max)
	{
		max = c;
	}
	printf("Maximum is %d\n", max);
#endif

#ifdef VERSION_B
	printf("Maximum is ");
	if (a > b && a > c)
	{
		printf("%d\n", a);
	}
	else if (b > c)
	{
		printf("%d\n", b);
	}
	else
	{
		printf("%d\n", c);
	}
#endif

#ifdef VERSION_C
	max = (a > b) ? a : b;
	max = (c > max) ? c : max;
	printf("Maximum is %d\n", max);
#endif

#ifdef VERSION_D
	printf("Maximum is %d\n", (a > b && a > c) ? a : (b > c) ? b : c);
#endif

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice7_Equation2.c id=1242.1_Exercices_05.01_FlowControl_Exercice7_Equation2.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice7_Equation2.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <math.h>

int main(void)
{
	double a, b, c;
	double delta;
	int status = 0;
	
	int nbExpectedValues = 3;
	do
	{
		printf("Compute solutions of an equation of the form ax^2 + bx + c = 0 \n");
		printf("Please enter coefficients a, b, and c: ");
		status = scanf("%lf %lf %lf", &a, &b, &c);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues);


	if (a == 0 && b == 0 && c == 0)
	{
		printf("Any real is solution of this equation.\n");
	}
	else if (a == 0 && b == 0) // Contradiction: c != 0 and c = 0
	{
		printf("This equation has no solution.\n");
	}
	else if (a == 0) //  Linear equation bx + c = 0
	{
		printf("The solution of this linear equation is :\n");
		printf("x = %.4lf\n", -c / b);
	}
	else
	{
		delta = pow(b, 2) - 4.0 * a * c;
		if (delta < 0)
		{
			printf("This equation has no real solution.\n");
		}
		else if (delta == 0)
		{
			printf("This equation has a single real solution:\n");
			printf("x =  %.4lf\n", -b / (2 * a));
		}
		else
		{
			printf("The real solutions of this equation are:\n");
			printf("x1 = %.4lf\n", (-b + sqrt(delta)) / (2 * a));
			printf("x2 = %.4lf\n", (-b - sqrt(delta)) / (2 * a));
		}
	}

	return 0;
}
```
<!-- SNIPPET:END -->

### `1242.1_05.02_FlowControl`

<!-- SNIPPET:BEGIN source_file=Exercice1_If2Switch.c id=1242.1_Exercices_05.02_FlowControl_Exercice1_If2Switch.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice1_If2Switch.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{
	int status = 0;
	const int nbExpectedValues = 1;
	int x;
	do
	{
		printf("%s", "Entrer un nombre : ");
		status = scanf("%d", &x);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues);

	switch (x)
	{
	case 0: printf("ERROR\n");
		break;
	default: printf("100/%d = %f\n", x, 100. / x);
	}

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice2_Exchange.c id=1242.1_Exercices_05.02_FlowControl_Exercice2_Exchange.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice2_Exchange.c`**

```c
// Convert to Swiss Francs from:
//  - won (W)
//  - dollars ($)
//  - yens (Y)
//  - pounds (L) 
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <ctype.h>             // for toupper(devise)
#include <stdbool.h>

int main(void)
{
	double swissFrancs = 0;
	const double WON2CHF = 0.00070;
	const double USD2CHF = 0.99;
	const double YEN2CHF = 0.0067;
	const double POUND2CHF = 1.13;

	int status = 0;
	const int nbExpectedValues = 2;
	bool inputIsValid = false;
	double amount;
	char currency;
	do
	{
		printf("USAGE: non-negative value [W | $ | Y | P]\n");
		printf("Won = W  Dollar = $  Yen = Y  Pound = P\n");
		printf("Please enter the amount to convert: ");
		status = scanf(" %lg %c", &amount, &currency);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			printf("The input format is not correct!!\n");
			inputIsValid = false;
		}
		else
		{
			// Check that the input currency is supported
			bool currencyIsSupported = (currency == 'W' || currency == '$' || currency == 'Y' || currency == 'P');
			if (currencyIsSupported == false)
			{
				printf("Unsupported currency!!\n");
			}

			// Check that the input amount is positive
			bool amountIsPositive = (amount >= 0);
			if (amountIsPositive == false)
			{
				printf("The input amount is negative!!\n");
			}

			inputIsValid = (status == nbExpectedValues && currencyIsSupported == true && amountIsPositive == true);
		}
	} while (inputIsValid == false);

	currency = toupper(currency);

	// We already know that currency is supported
	switch (currency)
	{
	case 'W': swissFrancs = amount * WON2CHF;
		break;
	case '$': swissFrancs = amount * USD2CHF;
		break;
	case 'Y': swissFrancs = amount * YEN2CHF;
		break;
	case 'P': swissFrancs = amount * POUND2CHF;
		break;
		// default  :
	}

	printf("Swiss francs: %.3lf\n", swissFrancs);

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice3_numberOfDays.c id=1242.1_Exercices_05.02_FlowControl_Exercice3_numberOfDays.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice3_numberOfDays.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{
	int nbDays = 0, month = 0;

	int status = 0;
	const int nbExpectedValues = 1;
	do
	{
		printf("Please enter the number of the month (january=1, ... , december=12): ");
		status = scanf(" %d", &month);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues || month < 1 || month > 12)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues || month < 1 || month > 12);

	switch (month)
	{
	case 2:
		nbDays = 28;
		break;
	case 4:
	case 6:
	case 9:
	case 11:
		nbDays = 30;
		break;
	default:
		nbDays = 31;
	}
	printf("The %dth month has %d days.\n", month, nbDays);

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice4_RGB.c id=1242.1_Exercices_05.02_FlowControl_Exercice4_RGB.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice4_RGB.c`**

```c
#include <stdio.h>
#include <ctype.h>

// NOTE: keep French to match the instructions
int main(void)
{
	char choice;

	switch (choice = toupper(getchar()))
	{
	case 'R': printf("RED");
		break;
	case 'V': printf("GREEN");
		break;
	case 'B': printf("BLUE");
		break;
	default: printf("Error");
	}

	return 0;
}
```
<!-- SNIPPET:END -->

### `1242.1_05.03_FlowControl`

<!-- SNIPPET:BEGIN source_file=Exercice1_Loops.c id=1242.1_Exercices_05.03_FlowControl_Exercice1_Loops.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice1_Loops.c`**

```c
#include <stdio.h>

// NOTE: keep French to match the instructions
int main(void)
{
	/// a)
	printf("a)\n");
	int n = 1;
	while (n < 40)
	{
		printf("value %d\n", n);
		n *= 2;
	}

	/// b)
	printf("b)\n");
	int	count = 0;
	do
	{
		printf("%d ", count);
		++count;
	} while (count % 8 != 0);

	/// c)
	printf("c)\n");
	while (n == 0); // No-operation loop (either infinite, or never executed)

	/// d)
	printf("d)\n");
	for (int x = 0; x < 1000; ++x)
	{
		printf("%d ", x);
	}

	/// e)
	printf("e)\n");
	for (double money = 100; money < 10000; money *= 2.0)
	{
		printf("Fortune = %g\n", money);
	}		

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice2_SumProductMean.c id=1242.1_Exercices_05.03_FlowControl_Exercice2_SumProductMean.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice2_SumProductMean.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{
	int nbVal;

	// B)
	int status = 0;
	const int nbExpectedValues = 1;
	do
	{
		printf("Number of values to read: ");
		status = scanf(" %d", &nbVal);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues || nbVal < 1 || nbVal > 15)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues || nbVal < 1 || nbVal > 15);

	// Initialisation
	int currentValue = 0;
	int sum = 0;
	int product = 1;

	for (int i = 1; i <= nbVal; i++)
	{
		do
		{
			printf("%d. number: ", i);
			status = scanf("%d", &currentValue);

			{
				int c;
				do
				{
					c = getchar();
				} while (c != '\n' && c != EOF);
			}

			if (status != nbExpectedValues)
			{
				// printf("\a");
			}
		} while (status != nbExpectedValues);

		sum += currentValue;
		product *= currentValue;
	}

	printf("Sum = %d\n", sum);
	printf("Product = %d\n", product);
	printf("Mean = %.4lf\n", (double)sum / nbVal);

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice3_Factorial.c id=1242.1_Exercices_05.03_FlowControl_Exercice3_Factorial.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice3_Factorial.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{
	int  N;
	double factorial; // Double because of the size of the result

	const int nbExpectedValues = 1;
	int status = 0;
	do
	{
		printf("Please enter a positive integer N: ");
		status = scanf("%d", &N);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues || N < 0)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues || N < 0);

	factorial = 1.0; // 0! = 1.0 by definition
	for (int i = 1; i <= N; i++)
	{
		factorial *= i;
	}
	printf("%d! = %.0lf\n", N, factorial);

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice4_SquareRoot.c id=1242.1_Exercices_05.03_FlowControl_Exercice4_SquareRoot.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice4_SquareRoot.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <math.h>
#include <stdio.h>

int main(void)
{
	double A;           // Input
	double epsilon;     // Precision required for the estimate
	double root_cur;    // Current estimate of square_root(A)
	double root_prev;   // Previous estimate of square_root(A)

	const int nbExpectedValues = 1;
	int status = 0;
	do
	{
		printf("Please enter a positive real A: ");
		status = scanf("%lf", &A);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues || A < 0)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues || A < 0);

	do
	{
		printf("Needed precision in ]0 ...  0.1]: ");
		scanf("%lf", &epsilon);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues || epsilon <= 0 || epsilon > 1E-1)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues || epsilon <= 0 || epsilon > 1E-1);

		double residualError;
	int j = 1;
	root_cur = A;   // first approximation x_1 = A
	do
	{
		root_prev = root_cur;
		root_cur = (root_prev + A / root_prev) / 2;
		residualError = fabs(root_cur - root_prev);
		printf("The %2d%s approximation of square root of %.2lf is %.6lf\t[residual error: %G] \n"
			, j, (j == 1) ? "st" : "th  ", A, root_cur, residualError);
		j++;
	} while (residualError > epsilon);

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice5_Pyramid.c id=1242.1_Exercices_05.03_FlowControl_Exercice5_Pyramid.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice5_Pyramid.c`**

```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{
	int lineNumber;

	const int nbExpectedValues = 1;
	int status = 0;
	do
	{
		printf("Number of lines (min:1, max:20): ");
		status = scanf("%d", &lineNumber);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues || lineNumber < 1 || lineNumber>20)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues || lineNumber < 1 || lineNumber>20);

	// METHOD 1: using variables spaceNumber et starNumber
	{
		int spaceNumber = lineNumber - 1;
		int starNumber = 1;
		for (int line = 1; line <= lineNumber; line++)
		{
			for (int column = 1; column <= spaceNumber; column++)
			{
				putchar('.');
			}
			for (int column = 1; column <= starNumber; column++) // 2*l-1 = number of stars on line l
			{
				putchar('*');
			}

			putchar('\n');

			spaceNumber -= 1;
			starNumber += 2;
		}
		putchar('\n');
	}

	// METHODE 2: direct computation of the number of spaces and the number of stars
	{
		for (int line = 1; line <= lineNumber; line++)
		{
			for (int column = 1; column <= lineNumber - line; column++)
			{
				putchar('.');
			}
			for (int column = 1; column <= 2 * line - 1; column++)
			{
				putchar('*');
			}

			putchar('\n');
		}

		putchar('\n');
	}

	// METHOD 3: less efficient, but may be useful.
	//       Go through all possible points and test whether to display a space, or a star
	// NOTE: the result is slightly different
	for (int line = 0; line < lineNumber; line++)
	{
		for (int column = 0; column < 2 * lineNumber; column++)
		{
			if (column >= (-line + lineNumber - 1) && column <= (line + lineNumber - 1))
			{
				putchar('*');
			}
			else
			{
				putchar('.');
			}
		}

		putchar('\n');
	}

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice6_MultiplicationTable.c id=1242.1_Exercices_05.03_FlowControl_Exercice6_MultiplicationTable.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice6_MultiplicationTable.c`**

```c
#include <stdio.h>

int main(void)
{
	const int MAX = 10; // number of lines and columns

	printf(" X*Y |");
	for (int j = 0; j <= MAX; j++)
	{
		printf("%4d", j);
	}
	printf("\n");

	printf("______");
	for (int j = 0; j <= MAX; j++)
	{
		printf("____");
	}
	printf("\n");

	for (int i = 0; i <= MAX; i++)
	{
		printf("%3d  |", i);
		for (int j = 0; j <= MAX; j++)
		{
			printf("%4d", i * j);
		}
		printf("\n");
	}

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice7_FizzBuzz.c id=1242.1_Exercices_05.03_FlowControl_Exercice7_FizzBuzz.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice7_FizzBuzz.c`**

```c
#include <stdio.h>

int main(void)
{
	const int NMax = 100;

	for (int number = 1; number <= NMax; number++)
	{
		if ((0 == (number % 3)) && (0 == (number % 5)))
		{
			printf("Fizz Buzz,");
		}
		else if (0 == (number % 3))
		{
			printf("Fizz,");
		}
		else if (0 == (number % 5))
		{
			printf("Buzz,");
		}
		else
		{
			printf("%d,", number);
		}
	}

	return 0;
}
```
<!-- SNIPPET:END -->

### `1242.1_05.04_FlowControl`

<!-- SNIPPET:BEGIN source_file=Exercice1.c id=1242.1_Exercices_05.04_FlowControl_Exercice1.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice1.c`**

```c
#include <stdio.h>

int main(void)
{
	int i, j, x = 0;
	printf("Serie 5.4 exercice 1\n");
	for (i = 0; i < 5; ++i)
		for (j = 0; j < i; ++j)
		{
			switch (i + j - 1)
			{
			case -1:
			case  0:
				x += 1;
				break;
			case  1:
			case  2:
			case  3:
				x += 2;
				break;
			default:
				x += 3;
			}
			printf("%d ", x);
		}

	printf("\nx = %d\n", x);

	return 0;
}
```
<!-- SNIPPET:END -->

<!-- SNIPPET:BEGIN source_file=Exercice2.c id=1242.1_Exercices_05.04_FlowControl_Exercice2.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `Exercice2.c`**

```c
#include <stdio.h>

int main(void)
{
	int i, j, x = 0;
	printf("Serie 5.4 exercice 2\n");
	for (i = 0; i < 5; ++i)
		for (j = 0; j < i; ++j)
		{
			switch (i + j - 1)
			{
			case -1:
			case  0:
				x += 1;
				break;
			case  1:
			case  2:
			case  3:
				x += 2;
				// warning: this statement may fall through
			default:
				x += 3;
			}
			printf("%d ", x);
		}

	printf("\nx = %d\n", x);

	return 0;
}
```
<!-- SNIPPET:END -->

## Solutions Auto-évaluations
### `ch05_ex02_LowercaseUppercase`
```c
#include <stdio.h>

void ch05_ex02_LowercaseUppercase(void);

#ifndef IGNORE_MAIN
int main(void)
{
  ch05_ex02_LowercaseUppercase();

	return 0;
}
#endif

void ch05_ex02_LowercaseUppercase(void)
{
	// TODO
	// START REMOVE LINES
  char letter;
  int status = 0;
  int nbExpectedValues = 1;
  do
  {
    printf("Type a letter: ");
    status = scanf("%c", &letter);

    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }

    if (status != nbExpectedValues)
    {
      // printf("\a");
    }
  } while (status != nbExpectedValues);

  if ((letter >= 'A') && (letter <= 'Z'))
  {
    printf("UPPERCASE\n");
  }
  else if ((letter >= 'a') && (letter <= 'z'))
  {
    printf("lowercase\n");
  }
  else
  {
    printf("The character you entered is not a letter.\n");
  }
  // END REMOVE LINES
}
```	

### `ch05_ex03_MultiplicationSign`
```c
#include <stdio.h>

void ch05_ex03_MultiplicationSign(void);

#ifndef IGNORE_MAIN
int main(void)
{
  ch05_ex03_MultiplicationSign();

	return 0;
}
#endif

void ch05_ex03_MultiplicationSign(void)
{
	// TODO
	// START REMOVE LINES
	int a, b;
	int status = 0;

	int nbExpectedValues = 2;
	do
	{
		printf("Please enter 2 integers: ");
		status = scanf("%d %d", &a, &b);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues);

	if ((a == 0) || (b == 0))
	{
		printf("%d * %d = 0\n", a, b);
	}
	else if ((a > 0 && b > 0) || (a < 0 && b < 0))
	{
		printf("%d * %d > 0\n", a, b);
	}
	else
	{
		printf("%d * %d < 0\n", a, b);
	}
	// END REMOVE LINES
}
```	

### `ch05_ex04_DecreasingOutput`
```c
#include <stdio.h>

void ch05_ex04_DecreasingOutput(void);

#ifndef IGNORE_MAIN
int main(void)
{
  ch05_ex04_DecreasingOutput();

  return 0;
}
#endif

void ch05_ex04_DecreasingOutput(void)
{
	// TODO
	// START REMOVE LINES
  int a, b, c, x;
  int status = 0;

  int nbExpectedValues = 3;
  do
  {
    printf("Please enter 3 integers separated by commas: ");
    status = scanf("%d , %d , %d", &a, &b, &c);

    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }
  } while (status != nbExpectedValues);

  if (a < b)
  {
    x = a;
    a = b;
    b = x; // Swap a and b
  }
  if (b < c)
  {
    x = b;
    b = c;
    c = x; // Swap b and c
  }
  if (a < b)
  {
    x = a;
    a = b;
    b = x; // ANOTHER Swap a and b
  }

  printf("The 3 integers sorted in decreasing order: %d, %d, %d\n", a, b, c);
  // END REMOVE LINES
}
```	

### `ch05_ex07_SecondOrderEquation`
```c
#include <stdio.h>
#include <math.h>

void ch05_ex07_SecondOrderEquation(void);

#ifndef IGNORE_MAIN
int main(void)
{
  ch05_ex07_SecondOrderEquation();

  return 0;
}
#endif

void ch05_ex07_SecondOrderEquation(void)
{
	// TODO
	// START REMOVE LINES
  double a, b, c;
  double delta;
  int status = 0;

  int nbExpectedValues = 3;
  do
  {
    printf("Compute solutions of an equation of the form ax^2 + bx + c = 0 \n");
    printf("Please enter coefficients a, b, and c: ");
    status = scanf("%lf %lf %lf", &a, &b, &c);

    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }

    if (status != nbExpectedValues)
    {
      // printf("\a");
    }
  } while (status != nbExpectedValues);

  if (a == 0 && b == 0 && c == 0)
  {
    printf("Any real is solution of this equation.\n");
  }
  else if (a == 0 && b == 0) // Contradiction: c != 0 and c = 0
  {
    printf("This equation has no solution.\n");
  }
  else if (a == 0) //  Linear equation bx + c = 0
  {
    printf("The solution of this linear equation is :\n");
    printf("x = %.4lf\n", -c / b);
  }
  else
  {
    delta = pow(b, 2) - 4.0 * a * c;
    if (delta < 0)
    {
      printf("This equation has no real solution.\n");
    }
    else if (delta == 0)
    {
      printf("This equation has a single real solution:\n");
      printf("x =  %.4lf\n", -b / (2 * a));
    }
    else
    {
      printf("The real solutions of this equation are:\n");
      printf("x1 = %.4lf\n", (-b + sqrt(delta)) / (2 * a));
      printf("x2 = %.4lf\n", (-b - sqrt(delta)) / (2 * a));
    }
  }
  // END REMOVE LINES
}
```	

### `ch05_ex22_CurrencyConverter`
```c
#include <stdio.h>
#include <ctype.h> // for toupper(devise)
#include <stdbool.h> // for bool, true, false

void ch05_ex22_CurrencyConverter(void);

#ifndef IGNORE_MAIN
int main(void)
{
	ch05_ex22_CurrencyConverter();

	return 0;
}
#endif

void ch05_ex22_CurrencyConverter(void)
{
	// TODO
	// START REMOVE LINES	
	double swissFrancs = 0;
	const double WON2CHF = 0.00070;
	const double USD2CHF = 0.99;
	const double YEN2CHF = 0.0067;
	const double POUND2CHF = 1.13;

	int status = 0;
	const int nbExpectedValues = 2;
	bool inputIsValid = false;
	double amount;
	char currency;
	do
	{
		printf("USAGE: positive value [W | $ | Y | P]\n");
		printf("Won = W  Dollar = $  Yen = Y  Pound = P\n");
		printf("Please enter the amount (in CHF) to convert: ");
		status = scanf(" %lg %c", &amount, &currency);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues)
		{
			printf("The input format is not correct!!\n");
			inputIsValid = false;
		}
		else
		{
			// Check that the input currency is supported
			bool currencyIsSupported = (currency == 'W' || currency == '$' || currency == 'Y' || currency == 'P');
			if (currencyIsSupported == false)
			{
				printf("Unsupported currency!!\n");
			}

			// Check that the input amount is positive
			bool amountIsPositive = (amount >= 0);
			if (amountIsPositive == false)
			{
				printf("The input amount is negative!!\n");
			}

			inputIsValid = (status == nbExpectedValues && currencyIsSupported == true && amountIsPositive == true);
		}
	} while (inputIsValid == false);

	currency = toupper(currency);

	// We already know that currency is supported
	switch (currency)
	{
	case 'W':
		swissFrancs = amount * WON2CHF;
		break;
	case '$':
		swissFrancs = amount * USD2CHF;
		break;
	case 'Y':
		swissFrancs = amount * YEN2CHF;
		break;
	case 'P':
		swissFrancs = amount * POUND2CHF;
		break;
		// default  :
	}

	printf("Swiss francs: %.3lf\n", swissFrancs);
	// END REMOVE LINES
}
```	

### `ch05_ex23_DaysInMonth`
```c
#include <stdio.h>
#include <ctype.h> // for toupper(devise)

void ch05_ex23_DaysInMonth(void);

#ifndef IGNORE_MAIN
int main(void)
{
  ch05_ex23_DaysInMonth();

  return 0;
}
#endif

void ch05_ex23_DaysInMonth(void)
{
	// TODO
	// START REMOVE LINES  
  int nbDays = 0, month = 0;

  int status = 0;
  const int nbExpectedValues = 1;
  do
  {
    printf("Please enter the number of the month (january=1, ... , december=12): ");
    status = scanf(" %d", &month);

    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }

    if (status != nbExpectedValues || month < 1 || month > 12)
    {
      // printf("\a");
    }
  } while (status != nbExpectedValues || month < 1 || month > 12);

  switch (month)
  {
  case 2:
    nbDays = 28;
    break;
  case 4:
  case 6:
  case 9:
  case 11:
    nbDays = 30;
    break;
  default:
    nbDays = 31;
  }
  printf("The %dth month has %d days.\n", month, nbDays);
  // END REMOVE LINES
}
```	

### `ch05_ex32_SumProductMean`
```c
#include <stdio.h>

void ch05_ex32_SumProductMean(void);

#ifndef IGNORE_MAIN
int main(void)
{
  ch05_ex32_SumProductMean();

  return 0;
}
#endif

void ch05_ex32_SumProductMean(void)
{
	// TODO
	// START REMOVE LINES
	int nbVal;

	// B)
	int status = 0;
	const int nbExpectedValues = 1;
	do
	{
		printf("Number of values to read: ");
		status = scanf(" %d", &nbVal);

		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		if (status != nbExpectedValues || nbVal < 1 || nbVal > 15)
		{
			// printf("\a");
		}
	} while (status != nbExpectedValues || nbVal < 1 || nbVal > 15);

	// Initialisation
	int currentValue = 0;
	int sum = 0;
	int product = 1;

	for (int i = 1; i <= nbVal; i++)
	{
		do
		{
			printf("%d. number: ", i);
			status = scanf("%d", &currentValue);

			{
				int c;
				do
				{
					c = getchar();
				} while (c != '\n' && c != EOF);
			}

			if (status != nbExpectedValues)
			{
				// printf("\a");
			}
		} while (status != nbExpectedValues);

		sum += currentValue;
		product *= currentValue;
	}

	printf("Sum = %d\n", sum);
	printf("Product = %d\n", product);
	printf("Mean = %.4lf\n", (double)sum / nbVal);
	// END REMOVE LINES
}
```	

### `ch05_ex33_Factorial`
```c
#include <stdio.h>

void ch05_ex33_Factorial(void);

#ifndef IGNORE_MAIN
int main(void)
{
  ch05_ex33_Factorial();

  return 0;
}
#endif

void ch05_ex33_Factorial(void)
{
	// TODO
	// START REMOVE LINES
  int N;
  double factorial; // Double because of the size of the result

  const int nbExpectedValues = 1;
  int status = 0;
  do
  {
    printf("Please enter a positive integer N: ");
    status = scanf("%d", &N);

    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }

    if (status != nbExpectedValues || N < 0)
    {
      // printf("\a");
    }
  } while (status != nbExpectedValues || N < 0);

  factorial = 1.0; // 0! = 1.0 by definition
  for (int i = 1; i <= N; i++)
  {
    factorial *= i;
  }
  printf("%d! = %.0lf\n", N, factorial);
  // END REMOVE LINES
}
```	
