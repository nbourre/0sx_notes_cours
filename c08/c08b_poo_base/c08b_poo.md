# La programmation orientée objet avec Arduino <!-- omit in toc -->

# Table des matières <!-- omit in toc -->

# Introduction
La programmation orientée objet est une méthode de programmation populaire qui permet d'organiser le code autour de concepts appelés "objets". Ceux-ci ont des propriétés et des comportements.

# Concepts de base
## Concept de la classe
**Une classe est un modèle pour créer des objets**. Il s'agit d'un concept. Par exemple, si l'on parle d'un chien. À quoi pensez-vous?

Vous pouvez imaginer un chien noir qui a une certaine grandeur avec un pelage court. Il peut courrir, aboyer, marcher, etc.

Une classe décrit les propriétés et les comportements d'un objet.

Ainsi dans le cas d'un chien, nous avons les propriétés suivantes couleur, taille, pelage, etc. et les comportements suivants courrir, aboyer, marcher, etc.

On peut créer autant de concept que nécessaire pour un projet.

## Concept de l'objet
**Un objet est une instance d'une classe**. C'est-à-dire que c'est une représentation physique de la classe. Reprenons l'exemple du chien.

Si on dit "Idéfix" ou "Milou". On ne parle plus du concept d'un chien, mais d'une instance d'un chien c'est-à-dire que l'on parle d'un chien en particulier.

# Dans Arduino
Dans un projet électronique, nous avons des objets physiques. Par exemple, un bouton, un capteur, un moteur, etc. Nous pouvons définir des concepts plus haut-niveau par exemple un verrou, un ouvre-porte, etc. et créer des classes pour représenter ces objets.

L'avantage de créer des classes, c'est que cela rend le code plus facile à lire et à comprendre. De plus, cela permet de réutiliser le code pour d'autres projets.

# Création d'une classe
Dans Arduino, nous pouvons créer des classes pour représenter des objets physiques.

La syntaxe pour créer une classe est la suivante:

```cpp

class NomDeLaClasse {
  // Déclaration des attributs et méthodes
};

```

TODO : Continuer l'article


# Éléments publics et privés








Dans cet article, nous allons explorer la programmation orientée objet en simulant un verrou motorisé à l'aide un servo-moteur.

Pour ce projet, nous utiliserons une carte Arduino, un servo-moteur, une *breadboard* et des fils de raccordement.

Le servo-moteur est un moteur qui peut être contrôlé avec précision pour se déplacer dans une plage de mouvement spécifiée. Nous allons utiliser un servo-moteur pour simuler un verrou motorisé, qui peut être activé ou désactivé en tournant le servo-moteur dans une direction ou l'autre. Pour plus de détail sur le servo-moteur, consultez [cet article](../../c07/c07d_servo/C07d_servo.md).

Nous allons utiliser la programmation orientée objet pour créer une classe `Verrou` qui représente notre verrou motorisé. Cette classe aura des méthodes pour activer ou désactiver le verrou, ainsi qu'un attribut d'état pour suivre l'état actuel du verrou. Nous utiliserons également une machine à états pour gérer les transitions entre les différents états du verrou.

Maintenant que nous avons une vue d'ensemble de notre projet, passons à la création de la classe Verrou.

```cpp
#include <Servo.h>

enum EtatVerrou {
  FERME,
  OUVERT
};

class VerrouMotoriseServo {
  private:
    Servo servo;
    int angleOuvert;
    int angleFerme;
    int position;
    EtatVerrou etat;
    
  public:
    VerrouMotoriseServo(int pin, int angleOuvert, int angleFerme) {
      this->servo.attach(pin);
      this->angleOuvert = angleOuvert;
      this->angleFerme = angleFerme;
      this->position = angleFerme;
      this->etat = FERME;
      this->servo.write(this->position);
    }
    
    void activer() {
      if (this->etat == FERME) {
        this->position = angleOuvert;
        this->etat = OUVERT;
        this->servo.write(this->position);
      }
    }
    
    void desactiver() {
      if (this->etat == OUVERT) {
        this->position = angleFerme;
        this->etat = FERME;
        this->servo.write(this->position);
      }
    }
    
    EtatVerrou getEtat() {
      return this->etat;
    }
};


