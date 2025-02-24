# L'écran LCD 1602 - Partie 01 <!-- omit in toc -->

![LCD 1602](assets/lcd_1602.jpg)

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [LCD 1602 (mode 4 bits)](#lcd-1602-mode-4-bits)
  - [Fonctionnalités principales](#fonctionnalités-principales)
  - [Spécifications rapides](#spécifications-rapides)
  - [Exemple de branchement en mode 4 bits](#exemple-de-branchement-en-mode-4-bits)
- [Utilisation avec la bibliothèque `LiquidCrystal`](#utilisation-avec-la-bibliothèque-liquidcrystal)
  - [Exemple de base](#exemple-de-base)
  - [Exemple avec défilement (scrolling)](#exemple-avec-défilement-scrolling)
  - [Fonctions utiles](#fonctions-utiles)
- [Alternative I2C (avec la bibliothèque `LCD_I2C` de blackhat)](#alternative-i2c-avec-la-bibliothèque-lcd_i2c-de-blackhat)
- [Exercices](#exercices)
- [Références](#références)


---

# Introduction

- Les écrans LCD (Liquid Crystal Display) sont très répandus (montres, cadrans de voiture, cafetières, etc.).
- Un LCD 1602 offre 2 lignes de 16 caractères, donc un total de 32 caractères.
- Son utilisation nécessite quelques connexions, mais il est également possible de réduire la quantité de broches requises via un module I2C (détails ci-dessous).
- Nous verrons les spécificités techniques du protocole I2C au **prochain cours**.

---

# LCD 1602 (mode 4 bits)

## Fonctionnalités principales

- **Affichage de caractères** (dont certains caractères spéciaux ou accentués).
- **Réglage de la luminosité** et du contraste.
- **Fonctionnement en mode 4 bits** ou 8 bits (4 bits est plus courant pour économiser des broches).

## Spécifications rapides

- Le module LCD 1602 possède 16 broches.
- On l’alimente en 5V.
- On peut ajuster le contraste (V0) via un potentiomètre.
- Le branchement « 4 bits » nécessite moins de broches Arduino que le mode 8 bits.

## Exemple de branchement en mode 4 bits

- **Broches LCD**  
  - GND, R/W et K → Ground  
  - Vcc et A → 5V  
  - V0 → Potentiomètre (pour le contraste)  
  - RS → Broche 36 Arduino  
  - E (Enable) → Broche 34 Arduino  
  - D4 → Broche 32 Arduino  
  - D5 → Broche 30 Arduino  
  - D6 → Broche 28 Arduino  
  - D7 → Broche 26 Arduino

![image illustrant le branchement (Fritzing ou autre) avec description des connexions](assets/branchement_lcd_bb.png)

---

# Utilisation avec la bibliothèque `LiquidCrystal`

## Exemple de base

Points clés :  
- Inclure la bibliothèque `LiquidCrystal` standard  
- Déclarer les broches utilisées (RS, E, D4, D5, D6, D7)  
- Initialiser et afficher un message  

**Code** :
```cpp
#include <LiquidCrystal.h>

// Ajuster les broches selon le branchement
const int rs = 36, en = 34, d4 = 32, d5 = 30, d6 = 28, d7 = 26;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  lcd.begin(16, 2);
  lcd.print(F("Allo toi!"));
}

void loop() {
  lcd.setCursor(0, 1);
  lcd.print(millis() / 1000);
  delay(100);
}
```

## Exemple avec défilement (scrolling)

- Utilise `scrollDisplayLeft()` ou `scrollDisplayRight()`
- Permet de faire défiler le texte sur l’écran  
- Nécessite des **delays** pour la démonstration, mais attention à éviter les `delay()` en pratique (elles bloquent le programme)

**Code** :
```cpp
#include <LiquidCrystal.h>

const int rs = 36, en = 34, d4 = 32, d5 = 30, d6 = 28, d7 = 26;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  lcd.begin(16, 2);
  lcd.print("Hello!");
  delay(1000);
}

void loop() {
  // Défiler le texte vers la gauche
  for (int i = 0; i < 6; i++) {
    lcd.scrollDisplayLeft();
    delay(150);
  }

  // Défiler le texte vers la droite
  for (int i = 0; i < 22; i++) {
    lcd.scrollDisplayRight();
    delay(150);
  }

  // Ramener le texte à sa position initiale
  for (int i = 0; i < 16; i++) {
    lcd.scrollDisplayLeft();
    delay(150);
  }

  delay(1000);
}
```

## Fonctions utiles

- **`lcd.begin(16, 2)`** : initialise l’affichage (16 colonnes, 2 lignes).
- **`lcd.print("message")`** : affiche un texte à la position courante.
- **`lcd.setCursor(col, row)`** : positionne le curseur (colonnes et lignes débutent à 0).
- **`lcd.clear()`** : efface l’écran et replace le curseur en position (0,0).
- **`lcd.scrollDisplayLeft()` / `lcd.scrollDisplayRight()`** : fait défiler le contenu de l’écran.

---

# Alternative I2C (avec la bibliothèque `LCD_I2C` de blackhat)

Dans certains kits, on trouve un module LCD 1602 avec une interface I2C. Cela permet de réduire le nombre de broches utilisées sur l’Arduino.

Pour ceux qui possèdent un module LCD 1602 **avec** une interface I2C :

- Il existe la bibliothèque `LCD_I2C` (de blackhat) qui facilite l’utilisation :
  ```cpp
  #include <LCD_I2C.h>  // Bibliothèque LCD I2C de blackhat
  
  LCD_I2C lcd(0x27, 16, 2); 
  // 0x27 étant l'adresse I2C de l'écran
  // Pour trouver l'autre adresse, utilisez l'exemple Arduino "wire/i2c_scanner"
  // 16 x 2 sa taille en colonnes/lignes
  
  void setup() {
    lcd.begin();
    lcd.print("Bonjour I2C!");
  }
  
  void loop() {
    // Code similaire pour setCursor, etc.
  }
  ```


- **Branchement pour la version I2C** :  

![image avec la carte Arduino et l’écran I2C, annotée pour clarifier les connexions](assets/branchement_lcd_i2c_bb.svg)

  - On connecte seulement 4 fils : GND, VCC, SDA, SCL
  - Cette méthode économise des broches sur l’Arduino en n’utilisant que les lignes I2C (SDA/SCL). Cependant, il faut avoir le module I2C compatible.
  - Les détails complets du protocole I2C (adresses, vitesses de communication, etc.) seront expliqués dans le **prochain cours**.

---

# Exercices

1. **Branchement**  
   - Réalisez le branchement du LCD adapté à votre situation (mode 4 bits ou I2C).
2. **Caractères spéciaux**  
   - À l'aide de la bibliothèque adéquate, recherchez la fonction permettant d’afficher un caractère spécial.  
   - Essayez d’afficher un carré ou une lettre accentuée.
3. **Symboles personnalisés**  
   - Découvrez comment créer et afficher un symbole personnalisé avec l'exemple `CustomCharacter` dans la bibliothèque respective.
   - Utilisez le fichier [`createur_caractere.xlsx`](assets/createur_caractere.xlsx) (fourni) pour générer votre propre caractère.

---

# Références

- [Arduino LCD Tutorial](https://howtomechatronics.com/tutorials/arduino/lcd-tutorial/)
- [7 Arduino LCD tricks](https://www.baldengineer.com/arduino-lcd-display-tips.html)
- [Liquid crystal displays](https://docs.arduino.cc/learn/electronics/lcd-displays)
- [Bibliothèque `LCD_I2C` (blackhat)](https://github.com/blackhack/LCD_I2C) <!-- Exemple de lien, ajustez si nécessaire -->
```