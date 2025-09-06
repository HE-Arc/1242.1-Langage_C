---
title: "13 - Listes chaînées"
weight: 11
---

# CHAPITRE 13 : Structures de données dynamiques : les listes chaînées

## Cours
[1242.1.13_Listes_chainées](/pdf/1242.1.13_Listes_chainées.pdf)

## Quiz
[LISTES CHAINÉES](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=762228)

# EXERCICES

## Exercice 1
Écrire un programme qui permet de gérer une liste chaînée.

1. Il faut insérer en début de liste les nombres saisis par l'utilisateur, ceci tant que le nombre entré est différent de 0. Il s’agit de créer un nouveau nœud pour chaque nombre.
Les nœuds sont toujours insérés en début de liste !
2. Afficher la liste.
3. Parcourir la liste et augmenter le contenu de chaque nœud de 1.
4. Effacer un à un les nœuds en début de liste de la liste et libérer la mémoire.
Utilisez un pointeur sur le premier nœud : `Node *ptr_first;`

## Exercice 2
Modifier le programme précédent de manière à insérer les nombres positifs en début de liste et les nombres négatifs en fin de liste.

**Indication :** utiliser un second pointeur qui pointe sur le dernier nœud et mettez ces deux pointeurs dans une structure qui corresponde à une liste (`List`).

```c
typedef struct list
{
  Node *ptr_first;
  Node *ptr_last;
} List;
```

Allouer dynamiquement une liste avec la fonction `list_init();`

**Exemple :**
```c
int main(void)
{
  List list = list_init();
  list_display(list);
  list_inc(list);
  list_display(list);
  list_free(&list);
  list_display(list);

  return 0;
}
```
