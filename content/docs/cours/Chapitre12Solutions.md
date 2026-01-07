---
title: "Chapitre 12 : solutions"
draft: false
weight: 31
---
# Chapitre 12 : solutions

## Exemples
### `01_Structure`
```c
#include <stdio.h>
#include <string.h>

struct patient_file
{
  char name[25];
  int age;
  float height, weight;
};

int main(void)
{
  struct patient_file patient_a = {"Dupont", 25, 180.0f, 85.0f};
  struct patient_file patient_b;

  printf("patient_a.name: %s\n", patient_a.name);

  patient_b = patient_a;
  printf("patient_a.name: %s\n", patient_a.name);

  strcpy(patient_a.name, "Toto");
  printf("patient_a.name: %s\n", patient_a.name);
  printf("patient_b.name: %s\n", patient_b.name);

  // ERROR: we should use strcpy here
  // clientA.nom = clientB.nom;
  patient_a.age = 2 * patient_b.age;

  return 0;
}
```

### `02_StructureReturn`
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct patient_file
{
  char nom[25];
  int age;
  float taille, poids;
};

// 2 functions returning an address to a structure:
struct patient_file *function1();
struct patient_file *function2();

int main(void)
{
  struct patient_file patient_a = {"Dupont", 25, 180.0f, 85.0f};
  struct patient_file *ptr_patient_b;

  ptr_patient_b = function1();
  printf("%s\n", ptr_patient_b->nom);

  ptr_patient_b = function2();
  printf("%s\n", ptr_patient_b->nom);

  // int a,b=12,c[100]={1,1,1,1,1,1};    // to force having new variables in the stack
  printf("%s\n", ptr_patient_b->nom);

  return 0;
}

struct patient_file *function1()
{
  struct patient_file *ptr;
  ptr = malloc(sizeof(struct patient_file));
  strcpy(ptr->nom, "maFonction");

  // CORRECT: returns a pointer to a variable dynamically allocated
  //    => so it stays in memory after we returned
  return ptr;
}

struct patient_file *function2()
{
  struct patient_file patient = {"Dupont", 25, 180.0f, 85.0f};
  struct patient_file *ptr;
  ptr = &patient;
  printf("%s\n", ptr->nom);

  // WRONG: returns a pointer to a variable automatically allocated
  //    => the variable is deleted just after we returned
  //    => we have a pointer pointing to some meaningless memory now!
  // VS: warning C4172: returning address of local variable or temporary: client
  // return &patient;
  // GCC: will not warn even when using options "-Wall -Wextra".
  //  But it will when using optimization with option "-O2"
  // => Strange behavior to say the least.
  return ptr;
}
```

### `03_BitFields`
```c
#include <stdio.h>

// Structure of bitfields (43 bits)
// So 6 bytes in total normally!
// But data are aligned onto 4 bytes so total size is 8 bytes.
struct bitfield
{
  int i : 3;
  int j : 10;
  int k : 30;
};

// Test alignment
struct bitfieldshort
{
  int i : 1;
  int j : 1;
  int k : 1;
};

int main(void)
{
  struct bitfield bf;
  bf.i = 8; // In binary: 1000
            // But we only reserved 3 bits!
            // The additional bit is discarded.
  bf.j = 2;
  bf.k = 3;

  printf("sizeof(bf) : %d\n", (int)sizeof(bf));
  printf("sizeof(struct bitfield) : %d\n", (int)sizeof(struct bitfield));
  printf("bf.i = %d\n", bf.i);
  printf("bf.j = %d\n", bf.j);
  printf("bf.k = %d\n", bf.k);

  printf("sizeof(bitfieldshort) : %d\n", (int)sizeof(struct bitfieldshort));

  return 0;
}
```

### `04_Union`
```c
#include <stdio.h>

union Union1
{
	int i;
	float f;
};

union Union2
{
	short s;
	char c[2];
};

union Union3
{
	int integer;
	char n[4];
};

int main(void)
{
	union Union1 u;
	u.f = 1.2;

	printf("u.f = %f\n", u.f);
	printf("u.i (Hex.) = %x\n", u.i);
	printf("u.i (Dec.) = %d\n\n", u.i);

	union Union2 u2;
	u2.s = 64;
	printf("u2.s = %d, u2.c[0] = %d, u2.c[1] = %d\n", u2.s, u2.c[0], u2.c[1]);

	u2.c[0] = 'A';
	u2.c[1] = 'B';
	printf("u2.s = %d, u2.c[0] = %d, u2.c[1] = %d\n", u2.s, u2.c[0], u2.c[1]);

	union Union3 u3;
	u3.integer = 0x04030201;
	printf("\n\nu3.integer = %x\n", u3.integer);
	printf("u3.n[0], u3.n[1], u3.n[2], u3.n[3] = %d, %d, %d, %d\n", u3.n[0], u3.n[1], u3.n[2], u3.n[3]);

	printf("\nAddresses:\n");
	printf("\n\n&u3.integer = %p\n", &u3.integer);
	printf("&u3.n[0], &u3.n[1], &u3.n[2], &u3.n[3] = %p, %p, %p, %p\n", &u3.n[0], &u3.n[1], &u3.n[2], &u3.n[3]);

	return 0;
}
```

## Solutions
[1242.1.12_StructuresEtType_Correction.pdf](/pdf/1242.1.12_StructuresEtType_Correction.pdf)

### `Exercice1`
```c
//
// Author: OHU
// Date: 2014
#include <stdio.h>

// NOTE: keep French to stick to exercice.

// Il faut rendre le nouveau type "struct essai" visible dans tout le code
// pour cela on le met ici au debut du code source HORS des fonctions (port�e globale)
struct essai
{
	int n;
	float x;
};

// prototypes des fonctions
void Afficher(struct essai);
void RAZ(struct essai *);  // on doit avoir l'adresse (un pointeur sur) l'argument pour modifier son contenu

int main(void)
{
	struct essai maVariable;    // declaration d'une VARIABLE maVariable  de type     struct essai
	maVariable.n = 13;
	maVariable.x = -8.99;

	Afficher(maVariable);
	RAZ(&maVariable);
	Afficher(maVariable);

	return 0;
}

void Afficher(struct essai toto)
{
	printf("champ n: %d\n", toto.n);   // toto est une variable, avec l'operateur .  on accede a son champ n
	printf("champ x: %f\n", toto.x);
}

void RAZ(struct essai *ptrToto)        // on doit avoir l'adresse (un pointeur sur l'argument) pour modifier son contenu
{
	ptrToto->n = 0;     // on accede au champ de la variable pointee par ptrToto avec l'operateur d'indirection  ->
	ptrToto->x = 0.0;
	(*ptrToto).x = 0.0;   // est aussi correct
}
```

### `Exercice2`
```c
#include <stdio.h>

// NOTE: keep French and coding style to stick to exercices

// On définit ici le type "struct Personne" pour le type "struct Famille"
struct Personne
{
	char *prenom; // plus flexible que char prenom[32] par exemple
	unsigned short  age;
};

struct Famille
{
	char *nom;
	struct Personne pere;
	struct Personne mere;
	struct Personne fils;
	struct Personne fille;
};

// prototypes des fonctions
void affichageAgeTotal(struct Famille);
void unAnDePlus(struct Famille *);

int main(void)
{
	// déclaration et initialisation d'une VARIABLE de type struct Famille
	struct Famille uneFamille =
	{
			"Dupont",     	//champ nom de la Famille
			{"Jean", 38}, 	//champ pere (struct imbriquée --> accolade imbriquée)
			{"Eva",  36}, 	//champ mere
			{"Emma", 8},
			{"Kevin",4}
	};

	affichageAgeTotal(uneFamille); 	//appel avec la variable en argument
	unAnDePlus(&uneFamille);       	//appel avec l'adresse de uneFamille
	affichageAgeTotal(uneFamille);

	printf("La famille %s ", uneFamille.nom);
	printf("occupe %d octets\n", sizeof(uneFamille));

	return 0;
}
/* la structure passee en argument par main() est copiee. Si la
	 structure est grande, il est plus rapide de passer son adresse */
void affichageAgeTotal(struct Famille copie)
{
	int ageTotal = copie.pere.age + copie.mere.age +
		copie.fils.age + copie.fille.age;
	printf("L'age total de la famille %s est de %d ans\n", copie.nom, ageTotal);
}

// on doit avoir l'adresse (un pointeur sur) l'argument pour modifier son contenu
void unAnDePlus(struct Famille *ptrSurFamille)
{
	// puisque l'on a un pointeur, il faut employer l'opérateur ->

	ptrSurFamille->pere.age++;    // ou (*ptrSurFamille).pere.age++;
	ptrSurFamille->mere.age++;    // ou (*ptrSurFamille).mere.age++;
	ptrSurFamille->fils.age++;    // ou ...
	ptrSurFamille->fille.age++;
}
```

### `Exercice3`
```c
#include <stdio.h>

// NOTE: keep French to keep to exercice.

typedef struct
{
	float reelle;
	float imaginaire;
} ComplexeTy;

// Prototypes des fonctions
ComplexeTy saisie(void);
ComplexeTy somme_complexe(ComplexeTy a, ComplexeTy b);
ComplexeTy difference_complexe(ComplexeTy a, ComplexeTy b);
void affiche_complexe(ComplexeTy c);

int main(void)
{
	ComplexeTy c1, c2, resultat;
	c1 = saisie();
	c2 = saisie();

	resultat = somme_complexe(c1, c2);

	printf("\nSomme des deux nombres      : ");
	affiche_complexe(resultat);
	resultat = difference_complexe(c1, c2);
	printf("\nDifference des deux nombres : ");
	affiche_complexe(resultat);

	return 0;
}

ComplexeTy saisie(void)
{
	int status = 0;
	const int nbExpectedValues = 2;
	ComplexeTy nouveau;
	do
	{
		printf("Donner la valeur d'un nombre complexe (r,i): ");
		status = scanf("(%f,%f)", &nouveau.reelle, &nouveau.imaginaire);

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

	return nouveau;       // COPIE de la variable renvoyée au main
}

ComplexeTy somme_complexe(ComplexeTy a, ComplexeTy b)
{
	ComplexeTy c;

	c.reelle = a.reelle + b.reelle;
	c.imaginaire = a.imaginaire + b.imaginaire;

	return c;
}

ComplexeTy difference_complexe(ComplexeTy a, ComplexeTy b)
{
	ComplexeTy c;

	c.reelle = a.reelle - b.reelle;
	c.imaginaire = a.imaginaire - b.imaginaire;

	return c;
}

void affiche_complexe(ComplexeTy c)
{
	printf("(%f,%f)\n", c.reelle, c.imaginaire);
}
```
