# Introduction <!-- omit in toc -->
> "Un voyage de mille lieues commence toujours par un premier pas." – Lao Tseu

# Table des matières <!-- omit in toc -->
- [Le langage de programmation](#le-langage-de-programmation)
  - [Exemples](#exemples)
- [Comment programmer un Arduino](#comment-programmer-un-arduino)
- [La fonction `setup`](#la-fonction-setup)
- [La fonction `loop`](#la-fonction-loop)
- [Cycle de vie d'un programme Arduino](#cycle-de-vie-dun-programme-arduino)
  - [📌 Explications du diagramme :](#explications-du-diagramme)
- [Les principaux types de données](#les-principaux-types-de-donnees)
  - [🛠 Déclaration et utilisation](#declaration-et-utilisation)
  - [🏗 Comparaison des types et exemples d'utilisation](#-comparaison-des-types-et-exemples-dutilisation)
  - [⚠ Précision et limitations du type `float`](#precision-et-limitations-du-type-float)
  - [🔥 Problèmes de conversion `float → int`](#problemes-de-conversion-float-int)
- [📌 Les variables en Arduino](#les-variables-en-arduino)
  - [📍 La portée des variables](#la-portee-des-variables)
    - [1️⃣ Variables globales](#1-variables-globales)
    - [2️⃣ Variables locales](#2-variables-locales)
    - [3️⃣ Variables statiques](#3-variables-statiques)
  - [🔄 Illustration de la portée des variables](#illustration-de-la-portee-des-variables)
  - [🔘 Application pratique des variables statiques](#application-pratique-des-variables-statiques)
  - [✅ Bonnes pratiques](#bonnes-pratiques)
- [Wokwi - Simulateur Arduino](#wokwi-simulateur-arduino)
  - [Créer un projet](#creer-un-projet)
  - [Exercice - Premier projet](#exercice-premier-projet)
- [Exercices](#exercices)
  - [Recherches](#recherches)
  - [Questions](#questions)
  - [Programmation](#programmation)
    - [Défi](#defi)

---

# Le langage de programmation
Arduino utilise un langage de programmation spécifique appelé "Arduino Language" ou "Arduino C++".

Le langage Arduino est basé sur le langage C++, avec des modifications et des extensions spécifiques pour permettre une utilisation facile des fonctionnalités du microcontrôleur Arduino. Il est donc recommandé de connaître les bases du langage C++ avant de se lancer dans la programmation Arduino.

> **Note**
> 
> Si vous avez déjà programmé en C# ou Java, vous verrez que le langage Arduino est très proche de ces langages. C'est d'ailleurs pour cette raison que le langage Arduino est souvent utilisé pour initier les débutants à la programmation embarquée.

## Exemples

Voici quelques exemples de structures de base du langage Arduino :

- Déclaration de variables :

```cpp
int compteur = 0;           // Variable entière
float temperature = 25.5;   // Variable flottante
char caractere = 'A';       // Variable de caractère
bool etat = true;           // Variable booléenne (vrai/faux)
```

- Structures de contrôle de flux :

```cpp
if (conditionA) {
  // Code à exécuter si la conditionA est vraie
} else if (conditionB) {
  // Code à exécuter si la conditionB est vraie
}
else {
  // Code à exécuter si la condition est fausse
}

while (condition) {
  // Code à exécuter tant que la condition est vraie
}

for (int i = 0; i < 10; i++) {
  // Code à exécuter 10 fois (i va de 0 à 9)
}

```

- Fonctions :

```cpp
void maFonction() {
  // Code de la fonction
}

int maFonctionAvecRetour() {
  // Code de la fonction
  return 5; // Valeur de retour de la fonction
}

void maFonctionAvecParametres(int param1, float param2) {
  // Code de la fonction utilisant les paramètres param1 et param2
}

```

Il existe également de nombreuses fonctions prédéfinies dans le langage Arduino qui permettent d'interagir avec le microcontrôleur et ses périphériques (lecture et écriture sur les pins, gestion de l'horloge, gestion de la communication série, etc.).

# Comment programmer un Arduino

Voici la structure de base d'un programme Arduino :

```cpp
void setup() {
  // Code à exécuter une seule fois au démarrage
}

void loop() {
  // Code à exécuter en boucle
}
```

Le programme Arduino comporte deux fonctions de base obligatoire : `setup` et `loop`.

La fonction `setup` est exécutée une seule fois au démarrage du programme. On y met généralement le code de configuration, comme la définition des pin de sortie ou l'initialisation de certains paramètres.

La fonction `loop` est exécutée en boucle, c'est-à-dire qu'elle est répétée indéfiniment. C'est là que se trouve le code principal du programme.

Voici un exemple de programme Arduino simple qui fait clignoter une LED toutes les secondes :

```cpp
const int LED_PIN = 13; // Pin de la LED

void setup() {
  // Définition de la pin de la LED en sortie
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // Allumage de la LED
  digitalWrite(LED_PIN, HIGH);
  // Attente de 500 millisecondes
  delay(500);
  // Extinction de la LED
  digitalWrite(LED_PIN, LOW);
  // Attente de 500 millisecondes
  delay(500);
}
```

# La fonction `setup`
La fonction `setup` est exécutée une seule fois au démarrage du programme Arduino, avant la boucle infinie de la fonction `loop`.

Elle est généralement utilisée pour mettre en place l'environnement de travail du programme, c'est-à-dire pour configurer les paramètres et les dispositifs nécessaires au bon fonctionnement du programme.

Voici quelques exemples d'utilisations possibles de la fonction `setup` :
- Définition des modes d'entrée/sortie des pins du microcontrôleur Arduino : en utilisant la fonction `pinMode`, on peut indiquer si une pin doit être utilisée en entrée (par exemple pour lire une valeur provenant d'un bouton ou autre capteur) ou en sortie (par exemple pour envoyer une tension à une LED).
- Initialisation de paramètres et de variables : la fonction `setup` est souvent utilisée pour initialiser des variables qui seront utilisées tout au long du programme, comme des compteurs ou des variables de configuration.
- Configuration de périphériques externes : si le programme utilise des périphériques tels que des écrans LCD, des modules WiFi ou des capteurs, la fonction `setup` peut être utilisée pour configurer ces périphériques et les mettre en place pour l'utilisation ultérieure.

Voici un exemple de programme Arduino qui utilise la fonction setup pour définir le mode de la pin 13 en sortie et initialiser une variable de comptage à 0 :

```cpp
int compteur = 0; // Variable de comptage

void setup() {
  // Définition de la pin 13 en sortie
  pinMode(13, OUTPUT);
  // Initialisation de la variable de comptage à 0
  compteur = 0;
}

void loop() {
  // Incrémentation du compteur
  compteur++;
  // Allumage de la LED sur la pin 13
  digitalWrite(13, HIGH);
  // Attente de 500 millisecondes
  delay(500);
  // Extinction de la LED sur la pin 13
  digitalWrite(13, LOW);
  // Attente de 500 millisecondes
  delay(500);
}

```

> **Question** : De quelle façon, nous pourrions améliorer ce programme pour qu'il soit plus facile à maintenir?
> <details><summary>Indice</summary>
> Si l'on doit modifier la broche de la LED ou de la durée de l'attente que devrons-nous faire? 
> </details>

---

# La fonction `loop`
La fonction `loop` est exécutée en boucle, c'est-à-dire qu'elle est répétée indéfiniment. C'est là que se trouve le code principal du programme.

Cette boucle est très pratique dans les programmes Arduino car elle permet de mettre en place des actions qui sont répétées de manière périodique, comme la lecture de données sensorielles, l'affichage de données sur un écran ou encore la commande de dispositifs tels que des moteurs ou des LED.

> **Perle de culture**
>  
> Les microcontrôleurs doivent tous avoir une fonction similaire à `loop` pour fonctionner. Si vous ne mettez pas de fonction `loop` dans votre programme, le microcontrôleur ne fera rien.
> 
> Ainsi, on pourrait retrouver quelques choses comme ça dans le code d'un microcontrôleur :
> ```cpp
> void main() {
>   // ...
>   // Code de configuration
>   // ...
>   // ...
>   // Boucle principale
>   while (true) {
>     // ...
>     // Code principal répété    
>     // ...
>   }    
> }
> ```

# Cycle de vie d'un programme Arduino

![alt text](assets/lifecycle.drawio.svg)

## 📌 Explications du diagramme :
1. **Démarrage** :
   - L'Arduino est alimenté et initialise son matériel.
   - Il charge ensuite le programme stocké en mémoire.

2. **setup()** (exécuté une seule fois) :
   - Configuration des broches (`pinMode()`, `Serial.begin()`, etc.).
   - Initialisation des variables, capteurs, moteurs, etc.

3. **loop()** (exécuté en continu) :
   - Contient le **programme principal** qui tourne en boucle infinie tant que l'Arduino est sous tension.
   - Permet de **réagir aux événements**, de **lire des capteurs**, de **contrôler des actionneurs**, etc.

---

# Les principaux types de données
Le langage Arduino, basé sur le C++, offre plusieurs types de données adaptés aux contraintes des microcontrôleurs. Voici un tableau des principaux types disponibles :

| Type             | Description                               | Limite Inférieure       | Limite Supérieure         |
|-----------------|------------------------------------------|------------------------|--------------------------|
| `int`           | Entier signé 16 bits (sur Arduino Uno)   | -32,768               | 32,767                   |
| `unsigned int`  | Entier non signé 16 bits                | 0                      | 65,535                   |
| `long`          | Entier signé 32 bits                     | -2,147,483,648         | 2,147,483,647            |
| `unsigned long` | Entier non signé 32 bits                 | 0                      | 4,294,967,295            |
| `float`         | Nombre à virgule flottante (32 bits)     | ≈ -3.4 × 10³⁸         | ≈ 3.4 × 10³⁸             |
| `double`        | Identique à `float` sur Arduino AVR      | (32 bits)              | (Idem `float`)           |
| `char`          | Caractère unique (8 bits)                | -128                   | 127                      |
| `bool`          | Valeur booléenne (`true` ou `false`)     | `false` (0)            | `true` (1)               |

> ⚠ **Attention** : Sur les cartes basées sur des microcontrôleurs AVR (comme l’**Arduino Mega**), `double` est identique à `float` (32 bits). Sur d’autres plateformes (ESP32, ARM), `double` peut être en **64 bits**.

## 🛠 Déclaration et utilisation

Voici un exemple de déclaration de variables utilisant ces types :

```cpp
int entier = 10;
unsigned int entierNonSigne = 65535;
long entierLong = -2147483648;
unsigned long entierLongNonSigne = 4294967295;
float flottant = 3.14;
double flottantDouble = 3.141592653589793;
char caractere = 'A';
bool etat = true;
```


## 🏗 Comparaison des types et exemples d'utilisation

| Type            | Taille (octets) | Exemples d'utilisation                                      |
|----------------|---------------|--------------------------------------------------------------|
| `int`          | 2              | Compteur, indicateur d'état numérique                        |
| `unsigned int` | 2              | Index, compteur sans valeur négative                        |
| `long`         | 4              | Stocker des temps longs (`millis()`, `micros()`)            |
| `unsigned long`| 4              | Horodatage, gestion de délais (`millis()`, `micros()`)      |
| `float`        | 4              | Stockage de mesures précises (température, tension, etc.)   |
| `double`       | 4 (ou 8)        | Calculs scientifiques sur certaines cartes                  |
| `char`         | 1              | Stockage de caractères (`'A'`, `'Z'`, `'\n'`)               |
| `bool`         | 1              | Gestion d’états (`true` ou `false`)                         |

Étant programmé pour un appareil très limité en ressource, il est important de choisir le type de données le plus adapté pour stocker vos données, afin de maximiser l'efficacité et la précision de votre programme. Par exemple, il n'est pas recommandé d'utiliser un type `float` pour stocker des nombres entiers, car cela peut entraîner une perte de précision. De même, il est préférable d'utiliser un type `long` ou `unsigned long` pour stocker des nombres très grands, plutôt que de dépasser la limite supérieure du type `int`.

## ⚠ Précision et limitations du type `float`

Le type `float` est utile pour les calculs à virgule flottante, mais il a **une précision limitée** (7 chiffres significatifs). Il utilise une **représentation binaire**, ce qui peut entraîner des erreurs d'arrondi.

## 🔥 Problèmes de conversion `float → int`

```cpp
float d = 123456.789;
int e = (int) d;  // e = 123456 (tronqué, pas arrondi)
```

Il est donc important de prendre en compte ces limitations lors de l'utilisation du type `float` dans vos programmes Arduino.

---

# 📌 Les variables en Arduino
Une **variable** est un espace mémoire utilisé pour stocker une valeur. En programmation Arduino, les variables permettent de **manipuler des données dynamiquement** et sont essentielles à l'exécution des programmes.

---

## 📍 La portée des variables
La **portée** d’une variable définit où elle est accessible dans le programme. On distingue trois types principaux :

### 1️⃣ Variables globales
✅ **Définition** :  
- Déclarées **en dehors de toutes les fonctions**.
- Accessibles **partout** dans le programme.
- Conservent leur valeur pendant toute l’exécution du programme.

📌 **Exemple :**
```cpp
int compteur = 0;  // Variable globale

void setup() {
  Serial.begin(9600);
  compteur++;  // Incrémente la variable globale
}

void loop() {
  compteur++;  // Continue d'incrémenter à chaque cycle de loop()
  Serial.println(compteur);  
  delay(1000);
}
```
🔹 **Usage typique** : Partager des données entre plusieurs fonctions.  
⚠ **Attention** : Un usage excessif peut rendre le programme **difficile à déboguer**.

---

### 2️⃣ Variables locales
✅ **Définition** :  
- Déclarées **à l’intérieur d’une fonction**.
- **Inaccessibles en dehors** de cette fonction.
- **Réinitialisées à chaque appel** de la fonction.

📌 **Exemple :**
```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  int variableLocale = 0;  // Déclarée ici → sera recréée à chaque exécution de loop()
  variableLocale++;
  Serial.println(variableLocale);  // Affiche toujours "1"
  delay(1000);
}
```
🔹 **Usage typique** : Stocker des valeurs temporaires propres à une fonction.

---

### 3️⃣ Variables statiques
✅ **Définition** :  
- Déclarées **dans une fonction avec `static`**.
- **Conservent leur valeur** entre les appels de la fonction.
- **Accessibles uniquement dans la fonction où elles sont déclarées**.

📌 **Exemple :**
```cpp
void compteurStatique() {
  static int compteur = 0;  // La valeur est conservée entre chaque appel
  compteur++;
  Serial.println(compteur);
}

void loop() {
  compteurStatique();
  delay(1000);
}
```
🔹 **Usage typique** : Mémoriser un état sans utiliser une variable globale.

---

## 🔄 Illustration de la portée des variables
Le programme ci-dessous met en évidence **l’évolution des variables locales, globales et statiques**.

📌 **Exemple détaillé :**
```cpp
int variableGlobale = 0;  // Variable globale

void setup() {
  Serial.begin(9600);
}

void fonctionAvecStatique() {
  static int compteurStatique = 0;
  int compteurLocal = 0;

  compteurStatique++;  // Conserve la valeur entre les appels
  compteurLocal++;  // Se réinitialise à chaque appel

  Serial.print("Statique : ");
  Serial.print(compteurStatique);
  Serial.print("\tLocal : ");
  Serial.println(compteurLocal);
}

void loop() {
  variableGlobale++;  // Incrémente à chaque cycle

  Serial.print("Globale : ");
  Serial.println(variableGlobale);

  fonctionAvecStatique();

  delay(1000);
}
```

📝 **Explication des résultats attendus :**
| Type de variable  | Évolution |
|-------------------|-----------|
| `variableGlobale`  | Incrémente à chaque cycle de `loop()` |
| `compteurStatique` | Incrémente à chaque appel de `fonctionAvecStatique()` |
| `compteurLocal`    | Reste à `1` à chaque appel (réinitialisé) |

---

## 🔘 Application pratique des variables statiques
Un exemple concret : **compter le nombre de pressions sur un bouton sans utiliser de variable globale**.

📌 **Exemple avec bouton :**
```cpp
const int boutonPin = 2;  // Broche du bouton

void setup() {
  pinMode(boutonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(boutonPin) == LOW) {  // Si le bouton est pressé
    boutonClic();  
    delay(200);  // Anti-rebond simple
  }
}

void boutonClic() {
  static int compteur = 0;  // Garde la valeur entre les appels
  compteur++;
  Serial.print("Nombre de clics : ");
  Serial.println(compteur);
}
```

---

## ✅ Bonnes pratiques
✔ **Privilégier les variables locales** pour éviter les conflits et améliorer la clarté du code.  
✔ **Utiliser `static`** quand une valeur doit être conservée entre appels sans être globale.  
✔ **Limiter les variables globales** aux cas où elles sont vraiment nécessaires (ex. : timers, état général).  

---

# Wokwi - Simulateur Arduino
Il existe plusieurs sites qui permettent de simuler une partie des fonctionnalités de l'Arduino. Toutefois, je préconise Wokwi. Il est gratuit, il est en ligne, il est simple d'utilisation et il est très complet.

Plusieurs de mes captures d'écran proviendront de [Wokwi](https://wokwi.com/).

Simuler un projet sur un simulateur avant d'effectuer les branchements physiques permet de s'assurer que notre code fonctionne.

## Créer un projet
Pour créer un projet, il suffit d'aller dans le bas de la page dans la section "Start from scratch" et de cliquer sur la carte Arduino que l'on souhaite utiliser. Dans notre cas, il s'agira du Arduino Mega.

<!-- <video src="wokwi_new_project.mp4" width=640></video> -->

https://user-images.githubusercontent.com/2332679/210601281-1ecd0f4e-a510-4571-8242-067902a302e1.mp4

---

## Exercice - Premier projet
1. Si ce n'est déjà fait, créez un compte GitHub.
2. Connectez-vous à [Wokwi](https://wokwi.com/) avec votre compte GitHub.
3. À partir du logiciel Arduino IDE, ouvrir le projet exemple "Blink".
4. Créez un nouveau projet nommé `c01_ex01` et choisissez le type `Arduino Mega`.
5. Collez le projet "Blink" dans le nouveau projet Wokwi.
6. Exécutez le projet.
7. Modifiez les valeurs de *timing* pour d'autres valeurs et exécutez le projet.

---

# Exercices
## Recherches
Dans le but de vous habituer à faire des recherches sur Google, j'ai expressément mis des questions où l'information n'est pas directement dans ce document.

1. Dans certains exemples de code, on retrouve des noms de variable tout en majuscule. Pour quelle raison?
2. Dans nos cas d'utilisation, quelles sont les valeurs des variables `HIGH`, `LOW` et `LED_BUILTIN`?
3. Que fait la fonction `delay()`?
4. Que fait la fonction `pinMode()`?
5. Combien de mémoire RAM possède le Arduino Mega?

## Questions
1. Quelle est la différence entre une variable locale et une variable globale?
2. Quel type de variable est-il préférable d'utiliser pour stocker le temps en milliseconde?
3. Si je veux partager une variable entre les fonctions, quelle sera la portée de la variable que devrais-je prendre?
4. Si je veux conserver la valeur d'une variable à l'intérieur d'une même fonction, quelle sera la portée de la variable que devrais-je prendre?
5. À l'intérieur d'une fonction, si la valeur d'une variable doit être réinitialiser à chaque fois et elle n'est pas utile à l'extérieur de la dite fonction, quelle sera la portée de la variable?
6. Quelle est la différence entre une variable statique et une variable globale?
7. Quelle est la différence entre une variable locale et une variable statique?
8. Nommez une utilité pour une variable locale.
9.  Nommez une utilité pour une variable statique.
10. Nommez une utilité pour une variable globale.

<details><summary>Réponses</summary>

1. Une variable locale est déclarée à l'intérieur d'une fonction et n'est pas accessible à l'extérieur de la fonction. Une variable globale est déclarée à l'extérieur de toute fonction et est accessible à l'extérieur de toutes les fonctions.
2. `unsigned long`
3. Variable globale
4. Variable statique
5. Variable locale
6. Une variable statique conserve sa valeur entre les exécutions d'une fonction et n'est pas accessible aux autres fonctions. Une variable globale est accessible à l'extérieur de toutes les fonctions.
7. Une variable locale est déclarée à l'intérieur d'une fonction, n'est pas accessible à l'extérieur de la fonction et elle est réinitialisée à chaque exécution de la fonction. Une variable statique est déclarée à l'intérieur d'une fonction et conserve sa valeur entre les exécutions de la fonction.
8. Exemple : Avoir une variable qui sert à incrémenter un compteur.
9. Exemple : Conserver la valeur du temps entre les exécutions d'une fonction. Conserver l'état d'une LED entre les exécutions d'une fonction.
10. Exemple : Conserver l'heure globale du système. Conserver l'état d'un composant pour l'ensemble du système.
</details>

## Programmation
1. Modifiez le programme "Blink" pour faire clignoter la LED 5 fois par seconde.
2. Modifiez le programme "Fade" pour faire réagir la LED qui est intégrée sur le Arduino.
3. Modifiez le programme "Fade" pour faire graduer la LED plus rapidement.

### Défi
- Créez un programme qui fait clignoter la LED 2 fois dans une seconde. Ensuite, faire un graduation 100% vers 0% sur 1 seconde. Et recommencer.

https://user-images.githubusercontent.com/2332679/210662345-958f0043-521b-4025-aea2-3f0cf3fe7d0e.mp4


