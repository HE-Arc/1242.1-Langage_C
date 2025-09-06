---
title: "Chapitre 8 : solutions"
draft: false
weight: 21
---
# Chapitre 8 : solutions

## Exemples
### `01_ArraysDeclarations`
```c
#include <stdio.h>

#define NMAX 32

int main(void)
{
	double price[NMAX];
	printf("Array \"price\" has a size of %d\n", (int)(sizeof(price) / sizeof(double)));

	// Variable length array are not supported on Visual Studio
#ifndef _MSC_VER
	const int nMAX = 43;
	double price2[nMAX]; // VS : error C2057: expected constant expression
	printf("Array \"price2\" has a size of %d\n", (int)(sizeof(price2) / sizeof(double)));

	int nmax;
	printf("Please enter \"price3\" array size: ");
	scanf("%d", &nmax); // TODO: should use safe scanf here
	double price3[nmax]; // VS : error C2057: expected constant expression
	printf("Array \"price3\" has a size of %d\n", (int)(sizeof(price3) / sizeof(double)));
#endif

#ifdef __GNUC__
	// NOTE: nMAX6 is actually not a constant.
	// => price6 is a VLA and thus cannot be initialized like that.
	const int nMAX6 = 3;
	// double price6[nMAX6] = {1, 2, 3};
#endif

	return 0;
}
```

### `02_ArraysInitialisations`
```c
#include <stdio.h>

int main(void)
{
	// ALL elements are initialized
	int tablo[5] = { -12, 9, 5, 47, 66 };

	// SOME elements are initialized.
	// The others are set to 0.
	// SEE norm 6.7.9/19
	int tab[5] = { 1, 4, 9 };
	tab[3] = 11;

	// Size is automatically set to 4 because of initialisation
	double data[] = { 1.3, 2.6, -8.4, 0.1 };

	// Better, when possible, to enforce the size directly
	double data2[4] = { 1.3, 2.6, -8.4, 0.1 };

	// TOO FEW init values => the remaining values are set to the default value
	int tab2[4] = { 1, 2, 3 };

	// TOO MANY init values => error
	// int tab3[4] = { 1, 2, 3, 4, 5 };

	// TOO FEW init values => the remaining values are set to the default value
	char tab4[4] = { 'a', 'b', 'c' };

	// TOO MANY init values => error
	// char tab5[4] = { 'a', 'b', 'c', 'd', 'e' };

	// TOO FEW init values using literals => the remaining values are set to the default value
	char word[25] = "world";
	printf("%s", word); // Prints "world" + garbage as word is missing the null terminating character

	// TOO MANY init values using literals => "OK"
	// SEE norm 6.7.9/14
	char word2[5] = "world";
	printf("%s", word); // Prints "world" + garbage as word is missing the null terminating character

	return 0;
}
```

### `03_ArraysRemarks`
```c
#include <stdio.h>

// Prototypes
int input_size(void);
double input_value(void);

int main(void)
{
	// Variable length array are not supported on Visual Studio
#ifndef _MSC_VER
	int size = input_size();
	int tablo[size];

	// [Error with GCC] error: variable-sized object may not be initialized
	// double val[size] = { 1.1, 2.2, 3.3 };
#endif

	double x = 1.23;
	double values[3] = { 2.4, 1.2, x };

	// Can we initialize an array with values known at runtime?
	// Variable length array are not supported on Visual Studio
#ifndef _MSC_VER
	int value2 = input_value();

	// OK: constant-size array
	double array2[] = { 1.1, 2.2, value2 };

	int size3 = input_size();
	// [Error with GCC] error: variable-sized object may not be initialized
	// double array3[size3] = { 1.1, 2.2, value2 };
#endif

	int nbElements = sizeof(values) / sizeof(double);
	// Set all values in an array
	for (int i = 0; i < nbElements; ++i)
	{
		values[i] = i / 10.;
	}

	// Print all values in an array
	for (int i = 0; i < nbElements; ++i)
	{
		printf("%lf ", values[i]);
	}
	printf("\n");

	// Copy values from one to array to the other
	double values2[3];
	for (int i = 0; i < nbElements; ++i)
	{
		values2[i] = values[i];
		printf("%lf ", values2[i]);
	}
	printf("\n");

	return 0;
}

int input_size(void)
{
	int size;
	printf("Please enter array size: ");
	scanf("%d", &size); // TODO: use safe scanf here
	return size;
}

double input_value(void)
{
	// Handling User input errors:
	// 1) Print what is expected
	// 2) Read input from User
	// 3) Empty the stdin buffer
	// 4) Repeat until we got what we expected
	int status = 0;
	const int nbExpectedValues = 1;
	// Variables to store User input values
	int value;
	do
	{
		printf("Input value: ");
		status = scanf("%lf", &value);

		// IMPORTANT: fflush(stdin) does not always work!
		// It is strongly advised NOT to use it
		// fflush(stdin);
		// Instead, empty the buffer "manually"
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		// BIIIP to let user know when there is a problem
		if (status != nbExpectedValues)
		{
			printf("\a");
		}
	} while (status != nbExpectedValues);

	return value;
}
```

### `04_SideEffects`
```c
#include <stdio.h>

int main(void)
{
	int daysInMonth[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };

	// Out of range access
	// daysInMonth[12], daysInMonth[13] and daysInMonth[14] print garbage
	for (int i = -3; i < 15; i++)
	{
		printf("daysInMonth[%d] = %d\n", i + 1, daysInMonth[i]);
	}

	return 0;
}
```

### `05_ArrayOfConsts`
```c
#include <stdio.h>

int main(void)
{
	const double sinus[91] = { 0.000, 0.017, 0.035, 0.052, 0.070, 0.087 };

	printf("sinus[4] = %f\n", sinus[4]);
	// ERROR: error C2166: l-value specifies const object
	sinus[0] = 1.0;
	printf("sinus[0] = %f\n", sinus[0]);

	return 0;
}
```

### `06_Size`
```c
#include <stdio.h>

int main(void)
{
	int data[100] = { 1, 2, 3, 4, 5, 6, 7 };
	char vowels[] = { 'a', 'e', 'i', 'o', 'u', 'y' };

	// Total size
	printf("Total size of array \"data\" = %d\n", (int)sizeof(data));
	// Nb Elements in array data
	int nbElementsInData = (int)sizeof(data) / sizeof(int);
	printf("Number of elements in array \"data\" = %d\n", nbElementsInData);

	// Nb Elements in array vowels
	int nbElementsInVowels = (int)sizeof(vowels) / sizeof(char);
	printf("Number of elements in array \"vowels\" = %d\n", nbElementsInVowels);

	return 0;
}
```

### `07_ArraysParam`
```c
#include <stdio.h>

// NOTE: arrays cannot be passed by values so they decay into pointers when passed to functions
void display(int tab[], int nb)
{
	int i;
	// IMPORTANT: int tab[] here is treated as a pointer (an address). So sizeof(tab) returns the size of a pointer.
	//  ==>> ALWAYS pass an additional parameter giving the number of elements in the array
	printf("Array size as seen OUTSIDE the function is %d elements\n", nb);
	// NOTE: Visual Studio issues a warning here
	printf("Array size as seen INSIDE the function is %d elements\n", (int)(sizeof(tab) / sizeof(int)));
	for (i = 0; i < nb + 2; i++)
	{
		printf("%d\n", tab[i]);
	}
}

int main(void)
{
	int tablo[10] = { 1,2,3 };
	display(tablo, sizeof(tablo) / sizeof(int));

	return 0;
}
```

### `08_Multi`
```c
#include <stdio.h>

int main(void)
{
	int value[20][40];
	double volume[10][10][10];
	int matrix[2][4] = { {10,20,30,40}, {15,25,35,45} };

	printf("\"value\" size is %d\n", (int)(sizeof(value) / sizeof(int)));
	printf("\"volume\" size is %d\n", (int)(sizeof(volume) / sizeof(double)));
	printf("\"matrix\" size is %d\n\n", (int)(sizeof(matrix) / sizeof(int)));

	for (int i = 0; i < 2; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			printf("matrix[%d][%d] = %d\n", i, j, matrix[i][j]);
		}
	}

	printf("matrix[%d][%d] = %d\n", 1, 0, matrix[1][0]);

	return 0;
}
```

### `09_StructureCopy`
```c
#include <stdio.h>
#include <string.h>

struct User
{
	char login[16];
	int id;
};

int main(void)
{
	int current_id = 42;
	struct User user1 = { "toto", current_id++ };
	struct User user2 = { .id = current_id++, .login = "titi" };
	struct User user3;

	printf("INITIALISATION\n");
	printf("user1 {id, login}: {%d, %s}\n", user1.id, user1.login);
	printf("user2 {id, login}: {%d, %s}\n", user2.id, user2.login);
	printf("user3 {id, login}: {%d, %s}\n", user3.id, user3.login);// NOTE: prints garbage

	strcpy(user1.login, "tata");

	printf("strcpy from literal\n");
	printf("user1 {id, login}: {%d, %s}\n", user1.id, user1.login);
	printf("user2 {id, login}: {%d, %s}\n", user2.id, user2.login);
	printf("user3 {id, login}: {%d, %s}\n", user3.id, user3.login);// NOTE: prints garbage

	strcpy(user3.login, user1.login);

	printf("strcpy from other structure\n");
	printf("user1 {id, login}: {%d, %s}\n", user1.id, user1.login);
	printf("user2 {id, login}: {%d, %s}\n", user2.id, user2.login);
	printf("user3 {id, login}: {%d, %s}\n", user3.id, user3.login);

	user3 = user2;

	printf("Full structure assignment\n");
	printf("user1 {id, login}: {%d, %s}\n", user1.id, user1.login);
	printf("user2 {id, login}: {%d, %s}\n", user2.id, user2.login);
	printf("user3 {id, login}: {%d, %s}\n", user3.id, user3.login);

	return 0;
}
```

### `10_MemoryAllocationStringInt`
```c
#include <stdio.h>
#include <string.h>

/* Allocation de:

		k       vaut 30 a la fin de la boucle
		a=1     0x0001
		b
		c= -1 = 0xFFFF
		t1="abcd"
		t2="xyz"
		En memoire on a :
		x y z \0 a b c d \0 0xFFFF **** 1000 00021 ******
		t1       t2         c      b    a    k

		strcpy(t2,"1234567890");

		En memoire on a :
		1 2 3 4 5 6 7 8 0x90FF **** 1000 00021 ******
		t1      t2      c      b    a    k
*/

int main(void)
{
	int  k;
	int  a = 1;
	int  b;
	int  c = -1;
	char t1[] = "abcd";
	char t2[] = "xvy";

	printf("&a:%p(%d)\n&b:%p(%d)\n&c:%p(%d)\nt1:%p(%d)\nt2:%p(%d)\n", &a, &a, &b, &b, &c, &c, t1, t1, t2, t2);
	printf("-----------------------\n");

	for (k = 0; k < 30; k++)
	{
		printf("%p(%d) %c %d\n", &t2[k], &t2[k], t2[k], t2[k]);
	}
	printf("-----------------------\n");

	strcpy(t2, "1234567890");

	for (k = 0; k < 30; k++)
	{
		printf("%p(%d) %c %d\n", &t2[k], &t2[k], t2[k], t2[k]);
	}
	printf("-----------------------\n");

	printf("\n%s", t1);

	return 0;
}
```

### `11_StringsInitializations`
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
	char fileName[16] = "test.c";
	printf("%s", fileName);

	char word[] = {'H','e','l','l','o'};
	printf("%s", word);

	char chaine[256];
	char mini[4];
	scanf("%s", chaine);
	scanf("%s", mini);
	printf("%s\n", chaine);
	printf("%s\n", mini);

	return 0;
}
```

### `12_RevueCStrings`
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
	char letter   = 'a';
	char chaine[] = "a";

	char temp [] = "";
	char text [] = "Blablabla";

	int i = 0;
	
	for (; i < strlen(text)+1 ; i++)
	{
		temp[i] = text[i];
	}

	return 0;
}
```

### `1242.1_08.96_ArrayInitializationToZero`
```c
#include <stdio.h>

// Global or static array => elements automatically initialized to 0
int global_array[4];

int main(void)
{
	// Not initialized by default
	int local_array[4];
	// First element initialized => all the others initialized too
	int local_array1[4] = {0};
	// Works with GCC but non-standard => do not use.
	int local_array2[4] = {};

	// Global or static array => elements automatically initialized to 0
	static int static_array[4];

	return 0;
}
```

### `1242.1_08.97_ScanfBufferOverflow`
```c
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// IMPORTANT for Visual Studio: execute in RELEASE Mode to avoid additional debug padding around stack variables
int main(void)
{
	// IMPORTANT for Visual Studio: variables order on the stack is not guaranteed.
	// If we do char a[9] instead, then a and b will be in different order on the stack.
	bool access_granted = false;
	char expected_password[10] = "admin1234";

	char actual_password[10];

	printf("Please enter password: ");
	scanf("%s", actual_password); // Enter "admin99999999999999999"

	if (strcmp(actual_password, expected_password) == 0) // If password is correct
	{
		access_granted = true;
	}

	if (access_granted == true)
	{
		printf("CONGRATS: you gained control of the server!\n");
	}
	else
	{
		printf("SORRY: you do not have enough privileges!\n");
	}

	return 0;
}
```

### `1242.1_08.98_VLAs`
```c
#include <stdio.h>

// If not using MSVC
#ifndef _MSC_VER
// If C version is C11 or newer, VLAs are optional.
// => So explicitly check for their support
#if __STDC_VERSION__ >= 201100L
#ifndef _STDC_NO_VLA_
#define VLAS_SUPPORTED
#endif
// Else if C version is C99, VLAs are supported.
#elif __STDC_VERSION__ >= 199900L
#define VLAS_SUPPORTED
#endif
#endif

// OK with VS and GCC
#define DEF_ARRAY_SIZE 10
int array1[DEF_ARRAY_SIZE];

// NOTE: const in C means "read-only", not that it is a constant.
// => So const_array_size is still considered as a variable.
// VS: error C2057: expected constant expression
// GCC: error: variably modified tabg2 at file scope
const int const_array_size = 10;
// int array2[const_array_size];

void function(void)
{
	// Compile error with VS
	// VS: error C2057: expected constant expression
#ifdef VLAS_SUPPORTED
	// OK with GCC
	int array3[const_array_size];
	// NOTE: const in C means "read-only", not that it is a constant.
 	// GCC: error: variable-sized object may not be initialized
 	// int array4[const_array_size] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

	 // But the following is OK
	 int array5[10] =  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
#endif
}

int main(void)
{
	#ifdef VLAS_SUPPORTED
	printf("VLAs are supported on this compiler");	
	#endif

	function();
	return 0;
}
```

### `1242.1_08.99_StringOverflow`
```c
#include <stdio.h>

// Run it with the debugger and see what happens
int main(void)
{
	char string[4] = "123";
	printf("%s\n", string);

	scanf("%s", string);
	printf("%s\n", string);

	return 0;
}
```

## Solutions série 8.1
[1242.1.08.01_TableauxStructures_Correction.pdf](/pdf/1242.1.08.01_TableauxStructures_Correction.pdf)

### `1242.1_08.01_ArraysAndStructures`
```c
#include <stdio.h>

#define ACTIVATE_WARNINGS_AND_ERRORS 0

// To suppress warnings
// NOTE: no ';' here so that we are forced to put it in the code directly.
// That way, the final code ressembles to a normal code.
#define UNUSED(var) (void)(var)

void Exercice1(void)
{
#if ACTIVATE_WARNINGS_AND_ERRORS
	// Should be unsigned int matrice[3][3];
	unsigned int matrice[3, 3];
#endif

	// OK
	int vecteur[6]; UNUSED(vecteur);

#if ACTIVATE_WARNINGS_AND_ERRORS
	// Should be char ordinateur[] = "IBM PC";
	char ordinateur[] = 'IBM PC';
#endif

	// OK
	float mesure[2][1000]; UNUSED(mesure);
	int des[3][3][3]; UNUSED(des);

	// Should be char nom[9] = "François";
	// NOTE: Visual Studio does not complain
	char nom[8] = "François";
	char mois[14] = "juin";
}

void Exercice2(void)
{
	char a[] = "un\ndeux\ntrois\n";
	printf("Nb bytes in memory: %d\n", (int)sizeof(a));
	char b[14] = "un deux trois";
	printf("Nb bytes in memory: %d\n", (int)sizeof(b));
	// ERROR
	// char c[] = 'abcdefg';
	char c[] = "abcdefg";
	printf("Nb bytes in memory: %d\n", (int)sizeof(c));
	// ERROR
	// char d[10] = 'x';
	char d[10] = "x" ; // Or char d[10] = { 'x', '\0' };
	printf("Nb bytes in memory: %d\n", (int)sizeof(d));
	char e[5] = "cinq";
	printf("Nb bytes in memory: %d\n", (int)sizeof(e));
	char f[] = "Cette " "phrase " "est coupée"; // Equivalent to "cette phrase est coupée"
	printf("%s", f);
	printf("Nb bytes in memory: %d\n", (int)sizeof(f));
	char g[2] = { 'a', '\0' };
	printf("Nb bytes in memory: %d\n", (int)sizeof(g));
	// Compiles but still an ERROR
	// char h[4] = { 'a', 'b', 'c'};
	char h[4] = { 'a', 'b', 'c', 0x00 };
	printf("Nb bytes in memory: %d\n", (int)sizeof(h));
	char i[4] = "'o'";
	printf("Nb bytes in memory: %d\n", (int)sizeof(i));
}

// Use the debug to look at the memory layout
// Use 	printf("&values: %p\n", values); to print the address if needed
void Exercice3(void)
{
	double values[] = { 1.2, -2.3, 0. };
	short int IDEtudiant[5] = { 1234, 4576, 7345, 9999 };
	int serie[5];
	for (int i = 0; i < 5; i++)
	{
		serie[i] = 2 * i + 1;
	}
	
	char texte[] = "Alea jacta est";
	struct XY { char x; double y; } var1 = { '5',5.f };
	struct XY tabStruct[3] = { {'5',5.f}, {'6',6.f}, {'7',7.f} };
	printf("&tabStruct[]: %p\n", tabStruct);
	for (int i = 0; i < 3; ++i)
	{
		printf("&tabStruct[%d]: %p\n", i,  &tabStruct[i]);
		printf("&tabStruct[%d].x: %p\n", i, &tabStruct[i].x);
		printf("&tabStruct[%d].y: %p\n", i, &tabStruct[i].y);
	}
}

int main(void)
{
	Exercice1();
	Exercice2();
	Exercice3();

	return 0;
}
```

## Solutions série 8.2
[1242.1.08.02_TableauxStructures_Correction.pdf](/pdf/1242.1.08.02_TableauxStructures_Correction.pdf)

### `1242.1_08.02_ArraysAndStructures - Exercice 1`
```c
#include <stdio.h>

#define CAPACITY 50

void Exercice1(void)
{
	int array[CAPACITY];
	int nbVal;
	long sum;  // type long to avoid overflow

	int nbExpectedValues = 1;
	int status = -1;
	do
	{
		printf("Nb values (max.%d): ", CAPACITY);
		status = scanf("%d", &nbVal);

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
	} while (status != nbExpectedValues || nbVal < 0);

	for (int i = 0; i < nbVal; ++i)
	{
		nbExpectedValues = 1;
		do
		{
			printf("Value %d? ", i);
			status = scanf("%d", &array[i]);
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
	}

	printf("array:\n");	
	for (int i = 0; i < nbVal; ++i)
	{
		printf("%d ", array[i]);
	}
	printf("\n");

	sum = 0;
	for (int i = 0; i < nbVal; ++i)
	{
		sum += array[i];
	}

	printf("Total sum: %ld\n", sum);
}

int main(void)
{
	Exercice1();

	return 0;
}
```

### `1242.1_08.02_ArraysAndStructures - Exercice 2`
```c
#include <stdio.h>

#define CAPACITY 50

int main(void)
{
	int tab[CAPACITY], tabPos[CAPACITY], tabNeg[CAPACITY];
	int nbVal;
	int i, iPos, iNeg;

	printf("Nb values (max.%d): ", CAPACITY);
	scanf("%d", &nbVal); // TODO: use safe scanf
	for (i = 0; i < nbVal; i++)
	{
		printf("Value %d ? ", i);
		scanf("%d", &tab[i]);
	}

	iPos = 0;
	iNeg = 0;

	for (i = 0; i < nbVal; i++)
	{
		if (tab[i] > 0)
		{
			tabPos[iPos] = tab[i];
			iPos++;
		}
		else
			if (tab[i] < 0)
			{
				tabNeg[iNeg] = tab[i];
				iNeg++;
			}
	}

	printf("Positive array:\n");
	for (i = 0; i < iPos; i++)
	{
		printf("%d ", tabPos[i]);
	}
	printf("\n");

	printf("Negative array:\n");
	for (i = 0; i < iNeg; i++)
	{
		printf("%d ", tabNeg[i]);
	}
	printf("\n");

	return 0;
}
```

### `1242.1_08.02_ArraysAndStructures - Exercice 3`
```c
#include <stdio.h>

#define N 50

void Exercice3(void)
{
	int array[N][N];
	int nbLines, nbColumns;
	int i, j;
	long sum = 0;

	int nbExpectedValues = 1;
	int status = -1;
	do
	{
		printf("Nb lines (max.%d): ", N);
		status = scanf("%d", &nbLines);
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}
	} while (status != nbExpectedValues || nbLines < 0);

	do
	{
		printf("Nb columns (max.%d): ", N);
		status = scanf("%d", &nbColumns);
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}
	} while (status != nbExpectedValues || nbColumns < 0);


	for (i = 0; i < nbLines; i++)
	{
		for (j = 0; j < nbColumns; j++)
		{
			printf("array[%d][%d]: ", i, j);
			scanf(" %d", &array[i][j]);
		}
	}

	for (i = 0; i < nbLines; i++)
	{
		for (j = 0; j < nbColumns; j++)
		{
			sum += array[i][j];
		}
	}

	printf("Total sum: %ld\n", sum);
}

int main(void)
{
	Exercice3();

	return 0;
}
```

### `1242.1_08.02_ArraysAndStructures - Exercice 4`
```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long vectors_dot_product(int [], int [], int n);

#define MAX_DIM 50

int main(void)
{
	int u[MAX_DIM], v[MAX_DIM];
	int i, nb_values;

	int nbExpectedValues = 1;
	int status = -1;
	do
	{
		printf("Vectors dimension (max.50): ");
		status = scanf("%d", &nb_values);
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}
	} while (status != nbExpectedValues || nb_values < 0);

	printf("** First vector **\n");
	for (i = 0; i < nb_values; i++)
	{
		int current_value = 0;
		do
		{
			printf("Element %d: ", i);
			status = scanf("%d", &current_value); // TODO: use safe scanf
			{
				int c;
				do
				{
					c = getchar();
				} while (c != '\n' && c != EOF);
			}
		} while (status != nbExpectedValues);
		u[i] = current_value;
	}

	printf("** Second vector **\n");
	for (i = 0; i < nb_values; i++)
	{
		int current_value = 0;
		do
		{
			printf("Element %d: ", i);
			status = scanf("%d", &current_value); // TODO: use safe scanf
			{
				int c;
				do
				{
					c = getchar();
				} while (c != '\n' && c != EOF);
			}
		} while (status != nbExpectedValues);
		v[i] = current_value;
	}
	
	long dot = vectors_dot_product(u, v, nb_values);

	printf("Dot product: %ld\n", dot);

	return 0;
}

long vectors_dot_product(int v1[], int v2[], int n)
{
	long dot = 0;

	for (int i = 0; i < n; ++i)
	{
		dot += (long)v1[i] * v2[i];
	}

	return dot;
}
```

### `1242.1_08.02_ArraysAndStructures - Exercice 5`
```c
#include <stdio.h>

#define CAPACITY 50

int main(void)
{
	int tab[CAPACITY];
	int nb_values;

	printf("Nombre de valeurs (max. %d) : ", CAPACITY);
	scanf("%d", &nb_values);
	for (int i = 0; i < nb_values; i++)
	{
		printf("Element %d: ", i);
		scanf("%d", &tab[i]);
	}

	printf("tab:\n");
	for (int i = 0; i < nb_values; i++)
	{
		printf("%d ", tab[i]);
	}
	printf("\n");

	int iMin = 0, iMax = 0;
	for (int i = 1; i < nb_values; i++)
	{
		if (tab[i] > tab[iMax])
		{
			iMax = i;
		}
		else if (tab[i] < tab[iMin])
		{
			iMin = i;
		}
	}

	printf("Min index: %d\n", iMin);
	printf("Max index: %d\n", iMax);
	printf("Min: %d\n", tab[iMin]);
	printf("Max: %d\n", tab[iMax]);

	return 0;
}
```

### `1242.1_08.02_ArraysAndStructures - Exercice 6`
```c
// Author: FRT
// Date: 11.12.2104

#include <stdio.h>

void matrix_print(int *M, int n, int m)
{
	int i, j;
	for (i = 0; i < n; i++)
	{
		printf("| ");
		for (j = 0; j < m; j++)
		{
			printf("%4d", M[i * m + j]);
		}
		printf("|\n");
	}
}

void matrix_fill(int *M, int n, int m)
{
	int i, j;
	printf("Matrix %d x %d\n", n, m);
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			printf("matrix[%d][%d] = ", i, j);
			scanf(" %d", &M[i * m + j]);
		}
	}
}

#define NB_LINES_A 2
#define NB_COLS_A 3
#define NB_COLS_B 2

// #define NB_LINES_B is the same as NB_LINE_A for the multiplication to be possible

#define NB_COL_B 3

int main(void)
{
	int i, j, k;

	printf("Matrix multiplication A(2, 3) * B(3, 2)\n");
	int A[NB_LINES_A][NB_COLS_A];
	int B[NB_COLS_A][NB_COLS_B];

	int C[NB_LINES_A][NB_COLS_B];

	printf("A:\n");
	matrix_fill((int *)A, NB_LINES_A, NB_COLS_A);
	printf("B:\n");
	matrix_fill((int *)B, NB_COLS_A, NB_COLS_B);

	for (i = 0; i < NB_LINES_A; i++)
	{
		for (j = 0; j < NB_COLS_B; j++)
		{
			C[i][j] = 0;
			for (k = 0; k < NB_COLS_A; k++)
			{
				C[i][j] += A[i][k] * B[k][j];
			}
		}
	}

	printf("A:\n");
	matrix_print((int *)A, NB_LINES_A, NB_COLS_A);
	printf("B:\n");
	matrix_print((int *)B, NB_COLS_A, NB_COLS_B);
	printf("C:\n");
	matrix_print((int *)C, NB_LINES_A, NB_COLS_B);

	return 0;
}
```

## Solutions série 8.3
[1242.1.08.03_TableauxStructures_Correction.pdf](/pdf/1242.1.08.03_TableauxStructures_Correction.pdf)

### `1242.1_08.03_ArraysAndStructures - Exercice 1`
```c
#include <stdio.h>

int main(void)
{
	char M1[30], M2[30], M3[30], M4[30], M5[30];
	printf("Please enter 5 words (separed with spaces):\n");
	scanf("%s %s %s %s %s", M1, M2, M3, M4, M5); // TODO: use safe scanf
	printf("%s %s %s %s %s\n", M5, M4, M3, M2, M1);

	return 0;
}
```

### `1242.1_08.03_ArraysAndStructures - Exercice 2`
```c
#include <stdio.h>
#include <string.h>
#define CAPACITY 50

int main(void)
{
	char text[CAPACITY + 1];
	char character;

	printf("Please enter a phrase: ");
	fgets(text, CAPACITY, stdin);

	// If we have a newline here, we know that we are ok.
	// Otherwise, we need to flush(strdin)
	if (strchr(text, '\n') == NULL)
	{
		int c;
		do
		{
			c = getchar();
		} while (c != '\n' && c != EOF);
	}

	printf("\nWhat character are you looking for?");
	scanf(" %c", &character);

	int i = 0;
	while (text[i] != character && text[i] != '\0')
	{
		i++;
	}

	// METHOD 1
	if (i < strlen(text))
	{
		printf("Character found at index %d.\n", i);
	}
	else
	{
		printf("Character NOT found.\n");
	}

	// METHOD 2
	if (text[i] == character)
	{
		printf("Character found at index %d.\n", i);
	}
	else
	{
		printf("Character NOT found.\n");
	}

	return 0;
}
```

### `1242.1_08.03_ArraysAndStructures - Exercice 3`
```c
#include <stdio.h>

#define MAXLENGTH 200

int main(void)
{
	char text[MAXLENGTH + 1];
	int text_length;

	printf("Please enter a phrase (max.%d characters):\n", MAXLENGTH);
	fgets(text, MAXLENGTH, stdin);

	// If we have a newline here, we know that we are ok.
	// Otherwise, we need to flush(strdin)
	if (strchr(text, '\n') == NULL)
	{
		int c;
		do
		{
			c = getchar();
		} while (c != '\n' && c != EOF);
	}

	// Or we can use strlen
	text_length = 0;
	while (text[text_length] != '\0')
	{
		text_length++;
	}
	printf("A) phrase length: %d characters.\n", text_length);

	int eCounter = 0;
	for (int i = 0; text[i]; i++)
	{
		if (text[i] == 'e')
		{
			eCounter++;
		}
	}
	printf("B) phrase contains %d \'e\'.\n", eCounter);

	// C) Display inverted phrase 
	for (int i = text_length - 1; i >= 0; i--)
	{
		printf("%c", text[i]);
	}
	putchar('\n');

	// D) Invert phrase
	for (int i = 0, j = text_length - 1; i < j; i++, j--)
	{
		// Swap
		int temp = text[i];
		text[i] = text[j];
		text[j] = temp;
	}
	printf("%s\n", text);

	return 0;
}
```

### `1242.1_08.03_ArraysAndStructures - Exercice 4`
```c
#include <stdio.h>
#include <string.h>

#define MAX_SIZE 128

int main(void)
{
	char text[MAX_SIZE];

	printf("text (max.%d) : ", MAX_SIZE);
	fgets(text, MAX_SIZE, stdin);
	printf("%s", text);

	// If we have a newline here, we know that we are ok.
	// Otherwise, we need to flush(strdin)
	if (strchr(text, '\n') == NULL)
	{
		int c;
		do
		{
			c = getchar();
		} while (c != '\n' && c != EOF);
	}

	for (int i = 0, j = 0; i < strlen(text) + 1; i++)
	{
		if (text[i] != ' ')
		{
			text[j] = text[i];
			j++;
		}
	}

	puts(text);

	return 0;
}
```

### `1242.1_08.03_ArraysAndStructures - Exercice 5`
```c
#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 128

int main(void)
{
	char text[MAX_SIZE];
	int i = 0;
	bool is_negative = false;

	printf("text (max.%d) : ", MAX_SIZE);
	fgets(text, MAX_SIZE, stdin);
	printf("%s", text);

	// If we have a newline here, we know that we are ok.
	// Otherwise, we need to flush(strdin)
	if (strchr(text, '\n') == NULL)
	{
		int c;
		do
		{
			c = getchar();
		} while (c != '\n' && c != EOF);
	}

	while ((text[i] < '0' || text[i]>'9') &&
		text[i] != '\0' &&              
		text[i] != '-')               
	{
		i++;
	}

	is_negative = (text[i] == '-');
	if (is_negative)
	{
		i++;
	}

	long value = 0;
	while ((text[i] >= '0') && (text[i] <= '9'))
	{
		value *= 10;  
		value += text[i] - '0';
		i++;
	}
	if (is_negative)
	{
		value *= -1;
	}

	printf("\n\n Found value: %ld\n\n", value);

	return 0;
}
```

## Solutions série 8.4
[1242.1.08.04_TableauxStructures_Correction.pdf](/pdf/1242.1.08.04_TableauxStructures_Correction.pdf)

### `1242.1_08.04_ArraysAndStructures - Exercice 1`
```c
#include <stdio.h>

typedef struct
{
	unsigned char hh;
	unsigned char mm;
	unsigned char ss;
} Time;

void print_time(Time t)
{
	printf("%02d:%02d:%02d\n", t.hh, t.mm, t.ss);
}

Time init_time(int h, int m, int s)
{
	Time t;
	t.hh = h;
	t.mm = m;
	t.ss = s;
	return t;
}

int main(void)
{
	// Time t1 = { 0, 0, 0 };
	// Time t2 = { 0, 0, 0 };
	// t1.hh = 5;
	// t1.mm = 3;
	// t1.ss = 17;
	// print_time(t1);
	Time t2 = init_time(5, 3, 17);
	print_time(t2);

	return 0;
}
```

### `1242.1_08.04_ArraysAndStructures - Exercice 2`
```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef struct
{
	double real;
	double imaginary;
} Complex;

Complex input_complex();
Complex sum_complex(Complex a, Complex b);
Complex diff_complex(Complex a, Complex b);
void print_complex(Complex c);

void flush_stdin()
{
	{
		int c;
		do
		{
			c = getchar();
		} while (c != '\n' && c != EOF);
	}
}

int main(void)
{
	Complex c1, c2, result;
	c1 = input_complex();
	c2 = input_complex();

	result = sum_complex(c1, c2);

	printf("\nSum = ");
	print_complex(result);
	result = diff_complex(c1, c2);
	printf("\nDiff = ");
	print_complex(result);

	return 0;
}

Complex input_complex()
{
	Complex complex;
	int status;

	printf("Please enter a complex number (r,i): ");
	status = scanf("(%lf, %lf)", &complex.real, &complex.imaginary);
	flush_stdin();
	while (status != 2)
	{
		printf("Please enter a complex number (r,i): ");
		status = scanf("(%lf, %lf)", &complex.real, &complex.imaginary);
		flush_stdin();
	};

	return complex;       // Returny a COPY
}

Complex sum_complex(Complex a, Complex b)
{
	Complex c;
	c.real = a.real + b.real;
	c.imaginary = a.imaginary + b.imaginary;

	return c;
}

Complex diff_complex(Complex a, Complex b)
{
	Complex c;
	c.real = a.real - b.real;
	c.imaginary = a.imaginary - b.imaginary;

	return c;
}

void print_complex(Complex c)
{
	printf("%.2lf + %.2lfi\n", c.real, c.imaginary);
}
```

### `1242.1_08.04_ArraysAndStructures - Exercice 3`
```c
#include <stdio.h>
#include <string.h>

typedef struct
{
  char lastname[21]; // Because of the null character
  char firstname[21]; // Because of the null character
	int  birthdate;
}
Person;

int main(void)
{
	const int actual_year = 2020;

	unsigned char N = 7;
	Person tab[] =
	{
			{ "Knuth",     "Donald",     1938},
			{ "Kernighan", "Brian",      1942},
			{ "Ritchie",   "Dennis",     1941},
			{ "Thompson",  "Ken",        1943},
			{ "Minsky",    "Marvin Lee", 1927},
			{ "Dijkstra",  "Edsger",     1930},
			{ "Stroustrup","Bjarne",     1950}
	};

	// N = sizeof(tab)/sizeof(PersonTy);   // instead of have to count

	printf("%d Persons\n", N);
	printf("Persons less than 80 years old:\n");
	for (int i = 0; i < N; i++)
	{
		if (actual_year - tab[i].birthdate < 80)
		{
			printf("%s %s %d years\n", tab[i].firstname, tab[i].lastname, actual_year - tab[i].birthdate);
		}
	}

	int min_id = 0;
	int max_id = 0;
	for (int i = 1; i < N; i++)
	{
		if (strcmp(tab[i].lastname, tab[min_id].lastname) < 0)
		{
			min_id = i;
		}
		if (strcmp(tab[i].lastname, tab[max_id].lastname) > 0)
		{
			max_id = i;
		}
	}

	printf("\nAlphabetic order:\n");
	printf("The first is: %s\n", tab[min_id].lastname);
	printf("The last is: %s\n", tab[max_id].lastname);

	return 0;
}
```

## Solutions Auto-évaluations
### `ch08_ex21_ArraySum`
```c
#include <stdio.h>

// TODO: add function prototype here
void ch08_ex21_ArraySum();

#ifndef IGNORE_MAIN
int main(void)
{
  // TODO: add function calls here
  ch08_ex21_ArraySum();
}
#endif

// TODO: add function definition here
void ch08_ex21_ArraySum()
{
  int array[50];

  int status = -1;
  int n = -1;
  
  do
  {
    printf("Nb values (max.50): ");
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
    printf("Value %d? ", i);
    scanf(" %d", &array[i]);
  }

  printf("array:\n");

  int sum = 0;
  for (int i = 0; i < n; i++)
  {
    printf("%d ", array[i]);
    sum += array[i];
  }

  printf("\nTotal sum: %d\n", sum);
}
```

### `ch08_ex23_Array2DSum`
```c
#include <stdio.h>

// TODO: add function prototype here
void ch08_ex23_Array2DSum();

#ifndef IGNORE_MAIN
int main(void)
{
  // TODO: add functions calls here
  ch08_ex23_Array2DSum();

  return 0;
}
#endif

// TODO: add function definition here
void ch08_ex23_Array2DSum()
{
  int array[50][50];

  int nb_rows = -1;
  int nb_cols = -1;
  int status = -1;
  
  do
  {
    printf("Nb lines (max.50): ");
    status = scanf(" %d", &nb_rows);
    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }
  } while (status != 1 || nb_rows < 0);

  do
  {
    printf("Nb columns (max.50): ");
    status = scanf(" %d", &nb_cols);
    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }
  } while (status != 1 || nb_cols < 0);

  for (int i = 0; i < nb_rows; i++)
  {
    for (int j = 0; j < nb_cols; j++)
    {
      printf("array[%d][%d]: ", i, j);
      scanf(" %d", &array[i][j]);
    }
  }

  int sum = 0;
  for (int i = 0; i < nb_rows; i++)
  {
    for (int j = 0; j < nb_cols; j++)
    {
      sum += array[i][j];
    }
  }

  printf("Total sum: %d\n", sum);
}
```

### `ch08_ex24_DotProduct`
```c
#include <stdio.h>

// TODO: add functions prototypes here
void ch08_ex24_DotProduct(void);

#ifndef IGNORE_MAIN
int main(void)
{
  // TODO: add functions calls here
  ch08_ex24_DotProduct();
}
#endif

// TODO: add functions definitions here
void ch08_ex24_DotProduct(void)
{
    int u[50];
    int v[50];
    
    int status = -1;
    int n = -1;
  
  do
  {
    printf("Vectors dimension (max.50): ");
    status = scanf(" %d", &n);
    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }
  } while (status != 1 || n < 0);

  printf("** First vector **\n");
  for (int i = 0; i < n; i++)
  {    
    printf("Element %d: ", i);
    scanf(" %d", &u[i]);
  }

  printf("** Second vector **\n");
  for (int i = 0; i < n; i++)
  {    
    printf("Element %d: ", i);
    scanf(" %d", &v[i]);
  }

  int dot_product = 0;
  for (int i = 0; i < n; i++)
  {
    dot_product += u[i] * v[i];
  }

  printf("Dot product: %d\n", dot_product);
}
```

### `ch08_ex41_Time`
```c
#include <stdio.h>

// TODO: define the Time structure
typedef struct
{
  int hours;
  int minutes;
  int seconds;
} Time;

// TODO: add functions prototypes here
 Time ch08_ex41_InitTime(int hours, int minutes, int seconds);
 void ch08_ex41_PrintTime(Time t);
 void ch08_ex41_Time();

#ifndef IGNORE_MAIN
int main(void)
{
  // TODO: add functions calls here
  ch08_ex41_Time();
}
#endif

// TODO: add functions definitions here
Time ch08_ex41_InitTime(int hours, int minutes, int seconds)
{
  Time t;
  t.hours = hours;
  t.minutes = minutes;
  t.seconds = seconds;
  return t;
}

void ch08_ex41_PrintTime(Time t)
{
  printf("%02d:%02d:%02d\n", t.hours, t.minutes, t.seconds);
}

void ch08_ex41_Time()
{
  Time t = ch08_ex41_InitTime(5, 3, 17);
  ch08_ex41_PrintTime(t);
}
```

### `ch08_ex42_Complex`
```c
#include <stdio.h>

// TODO: add Complex structure definition here
typedef struct
{
  double real;
  double imaginary;
} Complex;

// TODO: add functions prototypes here
Complex ch08_ex42_InputComplex();
Complex ch08_ex42_SumComplex(Complex a, Complex b);
Complex ch08_ex42_DiffComplex(Complex a, Complex b);
Complex ch08_ex42_PrintComplex(Complex c);
void ch08_ex42_Complex();

#ifndef IGNORE_MAIN
int main(void)
{
  // TODO: add functions calls here
  ch08_ex42_Complex();

  return 0;
}
#endif

// TODO: add functions definitions here
Complex ch08_ex42_InputComplex()
{ 
  double real = 0.0;
  double imaginary = 0.0;
  int status = -1;

  do
  {
    printf("Please enter a complex number (r,i): ");
    status = scanf("(%lf,%lf)", &real, &imaginary); 
    {
      int c;
      do
      {
        c = getchar();
      } while (c != '\n' && c != EOF);
    }
  } while (status != 2);

  Complex c;
  c.real = real;
  c.imaginary = imaginary;
  return c;
}

Complex ch08_ex42_SumComplex(Complex a, Complex b)
{
  Complex c;
  c.real = a.real + b.real;
  c.imaginary = a.imaginary + b.imaginary;
  return c;
}

Complex ch08_ex42_DiffComplex(Complex a, Complex b)
{
  Complex c;
  c.real = a.real - b.real;
  c.imaginary = a.imaginary - b.imaginary;
  return c;
}

Complex ch08_ex42_PrintComplex(Complex c)
{
  printf("%.2lf + %.2lfi\n", c.real, c.imaginary);
  return c;
}

void ch08_ex42_Complex()
{
  Complex a = ch08_ex42_InputComplex();
  Complex b = ch08_ex42_InputComplex();
  Complex c = ch08_ex42_SumComplex(a, b);
  Complex d = ch08_ex42_DiffComplex(a, b);
  printf("\nSum = ");
  ch08_ex42_PrintComplex(c);
  printf("\nDiff = ");
  ch08_ex42_PrintComplex(d);
}
```

### `ch08_ex43_Person`
```c
#include <stdio.h>
#include <string.h>

// TODO: add the Person structure definition here
typedef struct
{
  char lastname[20];
  char firstname[20];
  int birthyear;
} Person;

// TODO: add functions prototypes here
void ch08_ex43_Person();

#ifndef IGNORE_MAIN
int main(void)
{
	// TODO: add functions calls here
  ch08_ex43_Person();

  return 0;
}
#endif

// TODO: add functions definitions here
void ch08_ex43_Person()
{
  Person persons[10] = 
  {
    {"Knuth", "Donald", 1938},
    {"Kernighan", "Brian", 1942},
    {"Ritchie", "Dennis", 1941},
    {"Thompson", "Ken", 1943},
    {"Minsky", "Marvin", 1927},
    {"Dijkstra", "Edsger", 1930},
    {"Stroustrup", "Bjarne", 1950}
  };

  printf("7 Persons\n");
  printf("Persons less than 80 years old:\n");
  for (int i = 0; i < 7; i++)
  {
    int age = 2020 - persons[i].birthyear;
    if (age < 80)
    {
      printf("%s %s %d years\n",  persons[i].firstname, persons[i].lastname, age);
    }
  }

  printf("\nAlphabetic order:\n");

  char first[100] = "ZZZZ";
  char last[100] = "AAAA";
  for (int i = 0; i < 7; i++)
  {
    int cmp = strcmp(persons[i].lastname, first);
    if (cmp < 0)
    {
      strcpy(first, persons[i].lastname);
    }

    cmp = strcmp(persons[i].lastname, last);
    if (cmp > 0)
    {
      strcpy(last, persons[i].lastname);
    }    
  }
  
  printf("The first is: %s\n", first);
  printf("The last is: %s\n", last);
}
```
