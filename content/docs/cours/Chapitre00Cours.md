---
title: "0  - Organisation du cours"
weight: 1
---

# CHAPITRE 0 : Organisation du Cours

## Slides
{{<pdf src="/pdfs/1242.1.00_OrganisationDuCours.pdf" >}}

<!-- {{< embed-pdf url="/pdf/1242.1.00_OrganisationDuCours.pdf" >}}-->

## Installation de l'environnement de développement

{{< hint info >}}
Ce qui suit est extrait du tutoriel accessible **[ici](https://code.visualstudio.com/docs/cpp/config-mingw)**.
{{< /hint >}}

1. Installer **[Visual Studio Code](https://code.visualstudio.com/)**
2. Installer les **[extensions Visual Studio Code recommandées pour le C](/docs/cours/faq/#quelles-sont-les-extensions-vs-code-recommandées-pour-le-c-)**
3. Télécharger et installer **[MSYS2 ](https://www.msys2.org/)**.

{{< hint danger >}}
**ATTENTION :**  l'installeur s'affiche mal avec le thème sombre de Windows. 
{{< /hint >}}

4. Lancer MSYS2. Il doit se lancer automatiquement après l'installation si vous avez coché la case correspondante.
5. Copier-coller et exécuter la commande suivante : **`pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain`** dans le terminal MSYS2.

{{< hint info >}}
**Répondez yes / all / default quand c'est demandé**
{{< /hint >}}

6. Ajouter le chemin vers gcc dans les variables d'environnement (**`C:\msys64\ucrt64\bin`** par défaut).
   1. Clique droit sur **Ce PC** puis **Propriétés**.
   2. Cliquez sur **Paramètres système avancés**.
   3. Cliquez sur **Variables d'environnement**.
   4. Dans la section **Variables système**, sélectionnez la variable **Path** puis cliquez sur **Modifier**.
   5. Cliquez sur **Nouveau** et ajoutez le chemin vers gcc.
7. Relancer Visual Studio Code, ouvrir un nouveau terminal exécuter **`gcc --version`**. Si tout est correctement installé, vous devriez voir la version de gcc s'afficher.

## Commandes basiques du Terminal Visual Studio Code

- **`ls`** : liste les fichiers et dossiers du répertoire courant.
- **`cd nom_dossier`** : se déplace dans le dossier **`nom_dossier`**.
- **`cd ..`** : remonte au dossier parent.
- **`mkdir nom_dossier`** : crée un dossier **`nom_dossier`**.
- **`pwd`** : affiche le chemin du répertoire courant.
- **`clear`** : efface le terminal.
- **`exit`** : ferme le terminal.

{{< hint warning >}}
**IMPORTANT :** les fichiers et les dossiers sont placés dans la corbeille lorsqu'ils sont supprimés.

- **`rm nom_fichier`** : supprime le fichier **`nom_fichier`**.
- **`rm -r nom_dossier`** : supprime le dossier **`nom_dossier`** et son contenu.
{{< /hint >}}

{{< hint warning >}}
**IMPORTANT :** bien noter les **``.\``** devant le nom de l'exécutable s'il se trouve dans le répertoire courant.

- **`./nom_executable`** : exécute l'exécutable **`nom_executable`**.
{{< /hint >}}
- **`where.exe nom_executable`** : affiche le chemin de l'exécutable **`nom_executable`**. Cette commande est très utile pour vérifier qu'on utilise bien le bon exécutable.
  
## Commandes basiques de **``gcc``**
{{< hint info >}}
Les commandes suivantes sont à exécuter dans le terminal.
Nous irons plus en détail sur l'utilisation de **`gcc`** dans le chapitre dédié.
{{< /hint >}}

- **`where.exe gcc`** : affiche le chemin de l'exécutable **`gcc`**.
- **`gcc --version`** : affiche la version de gcc installée.
- **`gcc nom_fichier.c`** : compile le fichier **`nom_fichier.c`** en un exécutable **`a.exe`** (sous Windows).
- **`gcc -o nom_executable nom_fichier.c`** : compile le fichier **`nom_fichier.c`** en un exécutable **`nom_executable`**.
- **`gcc -Wall -o nom_executable nom_fichier.c`** : compile le fichier **`nom_fichier.c`** en un exécutable **`nom_executable`** en affichant tous les warnings.
- **`gcc -Wall -Werror -o nom_executable nom_fichier.c`** : compile le fichier **`nom_fichier.c`** en un exécutable **`nom_executable`** en affichant tous les warnings et en traitant les warnings comme des erreurs.
