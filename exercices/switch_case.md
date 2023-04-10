# switch-case - Exercices
Voici quelques exercices pour vous pratiquez à l'utilisation des `switch-case`.

# Exercice 1
Considérez le code suivant:

```cpp
if (input == 'A') {
    digitalWrite(13, HIGH);
} else if (input == 'B') {
    digitalWrite(12, HIGH);
} else if (input == 'C') {
    digitalWrite(11, HIGH);
} else {
    digitalWrite(10, HIGH);
}

```

Transformez ce code en utilisant un bloc `switch/case` pour contrôler les broches de l'Arduino en fonction de la valeur de input.

# Exercice 2
Considérez le code suivant:

```cpp
if (mode == 1) {
    Serial.println("Mode 1 activé");
} else if (mode == 2) {
    Serial.println("Mode 2 activé");
} else if (mode == 3) {
    Serial.println("Mode 3 activé");
} else {
    Serial.println("Mode inconnu");
}
```

Remplacez les conditions if/else if par un bloc `switch/case` pour afficher le message correspondant au mode sélectionné.

# Exercice 3
Considérez le code suivant:

```cpp
if (buttonState == LOW) {
    delay(1000);
} else if (buttonState == HIGH) {
    delay(500);
} else {
    delay(2000);
}
```

Réécrivez ce code en utilisant un bloc `switch/case` pour gérer les différentes durées de délai en fonction de l'état du bouton.

# Exercice 4
Considérez le code suivant:

```cpp
enum MotorSpeed { STOP, REVERSE_FULL, REVERSE_HALF, FORWARD_HALF, FORWARD_FULL };
MotorSpeed motorSpeed;
int pwmValue;
char receivedValue; // Supposons que cette valeur soit reçue via la communication en série

//... Code pour lire la valeur du port série

if (receivedValue == '0') {
    motorSpeed = STOP;
} else if (receivedValue == '1') {
    motorSpeed = REVERSE_FULL;
} else if (receivedValue == '2') {
    motorSpeed = REVERSE_HALF;
} else if (receivedValue == '3') {
    motorSpeed = FORWARD_HALF;
} else if (receivedValue == '4') {
    motorSpeed = FORWARD_FULL;
} else {
    motorSpeed = STOP;
}
```


# Exercice 5
Considérez le code suivant:

```cpp
if (sensorValue == 0) {
    display.clearDisplay();
} else if (sensorValue == 1) {
    display.print("Température:");
} else if (sensorValue == 2) {
    display.print("Humidité:");
} else {
    display.print("Erreur:");
}
```

Réécrivez ce code en utilisant un bloc `switch/case` pour gérer l'affichage de différentes informations sur un écran en fonction de la valeur du capteur.

# Exercice 6 - Extra recherche
Vous devez effectuer une recherche sur Internet pour trouver la réponse à cet exercice, car il se peut que vous n'ayez pas encore vu les switch-case qui utilisent des plages de valeurs.

Considérez le code suivant:

```cpp
if (analogValue < 200) {
    ledBrightness = 0;
} else if (analogValue < 600) {
    ledBrightness = 128;
} else if (analogValue < 800) {
    ledBrightness = 200;
} else {
    ledBrightness = 255;
}
```

Réécrivez ce code en utilisant un bloc `switch/case` pour gérer la luminosité de la LED en fonction de la valeur de analogValue.

# Réponses
Les réponses aux exercices sont disponibles [ici](switch_case_rep.md).