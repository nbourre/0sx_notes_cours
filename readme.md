# Notes de cours pour le cours de développement de systèmes embarqués <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Les leçons](#les-leçons)
- [Exercices de rappel](#exercices-de-rappel)
- [Extra](#extra)
- [Révision](#révision)
- [Introduction du cours](#introduction-du-cours)
  - [Les grandes lignes du cours](#les-grandes-lignes-du-cours)

<!-- TODO : Restructurer les fichiers de cours restants -->
# Les leçons
1. [Semaine 01 - Introduction](c01/readme.md)
2. Semaine 02
   1. [Fonctions de base et affichage Série](c02/C02_fonctions_comm.md)
      - [Exercices](c02/C02_fonctions_comm_exo.md)
3. Semaine 03
   1. [Branchement de base](c03/C03a_branchement_base.md)
      - [Exercices](c03/C03a_branchement_base_exo.md)
   2. [Résistance de rappel et de tirage](c03/C03aa_resistance_de_rappel.md)
   3. [millis() au lieu de delay()](c03/C03b_sans_delai.md)
   4. [Logique anti-rebond](c03/C03c_logique_antirebond.md)
4. Semaine 04
   1. Examen et révision
5. Semaine 05
   1. [Fonction `analogRead`](c04/C04a_fonction_analogRead.md)
   2. [Fonction `analogWrite`](c04/C04b_fonction_analogWrite.md)
   3. [Traceur série](c04/C04c_traceur_serie.md)
   4. [Exercices](c04/C04x_exercices.md)
6. Semaine 06
   1. [Composants analogues](c05/c05a_analog/C05a_composants_analogues.md)
   2. [Programmer en tâches](c05/c05b_taches/C05b_programmer_en_taches.md)
7. Semaine 07
   1. [Utilisation de librairies](c06/c06a_lib/readme.md)
   2. [Écran LCD](c06/c06b_lcd/readme.md)
   3. [Capteur ultrasonique](c06/c06c_dht11/C06b_lcd_1602.md)
   4. [Capteur d'humidité](c06/c06d_hcsr04/C06b_lcd_1602.md)
8. Semaine 08
   1. [Machine à états](./c07/c07a_machine_a_etats/readme.md)
   2. [Communication i2c](./c07/c07b_i2c/readme.md)
   3. [Moteur pas-à-pas](./c07/c07c_stepper/readme.md)
   4. [Servomoteur](./c07/c07d_servo/readme.md)
9. Semaine 09
   1. [Lecture du port série](./c08/c08a_serial_read/readme.md)
   2. [Programmation orientée objet base](./c08/c08b_poo_base/readme.md)
   3. [Module de puissance](./c08/c08c_psu/readme.md)
10. [Semaine 10](./c09/readme.md)
    1.  [Moteur DC et contrôleur L293D](./c09/c09a_moteur_dc/readme.md)
    2.  [Machine à états revisitée](./c09/c09b_fsm_revisited/readme.md)
11. [Semaine 11](./c10/readme.md)
    1. [Refactorisation](./c10/c10a_refactorisation/readme.md)
    2. [Module WiFi](./c10/c10b_wifi/readme.md)
12. [Semaine 12](./c11/readme.md)
    1. [Manette IR](./c11/manette_ir/readme.md)
13. Semaine 13
    1.  [Le protocole MQTT](c12/readme.md)

# Exercices de rappel
- [switch-case](exercices/switch_case.md)
- [Les pointeurs](exercices/pointeurs.md)

# Extra
- [Exemples que j'ai utilisé pour le cours](https://github.com/nbourre/0sx_projets_cours)
- [Améliorer son code](extras/ameliorer_son_code.md)
- [Algorithmes utilse](extras/algorithmes.md)
- [Dépannage](extras/depannage.md)
- [Loi d'Ohm](extras/loi_dohm.md)
- [Pointeurs](extras/pointeurs.md)

# Révision
- [Révision pour l'examen](révision/readme.md)

---

# Introduction du cours
Bienvenue dans le cours de développement de systèmes embarqués (420-0SX-SW). Ce cours est donné dans le cadre du programme de diplôme d'étude collégial des techniques de l'informatique du Cégep de Shawinigan. Ce cours est donné en français, mais plusieurs exemples de code seront en anglais.

Ce cours est donné en présentiel, mais les notes de cours sont disponibles en ligne. Vous pouvez les consulter sur GitHub.

Ce cours est donné à la session H24. Les notes de cours sont en cours de rédaction. Les notes de cours seront mises à jour régulièrement.

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