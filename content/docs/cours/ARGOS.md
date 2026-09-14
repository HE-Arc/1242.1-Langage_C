---
title: "ARGOS"
weight: 20
draft: true
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

## Outils CLI pour ARGOS
Un outil en ligne de commande (CLI) est disponible pour faciliter certaines opérations sur ARGOS.
Il est livré avec ARGOS.

{{< a_noter>}}
Il faut mettre à jour son repository local pour bénéficier de cet outil.
Pour cela, suivre la procédure décrite dans la section **Mettre à jour la liste des exercices**.
{{</a_noter>}}

### Installation
**`argos_cli`** nécessite CMake et Ninja pour fonctionner.
 1. Installer CMake : **[CMake for Windows](https://github.com/Kitware/CMake/releases/download/v4.2.0/cmake-4.2.0-windows-x86_64.msi)**.
 2. Installer Ninja : **[https://ninja-build.org/](https://ninja-build.org/)**. Copier le fichier **`ninja.exe`** dans le répertoire **`C:/Ninja`** (par exemple) et ajouter ce répertoire au **`PATH`** de Windows.

**`argos_cli`** est disponible dans le répertoire racine du projet ARGOS.

### Initialiser ARGOS
Pour initialiser ARGOS, exécuter la commande suivante depuis le répertoire racine de votre projet ARGOS :
```
.\argos_cli.exe init
```
Si tout se passe bien, un message de confirmation s'affiche :
```
Initializing ARGOS...Done.
```

### Compiler les exercices
Pour compiler les exercices, exécuter la commande suivante depuis le répertoire racine de votre projet ARGOS :
```
.\argos_cli.exe build
```
Si tout se passe bien, un message de confirmation s'affiche :
```
Building ARGOS...Done.
```

Il est aussi possible de recompiler tous les exercices en utilisant la commande :
```
.\argos_cli.exe rebuild
```

### Lancer les tests
{{< attention>}}
Il faut toujours recompiler les exercices avant de lancer les tests lorsque vous avez modifié le code source des exercices.
{{< /attention>}}

Pour lancer les tests des exercices, exécuter la commande suivante depuis le répertoire racine de votre projet ARGOS :
```
.\argos_cli.exe test
```
Vous obtenez un rapport de test similaire à celui-ci :
```
.\argos_cli.exe test
Testing ARGOS...Done.
🔴 ch01.ch01_ex01_printHelloWorld
🟢 ch01.ch01_ex02_printMathCalc
🟢 ch01.ch01_ex03_SomeCalculus
🟢 ch02.ch02_ex11_Swap
🟢 ch02.ch02_ex21_CelsiusToFarenheit
🟢 ch02.ch02_ex22_AssetInterestRate
🟢 ch04.ch04_ex01_Printf
🟢 ch04.ch04_ex02_ScanfPrintf
🟢 ch04.ch04_ex03_Circle
🟢 ch05.ch05_ex02_LowercaseUppercase
🟢 ch05.ch05_ex03_MultiplicationSign
🟢 ch05.ch05_ex04_DecreasingOutput
🟢 ch05.ch05_ex07_SecondOrderEquation
🟢 ch05.ch05_ex22_CurrencyConverter
🟢 ch05.ch05_ex23_DaysInMonth
🟢 ch05.ch05_ex32_SumProductMean
🟢 ch05.ch05_ex33_Factorial
🟢 ch06.ch06_ex04_Squares
🟢 ch06.ch06_ex06_Calculator
🟢 ch06.ch06_ex07_SumN
🟢 ch06.ch06_ex08_Invert
🟢 ch08.ch08_ex21_1_CompareArray
🟢 ch08.ch08_ex21_2_PrintArray
🟢 ch08.ch08_ex21_3_FillArray
🟢 ch08.ch08_ex21_ArraySum
🟢 ch08.ch08_ex23_Array2DSum
🟢 ch08.ch08_ex24_DotProduct
🟢 ch08.ch08_ex41_Time
🟢 ch08.ch08_ex42_ComplexSum
🟢 ch08.ch08_ex42_ComplexDiff
🟢 ch08.ch08_ex43_Person
🟢 ch09.ch09_ex06_CopyArrays
🟢 ch09.ch09_ex10_Swap
🟢 ch11.ch11_ex02_Reset
🟢 ch11.ch11_ex03_ResetPointer
🟢 ch11.ch11_ex07_EditArray
```

Il est aussi possible de ne tester qu'un ou plusieurs chapitres en particulier en utilisant l'option `--chapters` ou `-c` suivie des numéros des chapitres à tester :
```
.\argos_cli.exe test -c ch01 ch02
```
Vous obtenez un rapport de test similaire à celui-ci :
```
.\argos_cli.exe test -c ch01 ch02
Testing ARGOS...Done.
🔴 ch01.ch01_ex01_printHelloWorld
🟢 ch01.ch01_ex02_printMathCalc
🟢 ch01.ch01_ex03_SomeCalculus
🟢 ch02.ch02_ex11_Swap
🟢 ch02.ch02_ex21_CelsiusToFarenheit
🟢 ch02.ch02_ex22_AssetInterestRate
```

Pour identifier les erreurs dans les tests, vous pouvez utiliser l'option `--verbose` ou `-v` :
```
.\argos_cli.exe test -c ch01 --verbose
```
Ce qui donnera un rapport de test plus détaillé :
```
.\argos_cli.exe test -c ch01 --verbose
Testing ARGOS...

Test project D:/HE-Arc_WorkingFilesSYNC/COURS/ARGOS/benoit-le-callennec/BUILD
    Start 1: ch01.ch01_ex01_printHelloWorld
1/3 Test #1: ch01.ch01_ex01_printHelloWorld ...***Failed    0.02 sec
Running main() from D:/HE-Arc_WorkingFilesSYNC/COURS/ARGOS/benoit-le-callennec/BUILD/_deps/googletest-src/googletest/src/gtest_main.cc
Note: Google Test filter = ch01.ch01_ex01_printHelloWorld
[==========] Running 1 test from 1 test suite.
[----------] Global test environment set-up.
[----------] 1 test from ch01
[ RUN      ] ch01.ch01_ex01_printHelloWorld
D:/HE-Arc_WorkingFilesSYNC/COURS/ARGOS/benoit-le-callennec/UnitTests/ch01/ch01_TEST.cpp:25: Failure
Expected equality of these values:
  expected
    Which is: "hello, world\n"
  actual
    Which is: "hello, fdsaworld\n"

        CHECK ch01_ex01_PrintHelloWorld() output!

[  FAILED  ] ch01.ch01_ex01_printHelloWorld (10 ms)
[----------] 1 test from ch01 (10 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test suite ran. (11 ms total)
[  PASSED  ] 0 tests.
[  FAILED  ] 1 test, listed below:
[  FAILED  ] ch01.ch01_ex01_printHelloWorld

 1 FAILED TEST

    Start 2: ch01.ch01_ex02_printMathCalc
2/3 Test #2: ch01.ch01_ex02_printMathCalc .....   Passed    0.02 sec
    Start 3: ch01.ch01_ex03_SomeCalculus
3/3 Test #3: ch01.ch01_ex03_SomeCalculus ......   Passed    0.01 sec

67% tests passed, 1 tests failed out of 3

Total Test time (real) =   0.10 sec

The following tests FAILED:
          1 - ch01.ch01_ex01_printHelloWorld (Failed)
Errors while running CTest
Done.
🔴 ch01.ch01_ex01_printHelloWorld
🟢 ch01.ch01_ex02_printMathCalc
🟢 ch01.ch01_ex03_SomeCalculus
```

### All in-one
Il est possible de forcer la recompilation et les tests des exercices en une seule commande :
```
.\argos_cli.exe retest
```
Ce qui équivaut à exécuter les commandes suivantes :
```
.\argos_cli.exe clean
.\argos_cli.exe build
.\argos_cli.exe test
```
