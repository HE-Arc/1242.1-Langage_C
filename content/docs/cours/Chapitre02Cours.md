---
title: "2 - Types et variables"
weight: 1
---

# CHAPITRE 2 : types et variables

## Cours

{{< pdf src="/pdfs/1242.1.02_TypesEtVariables.pdf" >}}

## Squelette à remplir
```c
#include <stdio.h>

// CHAPTER 2

int main(void)
{
	// Experiment with identifiers.


	// Check size in bytes of most common types.
	// Example: printf("char          : %zu bits\n", 8 * sizeof(char));


	// Experiment with assignements


	// Experiment with blocks and variables


	// Write swap instructions


	// Declare constants with const keyword and #define preprocessor directives
	

	return 0;
}
```

{{< a_noter>}}
 **```%zu```** est le spécificateur de format pour des valeurs de type **```size_t```**.
{{< /a_noter>}}

## Quiz
[QUIZ TYPES ET VARIABLES (~15')](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=761388)

# EXERCICES

## Exercice 1 
Parmi les noms de variables suivants, indiquer ceux qui sont corrects :

```
nombre		Auto			Dollar$			Ligne4
17h20		ARC_EN_CIEL	RouGE7			vert/jaune
"poisson"	Pourcent		descriptiondinterface1
n			ZoRRo			arbre()			Lumière!
```

## Exercice 2
Vérifier si les déclarations de variables ci-dessous sont conformes aux règles du C.

```
{
  int a, b=2, c;
  float 4roues, Deux_Roues, tricycle;
  double PIBSuisse_;
  real  PIB_USA_en_$;
  char c;
}
```

Si ce n'est pas le cas, dire pourquoi.

## Exercice 3
Écrire la définition des variables pour un programme qui utilise les valeurs suivantes :
- la valeur de {{<katex>}}\pi{{</katex>}}
- un numéro de téléphone à 10 chiffres
- le sexe d'une personne (Homme / Femme)
- le taux de change de l'Euro en francs suisse
- le numéro du mois actuel (4 pour avril, 5 pour mai, ...)
- l'initiale de votre premier prénom
- la valeur boursière de la société Apple (>150'000'000'000 de $)
 
Justifier les choix faits.

## Exercice 4
Écrire la définition des variables pour le programme suivants :

```c
#include <stdio.h>

int main(void)
{
  // Definitions

  // Instructions
  pi = 3.14; // Not needed if we use const double pi = 3.14
  birthYear = 1963;
  month = 10;
  day = 10;
  letter = 'b';

  return 0 ;
}
```

## Exercice 5 
Représenter les nombres binaires suivants en notation décimale et hexadécimale.

{{<katex>}}01010001_{2} = {{</katex>}}
&nbsp;

{{<katex>}}00011110_{2} = {{</katex>}}

{{<katex>}}00111100_{2} = {{</katex>}}
&nbsp;

{{<katex>}}01111000_{2} = {{</katex>}}
&nbsp;

## Exercice 6
Représenter les nombres décimaux suivants en notation binaire et hexadécimale.

{{<katex>}}33_{10} = {{</katex>}}
&nbsp;

{{<katex>}}255_{10} = {{</katex>}}
&nbsp;

{{<katex>}}101_{10} = {{</katex>}}
&nbsp;

## Exercice 7
En représentation binaire, comment savoir si un nombre est pair ou impair ?

## Exercice 8  
Combien de valeurs peut-on dénombrer avec des mots de 8, 16, 32 et 64 bits ?

## Exercice 9
Soient 3 octets arrivant sur un bus de 8 bits, quel est leur code ascii associé et quel est le mot formé ? (exercice avec calculatrice et table ascii)

{{<katex>}}00111010_{2} = {{</katex>}}
&nbsp;

{{<katex>}}00101101_{2} = {{</katex>}}
&nbsp;

{{<katex>}}00101001_{2} = {{</katex>}}
&nbsp;

## Exercice 10
Soient 3 nombres hexadécimaux, quel est leur code ascii associé et quel est le mot formé ? (avec calculatrice)

{{<katex>}}31_{16}{{</katex>}}
&nbsp;

{{<katex>}}32_{16}{{</katex>}}
&nbsp;

{{<katex>}}32_{16}{{</katex>}}
&nbsp;

## Exercice 11

Compléter le programme suivant pour qu’il échange le contenu des variables {{<katex>}}variable1{{</katex>}} et {{<katex>}}variable2{{</katex>}}.

```c
#include <stdio.h>

int main(void)
{
  int variable1 = 10;
  int variable2 = 5;

  // Before swapping the variables content
  printf("Variable 1: %d \n", variable1); // Variable 1: 10
  printf("Variable 2: %d \n", variable2); // Variable 2: 5

  // Swap variables content

  ...

  // After swapping the variables content
  printf("Variable 1: %d \n", variable1); // Variable 1: 5
  printf("Variable 2: %d \n", variable2); // Variable 2: 10
}
```

{{< notion_avancee >}}
## Exercice 12
Écrire le code permettant d’échanger les valeurs contenues dans les deux variables a et b sans utiliser d’autre variable.
{{< /notion_avancee >}}

{{< notion_avancee >}}
## Exercice 13
Quelle est la valeur du nombre de type **`float`** dans la variable **`chouia`** dont le contenu mémoire est représenté ci-dessous ?

```c
float chouia    /* = ??? */    ;
```
{{< /notion_avancee >}}

{{< figure src="/images/chouia.png#center" >}}

## Exercice 21
Écrire un programme C qui convertit une température saisie par l’utilisateur en 
degrés Celsius, en degrés Fahrenheit et l’affiche :

```
Enter a temperature in Celsius: 12
12 degres Celsius correspond to a 53.6 degres Fahrenheit
```

Indication : {{<katex>}} T_F = 32 + 1.8*T_C {{</katex>}}

## Exercice 22
Écrire un programme C qui effectue un calcul d'intérêts et de capital pour un compte en banque.
Il demande à l'utilisateur d'introduire:
- Le capital initial sur le compte (francs et centimes)
- Le taux d'intérêt (annuel) du compte en pourcent
- La durée du dépôt (on ne peut retirer l'argent qu'au terme d'une année complète)
puis il calculera le montant disponible lors du retrait et l'affichera en francs et 
centimes selon la formule {{<katex>}}asset = initAmount * (1 + rate)^{duration}{{</katex>}}

```
What is your initial asset? 1000
What is your yearly interest rate (in pourcent)?: 2.5
Duration in years? 30

After 30 years, your assets (with interest) will be     2097.57 SFr
```

{{< notion_avancee >}}
## Exercice 23
Améliorer l'affichage pour avoir des séparateurs après les milliers, et millions, et 
arrondir le montant à 5 centimes. La valeur 1876435.264901 affichera par exemple **1'876'435.30 SFr**
{{< /notion_avancee >}}

{{< notion_avancee >}}
## Exercice 24
Implémenter le codage d’un nombre réel donné par l’utilisateur, en virgule flottante selon IEEE754
- Calcul du bit signe (facile)
- Calcul de l’exposant (moyen)
- Calcul de la mantisse (difficile?)
- Vérification avec les bits du nombre mémorisé dans une variable float (difficile)
{{< /notion_avancee >}}

# Défis

## Comparaison de flottants
Qu'affiche le programme suivant ? Pourquoi ? Quelle est la bonne manière de comparer des **`double`** ?

```c
#include <stdio.h>

int main(void)
{
  double d1 = 0.3;
  double d2 = 0.1 + 0.1 + 0.1;
  if (d1 == d2)
  {
    printf("d1 is equal to d2\n");
  }
  else
  {
    printf("d1 is NOT equal to d2\n");
  }
  

  return 0;
}
```

{{<details "Explications" >}}
Le programme affiche **`d1 is NOT equal to d2`**.
En effet, en représentation binaire, 0.1 est une valeur périodique (comme 1/3 en décimal).
Donc, 0.1 ne peut pas être représentée exactement en binaire.
Par conséquent, la somme de 3 fois 0.1 n'est pas exactement égale à 0.3.
La bonne manière de comparer des **`double`** est de vérifier que la différence entre les deux valeurs est inférieure à une petite valeur epsilon (typiquement la plus petite valeur représentable par un **`double`** : **`DBL_EPSILON`**).

```c
#include <stdio.h>
#include <math.h>
#include <float.h>

int main(void)
{
  double d1 = 0.3;
  double d2 = 0.1 + 0.1 + 0.1;
  if (d1 == d2)
  {
    printf("d1 is equal to d2\n");
  }
  else
  {
    printf("d1 is NOT equal to d2\n");
  }

  if (fabs(d1 - d2) < DBL_EPSILON)
  {
    printf("d1 is approximately equal to d2\n");
  }
  else
  {
    printf("d1 is NOT approximately equal to d2\n");
  }

  return 0;
}
```
{{</details>}}

## Cast de **`double`** en **`char`**

Qu'affiche le programme suivant ? Pourquoi ?

```c
#include <stdio.h>

int main(void)
{
	// Cast 128 into a char (8 bits) => overflow
	printf("c1 = %d\n", (char)128);
	char c1 = 128;
	printf("c1 = %d\n", c1);

	// 1)
	double d2 = 128.99;
	char c2 = (char) d2;
	printf("d2 = %lf\n", d2);
	printf("c2 = %d\n", (char) c2);

	// 2)
	double d3 = (char) 128.99;
	char c3 = (char) d3;
	printf("d3 = %lf\n", d3);
	printf("c3 = %d\n", (char) c3);
	printf("c3 = %d\n", (char) 128.99);

	return 0;
}
```

{{< details "Explications" >}}
Le code cast un **`double`** (128.99) en **`char`**.
Comme la valeur maximale représentable par un **`char`** est 127, il devrait y avoir débordement (overflow).
On s'attend donc à avoir -128 au final.

Cependant, le programme affiche :

```
c1 = -128
c1 = -128
d2 = 128.990000
c2 = -128
d3 = 127.000000
c3 = 127
c3 = 127
```

La norme dit :

> **6.3.1.4 Real floating and integer**
> 
> When a finite value of real floating type is converted to an integer type other than _Bool, the fractional part is discarded (i.e., the value is truncated toward zero).
> **If the value of the integral part cannot be represented by the integer type, the behavior is undefined.**

Donc, quand un **`double`** est casté en **`char`**, seule la partie entière est conservée.
Si elle ne peut pas être représentée dans le type entier demandé (ici **`char`**), alors c'est un **comportement indéfini**.

Dans l'exemple de code donné, les parties 1) et 2) sont donc des comportements indéfinis.
Et le compilateur (ici GCC) va faire les choses différemment.

Dans le cas 1), comme la valeur est stockée dans une variable, le cast se fera à l'exécution.
Il prend donc la valeur stockée dans la variable (128.99), ne garde que la partie entière (128), et la cast en **`char`**.
Si **`char`** est signé (plage [-128,127]), 128 n’est pas représentable : la conversion a un comportement indéfini.
Dans ce cas particulier, l’exécution affiche -128, mais elle pourrait tout aussi bien afficher 0, 127, 42, ou provoquer un crash.
Si **`char`** est non signé (plage [0,255]), la conversion est bien définie et donne 128.

Dans le cas 2), le compilateur voit directement que la partie entière de la constante 128.99 ne pourra pas être représentée sur un **`char`** et prend des mesures, donc directement durant la compilation.
En particulier, il décide d'utiliser la valeur maximale représentable par un **`char`**, et donc on récupère 127.

**👉 Ne jamais se fier au résultat d’un cast hors bornes. En C, c’est un comportement indéfini.**

{{< /details >}}
