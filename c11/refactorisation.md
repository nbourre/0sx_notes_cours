# La refactorisation <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Les principes de la refactorisation](#les-principes-de-la-refactorisation)
  - [Les principes SOLID](#les-principes-solid)
    - [Le principe de responsabilité unique (Single Responsibility Principle)](#le-principe-de-responsabilité-unique-single-responsibility-principle)
    - [Le principe d'ouverture/fermeture (Open/Closed Principle)](#le-principe-douverturefermeture-openclosed-principle)
- [Étude de cas](#étude-de-cas)
  - [Identification des problèmes](#identification-des-problèmes)
  - [Analyse du projet](#analyse-du-projet)
  - [Déterminer les responsabilités de chaque classe](#déterminer-les-responsabilités-de-chaque-classe)
    - [Classe `Eclairage`](#classe-eclairage)
    - [Classe `Affichage`](#classe-affichage)
  - [Code principal](#code-principal)
- [Résumé](#résumé)


# Introduction
Voici une mise en situation.

Vous avez travaillé sur un projet qui fonctionnait pour les besoins du moment. Mais maintenant, vous devez ajouter une nouvelle fonctionnalité. Vous vous rendez compte que le code est difficile à comprendre et à modifier. Si vous effectuez des modifications, vous risquez de casser le code existant. Vous décidez donc de le réécrire pour l'améliorer. C'est ce que l'on appelle la **refactorisation**.

La refactorisation est le processus de modification du code source pour améliorer sa structure interne sans changer son comportement externe. La refactorisation est généralement effectuée pour améliorer la lisibilité du code, faciliter sa maintenance et augmenter sa flexibilité pour les futures évolutions du logiciel. Elle peut également être effectuée pour réduire la complexité du code ou pour éliminer les défauts de conception.

# Les principes de la refactorisation
La refactorisation est un processus qui peut être appliqué à n'importe quel code, mais il existe des principes qui peuvent vous aider à améliorer votre code.

## Les principes SOLID
Les principes [SOLID](https://fr.wikipedia.org/wiki/SOLID_(informatique)) sont des principes de programmation orientée objet qui peuvent être appliqués à n'importe quel langage de programmation. Ils sont souvent utilisés pour décrire les bonnes pratiques de la programmation orientée objet.

À votre niveau, soit 1ère année, nous allons voir 2 principes des 5 principes du SOLID.

### Le principe de responsabilité unique (Single Responsibility Principle)
Le principe de responsabilité unique (SRP) stipule qu'**une classe doit avoir une seule responsabilité**. Si une classe a plusieurs responsabilités, cela signifie qu'elle est trop complexe et qu'elle doit être divisée en plusieurs classes.

### Le principe d'ouverture/fermeture (Open/Closed Principle)
Le principe d'ouverture/fermeture (OCP) stipule qu'une classe doit être ouverte à l'extension, mais fermée à la modification. **Cela signifie que vous devez pouvoir ajouter de nouvelles fonctionnalités sans modifier le code existant.**

# Étude de cas
Pour pratiquer la refactorisation, nous allons refaire le laboratoire 04 soit celui de l'éclairage automatique. Nous allons étudier le code qui suit. Il s'agit du code de votre collègue Vincent Bureau (Merci! 🙂).

```cpp
#include <LiquidCrystal.h>
#include <HCSR04.h>
const int rs = 36, en = 34, d4 = 32, d5 = 30, d6 = 28, d7 = 26;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
const int contrastPin = 38;

HCSR04 hc(12, 11); 
int distance;

unsigned long currentMillis;
unsigned long previousMillis;
int displayDelay = 250;
int serialDelay = 100;
int ledPin = 4;
const int lumSensorPin = A0;
int lumValue;
int luminosity;
int lumMin = 1023;
int lumMax = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  analogWrite(contrastPin, 100);
  lcd.begin(16, 2); 
}

int ultraSon(int currentMillis){
  distance = hc.dist();
  return distance;
}

void display(int distance,unsigned long currentMillis,int luminosity){
  if (currentMillis - previousMillis >= displayDelay){
    previousMillis = currentMillis;
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(F("Lum : "));
    lcd.print(luminosity);
    lcd.print("%");
    lcd.setCursor(0,1);
    lcd.print(F("Dist : "));
    lcd.print(distance);
  }
}

int autoLum(int currentMillis, int distance){
  lumValue = analogRead(lumSensorPin);
  if (lumValue > lumMax ){
    lumMax = lumValue;
  }
  if (lumValue < lumMin){
    lumMin = lumValue;
  }
  luminosity = map(lumValue,lumMax,lumMin,0,100);

  if (luminosity < 30){
    digitalWrite(ledPin,HIGH);
  }else{
    digitalWrite(ledPin,LOW);
  }
  if(currentMillis-previousMillis >= serialDelay){
    currentMillis = previousMillis;
    Serial.print("Current:");
    Serial.println(luminosity);
    Serial.print("Min:");
    Serial.println(lumMin);
    Serial.print("Max:");
    Serial.println(lumMax);
    Serial.print("Distance:");
    Serial.println(distance);
  }
  return luminosity;
}
void loop() {
  currentMillis = millis();
  distance = ultraSon(currentMillis);
  luminosity = autoLum(currentMillis,distance);
  display(distance,currentMillis,luminosity);
}
```



## Identification des problèmes
Avant de faire la refactorisation, il faut identifier les problématiques du code actuel. 

> **Remarques :** Il y a beaucoup de problèmes dans le code et c'est normal. Vous êtes en apprentissage et cela fait partie du processus. Vous allez apprendre à identifier les problèmes et à les résoudre au fur et à mesure.

- La fonction `ultrason` :
  - est une fonction qui ne fait qu'appeler une fonction de la librairie `HCSR04`. Il n'y a donc pas de raison de faire une fonction pour ça.
  - a le paramètre `currentMillis` qui n'est pas utilisé.
- La fonction `display` :
  - a le paramètre `distance` qui peut être remplacé par la variable globale du même nom.
  - a le paramètre `currentMillis` qui peut être remplacé par la variable globale du même nom.
  - a le paramètre `luminosity` qui peut être remplacé par la variable globale du même nom.
  - est dépendante d'élément externe.
- La fonction `autoLum` :
  - a le paramètre `currentMillis` qui peut être remplacé par la variable globale du même nom.
  - a le paramètre `distance` qui peut être remplacé par la variable globale du même nom.
  - a des éléments qui n'ont pas de lien avec la fonction.
  - est dépendante d'élément externe.

Ce sont tous des problématiques que la refactorisation va permettre de résoudre.

## Analyse du projet
La première étape sera de déterminer les différents systèmes de ce projet.

Les grandes lignes du projet étaient ceci :
- Lire les valeurs du capteur de luminosité;
- Calibrer le déclenchement de la lumière avec la valeur minimum et maximum du capteur de luminosité;
- Allumer une DEL lorsque la luminosité est plus basse qu'un seuil;
- Lire la valeur de la distance avec le capteur ultrason;
- Afficher des valeurs dans le port série
- Afficher des valeurs sur l'écran LCD.

Dans ce projet, nous avons 3 systèmes :
- Le système de lecture de la luminosité;
- Le système de lecture de la distance;
- Le système d'affichage.

Le système de distance n'a aucun lien avec le système de luminosité. Il n'y a donc pas de raison de les regrouper. Nous avons donc besoin 2 classes pour ces systèmes.

L'affichage est un système qui a besoin des données des autres systèmes. Il reçoit donc les données des autres systèmes. On effectue aussi plusieurs opérations avec celui-ci. Nous avons donc besoin d'une classe pour l'affichage. Nous avons donc besoin de 3 classes pour ce projet.

Pour le système de distance, nous n'avons pas besoin de faire de classe, car on utilise déjà la librairie `HCSR04` et on ne fait que lire la distance.

> **Note :** Je sais que nous avons le système d'alarme, mais on se concentre sur le système d'éclairage automatique.

## Déterminer les responsabilités de chaque classe
Nous avons donc besoin de 2 classes pour ce projet. Nous allons maintenant déterminer les responsabilités de chaque classe.

Pour l'instant, on n'a pas besoin de classe pour la distance. Nous allons donc nous concentrer sur les 2 autres classes.

### Classe `Eclairage`
La classe `Eclairage` va gérer le système d'éclairage. Elle va lire la valeur du capteur de luminosité et allumer la DEL lorsque la luminosité est trop basse.

Dans sa première moutures, les fonctions publiques de cette classe seront :
- `getLuminosity()`; Pour lire la valeur du capteur de luminosité;
- `update()`; Pour mettre à jour la valeur de la luminosité en continu;
- `getMinLuminosity()`; Qui retournera la valeur minimum de la luminosité;
- `getMaxLuminosity()`; Qui retournera la valeur maximum de la luminosité;
- `setThreshold(int threshold)`; Pour définir le seuil de déclenchement de la DEL;
- `getThreshold()`; Pour obtenir le seuil de déclenchement de la DEL;

Voici un code qui répond à l'analyse de la classe `Eclairage` :

```cpp
class Eclairage{
  public:
    // Constructeur
    Eclairage(int lumSensorPin, int ledPin);

    int getLuminosity() { return _lumValue; }
    int getMinLuminosity() { return _lumMin; }
    int getMaxLuminosity() { return _lumMax; }
    void setThreshold(int threshold);
    int getThreshold() { return _threshold; }

    // Fonction appelée dans le loop
    void update();

  private:
    int _lumSensorPin;
    int _ledPin;
    int _lumValue;
    int _lumMin;
    int _lumMax;
    int _threshold;
};

// Peut être déplacé dans le fichier Eclairage.cpp
Eclairage::Eclairage(int lumSensorPin, int ledPin){
  _lumSensorPin = lumSensorPin;
  _ledPin = ledPin;
  _lumMin = 1023;
  _lumMax = 0;
  _threshold = 30;
  pinMode(_ledPin, OUTPUT);
}

void Eclairage::update(){
  _lumValue = analogRead(_lumSensorPin);
  if (_lumValue > _lumMax ){
    _lumMax = _lumValue;
  }
  if (_lumValue < _lumMin){
    _lumMin = _lumValue;
  }
  int luminosity = map(_lumValue,_lumMin,_lumMax,0,100);
  if (luminosity < _threshold){
    digitalWrite(_ledPin,HIGH);
  }else{
    digitalWrite(_ledPin,LOW);
  }
}
```

### Classe `Affichage`
Pour la classe `Affichage`, celle-ci va recevoir les données des autres classes et les afficher sur l'écran LCD. Ne sachant pas encore tous les systèmes qui devront afficher de l'information, nous allons développer une classe indépendante de tout autre système.

On veut rafraîchir l'affichage à toutes les temps données. On a donc besoin d'une fonction pour indiquer le temps entre chaque rafraîchissement.

Dans sa première moutures, les fonctions publiques de cette classe seront :
- `setLine1(String line1)`; Pour définir la première ligne de l'écran LCD;
- `setLine2(String line2)`; Pour définir la deuxième ligne de l'écran LCD;
- `update()`; Pour mettre à jour l'affichage sur l'écran LCD;
- `clear()`; Pour effacer l'écran LCD;
- `setRefreshRate(int refreshRate)`; Pour définir le temps entre chaque rafraîchissement de l'écran LCD;
- `getRefreshRate()`; Pour obtenir le temps entre chaque rafraîchissement de l'écran LCD;

Voici le code qui répond à l'analyse de la classe `Affichage` :

```cpp
#include <LiquidCrystal_I2C.h>

class Affichage {
  public:
    // Constructeur
    Affichage(uint8_t lcdAddress, uint8_t lcdColumns, uint8_t lcdRows);

    void setLine1(String line1);
    void setLine2(String line2);
    void update();
    void clear();
    void setRefreshRate(int refreshRate) { _refreshRate = refreshRate; }
    int getRefreshRate() { return _refreshRate; }

  private:
    int _refreshRate = 250;
    String _line1;
    String _line2;
    
    unsigned long _currentTime;
    bool _needUpdate = false; // Drapeau pour indiquer si l'affichage doit être mis à jour
    
    LiquidCrystal_I2C _lcd;
};

// Peut être déplacé dans le fichier Affichage.cpp
Affichage::Affichage(uint8_t lcdAddress, uint8_t lcdColumns, uint8_t lcdRows):
  _lcd (lcdAddress, lcdColumns, lcdRows) // Initialisation de l'écran LCD
{
  _lcd.init();
  _lcd.backlight();
}

void Affichage::setLine1(String line1){
  // On sort de la méthode si la ligne est la même que la précédente 
  if (line1.equals(_line1)){
    return;
  }

  _line1 = line1;
  _needUpdate = true;
}

void Affichage::setLine2(String line2){
  // On sort de la méthode si la ligne est la même que la précédente
  if (line2.equals(_line2)){
    return;
  }
  _line2 = line2;
  _needUpdate = true;
}

void Affichage::clear(){
  _lcd.clear();
}

void Affichage::update(){
  static unsigned long lastUpdate = 0;
  _currentTime = millis();

  // On sort de la méthode si le temps entre le dernier rafraîchissement est plus petit que le temps de rafraîchissement
  if (_currentTime - lastUpdate < _refreshRate){
    return;
  }

  // Pourquoi afficher si on n'a pas besoin de mettre à jour l'affichage?
  if (!_needUpdate){
    return;
  }
  
  lastUpdate = _currentTime;

  _lcd.clear();
  _lcd.setCursor(0,0);
  _lcd.print(_line1);
  _lcd.setCursor(0,1);
  _lcd.print(_line2);

  // On redescent le drapeau
  _needUpdate = false;
}
```

## Code principal
Une fois que les classes sont réalisées, il ne reste plus qu'à les utiliser dans le code principal. 

```cpp
#include <Arduino.h>
#include "Eclairage.h"
#include "Affichage.h"
#include "HCSR04.h"

#define LED_PIN 4
#define LUM_SENSOR_PIN A0
#define ECHO_PIN 2
#define TRIGGER_PIN 3
#define LCD_ADDRESS 0x27
#define LCD_COLUMNS 16
#define LCD_ROWS 2

Eclairage eclairage(LUM_SENSOR_PIN, LED_PIN);
HCSR04 hc(ECHO_PIN, TRIGGER_PIN);
Affichage affichage(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

unsigned long currentTime;

void setup() {
  Serial.begin(9600);  
}

void loop() {
  currentTime = millis();

  eclairage.update();

  affichage.setLine1("Distance: " + String(hc.getDistance()));
  affichage.setLine2("Luminosite: " + String(eclairage.getLuminosity()));
  affichage.update();
}

```

Voilà! Le code principal est maintenant beaucoup plus lisible et facile à comprendre.

# Résumé
Dans ce tutoriel, nous avons vu comment utiliser les classes pour organiser le code. Nous avons vu comment définir une classe et comment utiliser les attributs et les méthodes d'une classe. Nous avons aussi vu comment utiliser les classes dans le code principal.

Il faut se rappeler que si j'utilise un attribut qui est un objet, il faudra faire une référence à cet objet à l'aide du symbole `&` dans le constructeur de la classe.

