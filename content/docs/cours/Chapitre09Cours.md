---
title: "9 - Pointeurs"
weight: 1
---

# CHAPITRE 9 : POINTEURS

## Cours
[1242.1.09_Pointeurs](/pdf/1242.1.09_Pointeurs.pdf)

## Quiz
[QUIZ SUR LES POINTEURS](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=761910)

# EXERCICES

## Exercice 1
Quelles sont les valeurs finales des variables **`a`**, **`b`** et **`c`** après exécution des deux séquences de programmes suivantes :

### A
```c
int a, b, c, *ptr;
ptr = &a;
*ptr = 4;
b = a + 5;
ptr = &b;
c = *ptr;
``` 

### B
```c
char a, b, c, *ptr;
a = b = 3;
ptr = &a;
c = *ptr += 2;
ptr = &c;
++(*ptr);
```

## Exercice 2
Si **`champ`** représente un tableau et si **`ptr`** est un pointeur du même type, pourquoi les instructions **`ptr = champ;`** et **`ptr = &champ[0];`** sont-elles équivalentes ?

## Exercice 3
Trouver les erreurs ou les incohérences figurant dans les deux extraits de programmes suivant :

### A
```c
char x[] = "abcd";
char y[] = "efgh";
char *ptr = x;
x = y;
y = ptr;
```

### B
```c
int nombre1, nombre2;
int *ptr = &nombre1;
ptr = 25;
nombre2 = ptr + 6;
ptr = &nombre2;
```

## Exercice 4
Un programme C contient les instructions suivantes :

```c
char *pc, c[10];
int *pi1, *pi2, i1[10], i2 = 7;
float *pf1, *pf2, f1[10], f2 = 3.14;
pc = c;
pi1 = i1;
pi2 = &i2;
pf1 = f1;
pf2 = &f2;
pc += 6;
pi1 += 6;
pf1 += 6;
*pf2 += 5;
*pi2 -= 2;
pi1 -= *pi2;
```
On suppose que **`c`** se trouve à l'adresse **`900`**, **`i1`** à l'adresse **`1000`**, **`i2`** à l'adresse **`1100`**, **`f1`** à l'adresse **`1200`** et **`f2`** à l'adresse **`1300`**.

Pour chacune des 11 instructions ci-dessus, donner la valeur assignée au membre de gauche.
Expliquer chacune de vos réponses.

## Exercice 5
Soit le programme ci-dessous.
Supposons que la variable **`a`** se trouve à l'adresse **`0x0012ff88`**, la variable **`ptr1`** à l'adresse **`0x0012ff84`** et la variable **`ptr2`** à l'adresse **`0x0012ff80`**.

```c
#include <stdio.h>
#include <stdlib.h>

int main (void)
{
int a = 1 ;
int* ptr1 ;
int** ptr2 ;
ptr1 = &a ;
ptr2 = &ptr1 ;
printf("&a : %p\n", &a);
printf("a : %d\n", a);
printf("&ptr1 : %p\n", &ptr1);
printf("ptr1 : %p\n", ptr1);
printf("*ptr1 : %d\n", *ptr1);
printf("&ptr2 : %p\n", &ptr2);
printf("ptr2 : %p\n", ptr2);
printf("*ptr2 : %p\n", *ptr2);
printf("**ptr2: %d\n", **ptr2);
system("pause");
return 0;
}
```

Quelle sera la sortie de ce programme ?

## Exercice 6
Écrire une fonction **`ch09_ex06_CopyArrays()`** qui prend 2 tableaux d'entiers (et leur taille) en paramètre et qui ajoute les éléments de **`B`** à la fin de **`A`**.

{{< hint danger >}}
**ATTENTION :** attention, il faut utiliser le formalisme pointeur quand c'est possible.
{{< /hint >}}

{{< hint info>}}
**NOTE :** pour tester la fonction, on peut par exemple créer un tableau **`A`** de 10 entiers, un tableau **`B`** de 4 entiers, puis appeler **`ch09_ex06_CopyArrays()`** en considérant que **`A`** n'a que 4 éléments.
{{< /hint >}}

**Exemple**

Avec les tableaux suivants :
```c
int A[] = {1, 2, 3, 4, 0, 0, 0, 0, 0, 0};
int B[] = {11, 12, 13, 14};
```
alors après l'appel à **`ch09_ex06_CopyArrays(A, 4, B, 4)`**, **`A`** devient **`{1, 2, 3, 4, 11, 12, 13, 14, 0, 0}`**.

## Exercice 7
**`ptr`** est un pointeur sur une variable de type entier.
Initialement **`ptr`** pointe sur la base d'un tableau d'entiers.
Quel élément du tableau est référencé par chacune des trois expressions suivantes :

### A
```c
ptr[1]
```

### B
```c
*(ptr+1) 
```

### C
```c
*(++ptr)
```

Laquelle de ces trois opérations modifie le pointeur ?

## Exercice 8
Trouver l'erreur qui se cache dans la séquence de programme suivante :

```c
int tablo[20], *ptr = tablo, n;
for (n = 0; n < 20; --n) *(ptr++) = 2;
```

## Exercice 9
Soit le programme suivant :

```c
#include <stdio.h>

int lectureTaille( float * );
int main(void)
{
 float tableau[ 20 ];
 printf("La taille du tableau en octets est %d"
 "\nLa taille renvoyée par lectureTaille est %d\n",
 sizeof( tableau ),
 lectureTaille( tableau ));
 return 0 ;
}
int lectureTaille( float *ptr )
{
 return sizeof( ptr );
}
```

Quelle sera sa sortie ?

## Exercice 10
Écrire une fonction **`ch09_ex10_Swap()`** qui échange le contenu de 2 variables entières définies dans le programme principal.

{{< hint danger >}}
**ATTENTION :** il faut bien choisir le type des arguments de la fonction **`ch09_ex10_Swap()`**.
{{< /hint >}}

**Exemple :**
Avec les définitions suivantes :
```c
int a = 5, b = 10;
```

la sortie après l'appel à **`ch09_ex10_Swap()`** doit être :

```c
Before: a: 5, b: 10
After:  a: 10, b: 5
```

## Exercice 11
Soit le programme suivant :

```c
int main(void)
 {
 int A = 1;
 int B = 2;
 int C = 3;
 int *P1, *P2;
 P1 = &A;
 P2 = &C;
 *P1 = (*P2)++;
 P1 = P2;
 P2 = &B;
 *P1 -= *P2;
 ++(*P2);
 *P1 *= *P2;
 A = ++(*P2) * *P1;
 P1 = &A;
 *P2 = *P1 /= *P2;
 return 0;
 }
```

Compléter le tableau ci-dessous pour chaque instruction du programme.

| |**`A`**|**`B`**|**`C`**|**`P1`**|**`P2`**|
| --- | --- | --- | --- | --- | --- |
|**`Initialisation`**|`1`|`2`|`3`|`?`|`?`|
|**`P1 = &A`**|`1`|`2`|`3`|`&A`|`?`|
|**`P2 = &C`**|`1`|`2`|`3`|`&A`||
|**`*P1 = (*P2)++`**||||||
|**`P1 = P2`**||||||
|**`P2 = &B`**||||||
|**`*P1 -= *P2`**||||||
|**`++(*P2)`**||||||
|**`*P1 *= *P2`**||||||
|**`A = ++(*P2) * *P1`**||||||
|**`P1 = &A`**||||||
|**`*P2 = *P1 /= *P2`**||||||


## Exercice 12
Soit **`p`** un pointeur qui 'pointe' sur un tableau **`a`** :

```c
int a[] = {12, 23, 34, 45, 56, 67, 78, 89, 90};
int *p;
p = a;
```
Quelles valeurs ou adresses fournissent les expressions suivantes :

a) **`*p + 2`**

b) **`*(p+2)`**

c) **`&a[4] - 3`**

d) **`a + 3`**

e) **`&a[7] - p`**

f) **`p + (*p - 10)`**

g) **`*(p + *(p+8) - a[7])`**

Pour une valeur, on écrira par exemple **`90`**.
Pour une adresse, on écrira par exemple l'adresse de la composante: **`A[8]`**
