---
title: "Cherry-Pick des modifications vers les exercices"
weight: 1
draft: false
tags: ["git", "ARGOS"]
---
{{< hint danger >}}
**ATTENTION :** cet article s'addresse aux développeurs d'ARGOS qui ont les droits pour faire des modifications sur les exercices.
Les étudiants ne doivent pas suivre ces instructions.
{{< /hint >}}

**`argos-exercices`** : repository de base pour les étudiants. Ils forkent ce repository pour faire les exercices.

**`argos-solutions`** : repository contenant les solutions des exercices. Les étudiants n'ont pas accès à ce repository.

Quand on souhaite ajouter des exercices (et tester les solutions), il est nécessaires de travailler sur **`argos-solutions`**.
Une fois des modifications testées et validées, il faut encore les reporter dans **`argos-exercices`** pour que les étudiants puissent y avoir accès.

{{< hint warning >}}
**REMARQUE :** Il est fortement déconseillé de copier-coller les modifications ou de faire un merge request, pour éviter de porter toutes les solutions vers les exercices par mégarde.
Il est donc préférable de le faire "à la main".
{{< /hint >}}

Les étapes à suivre sont les suivantes :
1. Se rendre dans le repository des exercices (celui qui sert d'origine pour les étudiants) :

      **`cd argos-exercices`** 

2. Ajouter **`argos-solutions`** en tant que remote (sous le nom **`solutions`**) :

      **`git remote add solutions argos-solutions`**

3. Récupérer les modifications de **`solutions`** :

      **`git fetch solutions`**

4. Récupérer le hash du commit que l'on souhaite cherry-pick de **`solutions`** :

      **`git log solutions/main -3 --patch`** (pour afficher les détails des 3 derniers commits).

1. Cherry-pick les modifications du commit souhaité sur la branche actuelle :

      **`git cherry-pick <commit-hash>`**

6. Résoudre les conflits si nécessaire. Il ne devrait pas y en avoir si les modifications sont bien faites.

7. Push les modifications sur le repository des exercices :

      **`git push origin main`**

8. Supprimer le remote **`solutions`** :
  
      **`git remote remove solutions`**

9. Vérifier que **`solutions`** n'est plus listé comme remote :

      **`git remote -v`**

10. Vérifier que les modifications sont bien présentes sur le repository des exercices.