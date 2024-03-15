# Lecture de données à partir du port série <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Arduino Mega : Spécificités](#arduino-mega--spécificités)
- [SoftwareSerial](#softwareserial)
- [Fonctions importantes de base](#fonctions-importantes-de-base)
- [Utilisation](#utilisation)
- [Exemple de contrôle via le PC](#exemple-de-contrôle-via-le-pc)
  - [Explication du code](#explication-du-code)
- [Exemple de contrôle via un appareil sur Série 3](#exemple-de-contrôle-via-un-appareil-sur-série-3)
- [Convertir un nombre en entier](#convertir-un-nombre-en-entier)
- [Fonction `serialEvent()`](#fonction-serialevent)
  - [Explication du code](#explication-du-code-1)
- [Fonction `serial.readStringUntil()`](#fonction-serialreadstringuntil)
  - [Explication du code](#explication-du-code-2)
- [Exercices](#exercices)
- [Références](#références)


# Introduction

Dans cet article, nous allons apprendre comment utiliser le port série d'un Arduino pour lire des données provenant du port série. Vous avez déjà appris à utiliser le port série pour envoyer des données de l'Arduino à l'ordinateur, nous allons donc nous concentrer sur la lecture de données dans cet article.

# Arduino Mega : Spécificités
Le Arduino Mega dispose de 4 ports série. Le port série 0 est utilisé pour la communication avec l'ordinateur. Les ports série 1, 2 et 3 sont utilisés pour la communication avec des périphériques externes.

Voici un tableau avec les broches utilisées pour chaque port série :

| Port Série | Broche TX | Broche RX |
|------------|----------|----------|
| Serial     | 1        | 0        |
| Serial1    | 18       | 19       |
| Serial2    | 16       | 17       |
| Serial3    | 14       | 15       |

> **Note** : On ne branche généralement rien sur les broches TX et RX du port série 0 car elles sont utilisées pour la communication avec l'ordinateur. Si vous branchez quelque chose sur ces broches, vous ne pourrez probablement plus téléverser de programme sur l'Arduino Mega.

# SoftwareSerial
Si vous avez un Arduino qui n'a plus de port série natif disponible, vous pouvez utiliser la bibliothèque `SoftwareSerial` pour utiliser les broches digitales de l'Arduino comme port série. Cela permet d'utiliser plusieurs ports série sur un Arduino. Cependant, il faut noter que `SoftwareSerial` n'est pas aussi rapide que les ports série natifs de l'Arduino.

Cette bibliothèque est souvent utilisée avec les cartes Arduino Uno, Nano, etc. qui n'ont qu'un seul port série natif.

# Fonctions importantes de base
Les fonctions importantes pour la lecture de données à partir du port série sont :

- `Serial.begin()` : Initialise le port série.
- `Serial.available()` : Retourne le nombre de caractères disponibles dans le buffer de réception.
- `Serial.read()` : Lit un caractère du buffer de réception.

# Utilisation

Pour savoir si des données sont disponibles dans le tampon (*buffer*) de réception, on utilise la fonction `Serial.available()`. Cette fonction retourne le nombre d'octet disponibles à la lecture dans le buffer de réception. Si le nombre d'octet est supérieur à 0, alors on peut lire le caractère avec la fonction `Serial.read()`.

Il faut toujours regarder si des données sont disponibles dans le buffer de réception avant de lire le caractère. Si vous lisez un caractère alors qu'aucune donnée n'est disponible, vous risquez de lire un caractère aléatoire.

# Exemple de contrôle via le PC

Voici un exemple de code qui allume et éteint la LED_BUILTIN de l'Arduino Mega après avoir reçu une commande via le port série :

```cpp
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    int command = Serial.read();

    switch (command) {
      case '1':
        cmdAllumer();
        break;
      case '0':
        cmdEteindre();
        break;
      default:
        afficherErreur();
    }
  }
}

void cmdAllumer() {
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("LED allumée");
}

void cmdEteindre() {
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("LED éteinte");
}

void afficherErreur() {
  Serial.println("Commande invalide");
}

```

## Explication du code
Dans ce code, nous avons tout d'abord initialisé le port série avec une vitesse de transmission de 9600 bauds et la broche LED_BUILTIN comme une sortie numérique dans la fonction "setup()".

Dans la boucle `loop()`, nous avons utilisé la fonction `Serial.available()` pour vérifier si des données ont été reçues via le port série. **Si des données sont disponibles**, nous lisons la commande envoyée en utilisant la fonction `Serial.read()`. Si la commande est égale à '1', nous exécutons la fonction `cmdAllumer()`, si la commande est égale à '0', nous exécutons la fonction `cmdEteindre()` et si la commande est différente de '1' ou '0', nous exécutons la fonction `afficherErreur()`.

En somme, ce code vous montre comment utiliser le port série pour recevoir des commandes et contrôler la `LED_BUILTIN` en fonction de ces commandes. Vous pouvez adapter ce code pour contrôler d'autres périphériques ou effectuer d'autres actions en fonction des commandes que vous recevez via le port série.

---

# Exemple de contrôle via un appareil sur Série 3

Voici un exemple modifié du précédent qui permet de contrôler la LED_BUILTIN de l'Arduino Mega via un appareil sur le port série 3 :

```cpp
void setup() {
  Serial.begin(9600);
  Serial3.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial3.available() > 0) {
    int command = Serial3.read();

    switch (command) {
      case '1':
        cmdAllumer();
        break;
      case '0':
        cmdEteindre();
        break;
      default:
        afficherErreur();
    }
  }
}

void cmdAllumer() {
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("LED allumée");
}

void cmdEteindre() {
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("LED éteinte");
}

void afficherErreur() {
  Serial.println("Commande invalide");
}

```

[![Exemple d'utilisation d'un HM-10](https://img.youtube.com/vi/Zc8daVkprjE/0.jpg)](https://www.youtube.com/watch?v=Zc8daVkprjE)

L'appareil connecté pourrait être un module Bluetooth, un autre Arduino, un Raspberry Pi, etc.

# Convertir un nombre en entier
Pour convertir un nombre en entier, on utilise la fonction `Serial.parseInt()`. Par défaut, cette fonction retourne le premier nombre entier trouvé dans le buffer de réception.

Voici un exemple de code qui utilise `parseInt` pour lire un nombre entier. Ensuite, on utilise ce nombre pour ajuster la luminosité de la LED_BUILTIN de l'Arduino Mega :

```cpp
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    int number = Serial.parseInt();
    analogWrite(LED_BUILTIN, number);
  }
}

```

Notez qu'il y a aussi la fonction `Serial.parseFloat()` qui permet de lire un nombre à virgule flottante. Le format de la valeur envoyée du PC doit être `123.45` par exemple.

# Fonction `serialEvent()`

Vous remarquez dans les exemples que nous avons utilisé la fonction `Serial.available()` pour vérifier si des données sont disponibles dans le buffer de réception. Cependant, il existe une autre fonction qui permet de faire la même chose : `serialEvent()`. Cette **fonction événementielle** est appelée automatiquement lorsque des données sont disponibles dans le buffer de réception. Cela permet d'éviter d'avoir à vérifier si des données sont disponibles dans le buffer de réception à chaque fois que l'on veut lire des données.

Pour le Mega, les fonctions `serialEvent` disponibles sont `serialEvent1`, `serialEvent2` et `serialEvent3`. Chacune étant associée à son port série.

Voici un exemple de code qui utilise la fonction `serialEvent` pour lire des données à partir du port série :

```cpp

String inputString = "";      // une chaîne pour contenir les données entrantes
bool stringCompleteFlag = false;  // indique si la chaîne est complète

void setup() {
  // initialiser la communication série :
  Serial.begin(9600);

  // réserver 200 octets pour inputString :
  inputString.reserve(200);
}

void loop() {
  // imprimer la chaîne lorsqu'un saut de ligne arrive :
  if (stringCompleteFlag) {
    Serial.println(inputString);
    // effacer la chaîne :
    inputString = "";
    stringCompleteFlag = false;
  }
}

/*
  SerialEvent se produit chaque fois qu'une nouvelle donnée arrive sur le RX série matériel. Cette
  routine est exécutée entre chaque exécution de loop(), donc utiliser delay dans loop peut
  retarder la réponse. Plusieurs octets de données peuvent être disponibles.
*/
void serialEvent() {
  while (Serial.available()) {
    // obtenir le nouveau byte :
    char inChar = (char)Serial.read();
    // l'ajouter à inputString :
    inputString += inChar;
    // si le caractère entrant est un saut de ligne, définir un drapeau pour que la boucle principale puisse
    // faire quelque chose à ce sujet :
    if (inChar == '\n') {
      stringCompleteFlag = true;
    }
  }
}

```

## Explication du code
Dans ce code, nous avons utilisé la fonction `serialEvent` pour lire des données à partir du port série. La fonction `serialEvent` est appelée automatiquement chaque fois qu'une nouvelle donnée arrive sur le port série. Dans cette fonction, nous avons utilisé une boucle `while` pour lire chaque caractère entrant et l'ajouter à la chaîne `inputString`. Lorsque nous rencontrons un saut de ligne, nous définissons un drapeau `stringCompleteFlag` pour indiquer que la chaîne est complète et prête à être traitée dans la boucle principale.

En somme, la fonction `serialEvent` est une alternative à la fonction `Serial.available()` pour lire des données à partir du port série. Vous pouvez utiliser l'une ou l'autre en fonction de vos besoins et de votre style de programmation.

> **Concept du drapeau (*flag*)**
> 
> <img src="https://upload.wikimedia.org/wikipedia/commons/d/db/725-open-mailbox-with-raised-flag.svg" style="max-height: 300px; max-width: 300px;" />
> 
> Un drapeau est une variable qui est utilisée pour indiquer si un événement s'est produit ou non. Dans ce cas, nous avons utilisé un drapeau `stringCompleteFlag` pour indiquer si la chaîne est complète et prête à être traitée dans la boucle principale.
>  
> Lorsque le programme a terminé de traiter la chaîne, il réinitialise le drapeau pour indiquer que la chaîne n'est plus complète.


Voici un exemple précédent modifié pour utiliser la fonction `serialEvent` :

```cpp
void setup() {
  Serial.begin(9600);
  Serial3.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // rien à faire ici
}

void serialEvent3() {
  if (Serial3.available() > 0) {
    int command = Serial3.read();

    switch (command) {
      case '1':
        cmdAllumer();
        break;
      case '0':
        cmdEteindre();
        break;
      default:
        afficherErreur();
    }
  }
}

void cmdAllumer() {
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("LED allumée");
}

void cmdEteindre() {
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("LED éteinte");
}

void afficherErreur() {
  Serial.println("Commande invalide");
}

```

---

# Fonction `serial.readStringUntil()`
Supposons que vous voulez lire une commande avec des paramètres envoyée via le port série. Par exemple, vous désirez envoyer des commandes dans un format comme `pin:13,1` pour allumer la LED connectée à la broche 13 ou encore `pin:A4,read` pour lire la valeur à la broche `A4`. Vous pouvez utiliser la fonction `serial.readStringUntil()` pour lire la commande complète et ensuite la traiter.

Voici un exemple complexe de code qui utilise `serial.readStringUntil()` avec `serialEvent` pour lire des commandes avec des paramètres envoyées via le port série :

```cpp

#define DEBUG_MODE 1

String cmd = "";
bool cmdReceived = false;

void setup() {
  // initialiser la communication série :
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (cmdReceived) {
    traiterCommande(cmd);
    cmdReceived = false;
  }
}

void serialEvent() {
  if (Serial.available()) {
    // Lire la chaîne jusqu'à ce qu'un caractère de nouvelle ligne ('\n') soit rencontré
    cmd = Serial.readStringUntil('\n');
    // Si cmd n'est pas vide, cela signifie que nous avons reçu une commande terminée par '\n'
    if (cmd.length() > 0) {
      cmdReceived = true;
    }
  }
}

// Format de la commande : pin:numéro,commande
// Exemple : pin:13,1
// Exemple : pin:A4,read
void traiterCommande(String commande) {
    if (!commande.startsWith("pin:")) {
        Serial.println("Commande invalide ou non implantée");
        return;
    }

    String pin, action;
    decomposerCommande(commande, pin, action);
    executerAction(pin, action);
}

// Sépare la commande en numéro de broche et action
void decomposerCommande(const String& commande, String& pin, String& action) {
    int pos = commande.indexOf(',');
    pin = commande.substring(4, pos);
    action = commande.substring(pos + 1);
}

// Traiter la lecture ou l'écriture sur une broche
void executerAction(const String& pinRcv, const String& action) {
    int pinNumber = convertirPin(pinRcv);
    if (pinNumber == -1) {
        Serial.println("Broche invalide");
        return;
    }

    if (action.startsWith("r") || action.startsWith("R")) {
        lirePin(pinNumber);
    } else {
        ecrireSurPin(pinNumber, action);
    }
}

// Convertit une désignation de broche en numéro de broche utilisable
int convertirPin(const String& pinRcv) {
    // Initialisation de pinNumber à -1, indiquant une valeur non valide ou non supportée
    int pinNumber = -1;

    // Vérifier si la broche reçue est numérique
    if (isDigit(pinRcv[0])) {
        pinNumber = pinRcv.toInt();
    } 
    // Gérer les cas où la broche est analogique, commençant par 'A' ou 'a'
    else if (pinRcv[0] == 'A' || pinRcv[0] == 'a') {
        if (pinRcv.length() > 1 && isDigit(pinRcv[1])) {
            int analogPin = pinRcv.substring(1).toInt();
            pinNumber = analogPinToDigitalPin(analogPin);
        } else {
            // Si le format de la broche analogique est incorrect (par exemple, "Aa"), indiquer une erreur
            Serial.println("Format de broche analogique invalide");
            return -1;
        }
    } 
    // Si le format de broche ne correspond à aucun format valide, afficher un message d'erreur
    else {
        Serial.println("Format de broche invalide");
        return -1;
    }

    // Retourner le numéro de broche converti ou -1 si non valide
    return pinNumber;
}


// Lit une broche et envoie sa valeur via Serial
void lirePin(int pinNumber) {
    int value = digitalRead(pinNumber);
    Serial.println(value);
}

// Écrit sur une broche numérique ou analogique selon la commande
void ecrireSurPin(int pinNumber, const String& cmd) {
    if (isDigit(cmd[0])) {
        int value = cmd.toInt();
        if (value > 1) { // Considérant tout ce qui est >1 comme une commande analogique
            analogWrite(pinNumber, value);
        } else {
            digitalWrite(pinNumber, value);
        }
    } else {
        Serial.println("Valeur invalide");
    }
}

// Fonction pour convertir un numéro de broche analogique en broche numérique
// ATTENTION!! Uniquement pour les cartes Arduino Mega ou Uno
int analogPinToDigitalPin(int analogPin) {
#if ((defined(__AVR_ATmega2560__) || defined(__AVR_ATmega2561__)))
  if (analogPin >= 0 && analogPin <= 15) {
    return analogPin + 54;
  }
#endif

#if defined(__AVR_ATmega328P__)
  if (analogPin >= 0 && analogPin <= 5) {
    return analogPin + 14;
  }
#endif

  Serial.println(F("Carte ou broche non supportée"));

  return -1;
}

```

## Explication du code
Dans ce code qui peut sembler relativement complexe est plus simple qu'on peut y penser. En effet, j'ai subdivisé le code en plusieurs fonctions pour le rendre plus lisible et plus facile à comprendre. Cela permet de mieux organiser le code et de le rendre plus modulaire. Cela permet aussi de réutiliser certaines parties du code dans d'autres projets.


> **Note** : Il y a aussi la fonction `Serial.readString()` qui lit une chaîne jusqu'à ce qu'un caractère de nouvelle ligne soit rencontré. Cependànt, cette commande ralentie la fonction attend un certain temps pour lire la chaîne. `Serial.readStringUntil()` est plus rapide car elle lit la chaîne jusqu'à ce qu'un caractère spécifié soit rencontré.


---

# Exercices
1. Essayez le code de l'exemple de la section "Fonction `serial.readStringUntil()`" pour voir comment il fonctionne.
2. Avec votre plaquette d'expérimentation, s'il y a un composant simple d'installer, essayez d'interagir avec lui via le port série. Par exemple, vous pouvez allumer et éteindre une LED, lire la valeur d'un capteur, etc.

---

# Références
- [Serial](https://www.arduino.cc/reference/en/language/functions/communication/serial/)