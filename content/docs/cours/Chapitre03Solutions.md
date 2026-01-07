---
title: "Chapitre 3 : solutions"
draft: false
weight: 21
---
# Chapitre 3 : solutions

## Exemples
### `1242.1_03.01_Modulo`
```c
#include <stdio.h>

#define ACTIVATE_WARNINGS_AND_ERRORS 0

int main(void)
{
	int a;

	a = 10 % 2;
	printf("%d\n", a);

	a = 10 % 3;
	printf("%d\n", a);

	a = 10 % 10;
	printf("%d\n", a);

	a = 5 % 10;
	printf("%d\n", a);

	// SEE standard page 494.
	// "The behavior is undefined in the following circumstances: [..]
	//	- The value of the second operand of the / or % operator is zero (6.5.5)."
#if ACTIVATE_WARNINGS_AND_ERRORS
	a = 10 % 0; // ERROR with VS: this is an UB according to standard.
	printf("%d\n", a);
#endif

	a = 0 % 10;
	printf("%d\n", a);

	return 0;
}
```

### `1242.1_03.02_Arithmetic`
```c
#include <stdio.h>

int main(void)
{
	int a = 0;

	a = (10 + 6) / (3 - 1);
	printf("%d\n", a);

	a = (10 + 6) / 3 - 1;
	printf("%d\n", a);

	a = 10 + 6 / (3 - 1);
	printf("%d\n", a);

	a = 10 + 6 / 3 - 1;
	printf("%d\n", a);

	return 0;
}
```

### `1242.1_03.03_Overflow`
```c
#include <stdio.h>
#include <math.h> // Needed for HUGE_VAL

#define ACTIVATE_WARNINGS_AND_ERRORS 0

int main(void)
{
	unsigned char a;
	a = 255 + 1; // WARNING: converting an int into an unsigned char
	printf("%d\n", a);

	char b;
	b = 127 + 1;
	printf("%d\n", b);

	// UB, compile error with VS
#if ACTIVATE_WARNINGS_AND_ERRORS
	double testWithLiteral = 1 / 0.;
#endif

	// UB, compile error with VS
#if ACTIVATE_WARNINGS_AND_ERRORS
#define ZERO 0.0;
	double testWithMacro = 1. / ZERO;
#endif

	// OK with VS but returns infinity
	const double zero = 0.0;
	double testWithVariable = 1. / zero;
	printf("%lf\n", testWithVariable);

	double x = HUGE_VAL;
	printf("%lf %lf\n", x, -HUGE_VAL);

	double y = x / x;
	printf("%lf %lf\n", y, -HUGE_VAL / HUGE_VAL);

	double z = 1 / HUGE_VAL;
	printf("%lf\n", z);

	return 0;
}
```

### `1242.1_03.04_Division`
```c
#include <stdio.h>
#include <math.h> // Needed for HUGE_VAL

int main(void)
{
	int   i1 = 5, i2 = 2, i3;
	float f1 = 5., f2 = 2., f3;

	f3 = f1 / f2;
	printf("%f\n", f3);

	i3 = i1 / i2;
	printf("%d\n", i3);

	f3 = i1 / i2; // WARNING: converting an int into a float
	printf("%f\n", f3);

	i3 = f1 / f2; // WARNING: converting a float into an int
	printf("%d\n", i3);

	return 0;
}
```

### `1242.1_03.05_Conversions`
```c
#include <stdio.h>

int main(void)
{
	{
		int x = 5;
		int y = 2;
		int r;
		r = x / y;
		printf("%d\n", r);
	}
	{
		int x = 5;
		int y = 2;
		float r;
		r = x / y; // WARNING: converting an int into a float
		printf("%f\n", r);
	}
	{
		int x = 5;
		int y = 2;
		float r;
		r = (float)x / y;
		printf("%f\n", r);
	}
	{
		float x = 5;
		int y = 2;
		int r;
		r = x / y; // WARNING: converting a float into an int
		printf("%d\n", r);
	}
	{
		float x = 5;
		int y = 2;
		float r;
		r = x / y;
		printf("%f\n", r);
	}
	{
		int x = 5;
		int y = 2;
		float r;
		r = (float)(x / y);
		printf("%f\n", r);
	}

	return 0;
}
```

### `1242.1_03.06_ConversionsOverflow`
```c
// This programs uses various operations using variables
// and mixing types
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	double result1, result2;
	long result3;
	unsigned int result4;
	result1 = 4. / 3;    // Division: double -> double
	result2 = 4 / 3;     // Division: int -> double
	result3 = result1;   // double -> long
	result4 = -result1;  // double -> unsigned int
	printf("double:         4. / 3  = %lg\n", result1);
	printf("double:         4  / 3  = %lg\n", result2);
	printf("long:           4. / 3  = %ld\n", result3);
	printf("unsigned int: -(4. / 3) = %u\n", result4);	// (2^32) - 1

	return 0;
}
```

### `1242.1_03.07_Increment`
```c
#include <stdio.h>

int main(void)
{
	{
		int x = 6, y;
		y = ++x;
		printf("%d\n", y);
	}
	{
		int x = 6, y;
		y = x++;
		printf("%d\n", y);
	}
	{
		int x = 6, y;
		y = --x;
		printf("%d\n", y);
	}
	{
		int x = 6, y;
		y = x--;
		printf("%d\n", y);
	}

	return 0;
}
```

### `1242.1_03.08_Bitwise`
```c
#include <stdio.h>

int main(void)
{
	unsigned char x = 0xAA; // 1010 1010

	printf("%X\n", x); 
	printf("%X\n", x & 0xFF); 
	printf("%X\n", x & 0x01); 
	printf("%X\n", x & 0x03);

	return 0;
}
```

### `1242.1_03.98_Conditional`
```c
// Conditional operator
#include <stdio.h>

#define ACTIVATE_WARNINGS_AND_ERRORS 0

int main(void)
{
	// Example from Slides
	int i = 1;

	int a = 3, b = 9, max, min;

	max = ((a > b) ? a : b);
	min = ((a > b) ? b : a);

	printf("Min / max: %d / %d\n", min, max);

	// It obviously also works without parenthesis
	max = (a > b) ? a : b;
	printf("Max: %d\n", max);

	// Q: can we nest ternary operator?
	// A: yes. A ternary operator needs expression as operands.
	//    So, as a ternary operator is an expression, it can contain
	//    other ternary opertors
	int value = 100;
	int quarter = value > 50 ? (value > 75 ? 4 : 3) : (value <= 25 ? 1 : 2);

	// It even works without parenthesis, but it is less readible
	int quarter2 = value > 50 ? value > 75 ? 4 : 3 : value <= 25 ? 1 : 2;

	// Q: why cannot we use blocks inside conditional operator?
	// A:
	//   ISO C standard
	//     6.5.15 Conditional operator
	//       "...the result is the value of the second or third operand	(whichever is evaluated), converted to the type described below..."
	//       ==>> blocks do not return values, expressions do.

	//  - VS: error C2059:  syntax error: '{'
	//  - GCC: error: expected expression before '{' token
#if ACTIVATE_WARNINGS_AND_ERRORS
	(i++ == 1) ? {printf("Hello\n"); } : {printf("World\n"); };
#endif

	//  - VS: error C2059:  syntax error: '{'
	//  - GCC (with -Wpedantic): 	warning: ISO C forbids braced-groups within expressions [-Wpedantic]
	//    but prints "Hello"
	//    ==>> GCC extension.
#if ACTIVATE_WARNINGS_AND_ERRORS
	(i++ == 1) ? ({ printf("Hello\n"); }) : ({ printf("World\n"); });
#endif

	// OK: a function call is an expression
	(i++ == 1) ? printf("Hello\n") : printf("World\n");

	return 0;
}
```

### `1242.1_03.99_Comma`
```c
#include <stdio.h>

int main(void)
{
	// The comma operator ',' is a binary operator with the lowest priority.
	// It uses two steps:
	// 1) it evaluates the first part (before the comma) and ignores the result;
	// 2) it evaluates the second part (after the comma) and returns the result (with the associated type!)

	float a = 5.2; // Warning	C4305 'initializing': truncation from 'double' to 'float'

	// Corner case (With VS): no warning because 5.5 can be exactly represented as a float
	float a_bis = 5.5;

	double b = 10.1;

	a = b; // Warning C4244 '=': conversion from 'double' to 'float', possible loss of data
	
	// , has the lowest priority, so it is the same as doing:
	// 1) a = a
	// 2) evalute b
	// => no problem here.
	a = a, b;

	// Here, we enforce the comma operator evaluation first using ().
	// So it is the same as:
	// 1) (a, b)
	//		1.1) evaluate a
	//		1.2) evaluate b and return the result AND its type
	// So the final type of (a, b) is the type of b, that is double
	// 2) then we do a = (a, b), and this affects a double to a float.
	a = (a, b); // Warning C4244 '=': conversion from 'double' to 'float', possible loss of data

	// QUESTION: what happens if we do:
	a, b = b, a; // OK, double affected to double

	// QUESTION: what happens if we do:
	a, b = a, b; // OK, float affected to double

	// QUESTION: what happens if we do:
	b, a = b, a; // Warning C4244 '=': conversion from 'double' to 'float', possible loss of data

	// QUESTION: what happens if we do:
	b, a = a, b; // OK, float affected to float.

	return 0;
}
```


## Solution exercices
[1242.1.03_Operateurs_Correction.pdf](/pdf/1242.1.03_Operateurs_Correction.pdf)

### `1242.1_03.01_Operators`
```c
#include <stdio.h>
#include <stdbool.h>
#include <limits.h>
#include <float.h>
#include <math.h>

#define ACTIVATE_WARNINGS_AND_ERRORS 0

int main(void)
{
	// EXERCICE 1
	{
		printf("EXERCICE 1\n");
		int memory = 42;
		memory += 1;

		int word = 42;
		word *= 8;

		int currency = 42;
		currency -= 1;

		int a = 42;
		int b = 2;
		a %= b;

		int part = 42;
		int nb_persons = 4;
		part /= nb_persons;

		int x = 10;
		int y, z;
		x *= y = z = 4;
		printf("x=%d y=%d z=%d\n", x, y, z);
	}

	// EXERCICE 2
	{
		// a)
		printf("EXERCICE 2a\n");
		int n = 5, p = 9;
		float x;
		x = p / n;
		printf("x=%f\n", x);
		x = (float)p / n;
		printf("x=%f\n", x);
		x = (p + 0.5) / n;
		printf("x=%f\n", x);
		x = (int)(p + 0.5) / n;
		printf("x=%f\n", x);

		// b)
		printf("EXERCICE 2b\n");
		int a;
		a = 10 % 10;
		printf("a=%d\n", a);
		a = 5 % 10;
		printf("a=%d\n", a);
		// ERROR: modulo zero
#if ACTIVATE_WARNINGS_AND_ERRORS
		a = 10 % 0;
		printf("%d\n", a);
#endif
		a = 0 % 10;
		printf("a=%d\n", a);
	}

	// EXERCICE 3
	{
		printf("EXERCICE 3\n");
		int x = 2, y = 1, z = 3;
		z += -x++ + ++y;
		printf("%d %d %d\n", x, y, z);
	}

	// EXERCICE 4
	{
		// a)
		printf("EXERCICE 4a\n");
		bool result = 3 <= 2 - 1;
		printf("result=%s\n", result ? "true" : "false"); // To display "true" or "false"
		result = 3 * (4 > 4) + 2.5;
		printf("result=%s\n", result ? "true" : "false");
		result = (4 == 5.1) / 2 + 1;
		printf("result=%s\n", result ? "true" : "false");
		result = true && false || true;
		printf("result=%s\n", result ? "true" : "false");
		int n = 42;
		result = 3 + (n > n - 1);
		printf("result=%s\n", result ? "true" : "false");
		result = !true && false || !false;
		printf("result=%s\n", result ? "true" : "false");

		// b)
		printf("EXERCICE 4b\n");
		int x = 5;
		result = (x >= 5) && (x <= 10);
		printf("result=%s\n", result ? "true" : "false");
		x = 10;
		result = (x >= 5) && (x <= 10);
		printf("result=%s\n", result ? "true" : "false");
		x = 7;
		result = (x >= 5) && (x <= 10);
		printf("result=%s\n", result ? "true" : "false");
		x = 4;
		result = (x >= 5) && (x <= 10);
		printf("result=%s\n", result ? "true" : "false");
		x = 11;
		result = (x >= 5) && (x <= 10);
		printf("result=%s\n", result ? "true" : "false");

		// c)
		printf("EXERCICE 4c\n");
		x = 5;
		result = (x < 5) || (x > 10);
		printf("result=%s\n", result ? "true" : "false");
		x = 10;
		result = (x < 5) || (x > 10);
		printf("result=%s\n", result ? "true" : "false");
		x = 7;
		result = (x < 5) || (x > 10);
		printf("result=%s\n", result ? "true" : "false");
		x = 4;
		result = (x < 5) || (x > 10);
		printf("result=%s\n", result ? "true" : "false");
		x = 11;
		result = (x < 5) || (x > 10);
		printf("result=%s\n", result ? "true" : "false");
	}

	// EXERCICE 5
	{
			// a)
			{
					printf("EXERCICE 5a\n");
					int n = 5, p = 9;
					int q;
					float x;
					q = n < p; /* 1 */
					printf("n=%d p=%d q=%d x=%d\n", n, p, q, x);
					q = n == p; /* 2 */
					printf("n=%d p=%d q=%d x=%d\n", n, p, q, x);
					q = p % n + (p > n); /* 3 */
					printf("n=%d p=%d q=%d x=%d\n", n, p, q, x);
			}

			// b)
			{
				printf("EXERCICE 5b\n");
				int n = 10, p = 5, q = 10, r;
				r = n == (p = q);
				n = p = q = 5;
				n += p += q;
				printf("n=%d p=%d q=%d r=%d\n", n, p, q, r);
			}

			// c)
			{
				printf("EXERCICE 5c\n");
				double a = 3.5 * 6;
				int b = 243 * -83;
				int c = (int)(20.35 * 24);
				int d = (int)85.35 * 2;
				int e = 'w' - 2024;
				char f = 23 / 9;
				printf("a=%lf b=%d c=%d d=%d e=%d f=%d \n", a, b, c, d, e, f);
			}

			// d) SEE correction

			// e)
			{
				printf("EXERCICE 5e\n");
				int x = 2;
				printf("x=%d\n", x);
				x = 3 + (3 > x);
				printf("x=%d\n", x);
				x += x -= 2;
				printf("x=%d\n", x);
				x = (++x - 6) * 3;
				printf("x=%d\n", x);
				x *= (5 > x) * (3 + 23);
				printf("x=%d\n", x);
			}
			
		// f) SEE correction
	}

	// EXERCICE 6 A)
	{
		printf("EXERCICE 6A\n");
		unsigned char x = 0xAA; // 1010 1010

		printf("Masking %x\n", x);
		x = x | 0xC0; // x|=0xC0;
		printf("Masking the 2 most significant bits: %x\n", x);
		x = x & 0xFC; // x&=0xFC
		printf("Masking the 2 least significant bits: %x\n", x);
		x = (x >> 3) & 0x07;
		printf("Display bits 3, 4 and 5: %x\n", x);

		// In binary (bit shift, then masking to keep least significant bit, then print as integer)
		unsigned char bit3 = (x >> 0) & 0x01;
		unsigned char bit4 = (x >> 1) & 0x01;
		unsigned char bit5 = (x >> 2) & 0x01;
		printf("Display bits 3, 4 and 5 in binary = %d%d%d\n", bit5, bit4, bit3);
	}

	// EXERCICE 6 B) V1
	{
		printf("EXERCICE 6B V1\n");
		unsigned int x = 0x03020100;
		unsigned char b0, b1, b2, b3;
		unsigned int mask = 0xFF;

		b0 = ((x & mask));

		mask <<= 8;
		b1 = ((x & mask) >> 8);

		mask <<= 8;
		b2 = ((x & mask) >> 16);

		mask <<= 8;
		b3 = ((x & mask) >> 24);

		printf("b3:%X b2:%X b1:%X b0:%X\n", b3, b2, b1, b0);
	}

	// EXERCICE 6 B) V2
	{
		printf("EXERCICE 6B V2\n");
		unsigned int x = 0x03020100;
		unsigned char b0, b1, b2, b3;
		unsigned int mask = 0xFF;

		b0 = x;
		b1 = x >> 8;
		b2 = x >> 16;
		b3 = x >> 24;

		printf("b3:%X b2:%X b1:%X b0:%X\n", b3, b2, b1, b0);
	}

	// EXERCICE 7
	{
		printf("EXERCICE 7\n");
		// Integer overflow: INT_MAX + 1 = INT_MIN
		printf("INT_MAX: %d INT_MAX+1: %d\n", INT_MAX, INT_MAX + 1);
		printf("DBL_MAX: %g\n", DBL_MAX);
		// 1000 is NOT significant compared to DBL_MAX
		// DBL_MAX + 1000 == DBL_MAX
		printf("DBL_MAX+1000: %g\n", DBL_MAX + 1000);
		// => Infinity
		printf("DBL_MAX*2 : %g\n", DBL_MAX * 2);
	#if ACTIVATE_WARNINGS_AND_ERRORS
		printf("q = 1/0: %f \n", 1 / 0);
		float q = 1.0f / 0;
		printf("q = 1.0f/0: %f \n", q);
		printf("1/q : %f \n", 1 / q);
		printf("q/q : %f \n", q / q);
	#endif
		printf("sqrt(-1) : %f \n", sqrt(-1));
	}
	
	return 0;
}
```

## Solutions Auto-évaluations
Pas d'auto-évaluation pour ce chapitre.
