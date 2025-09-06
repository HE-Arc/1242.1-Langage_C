---
title: "12 - Structures II"
weight: 11
---

# CHAPITRE 12 : STRUCTURES ET TYPES COMPOSÉS

## Cours
[1242.1.12_StructuresEtType](/pdf/1242.1.12_StructuresEtType.pdf)

## Quiz
[STRUCTURES ET TYPES](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=762168)

# EXERCICES

## Exercice 1
Compléter le programme suivant :

```c
#include <stdio.h>

// NOTE: keep French to stick to exercice.

// Il faut rendre le nouveau type "struct essai" visible dans tout le code
// pour cela on le met ici au debut du code source HORS des fonctions (portée globale)
struct essai
{
  int n;
  float x;
};

// TODO: prototypes des fonctions

int main(void)
{
  // TODO: déclarer une variable toto et l'initialiser

  Afficher(toto);
  // TODO: passer toto pour qu'il soit modifié
  RAZ(...);
  Afficher(toto);

  return 0;
}

// TODO: définitions des fonctions

```

- Écrire une fonction afficher qui affiche les différents champs de la structure passée en argument.
- Écrire une fonction nommée **`RAZ`** permettant de remettre à zéro les 2 champs d'une structure de ce type.
La transmission de l'argument doit se faire par adresse.

## Exercice 2
**IMPORTANT : IL NE FAUT PAS UTILISER DE VARIABLES GLOBALES !**

a) Déclarer les structures **`Personne`** et **`Famille`** adéquates pour mémoriser les informations suivantes: 
- Nom de famille 
- Mere(*)
- Pere(*)
- Fille(*)
- Fils(*)

(*) **`Personne`** ayant un prénom et un âge (entier)

b) Déclarer une variable pour la famille Dupont et l'initialiser d'après cette photo de famille :
{{< figure src="/images/FamilleDupont.png#center" >}}

c) Réaliser et tester une fonction **`AfficheAgeTotal`** qui affichera la somme des âges des membres d'une famille.

**Exemple :**
```
Dupont 86
```

d) Écrire une fonction **`UnAnDePlus`** qui ajoute un an à chacun des membres d'une famille. Vérifier son bon fonctionnement dans un programme.

e) Afficher la taille en octets de la variable représentant la famille Dupont.

f) [AVANCÉ] Réaliser un nouveau projet avec une famille composée d'une mère, d'un père et d'un nombre variable d'enfants auxquels on accèdera par un tableau de pointeurs. Écrire et tester deux fonctions : **`AjouterEnfant(...)`** et **`AfficherFamille(...)`**

# Exercice 3
Compléter le programme donné suivant :

```c
#include <stdio.h>

// NOTE: keep French to keep to exercice.

// TODO: prototypes and declarations

int main(void)
{
  ComplexTy c1, c2, resultat;

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

// TODO: definitions
```

- Définir le type `ComplexTy` avec 2 membres de type réel : reelle, imaginaire
- Ajouter le code à `scanf pour que la saisie d'un nombres complexe ne se fasse qu'au format (r,i) et encapsuler ce code dans une fonction `Saisie`.
- Ajouter les fonctions appelées pour calculer la somme, et la différence de deux nombres complexes.
- Implémenter une fonction `affiche_complexe(…)` pour afficher un nombre complexe sous la forme `(r, i)`, partie réelle et partie imaginaire.

**Note :** on demande d'écrire les déclarations et les fonctions manquantes.