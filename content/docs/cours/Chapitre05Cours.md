---
title: "5 - Structures de contrôle"
weight: 1
---

# CHAPITRE 5 : structures de contrôle
## Cours
[1242.1.05_StructuresDeControle](/pdf/1242.1.05_StructuresDeControle.pdf)

## Squelette à remplir

```c
#include <stdio.h>

// CHAPTER 5

int main(void)
{
	// Experiment with if () {...} else {...}
	// => read an integer, then check whether it is divisible by 13 (for example)

	// Experiment with the ternary operator (example are in chapter 3 as it is an operator)

	// Experiment with switch
	// =>  For example, read 2 values and an operation (in +, -, * and /) and perform the calculation.

	// Experiment with while(){...}
	// => Read 2 integers M and N, then compute modulo
	// => Copy examples from chapter 5 then check the answers
	// => Read an integer N, then compute the summation from 1 to N

	// Experiment with do{...}while()
	// => See friendly scanf example
	// => Continuously read values and sum them. Stop when the user enters 0.

	// Experiment with for(;;){...}
	// => (SEE example chapter 5) Read an integer N, then display the iteration number.
	// => (SEE example chapter 5) Copy loop examples then check your answers.
	// => (SEE example chapter 5) Read an integer N, then display the list of powers of 2, from 1 to N.

	// Experiment with return, exit(), break and continue inside for loops

	return 0;
}
```

## Quiz
[QUIZ SUR LES INSTRUCTIONS DE CONTRÔLE (~10')](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=761481)

# EXERCICES

{{< hint info >}}
**NOTE :** pour des raisons historiques, la numérotation des exercices n'est pas continue.
{{< /hint >}}

## Exercice 1

1) Parmi les instructions suivantes, indiquer celles qui sont fausses et dire pourquoi :

```c
//a)
if (number < 1) ++number;
//b) 
if (x < limit) 
    x *= 2 
else if (x >= limit)
    x /=2;
//c) 
if (offer > demand)
    price *= 0.95;
else
    price *= 1.07;
//d) 
if (value >= 0);
    printf("positive value");
//e) 
if (color = red)
{
    color= green;
    printf("green\n");
}
```

2) Réécrire les instructions a), b) et c) avec l’opérateur ternaire **`?`** et **corriger les éventuelles erreurs**.

## Exercice 2
Écrire un programme qui détermine si le caractère qu'on tape est une minuscule (code ASCII compris entre 97 et 122) ou une majuscule (code compris entre 65 et 90).

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** l'affichage doit se terminer par un retour à la ligne.
{{< /hint >}}

**Exemple 1**
```code
$ .\ch05_ex02_LowercaseUppercase.exe
Type a letter: u
lowercase
```

**Exemple 2**
```code
$ .\ch05_ex02_LowercaseUppercase.exe
Type a letter: F
UPPERCASE
```

**Exemple 3**
```code
$ .\ch05_ex02_LowercaseUppercase.exe
Type a letter: !
The character you entered is not a letter.
```

## Exercice 3
Écrire un programme qui lit deux valeurs entières (a et b) au clavier et qui affiche le signe du produit (positif, négatif ou zéro) de a et b **sans faire la multiplication**.

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** l'affichage doit se terminer par un retour à la ligne.
{{< /hint >}}

**Exemple 1**
```code
$ .\ch05_ex03_MultiplicationSign.exe
Please enter 2 integers: 1 2
1 * 2 > 0
```

**Exemple 2**
```code
$ .\ch05_ex03_MultiplicationSign.exe
Please enter 2 integers: 0 0
0 * 0 = 0
```

**Exemple 3**
```code
$ .\ch05_ex03_MultiplicationSign.exe
Please enter 2 integers: a b
Please enter 2 integers: b 1
Please enter 2 integers: -1 3
-1 * 3 < 0
```

## Exercice 4
Écrire un programme qui affiche dans l'ordre décroissant trois nombres introduits au clavier par l'utilisateur.
Il s’agit d’échanger le contenu des variables de manière à mettre la plus grande valeur dans la première variable, la médiane dans la seconde et la plus petite dans la troisième.

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** l'affichage doit se terminer par un retour à la ligne.
{{< /hint >}}

**Exemple 1**
```code
$ .\ch05_ex04_DecreasingOutput.exe
Please enter 3 integers separated by commas: 1,2,3
The 3 integers sorted in decreasing order: 3, 2, 1
```

**Exemple 2**
```code
$ .\ch05_ex04_DecreasingOutput.exe
Please enter 3 integers separated by commas: 1,-2,0
The 3 integers sorted in decreasing order: 1, 0, -2
```

**Exemple 3**
```code
$ .\ch05_ex04_DecreasingOutput.exe
Please enter 3 integers separated by commas: a,1,2
Please enter 3 integers separated by commas: 1, -9, c
Please enter 3 integers separated by commas: 0,0,0
The 3 integers sorted in decreasing order: 0, 0, 0
```

## [AVANCÉ] Exercice 5
Écrire un programme qui lit deux valeurs entières (a et b) au clavier et qui affiche le signe (positif, négatif ou zéro) de la somme de a et b sans faire l'addition. Au besoin, vous pouvez utiliser la fonction abs de la bibliothèque <math.h>.

## Exercice 6
Écrire un programme qui lit trois valeurs entières (a, b et c) au clavier et qui affiche la plus grande des trois valeurs, en utilisant :
1. if - else et une variable d'aide max
2. if - else if - ... - else sans variable d'aide
3. les opérateurs ternaires et une variable d'aide max
4. les opérateurs ternaires sans variable d'aide

## Exercice 7
Écrire un programme qui calcule la ou les solutions réelles d'une équation du second degré de la forme suivante :

<center>
{{<katex>}}ax^{2}  + bx + c = 0{{</katex>}}
</center>

en utilisant la formule suivante :

<center>
{{<katex>}}x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}{{</katex>}}
</center>

Considérer aussi les cas où l'utilisateur entre :
- une valeur nulle pour a; 
- des valeurs nulles pour a et b; 
- des valeurs nulles pour a, b et c.
 
Afficher les résultats et les messages nécessaires sur l'écran.

{{< hint danger >}}
**ATTENTION :** il faut afficher les réels avec 4 chiffres significatifs après la virgule.
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** l'affichage doit se terminer par un retour à la ligne.
{{< /hint >}}

**Exemple 1**
```code
$ .\ch05_ex07_SecondOrderEquation.exe
Compute solutions of an equation of the form ax^2 + bx + c = 0 
Please enter coefficients a, b, and c: 0 0 0
Any real is solution of this equation.
```

**Exemple 2**
```code
$ .\ch05_ex07_SecondOrderEquation.exe
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 1 1 
This equation has no real solution.
```

**Exemple 3**
```code
$ .\ch05_ex07_SecondOrderEquation.exe
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 1 -2
The real solutions of this equation are:
x1 = 1.0000
x2 = -2.0000
```

**Exemple 4**
```code
$ .\ch05_ex07_SecondOrderEquation.exe
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: a 1 2
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 1 b -2
Compute solutions of an equation of the form ax^2 + bx + c = 0
Please enter coefficients a, b, and c: 2 -1 -2
The real solutions of this equation are:
x1 = 1.2808
x2 = -0.7808
```

## Exercice 21
Remplacer l'instruction **`if`** suivante par une instruction **`switch`** équivalente et créer un programme pour vérifier cette transformation (le type de x est **`int`** ou **`char`**) :
```c
if (x == 0)
    printf("Error\n");
else
    printf("100/%d = %f\n", x, 100./x);
```

## Exercice 22
Écrire un programme qui effectue la conversion en francs suisses d’une somme donnée en won (W), dollars ($), yens (Y) ou livres sterling (P).
Pour la saisie, utiliser une des instructions suivantes :
```c
scanf(" %g %c", &amount, &currency); // To store in a float
```

ou

```c
scanf(" %lg %c", &amount, &currency); // To store in a double
```

Pour les taux de changes, il faut utiliser les constantes suivantes :
```c
const double WON2CHF = 0.00070;
const double USD2CHF = 0.99;
const double YEN2CHF = 0.0067;
const double POUND2CHF = 1.13;
```

{{< hint danger >}}
**ATTENTION :** il faut afficher les réels avec 3 chiffres significatifs après la virgule.
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** l'affichage doit se terminer par un retour à la ligne.
{{< /hint >}}

**Exemple 1**
```code
$ .\ch05_ex22_CurrencyConverter.exe
USAGE: positive value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount (in CHF) to convert: 123 W
Swiss francs: 0.086
```

**Exemple 2**
```code
$ .\ch05_ex22_CurrencyConverter.exe
USAGE: positive value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount (in CHF) to convert: 123 $
Swiss francs: 121.770
```

**Exemple 3**
```code
$ .\ch05_ex22_CurrencyConverter.exe
USAGE: positive value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount (in CHF) to convert: -123 Y
The input amount is negative!!
USAGE: positive value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount (in CHF) to convert: 123 Y
Swiss francs: 0.824
```

**Exemple 4**
```code
$ .\ch05_ex22_CurrencyConverter.exe
USAGE: positive value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount (in CHF) to convert: 123 L
Unsupported currency!!
USAGE: positive value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount (in CHF) to convert: 123 P
Swiss francs: 138.990
```

**Exemple 5**
```code
$ .\ch05_ex22_CurrencyConverter.exe
USAGE: positive value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount (in CHF) to convert: d W
The input format is not correct!!
USAGE: positive value [W | $ | Y | P]
Won = W  Dollar = $  Yen = Y  Pound = P
Please enter the amount (in CHF) to convert: 122 W
Swiss francs: 0.085
```

## Exercice 23
Écrire un programme qui demande à l'utilisateur le numéro d'un mois (1 pour janvier, 2 pour février, ...) et lui affiche le nombre de jours correspondant (31 jours en janvier, 28 en février, ...).

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** l'affichage doit se terminer par un retour à la ligne.
{{< /hint >}}

**Exemple 1**
```code
$ .\ch05_ex23_DaysInMonth.exe
Please enter the number of the month (january=1, ... , december=12): 1
The 1th month has 31 days.
```

**Exemple 2**
```code
$ .\ch05_ex23_DaysInMonth.exe
Please enter the number of the month (january=1, ... , december=12): 12
The 12th month has 31 days.
```

**Exemple 3**
```code
$ .\ch05_ex23_DaysInMonth.exe
Please enter the number of the month (january=1, ... , december=12): 13
Please enter the number of the month (january=1, ... , december=12): 7
The 7th month has 31 days.
```

**Exemple 4**
```code
$ .\ch05_ex23_DaysInMonth.exe
Please enter the number of the month (january=1, ... , december=12): a
Please enter the number of the month (january=1, ... , december=12): b
Please enter the number of the month (january=1, ... , december=12): 0
Please enter the number of the month (january=1, ... , december=12): 8
The 8th month has 31 days.
```

## Exercice 24
Expliquer ce que fait le programme ci-dessous. Donner quelques exemples d'utilisation.

```c
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char choice;
    switch(choice = toupper(getchar()))
    {
    case 'R' : printf("RED");
    break;
    case 'V' : printf("GREEN");
    break;
    case 'B' : printf("BLUE");
    break;
    default : printf("Error");
    }
return 0 ;
}
```

## Exercice 31
Expliquer ce que font les boucles suivantes :

**a)**
```c
    n = 1;
    while (n < 40) 
    {
      printf("value %d\n", n);
      n *= 2;
    }
```

**b)**
 ```c
   int count = 0;
   do
   {
     printf("%d ", count);
     ++count;
   }
   while (count% 8 != 0);
   ```

**c)** 
 ```c
    while (n == 0);
   ```

**d)** 
```c
   for (x = 0; x < 1000; ++x)
     printf("%d ", x);
   ```

**e)** 
```c
   for (money = 100; money < 10000; money *= 2.0)
     printf("Fortune = %f\n", money);
   ```

## Exercice 32
a) Écrire un programme qui lit N nombres entiers au clavier et qui affiche leur somme, leur produit et leur moyenne.
Choisissez un type approprié pour les valeurs à afficher.
Le nombre N est à entrer au clavier.
Il faut utiliser la boucle la plus appropriée.

{{< hint danger >}}
**ATTENTION :** il faut afficher les réels avec 4 chiffres significatifs après la virgule.
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** l'affichage doit se terminer par un retour à la ligne.
{{< /hint >}}

b) Répéter l'introduction du nombre N jusqu'à ce que N ait une valeur entre 1 et 15.

**Exemple**
 ```code
 $ .\ch05_ex32_SumProductMean.exe
Number of values to read: 16
Number of values to read: 0
Number of values to read: -1
Number of values to read: 3
1. number: a
1. number: 1
2. number: b
2. number: 2
3. number: c
3. number: 3
Sum = 6
Product = 6
Mean = 2.0000
```

## Exercice 33
Calculer la factorielle {{<katex>}}N!{{</katex>}} d'un entier naturel N telle que :

<center>
{{<katex>}}N! = 1*2*3*...*(N-1)*N{{</katex>}}
</center>

et

<center>
{{<katex>}}0! = 1{{</katex>}}
</center>

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** l'affichage doit se terminer par un retour à la ligne.
{{< /hint >}}

**Exemple 1**
```code
$ .\ch05_ex33_Factorial.exe
Please enter a positive integer N: 6
6! = 720
```

**Exemple 2**
```code
$ .\ch05_ex33_Factorial.exe
Please enter a positive integer N: -1
Please enter a positive integer N: a
Please enter a positive integer N: 6
6! = 720
```

## [AVANCÉ] Exercice 34
a) Calculer la racine carrée x d'un nombre réel positif A par approximations successives en utilisant la relation de récurrence suivante :

<center>
{{<katex>}}X {j+1} = (X {j} + A/X {j}) / 2 {{</katex>}}
</center>

avec

<center>
{{<katex>}}X {1} = A{{</katex>}}
</center>

L’utilisateur doit entrer la précision ɛ du calcul souhaitée.
Le programme doit s’arrêter lorsque {{<katex>}}| X {J+1} - X {1} | < E{{</katex>}}.

b) Assurez-vous lors de l'introduction des données que la valeur pour A et ɛ sont des réels positifs.

c) Affichez lors du calcul toutes les approximations calculées : 
```
 The first square root approximation of ... is ...
 The second square root approximation of ... is ...
 The third square root approximation of ... is ...
 ...
 ```

## Exercice 35
Afficher un triangle isocèle formé d'étoiles de N lignes (N est fourni au clavier) :

```code
line count: 8
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
```
## Exercice 36
Afficher la table des produits pour N variant de 1 à 10 :

```code
X*Y   I   0   1   2   3   4   5   6   7   8   9  10
---------------------------------------------------
 0    I   0   0   0   0   0   0   0   0   0   0   0
 1    I   0   1   2   3   4   5   6   7   8   9  10
 2    I   0   2   4   6   8  10  12  14  16  18  20
 3    I   0   3   6   9  12  15  18  21  24  27  30
 4    I   0   4   8  12  16  20  24  28  32  36  40
 5    I   0   5  10  15  20  25  30  35  40  45  50
 6    I   0   6  12  18  24  30  36  42  48  54  60
 7    I   0   7  14  21  28  35  42  49  56  63  70
 8    I   0   8  16  24  32  40  48  56  64  72  80
 9    I   0   9  18  27  36  45  54  63  72  81  90
10    I   0  10  20  30  40  50  60  70  80  90 100
```


Les colonnes sont alignées grâce au format %3d.

## Exercice 37
Faire un programme affichant le résultat d'une partie de FizzBuzz (sans erreur) pour les nombres de 1 à 100.

Description du jeu:

_Les joueurs sont assis en cercle. Un joueur commence et dit le nombre "1" puis son voisin 
incrémente le nombre et le dit (donc "2"), puis … Cependant chaque fois que le nombre est 
divisible par 3, le joueur doit dire fizz au lieu du nombre, et si le nombre est divisible par 5, il doit dire buzz. Les nombres divisibles par 3 et par 5 deviendront fizzbuzz. Le joueur qui se trompe est éliminé._

Un début de partie donnera donc les résultats suivant:
 ```
 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, 
 Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz
 ```

**AVANCÉ (optionnel) :** adapter le programme pour jouer au "BEUZEU".

## Exercice 41

Qu'affiche ce programme :

```c
  #include <stdio.h>
  int main(void)
  {
    int i, j, x = 0 ;
    for (i = 0 ; i < 5 ; ++i)
    for (j = 0; j < i; ++j)
    {
      switch(i + j – 1)
      {
      case –1 :
      case 0  : x += 1;
                break;
      case 1  :
      case 2  :
      case 3  : x += 2;
                break;
      default : x += 3;
      }
   printf("%d ", x);
   }
   printf("\nx = %d\n", x);
   return 0;
}
```

## Exercice 42

Qu'affiche ce programme : 

```c
  #include <stdio.h>
  
int main(void)
  {
    int i, j, x = 0;
    for (i = 0 ; i < 5 ; ++i)
      for (j = 0; j < i; ++j)
      {
        switch(i + j – 1)
        {
          case –1 :
          case 0  : x += 1;
                   break;
          case 1  :
          case 2  :
          case 3  : x += 2;
          default : x += 3
       }
       printf("%d ", x);
   }
   printf("\nx = %d\n", x);
   return 0;
}
```

