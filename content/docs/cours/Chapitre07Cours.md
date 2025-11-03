---
title: "7 - Compilation et modularisation"
weight: 1
---

# CHAPITRE 7 : compilation et modularisation
## Cours
{{< pdf src="/pdfs/1242.1.07_Compilation.pdf" >}}

## Quiz
[QUIZ SUR LA COMPILATION](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=761712)

# Défis

## MACROS
Que fait le programme suivant ? Pourquoi ? Que faut-il modifier pour qu'il fonctionne correctement ?

```c
#include <stdio.h>

#define SQUARE(x) x * x

int main(void)
{
  int a = 5;
  int b = SQUARE(a + 1);
  printf("b = %d\n", b);
  
  return 0 ;
}
```

{{< details "Explications" >}}
L'utilisation de macros peut entraîner des comportements inattendus en raison de l'expansion de texte. Dans cet exemple, l'expression `SQUARE(a + 1)` sera développée en `a + 1 * a + 1`, ce qui ne donne pas le résultat attendu. Pour corriger cela, il faut ajouter des parenthèses autour des arguments de la macro :

```c
#define SQUARE(x) ((x) * (x))
```

Avec cette modification, l'appel `SQUARE(a + 1)` sera correctement évalué comme `(a + 1) * (a + 1)`.
{{< /details >}}
