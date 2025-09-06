---
title: "3 - Opérateurs"
weight: 1
---

# CHAPITRE 3 : opérateurs
## Cours
[1242.1.03_Operateurs.pdf](/pdf/1242.1.03_Operateurs.pdf)

## Squelette à remplir

```c
#include <stdio.h>

// CHAPTER 3

int main(void)
{
	// Experiment with modulo

	// Experiment with arithmetic operators

	// Experiment with overflow

	// Experiment with division operator

	// Conversions

	// Increment / Decrement operators

	// Experiment with comma operator

	// Experiment with logical operators

	// Experiment with bitwise operators

	// Experiment with bit shifts

	return 0;
}
```

## Quiz
[QUIZ SUR LES OPÉRATEURS (PARTIE 1, ~5')](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=761424)

[QUIZ SUR LES OPÉRATEURS (PARTIE 2, ~15')](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=761427)

# EXERCICES

## Exercice 1 : assignation / affectation
A) Réécrire les instructions suivantes en utilisant des opérateurs d'affectation composés.

```c
memory = memory + 1;	
word = word * 8;	
currency = currency - 1;	
a = a % b;	
part = part / nb_persons;	
```

B) Quelle sont les valeurs des variables **`x`**, **`y`** et **`z`** ?

```c
int x = 10;
int y, z;
x *= y = z = 4;
```

## Exercice 2 : opérateurs arithmétiques

A) Addition et division : quelle est la valeur de la variable **`x`** ?

```c
int n = 5, p = 9;
float x;

x = p / n ;	
x = (float) p / n ;	
x = (p + 0.5) / n ;	
x = (int) (p + 0.5) / n ; 	
```

B) Modulo : quelle est la valeur de la variable **`a`** ?

```c
int a;
a = 10 % 10; 
a =  5 % 10; 
a = 10 %  0; 
a =  0 % 10; 
```

## Exercice 3 : opérateurs d’incrémentation

Quelles sont les valeurs des variables **`x`**, **`y`** et **`z`** ?

```c
int x = 2, y = 1, z = 3;
z += -x++ + ++y;
```

## Exercice 4 : opérateurs de comparaison et logique
A) Evaluer les expressions suivantes :

**`3 <= 2-1`**

**`3 * (4 > 4) + 2.5`**

**`(4 == 5.1) / 2 + 1`**

**`true && false || true`**

**`3 + (n > n - 1)`**

**`!true && false || !false`**

B) Assigner à une variable booléenne b. La valeur est vraie si la variable **`x`** est comprise strictement entre 5 et 10, fausse sinon.

{{<katex>}}
b =
\begin{cases}
vrai  & \quad \text{si $x \in [5..10]$}\\ 
faux  & \quad \text{sinon}
\end{cases}
{{</katex>}}

C) Assignez à une variable booléenne b. La valeur est vraie si la variable x n’est pas comprise strictement entre 5 et 10, fausse sinon.

{{<katex>}}
b =
\begin{cases}
vrai  & \quad \text{si $x \notin [5..10]$}\\ 
faux  & \quad \text{sinon}
\end{cases}
{{</katex>}}

## Exercice 5 : divers opérateurs

A) Que vaut **`q`** :

```c
int n = 5, p = 9;
int q;
float x;
q = n < p ;	/* 1 */
q = n == p ;	/* 2 */
q = p % n + (p > n) ;	/* 3 */
```

B) Quels résultats fournit le programme suivant :

```c
int n = 10, p = 5, q = 10, r ;
r = n == (p = q) ;
n = p = q = 5;
n += p += q ;
```

C) Donner les résultats des calculs suivants et en préciser le type :

a) **`3.5 * 6`**

b) **`243 * -83`**

c) **`(int)(20.35 * 24)`**

d) **`(int)85.35 * 2`**

e) **`'w' - 2024`**

f) **`(char)(23 / 9)`**

D) Quel doit être le type de **`var`** pour que les affectations suivantes ne provoquent pas d'erreur d'arrondi :

a) **`var = 12 + 'g';`**

b) **`var = (1 < 3);`**

c) **`var = 13 - 274.3;`**

d) **`var += 2.5;`**

e) **`var = 255 + 1;`**

f) **`var = 2 / 7.;`**

E) Donner la valeur de la variable **`x`** (de type **`int`**) après chaque instruction de la séquence de programme suivante (pour chaque instruction, la valeur de **`x`** est celle calculée à l'instruction précédente).
Indiquer également s'il y a des comportements indéfinis (UB) :

```c
x = 2;
x = 3 + (3 > x);
x += x -= 2;
x = (++x - 6) * 3;
x *= (5 > x) * (3 + 23);
```

F) Dans les expressions suivantes, repérer les parenthèses inutiles.

a) **`a = (x * w) + 3;`**

b) **`f *= 15 - (3 + f);`**

c) **`g = (g++ + g) * 3;`**

d) **`m = k > (b || 1);`**

e) **`h = (n += 12);`**

f) **`b *= (20 + 3);`**

## Exercice 6 : opérateurs bit à bit

A) Écrire un programme qui met i) les deux bits de poids forts à 1 et ii) les deux bits de poids faible à 0.

**Exemple :**
 
```c
unsigned char x = 0xAA; // 1010 1010
```
devient **11**1010**00**

B) Écrire un programme qui affiche le contenu des bits 3, 4 et 5 de la variable **`x`**. 10**011**010 doit afficher 3.
 
C) Soit la déclaration de variable suivante :

```c
unsigned int x=0x03020100;
```

Écrire un programme qui décompose la variable **`x`** en 4 variables **`b0`**, **`b1`**, **`b2`**, **`b3`** contenant les 4 bytes de **`x`**.

## [AVANCÉ] Exercice 7 : débordement

A) Décrire ce qui se passe lorsque la valeur d'une variable dépasse sa valeur maximale admise dans le programme suivant :

```c
printf("INT_MAX: %d  INT_MAX+1: %d\n", INT_MAX,INT_MAX+1);
printf("DBL_MAX: %g\n",      DBL_MAX);
printf("DBL_MAX+1000: %g\n", DBL_MAX+1000);
printf("DBL_MAX*2   : %g\n", DBL_MAX*2);

printf("q = 1/0: %f  \n", 1/0);
float q  =  1.0f/0;
printf("q = 1.0f/0: %f  \n", q);
printf("1/q       : %f  \n", 1/q);
printf("q/q       : %f  \n", q/q);

printf("sqrt(-1)  : %f  \n", sqrt(-1));
```
