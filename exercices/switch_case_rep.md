# switch-case - Réponses
Voici les réponses aux exercices sur les `switch-case`.

# Exercice 1

```cpp
switch (input) {
    case 'A':
        digitalWrite(13, HIGH);
        break;
    case 'B':
        digitalWrite(12, HIGH);
        break;
    case 'C':
        digitalWrite(11, HIGH);
        break;
    default:
        digitalWrite(10, HIGH);
        break;
}
```

# Exercice 2

```cpp
switch (mode) {
    case 1:
        Serial.println("Mode 1 activé");
        break;
    case 2:
        Serial.println("Mode 2 activé");
        break;
    case 3:
        Serial.println("Mode 3 activé");
        break;
    default:
        Serial.println("Mode inconnu");
        break;
}
```

# Exercice 3

```cpp
switch (buttonState) {
    case LOW:
        delay(1000);
        break;
    case HIGH:
        delay(500);
        break;
    default:
        delay(2000);
        break;
}
```

# Exercice 4

```cpp
enum MotorSpeed { STOP, REVERSE_FULL, REVERSE_HALF, FORWARD_HALF, FORWARD_FULL };
MotorSpeed motorSpeed;
int pwmValue;
char receivedValue; // Supposons que cette valeur soit reçue via la communication en série

switch (receivedValue) {
    case '0':
        motorSpeed = STOP;
        break;
    case '1':
        motorSpeed = REVERSE_FULL;
        break;
    case '2':
        motorSpeed = REVERSE_HALF;
        break;
    case '3':
        motorSpeed = FORWARD_HALF;
        break;
    case '4':
        motorSpeed = FORWARD_FULL;
        break;
    default:
        motorSpeed = STOP;
        break;
}

// Utilisez motorSpeed pour contrôler la vitesse du moteur en fonction de la valeur déterminée
```

Dans cet exercice, nous avons défini une énumération MotorSpeed avec cinq valeurs possibles: `STOP`, `REVERSE_FULL`, `REVERSE_HALF`, `FORWARD_HALF`, et `FORWARD_FULL`. Ensuite, nous avons utilisé un bloc switch/case pour déterminer la valeur de motorSpeed à partir de la valeur reçue en série.

# Exercice 5

```cpp

switch (sensorValue) {
    case 0:
        display.clearDisplay();
        break;
    case 1:
        display.print("Température:");
        break;
    case 2:
        display.print("Humidité:");
        break;
    default:
        display.print("Erreur:");
        break;
}
```

# Exercice 6

```cpp
switch (analogValue) {
    case 0 ... 199:
        ledBrightness = 0;
        break;
    case 200 ... 599:
        ledBrightness = 128;
        break;
    case 600 ... 799:
        ledBrightness = 200;
        break;
    default:
        ledBrightness = 255;
        break;
}
```

Le format de la réponse Exercice 4 dépend de la version du compilateur C++. Si vous rencontrez des problèmes de compilation avec les intervalles "case", vous devrez peut-être revenir à une structure if/else if.