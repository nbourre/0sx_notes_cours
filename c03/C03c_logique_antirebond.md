# Le rebond <!-- omit in toc -->

![Alt text](gif/ball-throw.gif)

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Principe de fonctionnement](#principe-de-fonctionnement)
- [Schéma](#schéma)
- [Code](#code)
- [Résumé](#résumé)
- [Exercice](#exercice)

# Introduction
Certains d'entre vous avez peut-être remarqué que lors de l'appuie d'un bouton, on avait un effet indésirable. En effet, le bouton était enfoncé et relâché plusieurs fois même si l'on avait appuyé qu'une seule fois. C'est ce qu'on appelle un rebond.

![Alt text](switch-debounce-principle.jpg)

Si l'on regarde le graphique précédent, ce qui arrive, c'est qu'à l'échelle des microsecondes, lorsque l'on appuie sur le bouton, le contact de ne fait pas pleinement. Il y a des microvibrations que le microcontrôleur peut capter.  C'est un problème qui peut être résolu avec un peu de logique.

# Principe de fonctionnement
Lorsqu'un système physique change d'état, il y a souvent des oscillations pendant la période transitoire pour des raisons physiques (mécanique, temps de réponse, etc.). Il faut donc laisser un temps suffisant pour que l’état puisse se stabiliser. Cela peut être rendu possible par filtrage électronique ou mécanique ou bien numériquement grâce au programme qui traite la mesure.

# Schéma
Voici un schéma pour tester le code.

![Alt text](branchement_bouton_input_pullup.png)

# Code

Nous allons créer deux variables qui vont garder en mémoire l’état présent et passé du capteur. Nous allons lire l’entrée digitale et valider son état en fonction de l’état précédent et d’un délai anti-rebond. Cette méthode peut être implémentée avec la fonction `millis()`.

```cpp
int etatPresent = 0; // Etat présent du capteur
int etatPrecedent = 0; // Etat précédent du capteur
int delai = 50; // Délai anti-rebond en ms
unsigned long dernierChangement = 0; // Dernier changement d'état du capteur
int etat = 0; // Etat du capteur
int pinBouton = 2; // Pin du bouton

void setup() {
  Serial.begin(9600);
  pinMode(pinBouton, INPUT_PULLUP);
}

void loop() {
  etatPresent = digitalRead(pinBouton); // Lecture de l'état du capteur

  if (etatPresent != etatPrecedent) { // Si l'état a changé
    dernierChangement = millis(); // On enregistre le temps actuel
  }

  if ((millis() - dernierChangement) > delai) { // Si le délai est dépassé
    if (etatPresent != etat) { // Si l'état a changé
        etat = etatPresent; // On enregistre l'état actuel
      Serial.println(etat); // On affiche l'état du capteur
    }
  }

  etatPrecedent = etatPresent; // On enregistre l'état actuel pour la prochaine itération
}
```

# Résumé
Si vous variez le délai anti-rebond (`dernierChangement`), vous verrez que le capteur est plus ou moins sensible. En prenant un temps suffisamment long, vous verrez que le capteur ne sera plus sensible aux microvibrations.

Ce tutoriel permet de comprendre et d’implémenter la logique anti-rebond. Pour un plus grand simplicité d’utilisation, vous pouvez écrire une librairie ou utiliser une librairie existante comme OneButton.h.

# Exercice
- Testez le code dans l'exemple en faisant allumé et éteindre une DEL lorsque vous appuyez sur le bouton.
  - 1 clic - Allumé, 1 clic - Éteint