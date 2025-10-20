---
title: "ARGOS"
weight: 20
draft: false
---

# ARGOS : un système d'auto-Évaluations

## Récupérer le code source

1. Se rendre sur **[le git d'ARGOS contenant les exercices auto-évaluer](https://gitlab-etu.ing.he-arc.ch/isc/argos/argos-exercices)**.
2. Cliquer sur le bouton **`Fork`** :
{{< figure src="images/AE_Fork.png#center" >}}
3. Dans le champ **`Project name`**, remplacer **`Argos Exercices`** par votre prénom suivi de votre nom (voir Figure ci-dessous).
4. Dans le champ **`Select a namespace`**, chercher le nom de votre groupe. La première suggestion devrait être de la forme **`isc/argos/argos-etudiants/2025-2026/<groupe>)`** (voir Figure ci-dessous).
{{< figure src="images/AE_ForkedProject.png#center" >}}

{{< attention >}}
Bien laisser la visibilité du projet sur **`Internal`**.
{{< /attention >}}

5. Cliquer sur le bouton **`Fork project`**.
6. Cloner son repository.
7. Entrer ses informations en éditant le fichier **`Options/student_profile.json`**, comme par exemple :
```json
{
    "firstname": "Benoit",
    "lastname": "Le Callennec",
    "pseudo": "BLC",
    "year": 2025,
    "email": "benoit.lecallennec@he-arc.ch",
    "image": "BLC.png",
    "opt-out": false,
    "group": "group"
}
```
8. Faire un commit et un push pour mettre à jour son repository.

{{< attention >}}
Il faut toujours travailler sur la branche **`main`**.
{{< /attention >}}

## Consulter son dashboard
Un dashboard est disponible pour chaque étudiant sur le gitlab de la HE-Arc.
Il est accessible en cliquant sur Pages, dans l'onglet Deploy :
{{< figure src="images/AE_DashboardEtudiantsLink.png#center" >}}

Il ressemble à ça :
{{< figure src="images/AE_DashboardEtudiants.png#center" >}}

{{< a_noter>}}
Le dashboard peut prendre plusieurs minutes à générer les pages en fonction de la charge.
{{< /a_noter >}}

## Faire un exercice
1. Localiser les balises **`// TODO`** dans le code source.
2. Compléter le code source selon la donnée de l'exercice.
3. Compiler votre code avec **`gcc`**.
4. Lancer l'exécutable généré (**`./a.exe`** par défaut sous Windows) et tester que le résultat est correct.
5. Répéter les étapes 2 à 4 jusqu'à ce que le résultat soit correct.

## Valider un exercice
1. Faire un commit par exercice complété.
Il est important de bien nommer le commit avec un message clair et concis.
2. Faire un push sur votre repository.
3. Se rendre sur votre repository sur le gitlab de la HE-Arc et attendre que le pipeline se termine :
{{< figure src="images/AE_WaitingForPipeline.png#center" >}}
4. Si les tests des exercices ne passent pas, il faut choisir l'étape qui a échoué pour avoir plus de détails.
{{< figure src="images/AE_PipelineFailed.png#center" >}}
5. Les logs complets ressemblent à ce qui suit.

{{< a_noter>}}
Les tests qui ont échoué sont indiqués en surbrillance.
{{</a_noter>}}

{{< figure src="images/AE_PipelineTestFailedDetails.png#center" >}}

## Mettre à jour la liste des exercices
Au fur et à mesure de l'année, de nouveaux exercices seront ajoutés.
Le cas échéant, lorsqu'une mise à jour est disponible, un message s'affiche en haut de la page.

Pour mettre à jour votre repository local, il faut :
1. Cliquer sur le bouton **`Update fork`** pour mettre à jour son repository en ligne comme indiqué sur la figure ci-dessous :
{{< figure src="images/AE_UpdateAvailable.png#center" >}}
2. Mettre à jour son repository local en exécutant, depuis un Terminal dans Visual Studio Code, la commande **`git pull --rebase`**.

{{< attention >}}
Il ne faut modifier aucun autre fichier dans le répertoire **`UnitTests`**.
{{< /attention >}}
