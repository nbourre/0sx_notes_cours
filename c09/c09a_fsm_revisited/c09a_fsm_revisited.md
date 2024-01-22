# Revisitons la machine à états finis <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Rappel états et transitions](#rappel-états-et-transitions)
- [Les états](#les-états)
  - [L'entrée](#lentrée)
  - [L'exécution](#lexécution)
  - [La sortie](#la-sortie)
  - [Exemple](#exemple)
  - [Résumé](#résumé)
- [Définir les états requis](#définir-les-états-requis)
- [Utiliser la programmation orientée objet](#utiliser-la-programmation-orientée-objet)
  - [Définir la classe](#définir-la-classe)

# Introduction
Nous avons vu les bases de la programmation orientée objet en C++ dans le cours précédent. Nous allons maintenant voir comment utiliser la programmation orientée objet pour créer une machine à états finis.

# Rappel états et transitions
Nous avons vu comment utiliser des fonctions pour exécuter des actions en fonction de l'état dans le cours précédent.

Dans certaines situations, les états nécessitaient une certaine préparation avant de s'exécuter ou encore des modifications pour sortir de l'état. Cela pouvait vous occasionner des petits maux de tête. Nous allons voir comment séparer un état en 3 parties: l'entrée, l'exécution et la sortie.

**Prenez note que les entrées et sorties peuvent être optionnelles**. Par exemple, si vous avez un état qui ne nécessite pas de préparation avant de s'exécuter, vous n'aurez pas besoin d'une fonction d'entrée.

# Les états
Un état peut être séparé en 3 parties: l'entrée, l'exécution et la sortie. L'entrée est exécutée lorsque l'état est activé. L'exécution est exécutée tant que l'état est actif. La sortie est exécutée lorsque l'état est désactivé.

## L'entrée
L'entrée est exécutée lorsque l'état est activé. Elle est utilisée pour préparer l'état avant son exécution. Par exemple, si nous avons un état qui doit allumer une DEL avant de s'exécuter, nous allons utiliser l'entrée pour allumer la DEL.

Souvent la fonction aura le suffixe `Enter` pour indiquer qu'elle est utilisée pour l'entrée.

Par exemple, si l'on désire qu'une DEL soit allumée pendant que l'on tourne un moteur, nous allons utiliser l'entrée pour allumer la DEL.

```cpp
// Si l'on doit allumer une DEL avant de s'exécuter
void motorSpinEnter() {
    digitalWrite(ledPin, HIGH);
    state = MOTOR_SPIN;
}
```

## L'exécution
L'exécution est exécutée tant que l'état est actif. Elle est utilisée pour exécuter l'état. Souvent la fonction aura le suffixe `Execute` pour indiquer qu'elle est utilisée pour l'exécution.

Par exemple, le moteur doit tourner tant et aussi longtemps qu'un bouton n'est pas appuyé.

```cpp
// Si l'on doit tourner le moteur tant qu'un bouton n'est pas appuyé
void motorSpinExecute() {
    digitalWrite(motorPin, HIGH);
    if (digitalRead(buttonPin) == LOW) {
        digitalWrite(motorPin, LOW);

        // On désactive l'état
        motorSpinExit();
    }
}
```

## La sortie
La sortie est exécutée lorsque l'état est désactivé. Elle est utilisée pour nettoyer l'état avant de passer à un autre état. Par exemple, si nous avons un état qui doit éteindre une DEL avant de passer à un autre état, nous allons utiliser la sortie pour éteindre la DEL.

Souvent la fonction aura le suffixe `Exit` pour indiquer qu'elle est utilisée pour la sortie.

Par exemple, si l'on désire qu'une DEL soit éteinte après avoir tourné un moteur, nous allons utiliser la sortie pour éteindre la DEL.

```cpp
// Si l'on doit éteindre une DEL après avoir tourné le moteur
void motorSpinExit() {
    digitalWrite(ledPin, LOW);    
    state = MOTOR_STOP;
}
```

## Exemple

```cpp
// Définition des états
enum State {
    MOTOR_STOP,
    MOTOR_SPIN
};

bool motorSpinEnterDone = false;

// Définition des fonctions
void motorStopExecute();

void motorSpinEnter();
void motorSpinExecute();
void motorSpinExit();

// Définition des états
State state = MOTOR_STOP;

void motorStopExecute() {
    if (digitalRead(buttonPin) == LOW) {
        state = MOTOR_SPIN;
    }
}

void motorSpinEnter() {
    // Si l'on est déjà entré dans l'état, on ne fait rien
    if (motorSpinEnterDone) return;

    digitalWrite(ledPin, HIGH);
    state = MOTOR_SPIN;
    motorSpinEnterDone = true;
}

void motorSpinExecute() {
    // Si l'on n'est pas encore entré dans l'état, on ne fait rien
    if (!motorSpinEnterDone) return;

    digitalWrite(motorPin, HIGH);
    if (digitalRead(buttonPin) == LOW) {
        digitalWrite(motorPin, LOW);

        motorSpinExit();
    }
}

void motorSpinExit() {
    digitalWrite(ledPin, LOW);

    motorSpinEnterDone = false;
    state = MOTOR_STOP;    
}

void setup() {
    pinMode(ledPin, OUTPUT);
    pinMode(motorPin, OUTPUT);
    pinMode(buttonPin, INPUT);
}

void loop() {
    switch (state) {
        case MOTOR_STOP:
            motorStopExecute();
            break;
        case MOTOR_SPIN:
            motorSpinEnter();
            motorSpinExecute();
            break;
    }
}
```

## Résumé
Lorsque l'on veut faire une transition vers un nouvel état, on désactive l'ancien état et on active le nouvel état. Lorsque l'on désactive un état, on exécute la fonction de sortie de l'état. Lorsque l'on active un état, on exécute la fonction d'entrée de l'état.

Prenez note qu'il y a plusieurs façons de faire une machine à états finis. C'est une façon de faire qui est simple à comprendre et à utiliser pour les débutants.

# Définir les états requis
Avant de commencer à coder, il est important de définir les états requis pour notre machine à états finis. De plus, il faut aussi définir les transitions entre les états.

Les transitions consistent à passer d'un état à un autre. La transition peut être déclenchée par un événement ou par un délai. Dans le cas de l'exemple précédent, nous avons utilisé un bouton pour déclencher la transition entre les états.

# Utiliser la programmation orientée objet
Reprenons l'exemple précédent, mais convertissons-le en utilisant la programmation orientée objet. Nous allons aussi modifier le projet.
- Avant que le moteur entre en action, on doit faire clignoter une DEL.
- Pendant que le moteur tourne, la DEL doit être allumée.
- Pendant que le moteur arrête de tourner, la DEL doit être éteinte graduellement.

## Définir la classe
La classe doit avoir un constructeur qui prend en paramètre la broche du bouton, la broche de la DEL ainsi que celle du moteur. Elle doit aussi avoir une fonction `update()` qui devra être appelée dans la fonction `loop()`.

Voici le code pour l'entête de la classe.

```cpp
#pragma once
#include <OneButton.h>

class Motor {
public:
  enum State { OFF,
               RUN_ENTER,
               ON,
               RUN_EXIT };

  Motor(int motorPin, int ledPin, int buttonPin);

  void update();

private:
  const int _motorPin;
  const int _ledPin;
  unsigned long _previousTime = 0;
  unsigned long _currentTime = 0;
  
  const int _blinkRate = 50;
  
  bool _buttonPressed = false;
  State _state = OFF;

  OneButton _button;

  static Motor *instance;
  static void buttonClick(Motor *self);
  static void buttonLongPress(Motor *self);

  bool timeElapsed(unsigned long duration);
  
  void offExecute();
  void runEnter();
  void runExit();
  void runExecute();
};
```

Voici le code du fichier .cpp.

```cpp
#include "Motor.h"

// Initialisation de l'instance static du moteur
// Pour l'instant null
Motor *Motor::instance = nullptr;

// Constructeur
Motor::Motor(int motorPin, int ledPin, int buttonPin)
  : _motorPin(motorPin), _ledPin(ledPin) {
  pinMode(_motorPin, OUTPUT);
  pinMode(_ledPin, OUTPUT);

  instance = this;

  _button.setDebounceTicks(50);
  _button.setClickTicks(10);
  _button.setPressTicks(1000);

  _button.attachClick(buttonClick, instance);
  _button.attachLongPressStop(buttonLongPress, instance);
}

static void Motor::buttonClick(Motor *self) {
  self->_buttonPressed = true;
  self->_previousTime = millis();
  self->_state = RUN_ENTER;
}

static void Motor::buttonLongPress(Motor *self) {
  self->_buttonPressed = true;
  self->_state = RUN_EXIT;
  self->_previousTime = millis();
}

void Motor::offExecute() {
  digitalWrite(_motorPin, LOW);
  digitalWrite(_ledPin, LOW);
}

void Motor::runEnter() {
  static unsigned long lastTime = 0;
  
  if (timeElapsed(500)) {
    _state = ON;
    digitalWrite(_ledPin, HIGH);
  }
  
  if (_currentTime - lastTime >= _blinkRate) {
    lastTime = _currentTime;
    digitalWrite(_ledPin, !digitalRead(_ledPin));
  }
}

void Motor::runExecute() {
  digitalWrite(_motorPin, HIGH);
  digitalWrite(_ledPin, HIGH);
}

void Motor::runExit() {
  static unsigned long lastTime = 0;
  static int brightness = 255;
  
  if (timeElapsed(1000)) {
    _state = OFF;
    digitalWrite(_ledPin, LOW);
  }
  
  if (_currentTime - lastTime >= 4) {
    lastTime = _currentTime;
    
    brightness = brightness > 0 ? brightness - 1 : 0;
  }
  analogWrite(_ledPin, brightness);
}

void Motor::update() {
  _currentTime = millis();
  
  switch (_state) {
    case OFF:
      offExecute();
      break;
    case RUN_ENTER:
      runEnter();
      break;
    case ON:
      runExecute();
      break;
    case RUN_EXIT:
      runExit();
      break;
  }
}

bool Motor::timeElapsed(unsigned long duration) {
  if (millis() - _previousTime >= duration) {
    _previousTime = millis();
    return true;
  } else {
    return false;
  }
}
```
