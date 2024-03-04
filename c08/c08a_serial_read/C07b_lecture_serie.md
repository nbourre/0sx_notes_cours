# Lecture de données à partir du port série <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Arduino Mega : Spécificités](#arduino-mega--spécificités)
- [SoftwareSerial](#softwareserial)
- [Fonctions importantes](#fonctions-importantes)
- [Utilisation](#utilisation)
- [Exemple de contrôle via le PC](#exemple-de-contrôle-via-le-pc)
- [Exemple de contrôle via un appareil sur Série 1](#exemple-de-contrôle-via-un-appareil-sur-série-1)
- [Convertir un nombre en entier](#convertir-un-nombre-en-entier)
- [Fonction `serialEvent()`](#fonction-serialevent)
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


# SoftwareSerial
Si vous avez un Arduino qui n'a pas de port série natif disponible, vous pouvez utiliser la bibliothèque `SoftwareSerial` pour utiliser les broches digitales de l'Arduino comme port série. Cela permet d'utiliser plusieurs ports série sur un Arduino. Cependant, il faut noter que SoftwareSerial n'est pas aussi rapide que les ports série natifs de l'Arduino.

# Fonctions importantes
Les fonctions importantes pour la lecture de données à partir du port série sont :

- `Serial.begin()` : Initialise le port série.
- `Serial.available()` : Retourne le nombre de caractères disponibles dans le buffer de réception.
- `Serial.read()` : Lit un caractère du buffer de réception.


# Utilisation

Pour savoir si des données sont disponibles dans le buffer de réception, on utilise la fonction `Serial.available()`. Cette fonction retourne le nombre de caractères disponibles dans le buffer de réception. Si le nombre de caractères est supérieur à 0, alors on peut lire le caractère avec la fonction `Serial.read()`.

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
    if (command == '1') {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("LED allumée");
    } else if (command == '0') {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("LED éteinte");
    }
  }
}

```

Dans ce code, nous avons tout d'abord initialisé le port série avec une vitesse de transmission de 9600 bauds et la broche LED_BUILTIN comme une sortie numérique dans la fonction "setup()".

Dans la boucle "loop()", nous avons utilisé la fonction `Serial.available()` pour vérifier si des données ont été reçues via le port série. Si des données sont disponibles, nous lisons la commande envoyée en utilisant la fonction "Serial.read()". Si la commande est égale à '1', nous allumons la LED_BUILTIN en utilisant la fonction `digitalWrite()` avec la valeur `HIGH`. Si la commande est égale à '0', nous éteignons la `LED_BUILTIN` en utilisant la fonction `digitalWrite()` avec la valeur LOW.

En somme, ce code vous montre comment utiliser le port série de l'Arduino Mega pour recevoir des commandes et contrôler la `LED_BUILTIN` en fonction de ces commandes. Vous pouvez adapter ce code pour contrôler d'autres périphériques ou effectuer d'autres actions en fonction des commandes que vous recevez via le port série.

---

# Exemple de contrôle via un appareil sur Série 1

Voici un exemple modifié du précédent qui permet de contrôler la LED_BUILTIN de l'Arduino Mega via un appareil sur le port série 1 :

```cpp
void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial1.available() > 0) {
    int command = Serial1.read();
    if (command == '1') {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("LED allumée");
    } else if (command == '0') {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("LED éteinte");
    }
  }
}

```

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Zc8daVkprjE/0.jpg)](https://www.youtube.com/watch?v=Zc8daVkprjE)

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

Notez qu'il y a aussi la fonction `Serial.parseFloat()` qui permet de lire un nombre à virgule flottante.

# Fonction `serialEvent()`

Vous remarquez dans les exemples que nous avons utilisé la fonction `Serial.available()` pour vérifier si des données sont disponibles dans le buffer de réception. Cependant, il existe une autre fonction qui permet de faire la même chose : `serialEvent()`. Cette fonction est appelée automatiquement lorsque des données sont disponibles dans le buffer de réception. Cela permet d'éviter d'avoir à vérifier si des données sont disponibles dans le buffer de réception à chaque fois que l'on veut lire des données.

Pour le Mega, les fonctions `serialEvent` disponibles sont `serialEvent1`, `serialEvent2` et `serialEvent3`. Chacune étant associée à son port série.

Voici un exemple de code qui utilise la fonction `serialEvent` pour lire des données à partir du port série :
```cpp

String inputString = "";      // a String to hold incoming data
bool stringCompleteFlag = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(9600);

  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  // print the string when a newline arrives:
  if (stringCompleteFlag) {
    Serial.println(inputString);
    // clear the string:
    inputString = "";
    stringCompleteFlag = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringCompleteFlag = true;
    }
  }
}

```

# Exercices
1. Réalisez un programme qui permet de contrôler la LED_BUILTIN de l'Arduino Mega via le PC. Si vous envoyez la lettre 'a' via le port série, la LED_BUILTIN doit s'allumer. Si vous envoyez la lettre 'e' via le port série, la LED_BUILTIN doit s'éteindre.

---

# Références