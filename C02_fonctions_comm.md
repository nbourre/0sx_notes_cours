# Les fonctions de base et la communication <!-- omit in toc -->

---
# Table des matières <!-- omit in toc -->

- [Introduction](#introduction)
- [Exemple - Blink](#exemple---blink)
- [DEL par défaut](#del-par-défaut)
- [Fonctions de base](#fonctions-de-base)
  - [pinMode - Gestion des broches](#pinmode---gestion-des-broches)
  - [digitalWrite](#digitalwrite)
  - [delay](#delay)
  - [millis](#millis)
- [Exemple `Fade`](#exemple-fade)
  - [fonction `analogWrite`](#fonction-analogwrite)
- [Fonctions de communication](#fonctions-de-communication)
  - [Serial.begin()](#serialbegin)
  - [Serial.print() et Serial.println()](#serialprint-et-serialprintln)
  - [Moniteur série](#moniteur-série)
  - [Port série... mais c'est quoi??](#port-série-mais-cest-quoi)
- [Exercices](#exercices)

---

# Introduction
Dans ce cours, nous allons apprendre à utiliser quelques fonctions fondamentales de l'Arduino ainsi que l'échange d'information entre l'Arduino et le PC.

---

# Exemple - Blink

Voici le code de base pour faire clignoter une LED branchée sur la broche 13 de l'Arduino.

Nous allons nous y référer pour étudier les fonctions de base.

<table>
<tr>
<td>

**Code**
</td>
<td>

**Résultat**
</td>
</tr>
<tr>
<td>

```cpp
int led = 13;

void setup() {
  pinMode(led, OUTPUT);
}

void loop() {
  digitalWrite(led, HIGH);
  delay(1000);
  digitalWrite(led, LOW);
  delay(1000);
}
```
</td>
<td>

![Alt text](assets/c02_blink.gif)

</td>

</tr>


</table>

---

# DEL par défaut
Une DEL, ou *LED* en anglais, est une petite lampe qui émet de la lumière quand elle est alimentée. DEL est l'acronyme pour **D**iode **É**lectro**L**uminescente (***L**ight-**E**mitting **d**iode*).

Sur les Arduinos, il y a une DEL qui est branchée sur la **broche 13**. C'est la raison pour laquelle on voit souvent des exemples avec cette DEL, car elle est facile à utiliser.

---

# Fonctions de base

## pinMode - Gestion des broches

La fonction `pinMode` permet de définir le mode d'une broche. Il y a deux modes principaux : `INPUT` et `OUTPUT`.

> **Note**
> 
> Il y a aussi un 3e mode (`INPUT_PULLUP`) que nous verrons plus tard.

**La fonction prend 2 paramètres : le numéro de la broche et le mode de la broche.**

Généralement, on utilise la fonction `pinMode` dans la fonction `setup` pour définir le mode des broches.

| Mode | Description | Exemple | Exemple d'utilisation |
| --- | --- | --- | --- |
| INPUT | La broche est en mode entrée. | `pinMode(2, INPUT);` | Lecture d'un bouton |
| OUTPUT | La broche est en mode sortie. | `pinMode(3, OUTPUT);` | Contrôle d'une DEL ou d'un moteur |

Dans l'exemple précédent, nous avons utilisé la fonction `pinMode` pour définir la broche 13 en mode `OUTPUT` pour pouvoir y écrire une valeur.

---

## digitalWrite
La fonction digitalWrite en Arduino permet de mettre le niveau logique `HIGH` ou `LOW` sur une **broche numérique**.

`HIGH` vaut 1 et `LOW` vaut 0.

Lorsqu'on utilise cette fonction, il faut lui fournir deux arguments : le numéro de la broche sur laquelle on veut envoyer le signal et le niveau logique souhaitée (`HIGH` ou `LOW`). Par exemple, si vous voulez envoyer un signal de niveau logique `HIGH` sur la broche numérique 12, vous pouvez utiliser l'instruction suivante :

```cpp
digitalWrite(12, HIGH);
```

La fonction `digitalWrite` est souvent utilisée pour contrôler des dispositifs qui nécessitent un signal binaire, comme des LED, des relais, etc. Elle peut également être utilisée pour communiquer avec d'autres circuits ou des périphériques externes via des protocoles de communication tels que I2C ou SPI.

---

## delay
La fonction `delay` permet de faire une pause dans le programme. Elle prend en paramètre le nombre de millisecondes à attendre. Elle prend un seul argument, qui est le nombre de millisecondes de pause souhaité.

Voici un exemple d'utilisation de la fonction `delay` :
    
```cpp
digitalWrite(LED_BUILTIN, HIGH);  // Allume la LED intégrée
delay(1000);                       // Pause pendant 1000 millisecondes (1 seconde)
digitalWrite(LED_BUILTIN, LOW);   // Éteint la LED intégrée
```

La fonction `delay` est souvent utilisée pour créer des temporisations ou des pauses dans un programme Arduino. Elle peut être utilisée pour mettre en pause le programme pendant une durée précise avant de continuer à l'exécution. Par exemple, on peut utiliser delay pour créer des effets de clignotement sur une LED ou pour synchroniser l'exécution de différentes parties d'un programme.

> **Important!!**
> 
> Il est important de noter que la fonction `delay` bloque l'exécution du programme pendant la durée de la pause, ce qui est problématique dans certains cas. Si vous avez besoin de mettre en pause le programme sans bloquer l'exécution des autres parties du code, vous pouvez utiliser des variables de gestion de temps. Voir l'exemple `BlinkWithoutDelay` pour plus de détails.

---

## millis

La fonction `millis()` dans Arduino est une fonction qui renvoie le nombre de millisecondes qui se sont écoulées depuis le démarrage du microcontrôleur Arduino. Elle peut être utilisée pour calculer des délais précis, tels que le retardement dans une boucle `loop()`. Cela permet aux programmes Arduino d'effectuer des opérations à des intervalles de temps précis, ce qui est très utile pour les projets qui impliquent des délais ou des temps d'exécution.

Elle s'utilise sans paramètre et renvoie un **entier long** (`long int`).

---

# Exemple `Fade`

Voici un autre exemple de base fournit par Arduino. Il s'agit d'un programme qui fait varier la luminosité d'une DEL en utilisant la fonction `analogWrite`.
  
```cpp
int led = 9; // LED connectée à la broche 9
int brightness = 0; // Valeur de luminosité
int fadeAmount = 5; // Valeur de variation de luminosité

void setup() {
  pinMode(led, OUTPUT); // Définit la broche 9 en mode sortie
}

void loop() {
  analogWrite(led, brightness); // Change la luminosité de la LED
  brightness = brightness + fadeAmount; // Change la valeur de luminosité

  // Inverse la variation de luminosité quand la valeur de luminosité atteint 0 ou 255
  if (brightness <= 0 || brightness >= 255) {
    fadeAmount = -fadeAmount;
  }
  // Attend 30 millisecondes avant de recommencer
  delay(30);
}

```

---

## fonction `analogWrite`
La fonction `analogWrite` permet de générer une tension analogique sur une **broche PWM**. Elle prend en paramètre le numéro de la broche sur laquelle on veut envoyer le signal et la valeur de la tension souhaitée.
Pour être plus simple, pensez à une valeur en pourcentage sur 255. Voici quelques exemples :

```cpp
analogWrite(13, 127); // 50% de 255 = 127
analogWrite(13, 26); // 10% de 255 = 26
analogWrite(13, 255); // 100% de 255 = 255
```

Sur le Arduino Mega, les broches PWM sont les broches 2 à 13 ainsi que 44, 45 et 46.

Nous verrons en cours de session ce qu'est exactement le **PWM**.

---

# Fonctions de communication
Les fonctions de communication permettent d'envoyer et de recevoir des données à partir d'autres périphériques ou d'autres circuits. Elles sont utilisées pour communiquer avec des périphériques externes, comme des capteurs, des écrans LCD, des modules Bluetooth, etc.

Dans ce cours, nous allons nous intéresser aux fonctions de communication suivantes :
- `Serial.begin()`
- `Serial.print()`
- `Serial.println()`

## Serial.begin()
La fonction `Serial.begin()` permet de configurer la vitesse de communication avec le port série. Elle prend en paramètre la vitesse de communication en bauds. Par exemple, pour configurer la liaison série à 9600 bauds, on utilise la fonction `Serial.begin(9600)`.

Généralement, on utilise la fonction `Serial.begin()` dans la fonction `setup()`.

Exemple :

```cpp
void setup() {
  Serial.begin(9600);
  // Autre code
}
```
<br />

> **Note**
> 
> Un baud est une unité de mesure de la vitesse de transmission de données. Il représente le nombre de bits qui peuvent être transmis par seconde. Par exemple, 9600 bauds signifie que 9600 bits peuvent être transmis par seconde.

---

## Serial.print() et Serial.println()

La fonction `Serial.print()` est une fonction dans l'Arduino qui permet d'envoyer des données série à un port série. Il peut être utilisé pour envoyer un message texte, des données numériques ou des données binaires.

Par exemple, le code suivant permet d'envoyer le message "Bonjour!" à un port série:

```
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print("Bonjour!");
  delay(1000);
}
```

Ce code initialisera le port série à une vitesse de 9600 bits par seconde, puis enverra le message "Bonjour!" toutes les secondes.

La fonction `Serial.println()` ajoute un retour à la ligne à la fin du message envoyé.

Voici un exemple de code qui utilise les fonctions `Serial.print()` et `Serial.println()` :

```cpp

void setup() {
  // Initialisation du port
  // série à 9600 baud
  Serial.begin(9600);
}

int counter = 0;
void loop() {
  Serial.print("Boucle : ");
  Serial.println(counter);
  counter++;

  // Délai pour ne pas ralentir le µC
  delay(500);
}

```

![Alt text](assets/ex_serial_print.gif)

> **Note**
> 
> Il est important de mettre un délai entre chaque envoi de données via le port série. Si vous ne mettez pas de délai, le programme va envoyer les données aussi vite que possible. Cela peut ralentir le programme et causer des problèmes.  

## Moniteur série
Pour pouvoir voir les messages envoyés par le programme, il faut ouvrir le moniteur série. Pour cela, cliquez sur le menu `Outils` puis sur `Moniteur série`.

Il faudra s'assurer de sélectionner le bon port série ainsi que la bonne vitesse de communication. 

![Alt text](assets/arduino_serial_monitor_start.gif)

---

## Port série... mais c'est quoi??
Un port série est un port de communication qui permet d'envoyer et de recevoir des données. Il est composé de 2 fils, un fil pour envoyer des données et un fil pour recevoir des données.

Dans le cas des Arduino, le port série est utilisé pour envoyer des données à l'ordinateur. Il est également possible d'utiliser le port série pour envoyer des données à un autre Arduino.

Les ports séries sont identifiés par les lettres **TX** et **RX**. Le fil TX (transmission) est utilisé pour envoyer des données et le fil RX (réception) est utilisé pour recevoir des données.

Regardez votre Arduino et identifiez les broches TX et RX.

**Question** : Combien en comptez-vous?


TODO : Indiquer que le port série 0 est utilisé pour communiquer avec l'ordinateur via le câble USB.

---

# Exercices
- Programmez une DEL pour qu'elle clignote 2 fois dans une seconde et ensuite 5 fois dans une seconde.
- Modifiez le programme précédent qui envoit à l'ordinateur l'état du LED à chaque changement d'état.
  - Exemple de sortie : `LED allumée` ou `LED éteinte`