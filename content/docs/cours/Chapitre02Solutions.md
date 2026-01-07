---
title: "Chapitre 2 : solutions"
draft: false
weight: 21
---
# Chapitre 2 : solutions

## Exemples
### `1242.1_02.01_Prog_typeSize`
```c
#include <stdio.h>

int main(void)
{
	int* p;
	enum vowel{ a, e, i, o, u, y } vow;

	printf("_Bool         : %zu bits\n", 8 * sizeof(_Bool));
	printf("char          : %zu bits\n", 8 * sizeof(char));
	printf("unsigned char : %zu bits\n", 8 * sizeof(unsigned char));
	printf("\n");
	printf("short (int)   : %zu bits\n", 8 * sizeof(short int));
	printf("short         : %zu bits\n", 8 * sizeof(short));
	printf("unsigned short: %zu bits\n", 8 * sizeof(unsigned short));
	printf("\n");
	printf("int           : %zu bits\n", 8 * sizeof(int));
	printf("unsigned int  : %zu bits\n", 8 * sizeof(unsigned int));
	printf("\n");
	printf("long          : %zu bits\n", 8 * sizeof(long));
	printf("unsigned long : %zu bits\n", 8 * sizeof(unsigned long));
	printf("\n");
	printf("float         : %zu bits\n", 8 * sizeof(float));
	printf("double        : %zu bits\n", 8 * sizeof(double));
	printf("long double   : %zu bits\n", 8 * sizeof(long double));
	printf("\n");
	printf("enum          : %zu bits\n", 8 * sizeof(vow));
	printf("pointer       : %zu bits\n", 8 * sizeof(p));
	printf("\n");

	return 0;
}
```

### `1242.1_02.02_SwapAB`
```c
#include <stdio.h>

int main(void)
{
	int a = 10;
	int b = 5;
	int temp;

	// Before swapping variables values
	printf("BEFORE swap\n");
	printf("Variable a: %d \n", a); //  Variable a: 10
	printf("Variable b: %d \n", b); //  Variable b: 5

	/// Add here the instructions to SWAP the variables values
	/// Hint: 2 instructions are executed sequentially (one after the other)
	temp = a;
	a = b;
	b = temp;

	// After swapping varialbes values
	printf("\nAFTER swap\n");
	printf("Variable a: %d \n", a); //  Variable a: 5
	printf("Variable b: %d \n", b); //  Variable b: 10

	return 0;
}
```

### `1242.1_02.03_BinaryConversion`
```c
#include <stdio.h>

// Assumes little endian
void printBits(int size, void *ptr)
{
	unsigned char *b = (unsigned char*)ptr;

	for (int i = size - 1; i >= 0; --i)
	{
		for (int j = 7; j >= 0; --j)
		{
			// Take the i-th byte
			unsigned char byte = b[i];
			// Use a mask to keep the (j+1)-th bit.
			// 10000000 to keep 8th bit (j == 7)
			// 01000000 to keep 7th bit
			// ...
			// 00000001 to keep 1st bit (j == 0)
			unsigned char mask = 1 << j;
			byte = byte & mask;
			// Then offset byte so that the (j+1)-th bit is in the first position.
			// So the char will always be 0 or 1 depending on the value of the (j+1)-th bit
			byte >>= j;
			printf("%u", byte);
		}
	}

	puts("");
}

int main(void)
{
	char          c = 1;
	int           i = 1;
	float         f = 1.f;
	double        d = 1.;
	printf("char   c = 1  : "); printBits(sizeof(c), &c);
	printf("int    i = 1  : "); printBits(sizeof(i), &i);
	printf("float  f = 1.f: "); printBits(sizeof(f), &f);
	printf("double d = 1. : "); printBits(sizeof(d), &d);

	c = -1;
	i = -1;
	f = -1.f;
	d = -1.;
	printf("char   c = -1  : "); printBits(sizeof(c), &c);
	printf("int    i = -1  : "); printBits(sizeof(i), &i);
	printf("float  f = -1.f: "); printBits(sizeof(f), &f);
	printf("double d = -1. : "); printBits(sizeof(d), &d);

	c = '1';
	printf("char c = '1' : "); printBits(sizeof(c), &c);
	c = 49;
	printf("char c = 49  : "); printBits(sizeof(c), &c);

	printf("\nPrint values 1, 2 and 4 (float):\n");
	f = 1.f;
	printBits(sizeof(f), &f); // 0 0111 1111  00000000000000000000000 exp=127 (-127) => e=0 1*2^0 = 1
	f = 2.f;
	printBits(sizeof(f), &f); // 0 1000 0000  00000000000000000000000 exp=128 (-127) => e=1 1*2^1 = 2
	f = 4.f;
	printBits(sizeof(f), &f); // 0 1000 0001  00000000000000000000000 exp=129 (-127) => e=2 1*2^2 = 4

	return 0;
}
```

### `1242.1_02.04_BIIIP`
```c
#include <stdio.h>

int main(void)
{
	// BIIIP using a char
	char c = '\7';
	printf("%c", c);

	c = '\a';
	printf("%c", c);

	// BIIIP using a string
	const char* s = "\7";
	printf("%s", s);

	return 0;
}
```

### `1242.1_02.05_Booleans`
```c
#include <stdio.h>
// To use bool instead of _Bool
// Added in C99: https://en.wikipedia.org/wiki/C99
#include <stdbool.h>

int main(void)
{
	int oldBool = 42;
	if (oldBool == 0)
	{
		printf("%s", "oldBool is FALSE\n");
	}
	// Any other value is considered true
	else
	{
		printf("%s", "oldBool is TRUE\n");
	}

	// _Bool is a keyword of the language
	_Bool newBool = 42;
	if (newBool == 0)
	{
		printf("%s", "newBool is FALSE\n");
	}
	// Any other value is considered true
	else
	{
		printf("%s", "newBool is TRUE\n");
	}

	bool betterBool = true;
	if (betterBool == false)
	{
		printf("%s", "betterBool is FALSE\n");
	}
	else
	{
		printf("%s", "betterBool is TRUE\n");
	}

	// Test output
	{
		_Bool test = 3; //!=0 so considered true
		printf("%d\n", test);
		test = (2 * 3) < 7;
		printf("%d\n", test);
	}
	{
		bool test = true;
		printf("%d\n", test);
		test = (2 * 3) < 7;
		printf("%d\n", test);
	}

	_Bool x = true;
	bool y = true;
	char z = true;

	printf("x = %d\n", x);
	printf("y = %d\n", y);
	printf("z = %d\n", z);
	printf("(x == true) = %d\n", x == true);
	printf("Memory space: \n");
	printf("x: %d\n", (int) sizeof(x));
	printf("y: %d\n", (int) sizeof(y));
	printf("z: %d\n", (int) sizeof(z));
	printf("(x == true): %d\n", (int) sizeof(x == true));

	return 0;
}
```

## Solution série 2.1
[1242.1.02_TypesEtVariablesCorrigé.pdf](/pdf/1242.1.02_TypesEtVariablesCorrigé.pdf)
### `1242.1_02.01_Types_and_variables`
```c
// WARNING: this code is tested using visual studio 2019 and GCC 10.3.0
// Other compilers might return different results
#include <stdio.h>

#define ACTIVATE_WARNINGS_AND_ERRORS 1

int main(void)
{
	// EXERCICE 1
	{
		int nombre;
		// NOTE: identifiers are case-sensitive!
		int Nombre;

		int Auto;
		
#if ACTIVATE_WARNINGS_AND_ERRORS
		int Dollar$; // WARNING: Visual studio and GCC are ok with that!!!
#endif
		int Ligne4;
		// ERROR: starts with a numerical digit
#if ACTIVATE_WARNINGS_AND_ERRORS
		int 17h20;
#endif
		int ARC_EN_CIEL;
		int RouGE7;
		// ERROR: contains a '/'
#if ACTIVATE_WARNINGS_AND_ERRORS
		int vert / jaune;
#endif
		// ERROR: it's a string
#if ACTIVATE_WARNINGS_AND_ERRORS
		int "poisson";
#endif
		int Pourcent;
		int descriptiondinterface1;
		int n;
		int ZoRRo;
		int arbre(); // WARNING: ok, but this is a function, not a variable!
		// ERROR: contains an accent and an exclamation mark
#if ACTIVATE_WARNINGS_AND_ERRORS
		int Lumière!;
#endif
	}

	// EXERCICE 2
	{
		int a, b = 2, c;
		// ERROR : 4roues starts with a numerical digit
#if ACTIVATE_WARNINGS_AND_ERRORS
		float 4roues, Deux_Roues, tricycle;
#endif
		double PIBSuisse_;
		// ERROR: real is not a type
#if ACTIVATE_WARNINGS_AND_ERRORS
		real PIB_USA_en_$;
#endif
		// ERROR: variable c is already defined
#if ACTIVATE_WARNINGS_AND_ERRORS
		char c;
#endif
	}

	// EXERCICE 3
	{
		const double PI;
		char tel[10];
		enum { Homme, Femme } genre;
		float tauxDeChange;
		unsigned char noDuMois;
		char initialePrenom;
		double valeurBourseApple;
	}

	// EXERCICE 4
	{
		// Definitions
		double pi;
		// Or even better
		// const double pi = 3.14;
		int anneeDeNaissance;
		int mois;
		int jour;
		char lettre;

		// Instructions
		pi = 3.14; // Not needed if we use const double pi = 3.14
		anneeDeNaissance = 1963;
		mois = 10;
		jour = 10;
		lettre = 'b';
	}

	// EXERCICE 5, EXERCICE 6, EXERCICE 7, EXERCICE 8, EXERCICE 9, EXERCICE 10
	// => SEE CORRECTION IN PDF

	// EXERCICE 11
	{
		int variable1 = 10;
		int variable2 = 5;
		// Before swapping the variables content
		printf("Variable 1: %d \n", variable1); // Variable 1: 10
		printf("Variable 2: %d \n", variable2); // Variable 2: 5
		// Swap variables content
		int temp = variable1;
		variable1 = variable2;
		variable2 = temp;
		// After swapping the variables content
		printf("Variable 1: %d \n", variable1); // Variable 1: 5
		printf("Variable 2: %d \n", variable2); // Variable 2: 10
	}

	// EXERCICE 12
	// Version 1
	{
		int a = 2;
		int b = 3;
		printf("a = %d and b = %d\n\n", a, b);

		a = a + b;
		printf("a = a + b; : a = %d\n", a);
		b = a - b;
		printf("b = a - b; : b = %d\n", b);
		a = a - b;
		printf("a = a - b; : a = %d\n\n", a);

		printf("a = %d et b = %d\n\n", a, b);
	}
	// Version 2
	{
		int a = 2;
		int b = 3;
		printf("a = %d and b = %d\n\n", a, b);

		a = a ^ b;
		printf("a = a ^ b; : a = %d\n", a);
		b = a ^ b;
		printf("b = a ^ b; : b = %d\n", b);      // b = a ^ b ^ b = a
		a = a ^ b;
		printf("a = a ^ b; : a = %d\n\n", a);    // a = a ^ b ^ a = b

		printf("a = %d et b = %d\n\n", a, b);
	}
	// Version 3
	{
		int a = 2;
		int b = 3;
		printf("a = %d et b = %d\n\n", a, b);

		a ^= b ^= a ^= b;

		printf("a ^= b ^= a ^= b;\n\n");
		printf("a = %d and b = %d\n\n", a, b);
	}
	// Version 4
	// WARNING: does not work if a or b is equal to zero
	{
		int a = 2;
		int b = 3;
		printf("a = %d and b = %d\n\n", a, b);

		a = a * b;
		printf("a = a * b; : a = %d\n", a);
		b = a / b;
		printf("b = a / b; : b = %d\n", b);
		a = a / b;
		printf("a = a / b; : a = %d\n\n", a);

		printf("a = %d and b = %d\n\n", a, b);
	}

	return 0;
}
```

## Solution série 2.2

### `1242.1_02.02_Types_and_variables`
```c
// WARNING: this code is tested using VS Code and GCC 12.2.0
// Other compilers may return different results

#include <stdio.h>
#include <stdlib.h>
#include <math.h> // exercice 2

void chap02_2_ex1_CelsiusToFarenheit(void);
void chap02_2_ex2_AssetInterestRate(void);
void chap02_2_ex3_ImproveNumberDisplay(void);
void chap02_2_ex4_FloatingNumberCoding(void);

int main(void)
{
    chap02_2_ex1_CelsiusToFarenheit();
    chap02_2_ex2_AssetInterestRate();
    chap02_2_ex3_ImproveNumberDisplay();
    chap02_2_ex4_FloatingNumberCoding();

   return 0; 
}

void chap02_2_ex1_CelsiusToFarenheit()
{
    double temperatureC, temperatureF = 0.;
    printf("Enter a temperature in Celsius: ");
    scanf("%lf", &temperatureC);
    temperatureF = 32 + 1.8 * temperatureC;
    printf("%2.f degres Celsius correspond to a %2.1f degres Farenheit\n", temperatureC, temperatureF);
}

void chap02_2_ex2_AssetInterestRate()
{
    int duration = 0;

    double initAssets = 0.0;
    double interestRate = 0.0;
    double finalAssets = 0.0;

    printf("What is your initial asset? ");
    scanf("%lf", &initAssets);

    printf("What is your yearly interest rate (in pourcent)?: ");
    scanf("%lf", &interestRate);

    printf("Duration in years? ");
    scanf("%d", &duration);

    finalAssets = initAssets * pow( (1+interestRate/100),duration);

    printf("\nAfter %d years, your assets (with interest) will be  %10.2f SFr\n\n", duration, finalAssets);
}

void chap02_2_ex3_ImproveNumberDisplay()
{
    double finalAssets = 1876435.264901;
    int duration = 5;
    double millions=(int)(finalAssets/1e06);
    double thousands=(int)((finalAssets- 1e06*millions)/1000);
    double francs= (int)fmod(finalAssets, 1000);
    int centimes= 5 * (int) (20*(0.0499999999999 + finalAssets-(int)finalAssets));
    printf("\nAfter %d years, your assets (with interest) will be", duration);
    printf(" %3.0f'%03.0f'%03.0f.%02d", millions, thousands, francs, (int)centimes);
}

// Exercice 4 (very advanced)
typedef struct
{
    unsigned int mantisa : 23; // specify the number of bits used by the variable
    unsigned int exponent : 8;
    unsigned int sign : 1;
} BinaryFloatingNb;

/*
For the exercise, the original purpose of the union got "overriden" with something completely different:
writing one member of a union and then inspecting it through another member.
*/

typedef union
{
    float floatNb;
    BinaryFloatingNb BinaryNb;
    int floatHexa;

} FloatRepresentation;

void chap02_2_ex4_FloatingNumberCoding()
{
  FloatRepresentation floatingRep = { .floatNb = 1234567890 }; // CHANGE HERE the floating number you want to analyze
  printf("\nfloating number = %1.10e\n", floatingRep.floatNb);
  printf("sign = %x\n", floatingRep.BinaryNb.sign);  //%x = lower case hexa
  printf("exponent = %x\n", floatingRep.BinaryNb.exponent);
  printf("mantisa = %x\n", floatingRep.BinaryNb.mantisa);
  printf("hexa = %x\n", floatingRep.floatHexa);
}
```

## Solutions Auto-évaluations
### `ch02_ex11_Swap`
```c
#include <stdio.h>

void ch02_ex11_Swap(void);

#ifndef IGNORE_MAIN
int main(void)
{
	ch02_ex11_Swap();

	return 0;
}
#endif

void ch02_ex11_Swap(void)
{
	int variable1 = 10;
	int variable2 = 5;

	// Before swapping the variables content
	printf("Variable 1: %d \n", variable1); // Variable 1: 10
	printf("Variable 2: %d \n", variable2); // Variable 2: 5
	
	// Swap variables content
	// TODO
	// START REMOVE LINES
	int temp = variable1;
	variable1 = variable2;
	variable2 = temp;
	// END REMOVE LINES
	
	// After swapping the variables content
	printf("Variable 1: %d \n", variable1); // Variable 1: 5
	printf("Variable 2: %d \n", variable2); // Variable 2: 10
}
```

### `ch02_ex21_CelsiusToFarenheit`
```c
#include <stdio.h>

double ch02_ex21_CelsiusToFarenheit(double);

#ifndef IGNORE_MAIN
int main(void)
{
  double temperatureC, temperatureF = 0.;
  printf("Enter a temperature in Celsius: ");
  scanf("%lf", &temperatureC);

  temperatureF = ch02_ex21_CelsiusToFarenheit(temperatureC);

  printf("%2.f degres Celsius correspond to a %2.1f degres Farenheit\n", temperatureC, temperatureF);

  return 0;
}
#endif

double ch02_ex21_CelsiusToFarenheit(double temperatureC)
{
  double temperatureF = 0.;

  // TODO
  // START REMOVE LINES
  temperatureF = 32 + 1.8 * temperatureC;
  // END REMOVE LINES

  return temperatureF;
}
```

### `ch02_ex22_AssetInterestRate`
```c	
#include <stdio.h>
#include <math.h>

double ch02_ex22_AssetInterestRate(double, double, double);

#ifndef IGNORE_MAIN
int main(void)
{
  double initAssets = 0.0;
  double interestRate = 0.0;
  int duration = 0;
  double finalAssets = 0.0;

  printf("What is your initial asset? ");
  scanf("%lf", &initAssets);

  printf("What is your yearly interest rate (in pourcent)?: ");
  scanf("%lf", &interestRate);

  printf("Duration in years? ");
  scanf("%d", &duration);

  finalAssets = ch02_ex22_AssetInterestRate(initAssets, interestRate, duration);

  printf("\nAfter %d years, your assets (with interest) will be  %10.2f SFr\n\n", duration, finalAssets);

  return 0;
}
#endif

double ch02_ex22_AssetInterestRate(double initAssets, double interestRate, double duration)
{
  double finalAssets = 0.0;

	// TODO
	// START REMOVE LINES
  finalAssets = initAssets * pow((1 + interestRate / 100), duration);
  // END REMOVE LINES

  return finalAssets;
}
```