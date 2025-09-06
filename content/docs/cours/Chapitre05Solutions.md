---
title: "Chapitre 5 : solutions"
draft: false
weight: 21
---
# Chapitre 5 : solutions

## Exemples
### `1242.1_05.01_if_else_Divi13`
```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>

// A number N is a multiple of M, iff when dividing N by M, the reminder is 0
int main(void)
{
	int number = 0;
	int reminder = 0;
	int status = 0;
	const int nbExpectedValues = 1;

	do
	{
		printf("Number: ");
		status = scanf("%d", &number);

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

	if (number < 0)
	{
		// If the number is < 0
		// then we test for its positive counterpart only
		number = -number;
	}
	reminder = number % 13;

	if (reminder == 0)
	{
		printf("This number is divisible by 13.\n");
		printf("Result: %d / 13 = %d\n", number, number / 13);
	}
	else
	{
		printf("This number is NOT divisible by 13.\n");
		printf("The closest (lowest) multiple is %d.\n", number - reminder);
	}

	return 0;
}
```

### `1242.1_05.02_if_else_Equalin`
```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>
#include <math.h> // for fabs

int main(void)
{
	double a11, a12, a21, a22, c1, c2;
	double det, det1, det2, x, y;
	int status = 0;

	const int nbExpectedValues = 3;

	printf("This program solves a system of 2 linear equations of the form:\n");
	printf("    a11x + a12y = c1 \nAND a21x + a22y = c2\n");
	printf("Please enter equations system coefficients (with commas):\n");
	do
	{
		printf("a11, a12, c1   = ");
		status = scanf("%lf, %lf, %lf", &a11, &a12, &c1);

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

	do
	{
		printf("a21, a22, c2   = ");
		status = scanf("%lf, %lf, %lf", &a21, &a22, &c2);

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

	// Determinant
	det = a11 * a22 - a21 * a12;
	// There is a solution iff det != 0
	if (det != 0)
	{
		// Codeterminants
		det1 = c1 * a22 - c2 * a12;
		det2 = a11 * c2 - a21 * c1;

		// Solutions
		x = det1 / det;
		y = det2 / det;
		const double epsilon = 0.000001;
		if (fabs(x - y) < epsilon) 
		{
			printf("Solutions are equals: ");
		}

		printf("x = %lf, y = %lf\n", x, y);
	}
	else
	{
		printf("These equations do NOT have a unique solution.\n");
	}

	return 0;
}
```

### `1242.1_05.03_switch_Operat`
```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	double par1, par2, result;
	char operation;
	int status = 0;

	printf("This programs allows to apply +,-,* and / on numbers.\n");

	const int nbExpectedValues = 3;

	do
	{
		printf("Please enter operation: ");
		status = scanf(" %lf %c %lf", &par1, &operation, &par2);

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

	switch (operation)
	{
	case '+': result = par1 + par2;
		break;
	case '-': result = par1 - par2;
		break;
	case '*': result = par1 * par2;
		break;
	case '/': result = par1 / par2;
		break;
	default: result = 0.;
	}

	printf("Result: %lf %c %lf = %lf\n", par1, operation, par2, result);

	return 0;
}
```

### `1242.1_05.04_while_Sum`
```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int sum = 0, counter = 0, N;
	int status = 0;

	printf("This program compute the sum from 1 to N.\n");

	const int nbExpectedValues = 1;
	do
	{
		printf("Please enter N: ");
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

	while (counter <= N)
	{
		sum += counter;
		++counter;
	}
	printf("Result: %d\n", sum);

	return 0;
}
```

### `1242.1_05.04b_while_loops`
```c
#include <stdio.h>

int main(void)
{
  // Example 1
  printf("\nExemple 1\n");
  {
    int i = 0;

    while (i++ < 3)
    {
      printf(" %d ", i);
    }

    printf(" et %d ", i);
  }
  
  // Example 2
  printf("\nExemple 2\n");
  {
    int i = 0;

    while (++i < 3)
    {
      printf(" %d ", i);
    }
    printf(" et %d ", i);
  }

  // Example 3
  printf("\nExemple 3\n");
  {
    int i = 0;
    while (i < 3)
    {
      printf(" %d ", i++);
    }
    printf(" et %d ", i);
  }

  // Example 4
  printf("\nExemple 4\n");
  {
    int i = 0;

    while (i < 3)
    {
      printf(" %d ", ++i);
    }
    printf(" et %d ", i);
  }

  return 0;
}
```

### `1242.1_05.05_do_while_Addition`
```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	double sum = 0;
	int status = 0;

	printf("This programs compute the sum of list of reals (terminated by 0)\n");

	double value = 0; // Just in case
	do                                   /* Boucle de saisie */
	{
		const int nbExpectedValues = 1;
		do
		{
			printf("add: ");
			status = scanf("%lf", &value);

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

		sum += value;
	} while (value != 0);

	printf("Sum = %lf\n", sum);

	return 0;
}
```

### `1242.1_05.06_for_Power2`
```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int result, N, exponent = 0;
	int status = 0;

	printf("This programs displays the list of power of 2 from 1 to N\n");

	const int nbExpectedValues = 1;
	do
	{
		printf("Please enter N: ");
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

	for (result = 1; result <= N; result *= 2)
	{
		printf("2^%d = %d\n", exponent, result);
		++exponent;
	}

	return 0;
}
```

### `1242.1_05.07_for_loop_examples`
```c
#include <stdio.h>

int main(void)
{
	int n;
	for (n = 0; n < 2; ++n)
	{
		printf("Iteration:%d\n", n);
	}

	printf("Fin:%d", n);

	int i, j, c, k;

	printf("\n");
	for (i = 0; i < 5; i++)
		printf("%d,", i);

	printf("\n");
	for (j = 4; j <= 12; j = j + 2)
		printf("%d,", j);

	printf("\n");
	for (c = 'a'; c < 'f'; c += 1)
		printf("%c,", c);

	printf("\n");
	for (k = 5; k > 0; k--)
		printf("%d,", k);

	printf("\n");
	for (int i = 0, j = 0; i < 10; i++, j = i * i)
	{
		printf("x = %2d, x^2 = %2d\n", i, j);
	}

	return 0;
}
```

## Solutions exercices
[1242.1.05.01_StructuresDeControle_Correction.pdf](/pdf/1242.1.05.01_StructuresDeControle_Correction.pdf)

[1242.1.05.02_StructuresDeControle_Correction.pdf](/pdf/1242.1.05.02_StructuresDeControle_Correction.pdf)

[1242.1.05.03_StructuresDeControle_Correction.pdf](/pdf/1242.1.05.03_StructuresDeControle_Correction.pdf)

[1242.1.05.04_StructuresDeControle_Correction.pdf](/pdf/1242.1.05.04_StructuresDeControle_Correction.pdf)

### `05.01 Exercice1`
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

### `05.01 Exercice2`
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

### `05.01 Exercice3`
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

### `05.01 Exercice4`
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

### `05.01 Exercice5`
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

### `05.01 Exercice6`
```c
#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

#define VERSION_D

int main(void)
{
	int a, b, c, max;
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

### `05.01 Exercice7`
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

### `05.02 Exercice1`
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

### `05.02 Exercice2`
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

		// BIIIP to let user know when there is a problem
		if (inputIsValid == false)
		{
			// printf("\a");
			printf("USAGE : positive value [W | $ | Y | L]\n");
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

### `05.02 Exercice3`
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

### `05.02 Exercice4_RGB`
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

### `05.03 Exercice1`
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

### `05.03 Exercice2`
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

### `05.03 Exercice3`
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

### `05.03 Exercice4`
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

### `05.03 Exercice5`
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

### `05.03 Exercice6`
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

### `05.03 Exercice7`
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

### `05.04 Exercice1`
```c
#include <stdio.h>

int main(void)
{
	int i, j, x = 0;
	printf("Serie 5.4 exercice 1");
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

### `05.04 Exercice2`
```c
#include <stdio.h>

int main(void)
{
	int i, j, x = 0;
	printf("Serie 5.4 exercice 2");
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
			default:
				x += 3;
			}
			printf("%d ", x);
		}

	printf("\nx = %d\n", x);

	return 0;
}
```

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
