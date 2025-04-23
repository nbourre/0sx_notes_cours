# 🧠 Questions de révision – Arduino 420-0SX-SW

## Cours 07 : Servo, machine à états, I2C, Stepper

1. Quelle fonction permet de déplacer un servomoteur vers un angle spécifique?
2. Quelle bibliothèque est fréquemment utilisée pour contrôler un servomoteur?
3. Quels sont les avantages de programmer une machine à états?
4. Quelle est la différence entre un état et une transition?
5. Quel protocole montré en classe permet à plusieurs appareils de partager les mêmes fils pour communiquer avec l’Arduino?

<details>
<summary>Réponses</summary>

1. `servo.write(angle)` permet de déplacer le servomoteur vers l'angle voulu.
2. La bibliothèque `Servo.h`.
3. Avantages : meilleure organisation, simplification de la logique complexe, extensibilité du code.
4. Un **état** représente une situation stable, une **transition** est le passage d’un état à un autre basé sur une condition.
5. Le protocole **I2C** (Inter-Integrated Circuit).

</details>

---

## Cours 08 : Communication série avancée, POO de base

1. Quelle fonction permet de lire les données entrantes sur le port série?
2. Quel est l’intérêt de la programmation orientée objet dans un projet Arduino?
3. Quelle est la différence entre une classe et un objet?
4. Pourquoi utilise-t-on souvent `Serial.available()` avant de lire avec `Serial.read()`?
5. Quelle est la fonction spéciale d’une classe qui est appelée à sa création?

<details>
<summary>Réponses</summary>

1. `Serial.read()`.
2. Encapsulation du comportement, réutilisabilité du code, meilleure organisation et maintenance.
3. Une **classe** est un modèle, un **objet** est une instance concrète de cette classe.
4. Pour s’assurer qu’il y a des données disponibles dans le tampon avant de lire — éviter les lectures invalides.
5. Le **constructeur** (même nom que la classe, sans type de retour).

</details>

---

## Cours 09 : Moteur DC, machine à états revisitée

1. Quel composant a-t-on vu qui permet de contrôler la direction et la vitesse d’un moteur DC?
2. Quelle est la fonction utilisée pour contrôler un moteur avec PWM?
3. Dans un système à états, pourquoi peut-on vouloir revoir la logique des transitions?
4. Quelle est la différence principale entre un moteur DC et un moteur pas-à-pas?
5. Pourquoi est-il recommandé de regrouper les transitions dans une seule fonction?

<details>
<summary>Réponses</summary>

1. Le **L293D**, un double pont en H.
2. `analogWrite(pin, value)`.
3. Pour améliorer la lisibilité, modulariser et faciliter les modifications de comportement.
4. Le moteur DC tourne librement, le **stepper** se déplace par pas contrôlés.
5. Pour centraliser la logique de décision, éviter la duplication de code.

</details>

---

## Cours 10 : Refactorisation, Matrice MAX7219

1. Qu'est-ce que la refactorisation du code?
2. Quel est l'avantage d’utiliser une classe pour piloter un écran?
3. Comment écrit-on un pixel à l’écran avec la librairie U8g2?
4. Qu’est-ce que le MAX7219?
5. Quelle méthode permet de créer une animation avec les fonctions de dessin?

<details>
<summary>Réponses</summary>

1. C’est la réécriture du code pour améliorer sa structure sans changer son comportement.
2. Réutilisabilité, abstraction du matériel, séparation des responsabilités.
3. `u8g2.drawPixel(x, y)`.
4. Un contrôleur de matrice LED 8x8 (et plus) compatible SPI.
5. En combinant une boucle avec un délai (`delay()`, ou mieux `millis()`), et `clearBuffer()` + `sendBuffer()` à chaque cycle.

</details>

---

## Cours 11 : Communication WiFi (ESP), MQTT

1. Quelle bibliothèque est souvent utilisée avec les modules ESP8266 ou ESP32?
2. Quelle est la différence entre `client.publish()` et `client.subscribe()`?
3. Quel protocole est utilisé pour l’envoi léger de messages sur réseau?
4. Que signifie QoS dans MQTT?
5. Pourquoi utilise-t-on un identifiant unique (client ID) pour chaque appareil?

<details>
<summary>Réponses</summary>

1. `WiFiClient`, `PubSubClient`, ou `WiFiEsp` selon le module.
2. `publish()` envoie un message, `subscribe()` écoute un canal (topic).
3. **MQTT** — Message Queuing Telemetry Transport.
4. Quality of Service — indique la fiabilité de livraison (0, 1 ou 2).
5. Pour éviter les conflits et déconnexions imprévues sur le broker.

</details>

---

## Cours 12 : Infrarouge, fin du projet

Pas vu en 2025

1. Quelle bibliothèque permet de recevoir des signaux infrarouges?
2. Quel type de données est typiquement transmis par une télécommande IR?
3. Pourquoi faut-il souvent “décoder” les signaux IR?
4. Peut-on contrôler plusieurs appareils avec la même télécommande IR?
5. Quelle approche utilise-t-on pour détecter l’appui sur un bouton IR?

<details>
<summary>Réponses</summary>

1. `IRremote.h`
2. Un code numérique codé sur 32 bits (souvent en hexadécimal).
3. Car le protocole utilisé dépend de la marque de la télécommande.
4. Oui, si les codes sont compatibles ou si l’on les reprogramme.
5. On utilise `irrecv.decode()` puis on lit `results.value`.

</details>

