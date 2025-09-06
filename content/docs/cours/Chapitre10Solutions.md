---
title: "Chapitre 10 : solutions"
draft: false
weight: 31
---
# Chapitre 10 : solutions

## Exemples
### 01_ReadSentencesStaticMemory
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXSIZE 500 // Maximum allowed characters

int main(void)
{
  char buffer[MAXSIZE + 1];
  char *text[10];
  int i;
  long size = 0;

  printf("Please enter 10 sentences:\n\n");
  for (i = 0; i < 10; i++)
  {
    printf("%d : ", i + 1);
    fgets(buffer, MAXSIZE, stdin); // gets_s not always supported

    int nb_bytes = strlen(buffer);
    text[i] = (char *)malloc(nb_bytes + 1); // To hold \0 character

    // In case there is not enough memory, etc.
    if (text[i] == NULL)
    {
      printf("ERROR: not enough memory!\n");
      exit(-1);
    }

    strcpy(text[i], buffer); // copy sentence at the address returned by malloc
    size += nb_bytes;
  }

  printf("Print the 10 sentences:\n\n");
  for (i = 0; i < 10; i++)
  {
    printf("%s\n", text[i]);
  }

  printf("Total memory to store the sentences: %ld bytes intead of %d\n\n", size, 10 * MAXSIZE);

  return 0;
}
```

### `02_Malloc`
```c
#include <stdio.h>
#include <stdlib.h>

// Allocate memory in a loop
// WARNING: may crash your computer (or make it crawl)
int main(void)
{
	long total = 0;
	char *ptr = NULL;

	while (1)
	{
		ptr = malloc(1 * 1024 * 1024);

		if (ptr == NULL)
		{
			printf("\n\nNOT ENOUGH MEMORY!\n\n");
			return -1;
		}
		total += 1;
		printf("Allocate 1MB characters. Total memory = %ld MB\n", total);
	}

	printf("\nmain -> Done!");

	return 0;
}
```

### `03_2DArray_NoPointer`
```c
#include <stdio.h>
#include <string.h>

#define L 2
#define C 3
int main(void)
{
	int m[L][C] = { { 0, 1, 2},
								 {10,11,12}, };

	printf(" 0  1  2\n10 11 12\n\n");

	int l = 0, c;

	for (; l < L; l++)
	{
		for (c = 0; c < C; c++)
		{
			printf("m[%d][%d]    = %2d  a l'adresse %x (%ld) \n", l, c, m[l][c], &m[l][c], &m[l][c]);
		}
	}

	return 0;
}
```

### `04_2DArray`
```c
#include <stdio.h>
#include <string.h>

#define L 2
#define C 3
int main(void)
{
	int m[L][C] = { { 0, 1, 2},
								 {10,11,12},
	};

	int* ptr;
	int i, l, c;
	ptr = (int*)m;

	printf("m    = 0x%X &m    = 0x%X \n\n", m, &m);
	printf("m[0] = 0x%X &m[0] = 0x%X \n\n", m[0], &m[0]);
	printf("m[1] = 0x%X &m[1] = 0x%X \n\n", m[1], &m[1]);
	printf("m[0][0] = 0x%X &m[0][0] = 0x%X \n\n", m[0][0], &m[0][0]);

	printf("m = %p &m= %p \n\n", m, &m);

	l = c = 0;
	for (i = 0; i < L * C; i++)
	{
		printf("m[%d]=0x%X, &m[%d][%d]=0x%X (ptr+%d)=%X: *(ptr+%d) = %d\n", l, m[l], l, c, &m[l][c], i, (ptr + i), i, *(ptr + i));
		c++;
		if (c >= C)
		{
			c = 0;
			l++;
			printf("\n");
		}
	}
	printf("\n\n");

	return 0;
}
```

### `05_2DArray_Pointers_Equivalence`
```c
#include <stdio.h>
#include <string.h>

#define ROWS 2
#define COLUMNS 3

int main(void)
{
	int m[ROWS][COLUMNS] =
		{
			{0, 1, 2},
			{10, 11, 12}};

  // m is of type int (*)[3] => pointer to array of 3 ints
  printf("%d\n", m[1][2] + 3);
  printf("%d\n", (*(m + 1))[2] + 3);
  printf("%d\n", *(m[1] + 2) + 3);
  printf("%d\n", *(*(m + 1) + 2) + 3);

	return 0;
}
```

### `06_DynamicMatrix`
```c
#include <stdio.h>
#include <stdlib.h>

#define ROWS 3
#define COLUMNS 5

int main(void)
{
	int **matrix;
	int i, j;

	// Reserve an array with 3 pointers (one for each row)
	matrix = (int **)malloc(sizeof(int *) * ROWS);
	if (matrix == NULL) exit(-1);

	// Reserve 5 columns per row
	for (i = 0; i < ROWS; i++)
	{
		matrix[i] = (int *)malloc(sizeof(int) * COLUMNS);
		if (matrix[i] == NULL) exit(-1);
	}

	// Initialize elements
	for (i = 0; i < ROWS; i++)
	{
		for (j = 0; j < COLUMNS; j++)
		{
			matrix[i][j] = (i + 1) + j;
		}
	}

	printf("%p\n", matrix);
	printf("%p\n", matrix + 1);

	printf("%p\n", matrix[2]);
	printf("%p\n", matrix[2] + 1);

	// Print matrix
	for (i = 0; i < ROWS; i++)
	{
		for (j = 0; j < COLUMNS; j++)
		{
			printf("%d\t", matrix[i][j]);
		}
		printf("\n");
	}

	// Free memory
	for (i = 0; i < ROWS; i++)
	{
		free(matrix[i]);
	}
	free(matrix);
	matrix = NULL;

	return 0;
}
```

### `07_Parabole`
```c
#include <stdio.h>

#define NMAX 21

void ComputeParabole();
void PrintParabole();

float par[NMAX];

int main(void)
{
	ComputeParabole();
	PrintParabole();

	return 0;
}

void ComputeParabole()
{
	int n;
	float x = -7;
	for (n = 0; n < NMAX; ++n)
	{
		par[n] = x * x;
		x += 0.7;
	}
}

void PrintParabole()
{
	int n;
	int Y;
	char title[] = "Parabole :";
	char space[80];
	for (n = 0; n < 80; ++n) space[n] = ' ';
	space[79] = 0;
	printf("%s\n", title);
	for (n = 0; n < NMAX; ++n)
	{
		Y = par[n];
		space[Y] = 'X';
		puts(space);
		space[Y] = ' ';
	}
}
```

### `08_UnallocatedString`
```c
#include <stdio.h>

int main(void)
{
	// WRONG: storage for string is not allocated.
	// char *myString = "Hello World";

	// OK: storage is allocated (100 chars)
	char myString[100] = "Hello World";

	printf("%s\n", myString);
	scanf("%s", myString);
	printf("%s\n", myString);

	return 0;
}
```

## Solutions
[1242.1.10_AllocationDynamique_Correction.pdf](/pdf/1242.1.10_AllocationDynamique_Correction.pdf)

### `Exercice1`
```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	long int size;
	int nbloc = 0;
	char *address = NULL;
	printf("Enter block size (in MB): ");
	scanf("%ld", &size);
	do
	{
		address = malloc(size * 1024 * 1024);
		if (address != NULL)
		{
			printf("Allocating block number %d, %d[MB]\n", nbloc, nbloc * size);
			nbloc++;
		}
	} while (address != NULL);

	printf("Not enough memory\n");
	double allocatedMemoryInGByte = nbloc * size / 1024;
	printf("Total allocated memory: %0.2f [Gigabytes]\n", allocatedMemoryInGByte);

	return 0;
}
```

### `Exercice2`
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void print_array_as_array(int *values, int array_size)
{
	printf("==========  Printing array as array\n");
	for (int i = 0; i < array_size; ++i)
	{
		printf("%p => %d\n", &values[i], values[i]);
	}
}

void print_array_as_pointer(int *values, int arraySize)
{
	printf("==========  Printing array as pointer\n");
	for (int i = 0; i < arraySize; ++i)
	{
		printf("%p => %d\n", values + i, *(values + i));
	}
}

void print_array_as_incremented_pointer(int *values, int arraySize)
{
	printf("==========  Printing array as incremented pointer\n");
	for (int i = 0; i < arraySize; ++i)
	{
		printf("%p => %d\n", values, *values);
		// NOTE: Arguments evaluation order is undetermined
		++values;
	}
}

void print_array_as_char_pointer(int *values, int arraySize)
{
	printf("==========  Printing array as char pointers\n");
	for (int i = 0; i < arraySize; ++i)
	{
		char *firstChar = (char *)values;
		printf("%p => %c %c %c %c\n", values, *firstChar, *(firstChar + 1), *(firstChar + 2), *(firstChar + 3));
		// NOTE: Arguments evaluation order is undetermined
		++values;
	}
}

int main(void)
{
	// Handling User input errors:
	// 1) Print what is expected
	// 2) Read input from User
	// 3) Empty the stdin buffer
	// 4) Repeat until we got what we expected
	int status = 0;
	const int nb_expected_values = 1;
	// Variables to store User input values
	int array_size;
	do
	{
		printf("Please enter a number: ");
		status = scanf("%d", &array_size);

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
		if (status != nb_expected_values)
		{
			printf("\a");
		}
	} while (status != nb_expected_values);

	int *values = malloc(array_size * sizeof(int));
	if (values == NULL)
	{
		printf("ERROR: cannot allocate memory. Exiting...\n");
		exit(1);
	}

	int min_value = 32;
	int max_value = 126;
	// Init rand() calls with current time
	srand((unsigned int)time(NULL));
	for (int i = 0; i < array_size; ++i)
	{
		// returns a value between 0 and RAND_MAX
		int new_value = rand();
		// First rescale values from [0, RAND_MAX] to [0, maxValue - minValue]
		new_value = new_value % (max_value - min_value + 1);
		// Then shift values from [0, maxValue - minValue] to [minValue, maxValue]
		new_value += min_value;

		values[i] = new_value;
	}

	print_array_as_array(values, array_size);
	print_array_as_pointer(values, array_size);
	print_array_as_incremented_pointer(values, array_size);
	print_array_as_char_pointer(values, array_size);

	free(values);

	return 0;
}
```

### `Exercice4`
```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void print_matrix_as_array(int **matrix, int M, int N)
{
	printf("==========  Printing matrix as array\n");
	for (int i = 0; i < M; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			printf("%p => %d\n", &matrix[i][j], matrix[i][j]);
		}
	}
	printf("\n");

	// Only print values in a correct way
	for (int i = 0; i < M; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			printf("%d\t", matrix[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void print_matrix_as_pointer(int **matrix, int M, int N)
{
	printf("==========  Printing matrix as pointer\n");
	for (int i = 0; i < M; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			printf("%p => %d\n", *(matrix + i) + j, *(*(matrix + i) + j));
		}
	}
	printf("\n");

	// Only print values in a correct way
	for (int i = 0; i < M; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			printf("%d\t", *(*(matrix + i) + j));
		}
		printf("\n");
	}
	printf("\n");
}

void print_matrix_as_incremented_pointer(int **matrix, int M, int N)
{
	printf("==========  Printing matrix as incremented pointer\n");
	// Store a copy because we want to reuse matrix afterwards
	int **current_row = matrix;
	for (int i = 0; i < M; ++i)
	{
		int *current_element = *current_row;
		for (int j = 0; j < N; ++j)
		{
			printf("%p => %d\n", current_element, *current_element);
			current_element++;
		}
		current_row++;
	}
	printf("\n");

	// Only print values in a correct way
	current_row = matrix;
	for (int i = 0; i < M; ++i)
	{
		int *columns = *current_row;
		for (int j = 0; j < N; ++j)
		{
			printf("%d\t", *columns);
			columns++;
		}
		printf("\n");
		current_row++;
	}
	printf("\n");
}

void print_matrix_as_char_pointers(int **matrix, int M, int N)
{
	printf("==========  Printing matrix as char pointers\n");
	// Store a copy because we want to reuse matrix afterwards
	for (int i = 0; i < M; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			char *first_char = (char *)&matrix[i][j];
			printf("%p => %c %c %c %c\n", first_char, *first_char, *(first_char + 1), *(first_char + 2), *(first_char + 3));
		}
	}
	printf("\n");
}

int main(void)
{
	// Handling User input errors:
	// 1) Print what is expected
	// 2) Read input from User
	// 3) Empty the stdin buffer
	// 4) Repeat until we got what we expected
	int status = 0;
	const int nb_expected_values = 2;
	// Variables to store User input values
	int M, N;
	do
	{
		printf("Please enter matrix dimensions (M N): ");
		status = scanf("%d %d", &M, &N);

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
		if (status != nb_expected_values || M < 1 || N < 1)
		{
			printf("\a");
		}
	} while (status != nb_expected_values || M < 1 || N < 1);
	
	int **matrix = malloc(M * sizeof(int *));
	if (matrix == NULL)
	{
		printf("ERROR: cannot allocate memory. Exiting...\n");
		exit(1);
	}

	int *row = malloc(N * sizeof(int));
	if (row == NULL)
	{
		printf("ERROR: cannot allocate memory. Exiting...\n");
		exit(1);
	}

	for (int i = 0; i < M; ++i)
	{
		int *row = malloc(N * sizeof(int));
		if (row == NULL)
		{
			printf("ERROR: cannot allocate memory. Exiting...\n");
			exit(1);
		}
		matrix[i] = row;
	}

	int min_value = 32;
	int max_value = 126;
	// Init rand() calls with current time
	srand((unsigned int)time(NULL));
	for (int i = 0; i < M; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			// returns a value between 0 and RAND_MAX
			int new_value = rand();
			// First rescale values from [0, RAND_MAX] to [0, maxValue - minValue]
			new_value = new_value % (max_value - min_value + 1);
			// Then shift values from [0, maxValue - minValue] to [minValue, maxValue]
			new_value += min_value;

			matrix[i][j] = new_value;
		}
	}

	print_matrix_as_array(matrix, M, N);
	print_matrix_as_pointer(matrix, M, N);
	print_matrix_as_incremented_pointer(matrix, M, N);
	// print_matrix_as_char_pointers(matrix, M, N);

	for (int i = 0; i < M; ++i)
	{
		free(matrix[i]);
		matrix[i] = NULL;
	}
	free(matrix);
	matrix = NULL;

	return 0;
}
```

### `Exercice5`
```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Only prints the values.
void print_tensor_as_array(int ***tensor, int K, int M, int N)
{
	printf("==========  Printing tensor as array\n");
	for (int i = 0; i < K; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			for (int k = 0; k < N; ++k)
			{
				printf("%d\t", tensor[i][j][k]);
			}
			printf("\n");
		}
		printf("\n");
	}
}

// Only prints the values.
void print_tensor_as_pointer(int ***tensor, int K, int M, int N)
{
	printf("==========  Printing tensor as pointer\n");
	for (int i = 0; i < K; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			for (int k = 0; k < N; ++k)
			{
				printf("%d\t", *(*(*(tensor + i) + j) + k));
			}
			printf("\n");
		}
		printf("\n");
	}
}

// Only prints the values.
void print_tensor_as_incremented_pointer(int ***tensor, int K, int M, int N)
{
	printf("==========  Printing tensor as incrmented pointer\n");
	int ***current_matrix = tensor;
	for (int i = 0; i < K; ++i)
	{
		int **current_row = *current_matrix;
		for (int j = 0; j < M; ++j)
		{
			int *current_element = *current_row;
			for (int k = 0; k < N; ++k)
			{
				printf("%d\t", *current_element);
				current_element++;
			}
			current_row++;
			printf("\n");
		}
		current_matrix++;
		printf("\n");
	}
}

int main(void)
{
	// Handling User input errors:
	// 1) Print what is expected
	// 2) Read input from User
	// 3) Empty the stdin buffer
	// 4) Repeat until we got what we expected
	int status = 0;
	const int nb_expected_values = 3;
	// Variables to store User input values
	int K, M, N;
	do
	{
		printf("Please enter third-order tensor dimensions (K M N): ");
		status = scanf("%d %d %d", &K, &M, &N);

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
		if (status != nb_expected_values || K < 1 || M < 1 || N < 1)
		{
			printf("\a");
		}
	} while (status != nb_expected_values || K < 1 || M < 1 || N < 1);

	// First allocate the K matrices
	int ***tensor = malloc(K * sizeof(int **));
	if (tensor == NULL)
	{
		printf("ERROR: cannot allocate memory. Exiting...\n");
		exit(1);
	}

	// Then, allocate the M rows for all K matrices
	for (int i = 0; i < K; ++i)
	{
		int **matrix = malloc(M * sizeof(int *));
		if (matrix == NULL)
		{
			printf("ERROR: cannot allocate memory. Exiting...\n");
			exit(1);
		}
		tensor[i] = matrix;
	}
	
	// Finally, allocate for all M rows in all K matrices
	for (int i = 0; i < K; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			int *row = malloc(N * sizeof(int));
			if (row == NULL)
			{
				printf("ERROR: cannot allocate memory. Exiting...\n");
				exit(1);
			}
			tensor[i][j] = row;
		}
	}

	int min_value = 32;
	int max_value = 126;
	// Init rand() calls with current time
	// NOTE: do not mix K (the first dimension of the the tensor, and k, the index to access the elements.
	srand((unsigned int)time(NULL));
	for (int i = 0; i < K; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			for (int k = 0; k < N; ++k)
			{
				// returns a value between 0 and RAND_MAX
				int new_value = rand();
				// First rescale values from [0, RAND_MAX] to [0, maxValue - minValue]
				new_value = new_value % (max_value - min_value + 1);
				// Then shift values from [0, maxValue - minValue] to [minValue, maxValue]
				new_value += min_value;

				// For debug purposes
				// newValue = i * M * N + j * N + k;

				tensor[i][j][k] = new_value;
			}
		}
	}

	print_tensor_as_array(tensor, K, M, N);
	print_tensor_as_pointer(tensor, K, M, N);
	print_tensor_as_incremented_pointer(tensor, K, M, N);

	for (int i = 0; i < K; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			free(tensor[i][j]);
			tensor[i][j] = NULL;
		}
		free(tensor[i]);
		tensor[i] = NULL;
	}
	free(tensor);
	tensor = NULL;

	return 0;
}
```

### `Exercice6`
```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFERSIZE 40 // Readable characters + 1 (for \0)
#define N 4

int main(void)
{
	char *input_buffer = malloc(BUFFERSIZE);
	char *text[N];
	char *p_help;

	// Input + dynamic allocation
	printf("Please enter %d sentences separated by newlines\n", N);
	for (int i = 0; i < N; i++)
	{
		printf("Sentence %d : ", i);
		fgets(input_buffer, BUFFERSIZE, stdin);
		// Check if we got a '\n'. If yes, remove trailing '\n'. If not, empty buffer
		if (strchr(input_buffer, '\n'))
		{
			input_buffer[strcspn(input_buffer, "\n")] = 0;
		}
		else
		{
			int c;
			do
			{
				c = getchar();
			} while (c != '\n' && c != EOF);
		}

		text[i] = malloc(strlen(input_buffer) + 1);
		if (text[i] != NULL)
			strcpy(text[i], input_buffer);
		else
		{
			printf("\aNot enough memory\n");
			exit(-1);
		}
	}
	free(input_buffer);
	input_buffer = NULL;

	puts("Printing string array:");
	for (int i = 0; i < N; i++)
	{
		printf("[%d]%s", i, text[i]);
	}
	printf("\n");

	// Swap strings
	for (int i = 0, j = N - 1; i < j; i++, j--)
	{
		p_help = text[i];
		text[i] = text[j];
		text[j] = p_help;

		// ^ is not allowed on pointers. So we cast it to an int type containing 8 bytes
		//text[i] = (char *)((long long int)text[i] ^ (long long int)text[j]);
		//text[j] = (char *)((long long int)text[j] ^ (long long int)text[i]);
		//text[i] = (char *)((long long int)text[i] ^ (long long int)text[j]);
	}

	// Print string array
	puts("Printing string array:");
	for (int i = 0; i < N; i++)
	{
		printf("[%d]%s", i, text[i]);
	}
	printf("\n");

	// Free memory
	for (int i = 0; i < N; i++)
	{
		free(text[i]);
		text[i] = NULL;
	}

	return 0;
}
```