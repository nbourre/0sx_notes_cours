# Électricité de base <!-- omit in toc -->

- [Branchement de base](#branchement-de-base)
- [Voltage, intensité, résistance](#voltage-intensité-résistance)
  - [Le voltage](#le-voltage)
    - [Important *Life skill*](#important-life-skill)
- [Les conventions](#les-conventions)
  - [Voltage de l'arduino](#voltage-de-larduino)
- [Plaque d'essai](#plaque-dessai)
- [Références](#références)


# Branchement de base
Dans votre kit, je vous suggère le branchement de base permanent suivant :

![Alt text](assets/schemas/branchement_base_bb.png)

Ce branchement permet d'accélérer le démarrage de vos projets. Il vous permettra de tester vos programmes sans avoir à brancher et débrancher les fils de courant à chaque fois.

# Voltage, intensité, résistance
L'objectif de cette section n'est pas de vous donner une formation scientifique sur ce qu'est le voltage, l'ampérage, etc. D'ailleurs, ce sont des notions que vous avez vu au secondaire. Je vous suggère de vous référer à votre cours de physique pour vous rafraîchir la mémoire.

L'objectif est plutôt de savoir comment et où vous pouvez mesurer ces valeurs pour vous assurer que votre circuit fonctionne correctement.

## Le voltage
Le voltage est la différence de potentiel entre deux points. C'est la force qui pousse les électrons à circuler dans un circuit. Le voltage est mesuré en volt (V).

Lorsque l'on branche un circuit électronique il est super important de respecter le voltage de l'appareil, car si vous branchez un appareil à un adaptateur qui donne trop de voltage, vous risquez de brûler votre appareil.

### Important *Life skill*
Habituellement sur les appareils, on peut trouver une étiquette ou gravure près du port de branchement qui indique le voltage de l'appareil. Par exemple, un appareil qui fonctionne à 5V aura une étiquette qui indique 5V.

Voici quelques exemples d'étiquettes de voltage :

| Voltage | Description |
| --- | --- |
| ![Alt text](assets/voltage_01.jpg) | 5V |





# Les conventions

> ## Très important
> La convention veut que les fils rouges soient branchés sur les fils positifs (+) et les fils noirs sur les fils négatifs (-). C'est une convention, mais c'est une convention qui est respectée par la plupart des gens et l'industrie. **C'est donc une convention que vous devez respecter**.
> 
> Je retrancherai des points si vous ne respectez pas cette convention!

## Voltage de l'arduino
Le voltage de l'arduino est de 5V. C'est le voltage de sortie de la carte. C'est le voltage que vous devez utiliser pour brancher vos composants.

> **Attention!**
> 
> Toutefois, ceci n'est pas le standard de l'industrie. La plupart des composants sont branchés sur un voltage de 3.3V. C'est pourquoi il est important de lire la documentation de vos composants pour savoir quel voltage ils utilisent.

# Plaque d'essai

# Références
- [TUTO ARDUINO #1 : INSTALLATION ET FAIRE CLIGNOTER UNE LED!](https://www.youtube.com/watch?v=k0KYfGvZUCw&list=PLm9ko_-biSnQz-1PGorgsi3Q1CSN7HdNh&index=3)
- [TUTO ARDUINO #2 : FAIRE FONCTIONNER UN BOUTON / INTERRUPTEUR!](https://www.youtube.com/watch?v=MnzidiZ_6ok)