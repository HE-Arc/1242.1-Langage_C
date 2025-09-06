---
title: "FAQ"
---

# FAQ
## Quelle version du C devons-nous utiliser ?

Durant le cours 1242.1 Langage C, nous utilisons le C99.

En particulier, le compilateur installé par défaut est GCC (version 10.3 minimum). Comme indiqué dans le manuel utilisateur de GCC 10.3, la version par défaut du C utilisée est gnu11 c'est-à-dire le C11 avec les extensions GNU. Cette version ainsi que les extensions ne sont pas nécessaires pour le contenu du cours. Ainsi, la version C99 est suffisante.

## Comment déclarer la fonction main() ?

Les prototypes standards définis par la **[norme C99](/pdf/Draft_norme_ISO_C11.pdf)** sont :

```c
int main(void)
```

et

```c
int main(int argc, char *argv[])
```

ou équivalent.

En effet, la **[norme C99](/pdf/Draft_norme_ISO_C11.pdf)** précise :

{{< figure src="/images/norme_5.1.2.2.1.png#center" >}}

## Quel type entier faut-il utiliser par défaut ?

S'il n'y a pas de contraintes particulières, alors il faut utiliser le type **`int`** par défaut quand on souhaite représenter des entiers.

Si on souhaite représenter des grands entiers, alors on peut utiliser le type **`long int`**.

Si on souhaite économiser de la place en mémoire, et représenter des petits entiers, alors on peut utiliser les types **`short int`** voire **`char`**.

## Quelles tailles occupent les types entiers en mémoire ?

La norme C ne définit pas strictement la taille des types entiers en mémoire. Cependant, elle définit un domaine que chaque entier doit supporter au minimum.

Pour les **`int`** en particulier, leurs tailles étaient calquées sur la taille d'un mot mémoire. Donc, pour les architectures 16 bits, les entiers sont codés sur 16 bits, et sur les architectures 32 bits, ils sont codés sur 32 bits.  Sur les architectures 64 bits cependant, et pour des raisons de compatibilité, les **`int`** sont aussi codés sur 32 bits en général.

Si la place occupée en mémoire par certains types est importante, alors il faut le vérifier explicitement :

```c
    #include <stdio.h>
    
    int main(void)
    {
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
    
    	printf("\n");
    
    	return 0;
    }
```

## Qu'est-ce qu'un point de séquence en C ?

Un point de séquence en programmation est défini comme :

> A **sequence point** defines any point in a [computer program](https://en.wikipedia.org/wiki/Computer_program "Computer program")'s [execution](https://en.wikipedia.org/wiki/Execution_(computing) "Execution (computing)") at which it is guaranteed that all [side effects](https://en.wikipedia.org/wiki/Side_effect_(computer_science) "Side effect (computer science)") of previous evaluations will have been performed, and no side effects from subsequent evaluations have yet been performed.
<br><br>(https://en.wikipedia.org/wiki/Sequence_point)

En d'autres termes, quand votre programme atteint un point de séquence, vous avez la garantie que toutes les modifications des variables sont effectivement prises en compte.

L'annexe C de la **[norme C99](/pdf/Draft_norme_ISO_C11.pdf)** donne la liste des points de séquence suivante :

{{< figure src="/images/norme_annexe_C.png#center" >}}

Ce concept est important (bien qu'un peu avancé) car si une expression contient plusieurs effets de bord (comme des modifications de variables), alors il n'y a aucune garantie sur l'ordre de ces modifications entre 2 points de séquence.

En particulier, si on modifie 2 fois la même variable entre 2 points de séquence, alors le comportement est indéfini, comme détaillé dans la FAQ [Pourquoi l’expression i = i++ est un comportement indéfini ?](#pourquoi-lexpression-i--i-est-un-comportement-ind%c3%a9fini-).

## Pourquoi l'expression **`i = i++`** est un comportement indéfini ?

Pour le comprendre, il faut savoir ce qu'est un point de séquence en C (voir la FAQ [Qu’est-ce qu’un point de séquence en C ?](#quest-ce-quun-point-de-s%c3%a9quence-en-c-)).

En particulier, entre 2 points de séquence, il n'y a aucune garantie sur l'ordre dans lequel les effets de bord (modifications de variables) seront effectués.
Par conséquent, toute expression qui modifie 2 fois la même variable entre 2 points de séquence est un comportement indéfini (UB) en C.

Les expressions suivantes sont donc des UB :

```c
i = ++i;
i = i++;
j = ++i + i++;
i = (++i, i++);
```
Et elles produiront les warnings suivants (si l'option **`-Wall`**  est activée avec **GCC**) :

```BashSession
.\main.c: In function 'main':
.\main.c:10:11: warning: operation on 'i' may be undefined [-Wsequence-point]
   10 |         i = ++i;
      |         ~~^~~~~
.\main.c:11:11: warning: operation on 'i' may be undefined [-Wsequence-point]
   11 |         i = i++;
      |         ~~^~~~~
.\main.c:12:13: warning: operation on 'i' may be undefined [-Wsequence-point]
   12 |         j = ++i + i++;
      |             ^~~
.\main.c:22:5: warning: operation on 'i' may be undefined [-Wsequence-point]
   22 |   i = (++i, i++);
```

{{<hint info>}}
**À NOTER :** l'opérateur **`,`** (virgule, ou comma en anglais) introduit un point de séquence entre chaque **`,`**.
Donc le code suivant n'est pas un UB :
  
  ```c
  j = (++i, i++);
  ```
{{</hint>}}


## Comment afficher plus de messages (warnings) avec GCC dans VS Code ?

Avec `GCC`, il s'agit de rajouter l'option `-Wall` lors de la compilation. **[Le manuel de GCC](/pdf/gcc_10.3_User_Manual.pdf)** détaille tous les paramètres (et bien plus).

VS Code stocke certaines informations dans le répertoire `.vscode` . En particulier,  le fichier `tasks.json` détaille les informations importantes pour compiler vos programmes avec `GCC`.

{{< figure src="/images/gcc_compilation_params1.png#center" >}}

Dans le paramètres `args`, il faut donc rajouter l'argument `-Wall` comme ceci :

{{< figure src="/images/gcc_compilation_params2.png#center" >}}

À partir de maintenant, GCC affichera tous les warnings possibles. Il est encore possible d'être plus verbeux en rajoutant d'autres arguments comme `-Wextra` ou encore `-Wpedantic`.

## Quels sont les raccourcis clavier les plus utilisés dans VS Code pour le C ?

Voici les raccourcis les plus utiles quand on programme en C dans VS Code.

#### Édition

**`Ctrl + Tab`**  → basculer sur le fichier précédent

**`Ctrl + Shift + k`** → effacer la ligne courante

**`Ctrl + HOME`** → aller au début du fichier

**`Ctrl + END`** → aller à la fin du fichier

**`Ctrl + ↑`** → scroller vers le haut

**`Ctrl + ↓`** → scroller vers le bas

**`Ctrl + k Ctrl + c`** → commenter les lignes sélectionnées

**`Ctrl + k Ctrl + u`** → décommenter les lignes sélectionnées

**`Ctrl + §`** → commenter / décommenter les lignes sélectionnées

**`Ctrl + p`** → ouvrir un fichier

**`Ctrl + g`** → aller à une ligne précise

**`Ctrl + Shift + o`** → aller au symbole donné

**`Ctrl + Shift + m`** → afficher les warnings et les erreurs de compilation

**`F8`** → afficher le prochain problème (warning ou erreur)

**`Shift + F8`** → afficher le problème suivant (warning ou erreur)

**`Shift + Alt + f`** → formatter le fichier

**`F12`** → aller à la définition correspondante

**`F2`** → renommer le symbole automatiquement

#### Compilation / Exécution

**`Ctrl + Shift + b`** → compiler le fichier

**`F9`** → ajouter / enlever un breakpoint

**`F5`** → compiler et débugger le fichier / continuer

**`Ctrl + F5`** → compiler et exécuter le fichier

**`Shift + F5`** → arrêter de debugger

**`F10`** → exécuter la ligne et passer à la ligne suivante

**`F11`** → entrer dans la fonction

#### Divers

**`Ctrl + Shift + g, g`** → afficher la fenêtre **Source Control** (git)

## Pourquoi éviter d'utiliser des MACROS ?

Les MACROS doivent être évitées car elles conduisent souvent à des bugs très difficiles à détecter :

- il n'y a pas de vérification de type avec les MACROS

- l'expansion de MACROS peut conduire à des effets de bord difficiles à prévoir. En particulier, la MACRO suivante est buggée (comme vu en cours) :

      #define MAX_WRONG(x,y) x>y?x:y

- elles rendent l'exécutable plus volumineux car le code est copié-collé contrairement aux fonctions

- le code au final est moins lisible.

Pour remplacer des MACROS, il est conseillé d'utiliser des fonctions ou des définitions de variables constantes si besoin.

## Quelle est la différence entre **`#include <stdio.h>`** et **`#include "mon_fichier.h"`** ?

On utilise **`#include <header_standard>`** (avec des `<>`) pour inclure des fichiers standards.
Le preprocesseur ira donc chercher directement dans l'installation du compilateur pour trouver les fichiers d'en-têtes spécifiés.
Ainsi, quand on souhaite lire au clavier ou écrire à l'écran, on ajoute **`#include <stdio.h>`**.

Quand on souhaite inclure des fichiers d'en-têtes que nous avons écrits, alors il faut spécifier au compilateur de les chercher localement en premier.
Il faut donc include le fichier en utilisant des `" "` (avec des guillemets) comme ceci : **`#include "mon_fichier_header.h"`**.

## Peut-on imbriquer des opérateurs ternaires dans des opérateurs ternaires ?

**Oui.**

Le cours donne la syntaxe de l'opérateur ternaire comme :

{{< figure src="/images/ternary_operator.png#center" >}}

L'opérateur ternaire étant lui-même une expression, on peut donc les imbriquer. Les exemples suivants sont donc parfaitement valides :
```c
// Q: can we nest ternary operator?
// A: yes. A ternary operator needs expression as operands.
//    So, as a ternary operator is an expression, it can contain
//    other ternary operators
int value = 100;
int quarter = value > 50 ? (value > 75 ? 4 : 3) : (value <= 25 ? 1 : 2);

// It even works without parenthesis, but it is less readible
int quarter2 = value > 50 ? value > 75 ? 4 : 3 : value <= 25 ? 1 : 2;
```

## Pourquoi ne peut-on pas utiliser des blocs dans l'opérateur ternaire ?

En particulier, pourquoi l'exemple suivant ne fonctionne pas ?
```c
int i = 1;

(i++ == 1) ? {printf("Hello\n"); } : {printf("World\n"); };
```

Les blocs ne retournent pas de valeur, donc ne sont pas des expressions.
Ainsi, ils ne conviennent pas pour l'opérateur ternaire.

Il faut noter cependant que les fonctions retournent des valeurs (même si c'est `void`).
L'exemple suivant fonctionne donc parfaitement :

```c
int i = 1;
(i++ == 1) ? printf("Hello\n") : printf("World\n");
```

## Pourquoi **`int arr[size] = {1, 2, 3}`** est une erreur si **`size`** est un **`const int`** ?

Le code suivant ne fonctionne pas :

```c
const int size = 4;
int arr[size] = {1, 2, 3, 4};
```

En effet, GCC retourne l'erreur : **`error: variable-sized object may not be initialized`**.

Premièrement, il faut comprendre que le mot-clef **`const`** **en C**, signifie uniquement que la variable est ***read-only.***
En particulier, elle reste une variable, et n'est donc pas considérée comme une constante.

Par conséquent, **`arr`** est un ***variable-length array*** (ou ***VLA***) et ne peut donc pas être initialisé de cette manière.

**En particulier, la norme C99 précise :**

{{< figure src="/images/norme_VLA.png#center" >}}

## Comment vérifier dans mon code si les VLAs sont supportés par le compilateur ?

Les ***variable-length arrays*** (VLAs) sont supportés différemment selon les compilateurs, et selon les versions.
Ainsi, comment vérifier dans mon code si les VLAs sont supportés par le compilateur ?

Le support pour les VLAs a été rajouté en C99, puis rendu optionnel en C11. De plus, le compilateur de Microsoft ne les supporte pas du tout.

Donc il faut :
1. Vérifier qu'on n'utilise pas le compilateur de Microsoft `MSVC`.
2. Puis, si on utilise C11 ou plus récent, alors il faut vérifier que les VLAs sont effectivement supportés.
3. Puis, si on utilise C99, alors on sait qu'ils sont supportés.

En utilisant le preprocessor, on peut définir une MACRO `VLAS_SUPPORTED` de la façon suivante :

```c
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
```

## Quelles sont les extensions VS Code recommandées pour le C ?

[C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) (`ms-vscode.cpptools`)
{{< figure src="/images/ext_cpp.png#center" >}}

[C/C++ Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack) (`ms-vscode.cpptools-extension-pack`)
{{< figure src="/images/ext_cpp_ep.png#center" >}}

[GitLens — Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) (`eamodio.gitlens`)
{{< figure src="/images/ext_gitlens.png#center" >}}

[vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons) (`vscode-icons-team.vscode-icons`)
{{< figure src="/images/ext_icons.png#center" >}}

[TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight) (`wayou.vscode-todo-highlight`)
{{< figure src="/images/ext_todos.png#center" >}}

[Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) (`aaron-bond.better-comments`)
{{< figure src="/images/ext_better_comments.png#center" >}}

[Comment Anchors](https://marketplace.visualstudio.com/items?itemName=ExodiusStudios.comment-anchors) (`exodiusstudios.comment-anchors`)
{{< figure src="/images/ext_comment_anchors.png#center" >}}

## Quel type faut-il utiliser par défaut en C pour représenter des réels ?

Par défaut, il faut utiliser le type **`double`** pour représenter des réels en C.
En particulier, les fonctions déclarées dans **`math.h`** utilise aussi le type **`double`** par défaut.

Dans de rares cas (gestion de la mémoire par exemple), et sur certaines architectures, il peut être intéressant d'utiliser le type **`float`**.

De la même manière, si l'architecture le permet, il est possible d'utiliser le type **`long double`** s'il faut une précision supplémentaire ou s'il faut représenter des réels plus grands.

## Qu'est-ce qu'un buffer overflow ?

Un buffer overflow c'est quand un programme prévu pour écrire dans un buffer, écrit au final en dehors des limites de ce buffer (avant ou après en mémoire).
Ce type de bugs est souvent utilisé pour abuser un programme (le faire crasher, changer son comportement, prendre le contrôle d'une machine, etc.).

Voici un exemple "naïf" montrant ce bug potentiel en C.
En particulier, il est important de se rappeler qu'en C, il n'y a aucune vérification lors de la lecture avec `scanf` ni lors de l'écriture dans un tableau. 

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

## Comment initialiser tous les éléments d'un tableau en C ?

En C, les variables globales ou statiques sont automatiquement initialisées à la valeur par défaut du type considéré. Pour le type `int` en particulier, c'est 0.

De plus en C, si on initialise les premiers éléments d'un tableau, alors tous les éléments suivants sont initialisés à la valeur par défaut.

Le code suivant résume les différents cas de figure mentionnés ci-dessus.

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

## Quelles sont les principales différences entre tableaux et pointeurs en C ?

Les tableaux et les pointeurs en C sont très similaires.
En pratique, il est même possible d'accéder à un tableau en utilisant des pointeurs (comme vu en cours).
Il existe pourtant certaines différences.

#### Allocation de la mémoire

La déclaration d'un tableau alloue la mémoire nécessaire pour stocker les éléments du tableau.
La déclaration d'un pointeur n'alloue que la place nécessaire pour stocker une adresse (8 bytes sur des machines 64 bits).
Donc :
```c
int array1[5] = {1, 2, 3, 4, 5};
```
alloue bien la place pour stocker 5 entiers, alors que :
```c
int *pointer1 = array1;
```
n'alloue que la place pour 1 adresse.

#### Taille avec **`sizeof`**
Suite au point ci-dessus, l'opérateur `sizeof` retourne la taille totale d'un tableau, et retourne toujours `8` pour un pointeur sur une machine 64 bits.
L'exemple suivant affiche donc des valeurs différentes :
```c
printf("sizeof(array1) = %d\n", sizeof(array1));
printf("sizeof(pointer1) = %d\n", sizeof(pointer1));
```

#### Arithmétique sur les pointeurs
On peut utiliser l'arithmétique sur les tableaux, de la même manière que sur les pointeurs. Cependant, on ne peut pas modifier la variable du tableau elle-même.
```c
// Pointer arithmetic with arrays: OK
printf("*(array1 + 1) = %d\n", *(array1 + 1));
printf("*(pointer1 + 1) = %d\n", *(pointer1 + 1));
// OK with pointers
printf("*(pointer1++) = %d\n", *(pointer1++));
// BUT, we cannot change the array1 itself
// error: lvalue required as increment operand
// printf("*(array1++) = %d\n", *(array1++));
```

#### Tableaux de taille zéro impossibles
Comme la taille du tableau est allouée au moment de la déclaration, on ne peut pas avoir de tableau de taille 0.
Dans ce cas, il faut utiliser des pointeurs, et allouer la mémoire au moment nécessaire.

Les pointeurs à l'inverse peuvent pointer n'importe où, et en particulier "nulle part" :
```c
void *nothing_to_see_here = NULL;
```

## Pourquoi je peux assigner directement à un tableau passé à une fonction ?

On a vu en cours qu'on ne pouvait pas assigner à un tableau.
Pourtant, le code suivant ne retourne pas d'erreur :
```c
#include <stdio.h>


int assign_to_array(char string[])
{
  string = "Hello after assignment";
  printf("%s\n", string);
}

int main(void)
{
  char string[30] = "Hello before assignment";

  printf("%s\n", string);
  assign_to_array(string);
  printf("%s\n", string);
  
  return 0;
}
```

Les tableaux ne sont jamais véritablement passés comme paramètre d'une fonction.
Il sont au contraire convertis ("dégénérés") en pointeur.
De cette manière, seule l'adresse du début du tableau est accessible dans la fonction.
Les éléments du tableau ne sont donc pas recopiés.

Et comme vu en cours, on peut parfaitement assigner des adresses à des pointeurs.

Le code ainsi mentionné ne recopie pas les valeurs dans le tableau, mais le fait uniquement pointer "ailleurs" dans la fonction.
Le tableau déclaré dans le **`main`** pointe lui toujours au même endroit.

## Que fait l'expression **`3["012345"]`** en C (et pourquoi elle est parfaitement correcte) ?

Tout d'abord, il faut bien se rappeler que le formalisme tableaux et pointeurs sont similaires.
En particulier, quand on écrit **`array[15]`**, le compilateur va le comprendre comme **`*(array + 15)`**.

De plus, l'opérateur addition est commutatif : on peut intervertir ses opérandes, sans changer le résultat final.

Donc, si on applique le formalisme pointeurs à l'expression **`3["012345"]`** , on obtient que c'est équivalent à l'expression **`*(3 + "012345")`**.
Comme le **`+`** est commutatif, on peut le transformer en  **`*("012345" + 3)`.**
En utilisant le formalisme tableau, on obtient enfin **`"012345"[3]`**.
Cette dernière expression signifie donc simplement que l'on retourne le 4ième élément du tableau **`"012345"`**.
Donc **`printf("%c", 3["012345"]);`** affichera "tout simplement" **`3`**.

L'expression initiale est parfaitement valide en C.
Elle est cependant parfaitement inutile et doit être évitée.

## Pourquoi modifier une chaîne de caractères créée comme **`char *myString = "Hello World";`** n'est pas correct ?

En effet, le code suivant n'est pas correct :
```c
char *myString = "Hello World";
printf("%s\n", myString);
scanf("%s", myString);
printf("%s\n", myString);
```

La ligne **`char *myString = "Hello World";`** n'alloue pas l'espace pour stocker une chaîne de caractères.
Elle ne fait que définir un pointeur, qui va pointer à l'adresse où se trouve la chaîne de caractères **prédéfinie** **`"Hello World"`**.

Cet emplacement est réservé et ne peut pas être modifié.
La ligne **`scanf("%s", myString);`** va donc provoquer une erreur car elle va tenter d'écrire dans cet espace.

Si la chaîne de caractères doit être modifiée, il faut alors allouer l'espace nécessaire puis l'initialiser.
Le code suivant fonctionne correctement :
```c	
char myString[100] = "Hello World";
printf("%s\n", myString);
scanf("%s", myString);
printf("%s\n", myString);
```

## Est-il possible de soustraire 2 pointeurs sur **`void`** ?

En cours, nous voyons que non, pourtant le code suivant compile et semble fonctionner :

```c	
#include <stdio.h>

int main(void)
{
  int tab[4] = {1, 2, 3, 4};
  void *p1 = tab + 1;
  void *p2 = tab + 3;

  int i = p2 - p1;

  return 0;
}
```	

Soustraire 2 pointeurs sur **void** est un comportement indéfini (Undefined Behavior ou UB).
En effet, la **[norme C99](/pdf/Draft_norme_ISO_C11.pdf)** précise :

{{< figure src="/images/norme_sub_pointers.png#center" >}}

Un **`void *`** ne pointe sur rien par construction (même si, avant le cast, il peut pointer sur des données effectives comme dans l'exemple).
Donc, soustraire 2 **`void *`** est un comportement indéfini.

L'exemple semble fonctionner, car **`gcc`** va accepter cette erreur et retourner la différence en bytes entre les 2 pointeurs.
Ce comportement de **`gcc`** est non-standard et doit être évité.

## Comment forcer **`gcc`** à être moins permissif et à retourner des erreurs quand il détecte des comportements indéfinis ?

Dans de nombreuses situations pour lesquelles la norme ne définit pas de comportement, les compilateurs tentent tout de même de fournir un résultat logique.
Ces comportements indéfinis par la norme, peuvent varier d'un compilateur à l'autre.
Pour cette raison, il est souvent préférable de respecter la norme afin d'assurer une plus grande portabilité de son code.

Pour **gcc**, on peut le forcer à être plus strict avec la norme en utilisant le paramètre **`-pedantic-errors`**. 

Par exemple, par défaut, si on soustrait 2 **`void *`** , **`gcc`** va retourner la différence entre les 2 pointeurs en bytes.
Si on utilise **`-pedantic-errors`**, alors il va retourner l'erreur de compilation suivante : **`error: pointer of type 'void *' used in subtraction [-Wpointer-arith]`**.

## Pourquoi le format **`%f`** fonctionne pour les **`double`s** avec la fonction **`printf()`**, mais pas avec la fonction **`scanf()`** ?

#### Lire des **`double`s** avec **`scanf()`**

La fonction **`scanf()`** lit des valeurs et doit les stocker en mémoire.
Donc il faut lui passer des adresses sur les emplacement en mémoire qui seront modifiés.
Ainsi, dans le format, il faut lui dire précisément le type qui est lu et qui doit être stocké.
Si on lit des **`float`s**, il faut utiliser **`%f`**.
Si on lit des **`double`s**, il faut utiliser **`%lf`**.

#### Écrire des **`double`s** avec **`printf()`**

La fonction **`printf()`** écrit des valeurs qui lui sont passées en paramètres.
**`printf()`** étant une fonction variadique, c'est-à-dire qu'elle prend un nombre variable de paramètres (tout comme la fonction **`scanf()`**), les paramètres de type **`float`** sont automatiquement promus en **`double`**.
La fonction **`printf()`** ne voit donc au final que des **`double`s**.
Les formats **`%f`** et **`%lf`** sont donc strictement identiques pour les **`float`s** et les **`double`s** et peuvent être utilisés de manière interchangeable.
Pour des raisons de lisibilité, il est cependant fortement conseillé d'utiliser le format **`%f`** quand on écrit des **`float`s**, et le format **`%lf`** quand on écrit de **`double`s**.

## Que se passe-t'il quand on cast un **`double`** en **`char`** et qu'il y a débordement (overflow) ?

Le code suivant cast un **`double`** (128.99) en **`char`**.
Comme la valeur maximale représentable par un **`char`** est 127, il devrait y avoir débordement (overflow).
On s'attend donc à avoir -128 au final.
Mais ce n'est pas toujours le cas. Pourquoi ?

#### Code source

```c
#include <stdio.h>

int main(void)
{
	// Cast 128 into a char (8 bits) => overflow
	printf("c1 = %d\n", (char)128);
	char c1 = 128;
	printf("c1 = %d\n", c1);

	// Cast 128.99 into a char (8 bits)
	// Undefined Behavior
	// SEE: https://stackoverflow.com/questions/14774540/implicitly-casting-a-float-constant

	// 1) Undefined Behavior
	// Here, the value is first stored in a variable.
	// So the compiler will just cast at runtime and that will overflow.
	double d2 = 128.99;
	char c2 = (char) d2;
	printf("d2 = %lf\n", d2);
	printf("c2 = %d\n", (char) c2);

	// 2) Undefined Behavior
	// Here, the compiler can see that the constant 128.99 is not representable on a char, even after discarding the fractional part.
	// So it decides to clamp the value to the maximum value possible, that is 127.
	double d3 = (char) 128.99;
	char c3 = (char) d3;
	printf("d3 = %lf\n", d3);
	printf("c3 = %d\n", (char) c3);
	printf("c3 = %d\n", (char) 128.99);

	return 0;
}
```

#### Résultat affiché

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

{{< figure src="/images/norme_6.3.1.4.png#center" >}}

Donc, quand un **`double`** est casté en **`char`**, seule la partie entière est conservée.
Si elle ne peut pas être représentée dans le type entier demandé (ici **`char`**), alors c'est une **comportement indéfini**.

Dans l'exemple de code donné, les parties 1) et 2) sont donc des comportements indéfinis.
Et le compilateur va faire les choses différemment.

Dans le cas 1), comme la valeur est stockée dans une variable, le cast se fera à l'exécution.
Il prend donc la valeur stockée dans la variable (128.99), ne garde que la partie entière (128), et la cast en **`char`**, ce qui donne un débordement et retourne -128.

Dans le cas 2), le compilateur voit directement que la partie entière de la constante 128.99 ne pourra pas être représentée sur un **`char`** et prend des mesures, directement à la compilation.
En particulier, il décide d'utiliser la valeur maximale représentable par un **`char`**, et donc on récupère 127.


## Pourquoi le Task Manager de Windows ne montre pas la mémoire réellement utilisée par mon programme ?

Dans l'exercice 1 du chapitre 10 sur l'allocation dynamique de mémoire, il est demandé d'allouer des blocs de mémoire jusqu'à provoquer un dépassement.
Cependant, lorsqu'on ouvre le Task Manager sous Windows, on ne voit pas la RAM utilisée augmentée en conséquence.

Le Task Manager sous Windows n'est pas un outil suffisamment précis pour analyser l'utilisation de la mémoire vive (RAM) allouée dans un programme en C.
Mais il est tout de même possible d'afficher certains détails.
En particulier, ce qui est intéressant, c'est d'afficher la "Committed Memory" :

{{< figure src="/images/task_manager_commited_memory.png#center" >}}

La taille totale de la mémoire "Committed" peut être bien supérieure à la RAM disponible car il s'agit de la taille globale utilisée (RAM + Virtuelle).

## Pourquoi faut-il définir M_PI nous-même ?

M_PI est une constante qui représente la valeur de {{<katex>}}\pi{{</katex>}} dans les programmes C (en général).
Cependant, elle n'est pas définie par la norme C.
Mais elle peut parfois être tout de même définie par certains compilateurs (comme **`gcc`**).

Il faut donc la définir de manière portable de la manière suivante :

```c	
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif
```
## Comment faut-il vider le buffer **`stdin`** ?

Lorsque **`scanf()`** essaie de lire des données en entrée, et échoue, il laisse le buffer **`stdin`** inchangé.
Il faut donc vider le buffer **`stdin`** avant de pouvoir lire à nouveau des données.

Une solution est d'utiliser la fonction **`fflush()`** avec le buffer **`stdin`** en paramètre : **`fflush(stdin)`**.

Cependant, selon la norme (C11), **`fflush(stdin)`** est un comportement indéfini (UB) et ne doit donc pas être utilisé :

> ### 7.21.5.2 The fflush function
> 
> #### Description
> If stream points to an output stream or an update **stream in which the most recent
> operation was not input**, the fflush function causes any unwritten data for that stream
> to be delivered to the host environment to be written to the file; **otherwise, the behavior is
> undefined.**

La solution est donc de vider le buffer **`stdin`** "manuellement" en lisant les caractères un par un jusqu'à la fin du buffer.
Le code suivant montre comment faire :

```c
	// Handling User input errors:
	// 1) Print what is expected
	// 2) Read input from User
	// 3) Empty the stdin buffer
	// 4) Repeat until we got what we expected
	int status = 0;
	const int nbExpectedValues = 1;
	// Variables to store User input values
	int x;
	do
	{
		printf("Entrez un nombre : ");
		status = scanf("%d", &x);

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
	} while (status != nbExpectedValues);
```
