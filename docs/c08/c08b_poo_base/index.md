# La programmation orientée objet avec Arduino


![The image features a man in business casual attire - a white shirt with rolled-up sleeves with a fan and a thermometer](<assets/DALL·E 2024-03-18 14.59.55.webp>)

![A realistic image of an Arduino board on a wooden table with a small electric fan connected to it. The fan is running, and you can see the motion blur](<assets/DALL·E 2024-03-18 15.05.20.webp>)

![alt text](assets/think-smart.gif)

## Introduction
La programmation orientée objet est une méthode de programmation populaire qui permet d'organiser le code autour de concepts appelés "objets". Ceux-ci ont des propriétés et des comportements.

## Concepts de base
### Concept de la classe
**Une classe est un modèle pour créer des objets**. Il s'agit d'un concept. Par exemple, si l'on parle d'un chien. À quoi pensez-vous?

Vous pouvez imaginer un chien noir qui a une certaine grandeur avec un pelage court. Il peut courrir, aboyer, marcher, etc.

Une classe décrit les propriétés et les comportements d'un objet.

Ainsi dans le cas d'un chien, nous avons les propriétés suivantes couleur, taille, pelage, etc. et les comportements suivants courrir, aboyer, marcher, etc.

On peut créer autant de concept que nécessaire pour un projet.

### Concept de l'objet
**Un objet est une instance d'une classe**. C'est-à-dire que c'est une représentation physique de la classe. Reprenons l'exemple du chien.

Si on dit "Idéfix" ou "Milou". On ne parle plus du concept d'un chien, mais d'une instance d'un chien c'est-à-dire que l'on parle d'un chien en particulier.

![alt text](assets/idefix.png)

On pourrait dire que "Idéfix" est un chien blanc, de taille petite, avec un pelage court. Il peut courrir, aboyer, marcher, etc.

## Dans Arduino
Dans un projet électronique, nous avons des objets physiques. Par exemple, un bouton, un capteur, un moteur, etc. Nous pouvons définir des concepts plus haut-niveau par exemple un verrou, un ouvre-porte, etc. et créer des classes pour représenter ces objets.

L'avantage de créer des classes, c'est que cela rend le code plus facile à lire et à comprendre. De plus, cela permet de réutiliser le code pour d'autres projets.

Voici un diagramme simple pour représenter les classes typiques que l'on pourrait retrouver dans un projet de maison intelligente.

![alt text](<assets/Exemple diagramme POO.png>)

## Création d'une classe
Dans Arduino, nous pouvons créer des classes pour représenter des objets physiques.

Plusieurs langages de programmation modernes n'utilisent qu'un seul fichier pour définir une classe comme le C#. Cependant, Arduino utilise deux fichiers pour définir une classe. Un fichier `.cpp` pour la définition de la classe et un fichier `.h` pour la déclaration de la classe.

Il faut que le fichier `.h` soit inclus dans le fichier `.cpp` pour que la classe soit définie.

### Fichier .h
Le fichier `.h` contient la déclaration de la classe. C'est-à-dire que c'est ici que nous définissons les propriétés et les méthodes de la classe.

La syntaxe pour créer une classe est la suivante:

```cpp

class NomDeLaClasse {
  // Déclaration des attributs et méthodes
};

```

> **Convention de nommage :**
> En C++, les noms de classes commencent par une lettre majuscule. Par exemple, `Verrou`, `Chien`, `OuvrePorte`, etc.
> 
> Si la classe a plusieurs mots, on utilise la convention *upper CamelCase* pour nommer la classe. C'est-à-dire les autres mots commencent par une lettre majuscule. Par exemple, `VerrouMotorise`, `OuvrePorteAutomatique`, etc.	

### Les accesseurs public et private
Dans une classe, nous pouvons définir des attributs et déclarer des méthodes qui sont accessibles depuis l'extérieur de la classe et d'autres qui ne le sont pas. Cela permet de protéger les attributs et les méthodes qui ne doivent pas être modifiés ou appelés depuis l'extérieur de la classe.

Dans le cadre du cours, nous nous intéresserons uniquement aux attributs et méthodes publics ou privés.

Le mot-clé `public` permet de définir les attributs et méthodes qui sont accessibles depuis l'extérieur de la classe.

Le mot-clé `private` permet de définir les attributs et méthodes qui ne sont pas accessibles depuis l'extérieur de la classe.

En C++, on fait des blocs d'attributs et de méthodes publics et privés. 

On démarre un bloc public avec le mot-clé `public` et on termine le bloc avec le mot-clé `private`.

```cpp
class NomDeLaClasse {
  public:
    // Déclaration des attributs et méthodes publics
    int attributPublic; // exemple
    void methodePublique(); // exemple
  private:
    // Déclaration des attributs et méthodes privés
    int attributPrive; // exemple
    void methodePrivee(); // exemple
};
```

### Fichier .cpp

Le fichier `.cpp` est un fichier source C++ qui contient les définitions des méthodes d'une classe. Dans le cadre de la programmation orientée objet, les fichiers `.cpp` sont utilisés pour séparer la déclaration de la classe (dans un fichier `.h`) de sa définition.

Dans le fichier `.cpp`, chaque méthode de la classe est définie avec son corps de fonction correspondant. Cela inclut toutes les instructions nécessaires pour implémenter la fonctionnalité de la méthode, y compris l'accès aux variables et aux fonctions de la classe.

La syntaxe pour définir une méthode est la suivante:

```cpp
typeDeRetour NomDeLaClasse::NomDeLaMethode() {
  // Instructions
}
```


## Exemple VerrouMotorise
Dans cette partie, nous allons explorer la programmation orientée objet en simulant un verrou motorisé à l'aide un servo-moteur.

Pour ce projet, nous utiliserons une carte Arduino, un servo-moteur, une *breadboard* et des fils de raccordement.

Le servo-moteur est un moteur qui peut être contrôlé avec précision pour se déplacer dans une plage de mouvement spécifiée. Nous allons utiliser un servo-moteur pour simuler un verrou motorisé, qui peut être activé ou désactivé en tournant le servo-moteur dans une direction ou l'autre. Pour plus de détail sur le servo-moteur, consultez [cet article](../../c07/c07a_servo/index.md).

Nous allons utiliser la programmation orientée objet pour créer une classe `Verrou` qui représente notre verrou motorisé. Cette classe aura des méthodes pour activer ou désactiver le verrou, ainsi qu'un attribut d'état pour suivre l'état actuel du verrou. Nous utiliserons également une machine à états pour gérer les transitions entre les différents états du verrou.

Maintenant que nous avons une vue d'ensemble de notre projet, passons à la création de la classe Verrou.

```cpp
// Fichier : Verrou.h
#pragma once // Toujours inclure cette ligne dans  un .h pour éviter les problèmes de compilation
#include <Servo.h>

// Déclaration de l'énumération pour les états du verrou
enum EtatVerrou {
  FERME,
  OUVERT
};

class Verrou {

  public:
    // Constructeur
    Verrou(int pin, int angleOuvert, int angleFerme);
    
    void activer(); 
    void desactiver();
    
    // On peut aussi déclarer des méthodes inline
    // "inline" veut dire que l'on peut définir la méthode dans le fichier .h
    EtatVerrou getEtat() {
      return etat;
    }

  private:
    Servo servo;
    int angleOuvert;
    int angleFerme;
    int position;
    EtatVerrou etat;
    
};
```

Voici le code pour le fichier `.cpp` correspondant:

```cpp
// Fichier : Verrou.cpp
#include "Verrou.h"

Verrou::Verrou(int pin, int angleOuvert, int angleFerme) {
  servo.attach(pin);
  angleOuvert = angleOuvert;
  angleFerme = angleFerme;
  position = angleFerme;
  etat = FERME;
  servo.write(position);
}

void Verrou::activer() {
  if (etat == FERME) {
    position = angleOuvert;
    etat = OUVERT;
    servo.write(position);
  }
}

void Verrou::desactiver() {
  if (etat == OUVERT) {
    position = angleFerme;
    etat = FERME;
    servo.write(position);
  }
}
```

Dans le fichier du programme principal, nous allons créer une instance de la classe `Verrou` et l'utiliser pour activer et désactiver le verrou.

```cpp
#include <Arduino.h>
#include "Verrou.h"

// Création d'une instance de la classe
Verrou verrou(9, 0, 180);

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Verrou actif");
  verrou.activer();
  delay(2000);
  Serial.println("Verrou inactif");
  verrou.desactiver();
  delay(2000);
}
```

## Exercices
1. Reproduisez l'exemple du verrou motorisé à l'aide d'un servo-moteur. Utilisez la programmation orientée objet pour créer une classe `Verrou` qui représente votre verrou motorisé. Cette classe aura des méthodes pour activer ou désactiver le verrou, ainsi qu'un attribut d'état pour suivre l'état actuel du verrou. Utilisez une machine à états pour gérer les transitions entre les différents états du verrou.