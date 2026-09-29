---
title: "Chapitre 2 : solutions"
draft: true
weight: 21
---
# Chapitre 2 : solutions

## Solutions exercices

{{< pdf src="/pdfs/1242.1.02_TypesEtVariablesCorrigé.pdf" >}}

### `1242.1_02.01_Types_and_variables`

<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exercices_02.01_Types_and_variables_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

```c
// WARNING: this code is tested using visual studio 2019 and GCC 10.3.0
// Other compilers might return different results
#include <stdio.h>

#define ACTIVATE_WARNINGS_AND_ERRORS 0

void chap_02_ex11_swap(void);

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
		int birthYear;
		int month;
		int day;
		char letter;

		// Instructions
		pi = 3.14; // Not needed if we use const double pi = 3.14
		birthYear = 1963;
		month = 10;
		day = 10;
		letter = 'b';
	}

	// EXERCICE 5, EXERCICE 6, EXERCICE 7, EXERCICE 8, EXERCICE 9, EXERCICE 10
	// => SEE CORRECTION IN PDF

	// EXERCICE 11
	chap_02_ex11_swap();

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
  // WARNING: undefined behavior
	// {
	// 	int a = 2;
	// 	int b = 3;
	// 	printf("a = %d et b = %d\n\n", a, b);

	// 	a ^= b ^= a ^= b;

	// 	printf("a ^= b ^= a ^= b;\n\n");
	// 	printf("a = %d and b = %d\n\n", a, b);
	// }

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

void chap_02_ex11_swap(void)
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
```
<!-- SNIPPET:END -->

### `1242.1_02.02_Types_and_variables`

<!-- SNIPPET:BEGIN source_file=main.c id=1242.1_Exercices_02.02_Types_and_variables_main.c -->
<!--
  GENERATED FILE — DO NOT EDIT.
  This block is automatically regenerated.
-->
**Code source : `main.c`**

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
<!-- SNIPPET:END -->

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