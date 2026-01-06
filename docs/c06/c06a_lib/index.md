# Les librairies

---

## Introduction
Imaginons que vous vouliez faire un programme avec 1 seul bouton pour exécuter 3 actions différentes.

Par exemple, un montage avec 1 seul bouton pour allumer une DEL.
- 1 clic allume/éteint la DEL
- 2 clics fait clignoter la DEL rapidement
- 3 clics fait graduellement changer la luminosité de la DEL

Comment procéderiez-vous pour réaliser ce programme?

La logique de la gestion du bouton peut être complexe. Il faut gérer les états du bouton, les délais, etc.

**Un outil important pour simplifier le développement de projets, ce sont les librairies.**

Les librairies Arduino sont des ensembles de codes et de fonctions qui permettent d'ajouter de nouvelles fonctionnalités à votre projet. Elles ont été créées pour simplifier la tâche de programmation en offrant des fonctions déjà écrites pour l'utilisateur à utiliser dans son propre programme. Les librairies Arduino sont généralement créées par les utilisateurs d'Arduino ou par la communauté Arduino elle-même.

Avec un peu plus d'expérience, vous pourriez éventuellement écrire vous-même les librairies pour vos projet.

## Exemples de librairies Arduino
Voici quelques exemples de librairies Arduino courantes :

- `OneButton` : Cette librairie ajoute des fonctionnalités pour contrôler des boutons. Elle fournit des fonctions pour détecter les appuis sur le bouton et les relâchements.
- `HCSR04` : Cette librairie permet de contrôler le capteur de distance à ultrasons HC-SR04 à partir de votre Arduino. Elle fournit des fonctions pour mesurer la distance entre le capteur et un objet.
- `Servo` : Cette librairie permet de contrôler les servomoteurs à partir de votre Arduino. Elle fournit des fonctions pour contrôler la position et la vitesse du servomoteur.
- `LiquidCrystal` : Cette librairie permet de contrôler les écrans LCD à partir de votre Arduino. Elle fournit des fonctions pour afficher du texte et des images sur l'écran LCD.
- `Wire` : Cette librairie permet de communiquer avec des appareils externes en utilisant le protocole I2C. Elle fournit des fonctions pour envoyer et recevoir des données sur un bus I2C.

---

## Comment utiliser une librairie Arduino
Pour utiliser une librairie Arduino, vous devez d'abord la télécharger et l'installer sur votre ordinateur. 

L'IDE Arduino possède un gestionnaire de librairies qui permet grandement de faciliter l'installation de celles-ci.

Pour activer le gestionnaire, il suffit de cliquer sur le bouton "Gestionnaire de bibliothèques" dans la barre d'outils de l'IDE Arduino.
> Au moment d'écrire ces lignes, c'est le 3e bouton à partir du haut

![Alt text](arduino_libraries.gif)

Une fois le gestionnaire ouvert, vous pouvez rechercher une librairie en utilisant le champ de recherche. Vous pouvez également parcourir les différentes catégories de librairies pour trouver celle qui vous intéresse.

Une fois que vous avez trouvé la librairie que vous voulez installer, vous pouvez l'installer en cliquant sur le bouton "Installer".

> **Note :** **Il est important de bien lire la documentation** de la librairie avant de l'installer. Certaines librairies peuvent être incompatibles avec votre projet.
> 
> **Astuce :** Écrivez le nom de la composante que vous voulez utiliser dans le champ de recherche pour trouver la librairie qui vous intéresse.

> **Note 2 :** Pour les travaux, j'indiquerai dans la description du travail les librairies à installer. Il y aura le nom de la **librairie** et du **créateur**.

Une fois que vous avez importé la librairie, vous pouvez utiliser les fonctions qu'elle offre dans votre programme. Les fonctions disponibles dépendent de la librairie que vous utilisez, alors consultez la documentation de la librairie pour connaître les fonctions disponibles et leur utilisation.

---

## Utiliser les exemples
Généralement, les créateurs de librairies fournissent des exemples pour vous aider à utiliser leurs librairies. Ces exemples sont des programmes qui utilisent les fonctions de la librairie pour réaliser des tâches spécifiques.

Ceux-ci sont très utiles pour apprendre à utiliser une librairie. Vous pouvez les utiliser comme point de départ pour votre propre projet.

Pour accéder aux exemples, vous devez cliquer sur "Fichier" dans la barre d'outils de l'IDE Arduino, puis sur "Exemples". Vous verrez alors une liste de tous les exemples disponibles. Pour accéder aux exemples d'une librairie en particulier, vous devez cliquer sur le nom de la librairie dans la liste.

<img src="Arduino_libraries_examples.gif" height=720 />

---

## Utiliser une librairie dans votre programme
Pour utiliser une librairie dans votre programme, vous devez l'importer en utilisant la directive `#include`. La directive `#include` permet d'importer du code d'une autre source dans votre programme. Dans le cas des librairies Arduino, vous devez importer le fichier de la librairie que vous voulez utiliser.

Pour connaître le nom de la librairie, ouvrez un exemple de la librairie et regardez la première ligne du programme. Vous verrez quelque chose comme ceci :

```cpp
#include <OneButton.h> // <-- Nom de la librairie
//...
```

---

## Mise en pratique
Réalisez un montage avec un bouton et une DEL (Celle intégrée).
- Branchez le bouton sur la broche 2.
- Installez la librairie suivante :
  - [OneButton de Matthias Hertel](https://github.com/mathertel/OneButton)
  - Prenez le temps de lire la documentation de la librairie.

Tester et prenez le temps de comprendre le code suivant :

```cpp

#include "OneButton.h"

// Les tâches pouvant être faites
typedef enum {
  TASK_OFF,  // set DEL "OFF".
  TASK_ON,   // set DEL "ON"
  TASK_SLOW, // blink DEL "SLOW"
  TASK_FAST  // blink DEL "FAST"
} 
Tasks;

#define PIN_INPUT 2
#define PIN_LED 13

unsigned long currentTime = 0;

// Configurer un bouton avec LOW comme valeur d'entrée et
// activer la résistance de pull-up. Voir la documentation ou
// le code source. (CTRL+click sur le nom de la classe)
OneButton button(PIN_INPUT, true, true);

 // Aucune tâches au démarrage
Tasks currentTask = TASK_OFF;

void setup() {
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(9600);

  // Attacher la fonction qui s'exécutera
  // lorsqu'un clic sera détecter
  button.attachClick(myClickFunction);

  // Attacher la fonction qui s'exécutera
  // lorsqu'un double-clic sera détecter
  button.attachDoubleClick(myDoubleClickFunction);

  // Configurer un délai de debounce. Par défaut 50 ms
  button.setDebounceTicks(25);
  
  Serial.println ("Configuration complétée");
}

void loop() {
  currentTime = millis();

  // ******************
  // Cette fonction est OBLIGATOIRE pour
  // surveiller le bouton. C'est comme un tâche de
  // surveillance
  // ******************
  button.tick();
  
  switch (currentTask) {
    case TASK_OFF:
      turnOffTask();
      break;
    case TASK_ON:
      turnOnTask();
      break;
    case TASK_SLOW:
      blinkTask(currentTime);
      break;
    case TASK_FAST:
      fadeTask(currentTime);
      break;    
  }
  
  serialPrintTask(currentTime);
}

void turnOffTask() {
  digitalWrite(PIN_LED, LOW);  
}

void turnOnTask() {
  digitalWrite(PIN_LED, HIGH);
}

void blinkTask(unsigned long now) {
  static unsigned int lastTime = 0;
  const int rate = 500;
  
  if (now - lastTime >= rate) {
    lastTime = now;
    digitalWrite (PIN_LED, !digitalRead(PIN_LED));
    Serial.print(".");
  }
}

void fadeTask(unsigned long now) {
  static unsigned int lastTime = 0;
  static byte brightness = 1;
  static byte direction = 1;  
  
  const int rate = 8;
  
  if (now - lastTime >= rate) {
    lastTime = now;
    
    if (brightness <= 0 || brightness >= 255) {
      direction = -direction;
    }
    
    analogWrite (PIN_LED, brightness);
    
    brightness += direction;
  }
}

// Cette fonction sera appelée lorsqu'il n'y aura qu'un seul clic du bouton
void myClickFunction() {
  if (currentTask == TASK_OFF)
    currentTask = TASK_ON;
  else
    currentTask = TASK_OFF;
  
  Serial.println(currentTask);
}


// Cette fonction sera appelée lorsqu'il y aura un double-clic
void myDoubleClickFunction() {
  if (currentTask == TASK_ON) {
    currentTask = TASK_SLOW;

  } else if (currentTask == TASK_SLOW) {
    currentTask = TASK_FAST;

  } else if (currentTask == TASK_FAST) {
    currentTask = TASK_ON;
  }
  Serial.println(currentTask);
}

void serialPrintTask(unsigned long now) {
  static unsigned int lastTime = 0;
  const int rate = 1000;
  
  if (now - lastTime >= rate) {
    lastTime = now;
    
    Serial.print(now);
    Serial.print(" - Tache : ");
    Serial.println(currentTask);
  }   
}

```


----

## Conclusion
En résumé, les librairies Arduino sont des outils puissants pour ajouter des fonctionnalités à votre projet. Pour les utiliser, vous devez les télécharger, les installer et les importer dans votre programme. Une fois que vous avez importé une librairie, vous pouvez utiliser les fonctions qu'elle offre pour simplifier votre code et accélérer le développement.

---

## Références
- [Arduino - Librairies](https://www.arduino.cc/en/Guide/Libraries)
- [Documentation de la librairie OneButton](https://github.com/mathertel/OneButton)
