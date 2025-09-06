---
title: "8 - Tableaux et structures"
weight: 1
---

# CHAPITRE 8 : Tableaux et structures

## Cours
[1242.1.08_TableauxStructures](/pdf/1242.1.08_TableauxStructures.pdf)

## Quiz
[QUIZ SUR LES TABLEAUX, CHAÎNE DE CARACTÈRES ET STRUCTURES](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=761763)

# EXERCICES

{{< hint info >}}
**NOTE :** pour des raisons historiques, la numérotation des exercices n'est pas continue.
{{< /hint >}}

## Exercice 1
Parmi les définitions de tableaux suivantes, indiquer celles qui sont erronées et expliquer pourquoi :
```c
unsigned int matrice[3, 3];
int vecteur[6];
char ordinateur[] = 'IBM PC';
float mesure[2][1000];
int des[3] [3] [3];
char nom[8] = "François";
char mois[14] = "juin";
```

## Exercice 2
Lesquelles des chaînes suivantes sont initialisées correctement ?
Corrigez les déclarations fausses et indiquer pour chaque chaîne de caractères le nombre d'octets réservés en mémoire.
```c
char a[] = "un\ndeux\ntrois\n";
char b[12] = "un deux trois";
char c[] = 'abcdefg';
char d[10] = 'x';
char e[5] = "cinq";
char f[] = "Cette " "phrase " "est coupée";
char g[2] = {'a', '\0'};
char h[4] = {'a', 'b', 'c'};
char i[4] = "'o'";
```
## Exercice 3
À la suite des déclarations et instructions suivantes, placer le contenu mémoire des tableaux suivants (valeur décimale ou caractère) :

```c
double values[] = {1.2, -2.3, 0.};
short int IDEtudiant[5] = { 1234, 4576, 7345, 9999};
int serie[5];
for (int i=0; i < 5; i++)
serie[i]= 2 * i + 1;
char texte[]="Alea jacta est";
struct XY { char x; double y } var1 ={'5',5.f};
struct XY tabStruct[3] = {{'5',5.f}, {'6',6.f}, {'7',7.f} };
```

**Exemple :**
```c
char L[5]={ 'a', 't'};
```
donne :

| **`L[0]`** | **`L[1]`** | **`L[2]`** | **`L[3]`** | **`L[4]`** |
| ---- | ---- | ---- | ---- | ---- | 
| `'a'`| `'t'`| `0`  | `0`  | `0`  |

{{< hint info >}}
**REMARQUE :** chaque élément représente 1 byte.
{{< /hint >}}

## Exercice 21_1
Écrire une fonction **`ch08_ex21_1_CompareArray()`** qui compare deux tableaux d'entiers de même taille et renvoie **`true`** si les tableaux sont identiques, et **`false`** sinon.
**`ch08_ex21_1_CompareArray()`** prend 3 paramètres en entrée : les 2 tableaux d'entiers et leur taille, dans cet ordre.

**Exemples**

Pour les tableaux suivants :
```c
int array1[] = {1, 2, 3, 4, 4};
int array2[] = {1, 2, 3, 4, 5};
```

**`ch08_ex21_1_CompareArray(array1, array2, 0)`** renvoie **`true`**.
**`ch08_ex21_1_CompareArray(array1, array2, 4)`** renvoie **`true`**.
**`ch08_ex21_1_CompareArray(array1, array2, 5)`** renvoie **`false`**.

## Exercice 21_2
Écrire une fonction **`ch08_ex21_2_PrintArray()`** qui affiche à l'écran un tableau d'entiers, et ne retourne rien.
**`ch08_ex21_2_PrintArray()`** prend donc 2 paramètres en entrée : 1 tableau d'entiers et sa taille.

**Exemples**

Pour le tableau suivant :
```c
int array[] = {1, 2, 3, 4, 5};
```

**`ch08_ex21_2_PrintArray(array, 0)`** n'affiche rien.
**`ch08_ex21_2_PrintArray(array, 4)`** affiche **`1 2 3 4`**.
**`ch08_ex21_2_PrintArray(array, 5)`** affiche **`1 2 3 4 5`**.

{{<hint danger>}}
**ATTENTION :** chaque élément du tableau est suivi d'un espace, **sauf le dernier**. De plus, **il ne faut pas** terminer l'affichage par un **`\n`**.
{{</hint>}}

## Exercice 21_3
Écrire une fonction **`ch08_ex21_3_FillArray()`** qui remplit un tableau d'entiers passé en paramètre avec des valeurs saisies au clavier par l'utilisateur.
On s'arrête quand l'utilisateur entre une valeur négative.
La fonction **`ch08_ex21_3_FillArray()`** retourne le nombre de valeurs correctes saisies.

{{< hint danger >}}
**ATTENTION :** il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

**Exemples**

**`ch08_ex21_3_FillArray(array, -1)`** ne fait rien.

**`ch08_ex21_3_FillArray(array, 0)`** ne fait rien.

Pour le tableau :
```c
int array[] = {-2, -2, -2, -2};
```
alors **`ch08_ex21_3_FillArray(array, 4)`** avec les saisies au clavier
```
a
b
1
-1
```
change le tableau en :
```c
{1, -2, -2, -2};
```

Pour le tableau :
```c
int array[] = {-2, -2, -2, -2};
```
alors **`ch08_ex21_3_FillArray(array, 4)`** avec les saisies au clavier
```
2
2
-2
```
change le tableau en :
```c
{2, 2, -2, -2};
```

Pour le tableau :
```c
int array[] = {-2, -2, -2, -2};
```
alors **`ch08_ex21_3_FillArray(array, 4)`** avec les saisies au clavier
```
3
3
-2
```
change le tableau en :
```c
{3, 3, -2, -2};
```

## Exercice 21
En vous aidant des exercices précédents, écrire une fonction **`ch08_ex21_ArraySum()`** qui :
1. déclare un tableau pouvant contenir 50 entiers maximum
2. demande à l’utilisateur le nombre de valeurs **`n`** à saisir (maximum 50)
3. remplit le tableau avec n valeurs entrées au clavier
4. affiche les n premiers éléments du tableau
5. affiche la somme des valeurs saisies se trouvant dans le tableau

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

**Exemple 1**
```c
$ .\ch08_ex21_ArraySum.exe
Nb values (max.50): a
Nb values (max.50): b
Nb values (max.50): -2
Nb values (max.50): -1
Nb values (max.50): 0
array:

Total sum: 0
```

**Exemple 2**
```c
.\ch08_ex21_ArraySum.exe
Nb values (max.50): 4
Value 0? -2
Value 1? -1
Value 2? 0
Value 3? 1
array:
-2 -1 0 1
Total sum: -2
```

## Exercice 22
Écrire une fonction qui :
1. déclare un tableau pouvant contenir 50 entiers maximum
2. demande à l’utilisateur le nombre de valeurs n
3. remplit le tableau avec n valeurs entrées au clavier
4. copie toutes les valeurs strictement positives dans un 2ème tableau
5. copie toutes les valeurs strictement négatives dans un 3ème tableau
6. Affiche les tableaux

## Exercice 23
Écrire une fonction **`ch08_ex23_Array2DSum()`** qui :
1. déclare un tableau d'entiers (taille maximale : 50 lignes et 50 colonnes).
2. lit les tailles (nombre de lignes et nombre de colonnes) au clavier
3. remplit le tableau avec des valeurs entrées au clavier
4. affiche la somme de tous ses éléments

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

**Exemple 1 :**
```c
$ .\ch08_ex23_Array2DSum.exe
Nb lines (max.50): a
Nb lines (max.50): -1
Nb lines (max.50): 2
Nb columns (max.50): a
Nb columns (max.50): -1
Nb columns (max.50): 2
array[0][0]: 1
array[0][1]: 2
array[1][0]: 3
array[1][1]: 4
Total sum: 10
```

**Exemple 2 :**
```c
$ .\ch08_ex23_Array2DSum.exe
Nb lines (max.50): 0
Nb columns (max.50): 9
Total sum: 0
```

**Exemple 3 :**
```c
$ .\ch08_ex23_Array2DSum.exe
Nb lines (max.50): 9
Nb columns (max.50): 0
Total sum: 0
```

**Exemple 4 :**
```c
$ .\ch08_ex23_Array2DSum.exe
Nb lines (max.50): 0
Nb columns (max.50): 0
Total sum: 0
```

## Exercice 24
Écrire une fonction **`ch08_ex24_DotProduct()`** qui calcule le produit vectoriel de 2 vecteurs d'entiers {{<katex>}}\vec{u}{{</katex>}} et {{<katex>}}\vec{v}{{</katex>}}.
Les vecteurs sont passés en paramètres sous forme de tableaux d'entiers, avec leur taille, dans cet ordre.

{{< hint info >}}
**Rappel :** 

{{<katex>}}\vec{u} = (3, 2, -4){{</katex>}} et {{<katex>}}\vec{v} = (2, -3, 5){{</katex>}} alors 

{{<katex>}}
\vec{u}\cdot\vec{v} = \begin{pmatrix} x_{u} & y_{u} & z_{u} \end{pmatrix} \begin{pmatrix} x_{v}\\ y_{v}\\ z_{v} \end{pmatrix} \newline
\vec{u}\cdot\vec{v} = \begin{pmatrix} 3 & 2 & -4 \end{pmatrix} \begin{pmatrix} 2 \\ -3 \\ 5 \end{pmatrix} \newline
\vec{u}\cdot\vec{v} = 3 * 2 + 2 * (-3) + (-4) * 5 = -20
{{</katex>}}

{{< /hint >}}

**Exemple :**
Avec les tableaux suivants :
```c
int u[] = {3, 2, -4};
int v[] = {2, -3, 5};
```
alors **`ch08_ex24_DotProduct(u, v, 3)`** renvoie **`-20`**.

## Exercice 25
Écrire un programme qui détermine la plus grande et la plus petite valeur dans un tableau d'entiers.
Afficher ensuite la valeur et la position du maximum et du minimum.

**Note :** si le tableau contient plusieurs maxima ou minima, le programme retiendra la position du premier maximum ou minimum rencontré.

## [AVANCÉ] Exercice 26
Écrire une fonction qui calcule le produit matriciel de 2 matrices d'entiers {{<katex>}}A{{</katex>}} et {{<katex>}}B{{</katex>}} passées en paramètres.

## Exercice 31
Écrire une fonction qui lit 5 mots, séparés par des espaces et qui les affiche ensuite dans une ligne, mais dans l'ordre inverse.
Les mots sont mémorisés dans 5 variables **`M1`**, …, **`M5`**.

## Exercice 32
Écrire une fonction qui lit une ligne de texte (taille max. 50 caractères) et puis un caractère.
Elle doit indiquer si le caractère se trouve dans le texte.
Si oui, elle doit afficher à quelle position il se trouve (indice de la première occurrence).

{{< hint danger >}}
**Contrainte :** ne pas utiliser des fonctions de **`<string.h>`**.
{{< /hint >}}

## Exercice 33
Écrire une fonction qui lit une ligne de texte (taille maximale : 200 caractères), la mémorise dans une variable **`texte`** et affiche ensuite :
a) la longueur **`lChaine`** de la chaîne.
b) le nombre de **'e'** contenus dans le texte.
c) toute la phrase à rebours, sans changer le contenu de la variable **`texte`**.
d) toute la phrase à rebours, après avoir inversé l'ordre des caractères dans **`texte`**.

{{< hint info >}}
**Information :** il faut utiliser la fonction **`fgets()`** pour lire une ligne de texte comportant des espaces.
{{< /hint >}}

## [AVANCÉ] Exercice 34
Écrire une fonction qui lit une ligne de texte (taille maximale : 128 caractères), puis qui supprime tous les espaces dans la chaine et tasse les éléments restants.

{{< hint info >}}
**Indication :** commencer par faire l’exercice sur papier en raisonnant d’abord avec 2 chaines de caractères, puis avec une seule.
{{< /hint >}}

## [AVANCÉ] Exercice 35
Écrire une fonction qui lit une ligne de texte (taille maximale : 128 caractères), y récupère un chiffre (positif ou négatif), le mémorise dans une variable de type long et l’affiche.

{{< hint info >}}
**NOTE :** on supportera les formats simples comme "1748", "+1748" et "-1748".
{{< /hint >}}

## Exercice 41
Définir une structure **`Time`** capable de mémoriser le temps d’un marathon (hh:mm:ss).

1. Écrire une fonction **`ch08_ex41_InitTime()`** qui prend 3 entiers (heures, minutes, secondes) passés en paramètres et retourne une structure **`Time`**.
2. Écrire une fonction **`ch08_ex41_PrintTime()`** qui prend une structure **`Time`** en paramètre et affiche le temps associé.
3. Écrire une fonction **`ch08_ex41_Time()`** qui créé une structure **`Time`** contenant 5 heures, 3 minutes et 17 secondes en utilisant la fonction **`ch08_ex41_InitTime()`** et l’affiche en utilisant la fonction **`ch08_ex41_PrintTime()`**.

**Exemple :**
```c
  Time t = ch08_ex41_InitTime(5, 3, 17);
  ch08_ex41_PrintTime(t);
  ```

affichera **`05:03:17`** si on a stocké 5 heures 03 minutes et 17 secondes dans **`t1`**.

{{< hint info >}}
NOTE : utiliser un **`typedef`** en définissant la structure.
{{< /hint >}}

## Exercice 42
Écrire un programme pour gérer des nombres complexes.
En particulier :
1. définir le type **`Complex`** avec 2 membres de type réel : **`real`** et **`imaginary`**
2. ajouter le code à **`scanf`** pour que la saisie d'un nombres complexe ne se fasse qu'au format (r,i) et encapsuler ce code dans une fonction **`ch08_ex42_InputComplex()`** qui retourne une structure **`Complex`**.
3. ajouter les fonctions **`ch08_ex42_SumComplex()`** et **`ch08_ex42_DiffComplex()`** appelées pour calculer la somme, et la différence de deux nombres complexes stockés dans une structure **`Complex`**. Ces fonctions prennent 2 paramètres de type **`Complex`** et retournent un **`Complex`**.

**`sum_complex()`** : {{<katex>}}(a_1 + i b_1)+( a_2 + i b_2) = (a_1+a_2) + i (b_1+b_2){{</katex>}}

**`diff_complex()`** : {{<katex>}}(a_1 + i b_1)-( a_2 + i b_2) = (a_1-a_2) + i (b_1-b_2){{</katex>}}

4. implémenter une fonction **`ch08_ex42_PrintComplex()`** qui affiche un nombre complexe sous la forme suivante : **`5.00 + -3.00i`**.
5. écrire une fonction **`ch08_ex42_Complex()`** qui lit deux nombres complexes, calcule leur somme et leur différence et affiche les résultats.
{{< hint info >}}
**NOTE :** utiliser les fonctions écrites dans les points précédents.
{{< /hint >}}

{{< hint danger >}}
**ATTENTION :** il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

**Exemple :**
```c
$ .\ch08_ex42_Complex.exe
Please enter a complex number (r,i): a
Please enter a complex number (r,i): -1
Please enter a complex number (r,i): (1,1)
Please enter a complex number (r,i): (2,3) 

Sum = 3.00 + 4.00i

Diff = -1.00 + -2.00i
```

{{< hint danger >}}
**ATTENTION :** Il faut gérer les erreurs de saisie (cf [Comment faut-il vider le buffer stdin ?](/docs/cours/faq/#comment-faut-il-vider-le-buffer-stdin-)).
{{< /hint >}}

## Exercice 43
1. Créer un type **`Person`** pour une personne, caractérisée par son nom (20 caractères maximum), son prénom (20 caractères maximum) et son année de naissance.
2. Dans une fonction **`ch08_ex43_Person()`**, déclarer un tableau de 10 personnes et l'initialiser avec les données des sept personnes suivantes :
```c
"Knuth", "Donald", 1938
"Kernighan", "Brian", 1942
"Ritchie", "Dennis", 1941
"Thompson", "Ken", 1943
"Minsky", "Marvin", 1927
"Dijkstra", "Edsger", 1930
"Stroustrup", "Bjarne", 1950
```
3. Dans la fonction **`ch08_ex43_Person()`**, afficher toutes les personnes âgées de moins de 80 ans.
{{< hint danger >}}
**ATTENTION :** on considère que nous sommes en 2020.
{{< /hint >}}
4. Trouver les personnes dont le nom est en tête/en fin de classement selon l’ordre alphanumérique (le plus proche de « AAA » / le proche de « ZZZ » ).

{{< hint danger >}}
**NOTE :** utiliser la fonction **`strcmp()`** pour comparer les noms.
{{< /hint >}}

5. Qui sont ces personnes et qu’ont-elles fait ?

**Exemple :**
```c
7 Persons
Persons less than 80 years old:
Brian Kernighan 78 years
Dennis Ritchie 79 years
Ken Thompson 77 years
Bjarne Stroustrup 70 years

Alphabetic order:
The first is: Dijkstra
The last is: Thompson
```
