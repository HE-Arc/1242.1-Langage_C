---
title: "10 - Allocation dynamique"
weight: 11
---

# CHAPITRE 10 : ALLOCATION DYNAMIQUE

## Cours
[1242.1.10_AllocationDynamique](/pdf/1242.1.10_AllocationDynamique.pdf)

## Quiz
[QUIZ ALLOCATION DYNAMIQUE](https://cyberlearn.hes-so.ch/mod/quiz/view.php?id=761973)

# EXERCICES

## Exercice 1
Écrire un programme qui alloue dynamiquement des emplacements pour des tableaux d'entiers dont la taille est fournie par l'utilisateur.
Les allocations se poursuivront jusqu'à ce que l'on aboutisse à un débordement de mémoire.

{{< hint info >}}
**NOTE :** voir la FAQ [Pourquoi le Task Manager de Windows ne montre pas la mémoire réellement utilisée par mon programme ?](/docs/cours/faq/#pourquoi-le-task-manager-de-windows-ne-montre-pas-la-m%c3%a9moire-r%c3%a9ellement-utilis%c3%a9e-par-mon-programme-).
{{< /hint >}}

**Exemple :**

```c
Enter block size (in MB): 2000
Allocating block number 0, 0[MB]
Allocating block number 1, 2000[MB]
Allocating block number 2, 4000[MB]
Allocating block number 3, 6000[MB]
Allocating block number 4, 8000[MB]
Allocating block number 5, 10000[MB]
Allocating block number 6, 12000[MB]
Allocating block number 7, 14000[MB]
Allocating block number 8, 16000[MB]
Allocating block number 9, 18000[MB]
Allocating block number 10, 20000[MB]
Allocating block number 11, 22000[MB]
Allocating block number 12, 24000[MB]
Allocating block number 13, 26000[MB]
Allocating block number 14, 28000[MB]
Allocating block number 15, 30000[MB]
Allocating block number 16, 32000[MB]
Allocating block number 17, 34000[MB]
Allocating block number 18, 36000[MB]
Allocating block number 19, 38000[MB]
Allocating block number 20, 40000[MB]
Allocating block number 21, 42000[MB]
Allocating block number 22, 44000[MB]
Allocating block number 23, 46000[MB]
Allocating block number 24, 48000[MB]
Allocating block number 25, 50000[MB]
Allocating block number 26, 52000[MB]
Allocating block number 27, 54000[MB]
Allocating block number 28, 56000[MB]
Allocating block number 29, 58000[MB]
Allocating block number 30, 60000[MB]
Allocating block number 31, 62000[MB]
Allocating block number 32, 64000[MB]
Allocating block number 33, 66000[MB]
Allocating block number 34, 68000[MB]
Allocating block number 35, 70000[MB]
Allocating block number 36, 72000[MB]
Allocating block number 37, 74000[MB]
Allocating block number 38, 76000[MB]
Allocating block number 39, 78000[MB]
Allocating block number 40, 80000[MB]
Not enough memory
Total allocated memory: 80.00 [Gigabytes]
```

## Exercice 2
Écrire un programme qui alloue dynamiquement un tableau d'entiers.

1. La taille du tableau est saisie au clavier.
2. Le tableau est alloué dynamiquement.
3. Le tableau est rempli avec des valeurs aléatoires entre 32 et 126.
4. Parcourir le tableau et afficher les valeurs et les adresses du tableau, i) avec un formalime tableau; ii) avec un formalisme pointeur; iii) avec un pointeur incrémenté.
5. **[AVANCÉ]** idem que le point 4., mais en considérant que le tableau contient des caractères.
6. Libèrer la mémoire.

**Exemple (sans la partie avancée) :**
```
Please enter a number: -1
Please enter a number: a
Please enter a number: 4
==========  Printing array as array
0000000000761470 => 108
0000000000761474 => 110
0000000000761478 => 43
000000000076147C => 38
==========  Printing array as pointer
0000000000761470 => 108
0000000000761474 => 110
0000000000761478 => 43
000000000076147C => 38
==========  Printing array as incremented pointer
0000000000761470 => 108
0000000000761474 => 110
0000000000761478 => 43
000000000076147C => 38
```

## Exercice 3 (transféré à la série 11)

## Exercice 4
Même exercice que le 2) mais avec un tableau à 2 dimensions.

**Exemple :**

```
Please enter matrix dimensions (M N): a b
Please enter matrix dimensions (M N): -1 3
Please enter matrix dimensions (M N): 5 3
==========  Printing matrix as array
0000000000CC14C0 => 40
0000000000CC14C4 => 107
0000000000CC14C8 => 112
0000000000CC14E0 => 66
0000000000CC14E4 => 71
0000000000CC14E8 => 123
0000000000CC1500 => 95
0000000000CC1504 => 43
0000000000CC1508 => 54
0000000000CC1520 => 103
0000000000CC1524 => 55
0000000000CC1528 => 61
0000000000CC1540 => 36
0000000000CC1544 => 65
0000000000CC1548 => 53

40      107     112
66      71      123
95      43      54
103     55      61
36      65      53

==========  Printing matrix as pointer
0000000000CC14C0 => 40
0000000000CC14C4 => 107
0000000000CC14C8 => 112
0000000000CC14E0 => 66
0000000000CC14E4 => 71
0000000000CC14E8 => 123
0000000000CC1500 => 95
0000000000CC1504 => 43
0000000000CC1508 => 54
0000000000CC1520 => 103
0000000000CC1524 => 55
0000000000CC1528 => 61
0000000000CC1540 => 36
0000000000CC1544 => 65
0000000000CC1548 => 53

40      107     112
66      71      123
95      43      54
103     55      61
36      65      53

==========  Printing matrix as incremented pointer
0000000000CC14C0 => 40
0000000000CC14C4 => 107
0000000000CC14C8 => 112
0000000000CC14E0 => 66
0000000000CC14E4 => 71
0000000000CC14E8 => 123
0000000000CC1500 => 95
0000000000CC1504 => 43
0000000000CC1508 => 54
0000000000CC1520 => 103
0000000000CC1524 => 55
0000000000CC1528 => 61
0000000000CC1540 => 36
0000000000CC1544 => 65
0000000000CC1548 => 53

40      107     112
66      71      123
95      43      54
103     55      61
36      65      53
```

## [AVANCÉ] Exercice 5
Même exercice que le 2) mais avec un tableau à 3 dimensions.

## [AVANCÉ] Exercice 6
Écrire un programme qui lit 10 phrases d'une longueur maximale de 200 caractères au clavier et qui les mémorise dans un tableau de pointeurs sur `char` en réservant dynamiquement l'emplacement en mémoire pour les chaînes.
Ensuite, l'ordre des phrases est inversé en modifiant les pointeurs et le tableau résultant est affiché.
