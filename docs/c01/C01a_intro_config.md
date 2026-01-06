# Les premiers pas
> "Un éléphant, ça se mange une bouchée à la fois." - Proverbe africain

---

## Moodle
Pour avoir accès à certaines de mes notes ou évaluations, vous devrez avoir un compte Moodle et être inscrit à mon cours.

- **Lien vers le cours** : [Moodle](https://ena.cshawi.ca/course/view.php?id=19)
- **Code pour le cours** : `Groupe1!` (lundi pm) ou `Groupe2!` (mardi am)

<!-- #### Teams
Pour avoir accès à certaines de mes notes Office, vous devez être dans le Teams du cours.

- **Lien vers [Teams](https://teams.microsoft.com/l/team/19%3aMAZuLdF2Thx9FkXHF9_mGFCZCWK-L2k1FJXH2zkjL7k1%40thread.tacv2/conversations?groupId=d000a4c4-3d3d-4b05-af28-3d69589e53d3&tenantId=b03caa02-c798-45ad-a2bd-41c7e4851423)** -->

## Installation de Git
Vous devrez installer l'application Git sur votre ordinateur. Git est un logiciel de gestion de versions. Il est utilisé pour suivre les modifications apportées à un projet.

Il s'agit d'un outil **primordial pour les développeurs**. Vous devrez l'utiliser très fréquemment tout au long de votre parcours. Vous aurez un cours sur Git plus tard dans votre parcours.

### Tester si Git est déjà installé
1. Ouvrir un terminal
   1. Sur Windows, appuyez sur <kbd>Win</kbd> + <kbd>R</kbd>, tapez `cmd` et appuyez sur `Enter`.
2. Tapez la commande suivante et appuyez sur `Enter` :
   ```bash
   git --version
   ```
   
  ![alt text](assets/git_version.gif)

3. Si Git est installé, vous devriez voir la version de Git s'afficher. Sinon, vous verrez un message d'erreur et vous devrez installer Git.


### Installation de Git (Si nécessaire)

Vous pouvez le télécharger [**ici**](https://git-scm.com/).

https://github.com/user-attachments/assets/80e18aa8-df44-4598-b647-29d3efd276d4

## Compte GitHub
Si vous n'en n'avez pas encore, vous devez créer un compte GitHub. Vous pouvez le faire [**ici**](https://github.com/).

GitHub est un site permettant aux développeurs de partager leur code. Il est utilisé par de nombreux développeurs et est un outil très utile pour les projets de programmation. D'ailleurs, plusieurs enseignants utilisent GitHub pour partager leurs codes avec leurs étudiants.

Tout au long de votre parcours académique, vous devrez créer des projets et les envoyer sur GitHub. Vous devrez aussi cloner des projets de vos profs et les modifier.

## Logiciels
Vous devez installer le logiciel Arduino sur votre ordinateur. Vous pouvez le télécharger [ici](https://www.arduino.cc/en/Main/Software).

Vous devez télécharger la version Windows avec MSI Installer. Cliquez sur le lien pour télécharger le fichier. Une fois le fichier téléchargé, lancez l'installation.

## Configuration du matériel
Vous avez devant vous une plaque de développement Arduino. Il s'agit du même kit que vous devez vous procurer pour ce cours. Il est composé de deux parties : la carte Arduino et la plaque de support.

Branchez le câble USB de la carte Arduino à votre ordinateur. Vous devriez voir une petite lumière verte s'allumer sur la carte. Cela signifie que la carte est alimentée. Toutefois, cela ne signifie pas que la carte est prête à être utilisée.

En effet, on doit s'assurer que les pilotes sont installés.

Pour vérifier si les pilotes sont installés, ouvrez le logiciel Arduino. Vous devriez voir une fenêtre comme celle-ci :

![Alt text](assets/arduino_ide.png)

Maintenant, sélectionnez la barre défilante située dans la barre d'outils.

![Alt text](assets/arduino_ide_board.gif)

Si les pilotes sont installés, vous devriez voir dans la liste déroulante le nom de votre carte Arduino avec le port qui lui est assigné. Dans mon cas, c'était "Arduino Mega or Mega 2560" sur le `COM26` de mon ordinateur. Le numéro du port peut varier selon votre ordinateur.

> **Note :** `COM` est le préfixe donné pour les ports de communication sur les PC Windows. Il peut y avoir plusieurs ports de communication sur un ordinateur. Ceux-ci sont utilisés pour connecter des périphériques externes à l'ordinateur. Par exemple, un clavier, une souris, une imprimante, etc. Les numéros sont attribués en fonction de l'ordre de connexion des périphériques.

## Installation des pilotes - Si nécessaire
Généralement, Windows installe les pilotes automatiquement. Cependant, si ce n'est pas le cas, vous devez installer les pilotes manuellement.

Je vous invite à suivre la procédure sur ce site (Anglais): [Sparkfun - How to install CH340 Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all)

---

## À propos de cette leçon
Cette leçon n'enseigne pas vraiment l'électronique. Elle sert plutôt à s'assurer que tout est prêt pour les prochaines leçons. Elle permettra de vérifier que la carte fonctionne comme prévu et que l'ordinateur que vous utilisez est compatible.

Considérez ce tutoriel comme la "base" de votre voyage. Si les choses se compliquent, revenez ici et revérifiez cette leçon!

L'une des compétences les plus importantes que vous devrez apprendre est que, lorsque les choses tournent mal (et il y en aura beaucoup), vous devez revenir aux hypothèses les plus fondamentales. C'est un peu l'équivalent du "tu es sûr que c'est allumé" en électronique. Il est surprenant de voir combien d'ingénieurs qualifiés passent des heures à déboguer un circuit pour se rendre compte que... ce n'était pas branché!

J'ai fait un petite procédure de dépannage pour l'Arduino. Vous pouvez la consulter [ici](../extras/depannage.md). Celle-ci sera nourrie au fur et à mesure que nous avancerons dans le cours.

---

## Les communautés Arduino
Avant de débuter, je vous invite à vous joindre une des différentes communautés Arduino. Ce sont pour la plupart des communautés très actives et il y a beaucoup de ressources disponibles.

Voici une liste de différentes communautés Arduino. Vous pouvez les consulter pour trouver des projets intéressants à faire ou encore trouver de l'aide pour vos projets.

- [Serveurs Discord - Français](https://disboard.org/servers/tag/arduino?fl=fr)
  - [Anglais](https://disboard.org/servers/tag/arduino?fl=en)
- [Reddit - Arduino](https://www.reddit.com/r/arduino/)
- [Youtube - Ingéniérie et Projets](https://www.youtube.com/@Ingenierie-Projets)
  - L'ordre de la playlist n'est pas fameuse
- [Zeste de Savoir - Arduino](https://zestedesavoir.com/tutoriels/686/arduino-premiers-pas-en-informatique-embarquee/)
  - [Playlist Youtube](https://www.youtube.com/playlist?list=PLNBsspAtBwlL7lw9HI50YE3WJKY5us-cn)

---


## Qu'est-ce qu'un Arduino?

Arduino est le nom de la petite carte de circuit électronique que vous allez utiliser comme outil pour étudier et explorer la programmation et l'électronique.

Elle est fabriquée par arduino.cc, une société dirigée par Massimo Banzi, PDG d'Arduino. Voici comment ils se décrivent :

> Arduino est une plateforme de prototypage open-source basée sur du matériel et des logiciels faciles à utiliser. Les cartes Arduino sont capables de lire des entrées - de la lumière sur un capteur, un doigt sur un bouton ou un message Twitter - et de les transformer en une sortie - activer un moteur, allumer une LED, publier quelque chose en ligne. Vous pouvez indiquer à votre carte ce qu'elle doit faire en envoyant un ensemble d'instructions au microcontrôleur de la carte. Pour ce faire, vous utilisez le langage de programmation Arduino (basé sur Wiring), et le logiciel Arduino (IDE).
> 
> Au fil des ans, Arduino a été le cerveau de milliers de projets, des objets du quotidien aux instruments scientifiques complexes. Une communauté mondiale de  fabricants - étudiants, amateurs, artistes, programmeurs et professionnels - s'est rassemblée autour de cette plateforme open-source. Leurs contributions ont permis d'accumuler une quantité incroyable de connaissances accessibles qui peuvent être d'une grande aide pour les novices comme pour les experts.

**TL;DR :** Arduino est une carte de circuit électronique qui peut être programmée pour faire des choses. Il y a une communauté de gens qui partagent leurs projets et leurs connaissances sur Arduino.

> **Jargon web** :
> tl;dr : "too long; didn't read" - "trop long, j'ai pas lu" - en gros, c'est une abréviation pour dire que le texte est trop long et que vous n'avez pas le temps de le lire. C'est une expression utilisée sur internet pour dire que vous n'avez pas le temps de lire un texte trop long. **On l'utilise aussi pour signifier un résumé d'un texte trop long.**

### Quel Arduino?
Au cours des dix années qui ont suivi la sortie d'Arduino, il y a eu une énorme prolifération de centaines de "cartes Arduino" différentes disponibles. D'un côté, il existe un Arduino pour chaque type d'application spécialisée, mais d'un autre côté, cela peut devenir assez confus!

Dans ce cours, nous allons nous concentrer sur l'**Arduino Mega** qui est un Arduino plus puissant que l'Arduino UNO. Elle est en fait sa grande soeur. Elle est plus puissante et plus rapide avec une tonne de mémoire et de broches en plus, et une puce différente, l'ATmega2560. C'est une bonne mise à jour lorsqu'un projet ne rentre plus dans un UNO.

![Alt text](assets/arduino_mega.jpg)

Au fur et à mesure, vous découvrirez qu'il y a peut-être d'autres compatibles Arduino que vous pourriez vouloir !

<table>
  <tr>
    <td>
      <img src="assets/arduino_50-07.jpg"/>
    </td>
    <td>L'Arduino UNO est un classique, elle est de loin la plus populaire. Elle est basique et bien supportée.</td>
  </tr>
  <tr>
    <td>
      <img src="assets/arduino_micro.jpg"/>
    </td>
    <td>L'Arduino Micro, par contre... est un peu plus petit! Il a une puce Atmega32u4 différente qui peut faire de l'USB natif et peut donc agir comme un clavier ou une souris. Il est fin et possède des connecteurs à broche descendante pour pouvoir le brancher sur une planche à pain.</td>
  </tr>
  <tr>
    <td>
      <img src="assets/arduino_mkr1000.jpg"/>
    </td>
    <td>L'Arduino MKR1000 ressemble un peu à un Arduino Micro mais possède une puce ATSAM ARM 32 bits plus puissante et un WiFi intégré! Une excellente mise à niveau pour les projets liés à l'Internet des objets.</td>
  </tr>
  <tr>
    <td>
      <img src="assets/arduino_flora.png"/>
    </td>
    <td>Il y a aussi les Arduino-compatibles comme le Flora qui est fabriqué par Adafruit. C'est un Arduino rond et portable et plutôt que d'utiliser des fils, vous pouvez le coudre dans les vêtements pour des projets électroniques portables.</td>
  </tr>
</table>

### Raspberry Pi
Certains d'entre vous ont peut-être déjà entendu parler du Raspberry Pi ou même en possèdent un. Toutefois, il s'agit d'un tout autre type de carte que l'Arduino.

Le Raspberry Pi (rpi) est une carte de développement qui est très populaire pour les projets de programmation. Il est plus puissant que l'Arduino et peut être utilisé pour faire beaucoup de choses tel qu'un serveur web, de musique, de vidéos, etc. Il est également beaucoup plus cher que l'Arduino.

En plus des différentes versions, il y a plusieurs éditions de rpi.

- Raspberry Pi : Ordinateur sur carte (SBC : Single Board Computer) avec différents modèles de RAM et de stockage.
- Raspberry Pi Zero : Comme le Raspberry Pi, mais plus petit, moins cher et moins puissant.
- Raspberry Pi Zero W : Comme le Zero, mais avec un module WiFi et Bluetooth intégré.
- Raspberry Pi 400 : Comme le Raspberry Pi, mais avec un clavier intégré.
- Raspberry Pi Pico : Il s'agit d'une carte de développement avec un microcontrôleur similaire au Arduino Nano, mais plus puissant.
- Raspberry Pi Pico W : Comme le Pico, mais avec un module WiFi et Bluetooth intégré.

Nous sommes rendu à la 5e version du rpi.

### Autres microcontrôleurs
Il existe des milliers de microcontrôleurs différents sur le marché. Chacun a ses propres avantages et inconvénients. Certains sont plus puissants, d'autres sont plus petits, d'autres sont plus économes en énergie, etc.

Pour les débutants et hobbyistes, on retrouve souvent les microcontrôleurs suivants :
- **ESP32** : Il s'agit d'un microcontrôleur plus puissant que l'ESP8266. Il possède un module WiFi et Bluetooth intégré. On le retrouve souvent dans les appareils connectés.
- **RP2040** : Il s'agit du microcontrôleur du Raspberry Pi Pico. Il est très puissant et peu coûteux.

![alt text](assets/introduction-to-microcontrollers-3.png.webp)

---

## Différence entre un microcontrôleur et un microprocesseur
Les termes **microprocesseur** et **microcontrôleur** sont souvent utilisés de manière interchangeable. Toutefois, bien qu'ils partagent des similitudes, ils possèdent des différences fondamentales qui influencent leur usage dans divers domaines.

### Définition générale
#### Microprocesseur (CPU)
Un **microprocesseur** est un circuit intégré servant d’unité centrale de traitement (**CPU**) pour un ordinateur ou un système embarqué. Il exécute des instructions en effectuant des opérations arithmétiques et logiques sur des données numériques.

- **Caractéristiques** :
  - Nécessite des composants externes pour fonctionner (RAM, ROM, interfaces d'entrée/sortie).
  - Hautes performances, capable d’exécuter plusieurs tâches simultanément.
  - Présent dans les **ordinateurs**, **serveurs**, **tablettes**, et **smartphones**.

#### Microcontrôleur (MCU)
Un **microcontrôleur** est un système intégré sur une seule puce qui regroupe :
- Un processeur.
- De la mémoire (RAM et ROM).
- Des interfaces d'entrée/sortie.

- **Caractéristiques** :
  - Conçu pour exécuter une tâche **spécifique** en temps réel.
  - Intégration optimisée pour des applications autonomes.
  - Utilisé dans les **appareils embarqués** comme les **machines à laver**, **robots**, **systèmes de contrôle industriel**.

#### Résumé des différences
| Critère             | Microprocesseur | Microcontrôleur |
|---------------------|----------------|----------------|
| **Unité de calcul** | CPU seul       | CPU + RAM/ROM + E/S intégrés |
| **Mémoire**         | Externe        | Intégrée |
| **Utilisation**     | Systèmes complexes (PC, serveurs) | Tâches spécifiques (automobile, domotique) |
| **Consommation**    | Élevée         | Faible |
| **Coût**           | Plus cher      | Peu coûteux |

---

### Comparaison détaillée
#### 1. Puissance de calcul
- **Microprocesseur** : Très performant avec des fréquences d’horloge allant de 1 à 4 GHz. Optimisé pour **le multitâche et les traitements lourds**.
- **Microcontrôleur** : Fréquences bien plus faibles (généralement quelques MHz à centaines de MHz). Suffisant pour des **opérations en temps réel**.

#### 2. Gestion de la mémoire
- **Microprocesseur** :
  - Dépend d’une mémoire **externe** (RAM, ROM, SSD, etc.).
  - Permet une **grande flexibilité** dans la gestion des ressources.
- **Microcontrôleur** :
  - Mémoire **intégrée**, souvent limitée à quelques **Ko à Mo**.
  - L’accès mémoire est plus rapide grâce à son **intégration sur la puce**.

#### 3. Système d’exploitation
- **Microprocesseur** :
  - Nécessite un **système d’exploitation** (Windows, Linux, Android).
  - Conçu pour gérer **plusieurs processus simultanément**.
- **Microcontrôleur** :
  - Fonctionne généralement **sans OS**, avec un **micrologiciel** dédié.
  - Peut utiliser un **RTOS (Real-Time Operating System)** pour des applications plus complexes.

#### 4. Consommation d’énergie
- **Microprocesseur** :
  - Consommation **élevée** (plusieurs watts à dizaines de watts).
  - Nécessite un **système de refroidissement**.
- **Microcontrôleur** :
  - **Très économe** en énergie (quelques mW à W).
  - Idéal pour les **appareils alimentés par batterie**.

#### 5. Coût
- **Microprocesseur** : Cher (de **50$ à plusieurs centaines** selon la performance).
- **Microcontrôleur** : Peu coûteux (**moins de 1$ à quelques dizaines de dollars**).

#### Applications types
| Type de Système | Microprocesseur | Microcontrôleur |
|----------------|----------------|----------------|
| **PC et Serveurs** | ✅ | ❌ |
| **Smartphones/Tablettes** | ✅ | ❌ |
| **Thermostats, machines à laver** | ❌ | ✅ |
| **Automobile (ABS, capteurs, etc.)** | ❌ | ✅ |
| **Domotique et IoT** | ❌ | ✅ |

---

#### Exemples concrets
| Composant | Type | Caractéristiques | Prix Approx. |
|-----------|------|-----------------|-------------|
| **AMD Ryzen 7 9800X3D** | Microprocesseur | 8 cœurs, 5 GHz, multi-threading | ~700$ |
| **ATmega328P (Arduino Uno)** | Microcontrôleur | 16 MHz, 2 KB RAM, 32 KB Flash | ~3$ |
| **ESP32** | Microcontrôleur | WiFi, Bluetooth, 240 MHz, 520 KB RAM | ~6$ |

---

### Conclusion
Les **microprocesseurs** sont parfaits pour des systèmes nécessitant **beaucoup de puissance et de flexibilité**, tandis que les **microcontrôleurs** sont optimisés pour **les systèmes autonomes** nécessitant **une faible consommation d’énergie** et une exécution **en temps réel**.

Ainsi, dans le cadre de vos cours en robotique et systèmes embarqués, l’apprentissage et l’usage des **microcontrôleurs** comme ceux présents sur **Arduino** sont essentiels, car ils répondent aux exigences de **temps réel**, **faible consommation** et **coût réduit** nécessaires aux systèmes autonomes.

---

## Le matériel du cours

### Achat
Pour ce cours, vous aurez besoin d'un kit d'Arduino Mega sur plaque de montage et d'un ordinateur. Voici les liens pour acheter les items requis sur Amazon:
- [Arduino Mega](https://a.co/d/5wpBN96).
- [Plaque de support pour Arduino](https://a.co/d/fz2aTpk).
  - [Modèle alternatif A](https://a.co/d/cIoFSkc)
  - [Modèle alternatif B](https://a.co/d/6WJCW0G) : Ce modèle vient avec du matériel pour le Raspberry Pi.

---

## Exercices
1. Branchez la carte Arduino à votre ordinateur.
2. Ouvrez le logiciel Arduino IDE.
3. Trouvez l'exemple "Blink". Où est-il situé?
4. Téléversez l'exemple "Blink" sur la carte Arduino.
   - Avez-vous réussi du premier coup? Sinon, trouvez la solution au problème.
5. Essayez de comprendre le code de l'exemple "Blink".
6. Selon vous, que fait le code de l'exemple "Blink"?

---

## Exemple de questions pour une évaluation
1. Nommez deux raisons pour lesquelles, il serait mieux d'utiliser un rpi au lieu d'un Arduino.
2. Nommez deux raisons pour lesquelles, il serait mieux d'utiliser un Arduino au lieu d'un rpi.
3. Combien de broches numériques y a-t-il sur une carte Arduino Mega?
4. Combien de broches analogiques y a-t-il sur une carte Arduino Mega?
5. Nommez 2 logiciels qui peuvent être utilisés pour programmer une carte Arduino?

<details><summary>Réponses</summary>

1. Le rpi est plus puissant et peut donc faire plus de choses. Il est aussi plus facile de le connecter à un écran et à un clavier. Il vient avec un système d'exploitation. Il vient avec les connexions réseaux.
2. L'Arduino est moins cher. L'Arduino est plus économique en énergie. L'Arduino est plus petit et plus facile à transporter. L'Arduino est plus facile à programmer.
3. 54
4. 16
5. Arduino IDE, Visual Studio Code avec l'extension PlatformIO. 

</details>

---
## Pour les curieux

[![Thumbnail](https://img.youtube.com/vi/Tak8Pz4GSn8/0.jpg)](https://www.youtube.com/watch?v=Tak8Pz4GSn8)

Je vous suggère la chaîne Youtube de [Deus Ex Silicium](https://www.youtube.com/@dexsilicium). Il fait des vidéos sur l'électronique des appareils de la vie de tous les jours en analysant les composants électroniques en profondeur. C'est très intéressant!

---

## Références
- [Ladyada's Learn Arduino - Lesson ##2](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-2)
- [All3DP : Microprocessor vs Microcontroller](https://all3dp.com/2/difference-between-microprocessor-and-microcontroller/)
