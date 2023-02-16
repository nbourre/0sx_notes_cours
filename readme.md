# Notes de cours pour le cours de développement de systèmes embarqués <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Les leçons](#les-leçons)
- [Extra](#extra)
- [Introduction du cours](#introduction-du-cours)
  - [Les grandes lignes du cours](#les-grandes-lignes-du-cours)

# Les leçons
1. Semaine 01
   1. [Configuration de l'environnement de travail](C01_intro_config.md)
   2. [Introduction à la programmation Arduino](C01_intro_prog.md)
2. Semaine 02
   1. [Fonctions de base et affichage Série](C02_fonctions_comm.md)
      - [Exercices](C02_fonctions_comm_exo.md)
3. Semaine 03
   1. [Branchement de base](C03a_branchement_base.md)
      - [Exercices](C03a_branchement_base_exo.md)
   2. [Résistance de rappel et de tirage](C03aa_resistance_de_rappel.md)
   3. [millis() au lieu de delay()](C03b_sans_delai.md)
   4. [Logique anti-rebond](C03c_logique_antirebond.md)
4. Semaine 04
   1. [Fonction `analogRead`](C04a_fonction_analogRead.md)
   2. [Fonction `analogWrite`](C04b_fonction_analogWrite.md)
   3. [Traceur série](C04c_traceur_serie.md)
   4. [Exercices](C04x_exercices.md)
5. Semaine 05
   1. 

# Extra
- [Loi d'Ohm](extras/loi_dohm.md)

# Introduction du cours
Bienvenue dans le cours de développement de systèmes embarqués (420-0SX-SW). Ce cours est donné dans le cadre du programme de diplôme d'étude collégial des techniques de l'informatique du Cégep de Shawinigan. Ce cours est donné en français, mais plusieurs exemples de code seront en anglais.

Ce cours est donné en présentiel, mais les notes de cours sont disponibles en ligne. Vous pouvez les consulter sur GitHub.

Ce cours est donné à la session H22. Les notes de cours sont en cours de rédaction. Les notes de cours seront mises à jour régulièrement.

Ce cours est donné par M. Nicolas Bourré.

## Les grandes lignes du cours
Ce cours a pour but d'initier l'étudiant à la programmation de système embarqué et plus précisément à la programmation de microcontrôleur. Le microcontrôleur utilisé sera le ATMega2560 d'Atmel sur un Arduino Mega. Le cours couvrira les aspects suivants:
- Initiation à la programmation en C/C++ sur Arduino
- Éléctronique de base adaptée à la programmation de microcontrôleur
- Montage de circuits électroniques sur cartes de prototypage (*breadboard*)
- Utilisation des entrées/sorties numériques et analogiques 
- Utilisation de librairies
- Stratégies de débogage
- Stratégies de programmation (Ex : Fonctions, Tâches, etc.)