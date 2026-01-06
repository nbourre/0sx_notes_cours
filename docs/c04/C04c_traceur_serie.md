# Le traceur série

## Objectifs
- Savoir comment utiliser le traceur des courbes avec Arduino (Oscilloscope)
- Savoir afficher une ou plusieurs courbes avec Arduino
- Savoir calculer la valeur moyenne d’un signal

## Introduction
Dans ce cours, nous allons voir comment utiliser le traceur des courbes avec Arduino. Le traceur des courbes est un outil très utile pour visualiser les signaux analogiques.

![Alt text](assets/c04_plotter.gif)

## Démarrer le traceur
Pour démarrer le traceur série, il faut aller dans le menu `Outils` et sélectionner `Traceur série`.

![Alt text](assets/c04_plotter_menu.png)

## Utiliser le traceur
Pour utiliser le traceur, il faut d'abord envoyer des données dans le port série. Le format des données est le suivant :

`nomValeur:Valeur[,nomValeur2:Valeur2[,...]]`

Par exemple, si on veut envoyer la valeur 10 pour la courbe `Courbe1` et la valeur 20 pour la courbe `Courbe2`, on envoie la chaîne de caractères suivante :

`Courbe1:10,Courbe2:20`

Il faut terminer la chaîne de caractères par un retour à la ligne (`\n`) soit en utilisant la fonction `Serial.println()`;

### Exemple
Dans cet exemple, nous allons afficher la valeur de la tension mesurée par une photorésistance sur le port A0.

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  int val = analogRead(A0);
  Serial.print("Lumiere:");
  Serial.println(val);
  delay(100);
}

```

Branchement de la photorésistance sur l'Arduino Mega
![Alt text](assets/photoresistance.png)

---

## Calcul de la valeur moyenne d'un signal
Pour calculer la valeur moyenne d'un signal, il faut faire la moyenne des valeurs lues sur un certain nombre de points. Par exemple, si on veut calculer la valeur moyenne de la tension mesurée par une photorésistance, on peut lire la valeur de la tension 10 fois et faire la moyenne des 10 valeurs lues.

```cpp
unsigned long currentTime = 0;

// String est une classe qui permet de manipuler des chaînes de caractères
String msg = "";

void setup() {
  Serial.begin(9600);
}

void loop() {
    currentTime = millis();
    int val = sensorTask();
    msg += "Lumiere:" + String(val);
    serialPrintTask();
}

// Tâche de lecture de la valeur de la photorésistance
int sensorTask() {
    static unsigned long lastTime = 0;
    static unsigned int valSum = 0;
    static int val = 0;
    static int sampleCount = 0;

    // Taux de rafraîchissement de la lecture de la valeur de la photorésistance
    int rate = 100;
    int nbSamples = 16;

    if (currentTime - lastTime > rate) {
        lastTime = currentTime;

        // Somme des valeurs lues
        valSum += analogRead(A0);

        if (++sampleCount >= nbSamples) {
             // Décalage de 4 bits vers la droite équivaut à la division par 16
             // C'est plus rapide que la division
            val = valSum >> 4;

            // Remise à zéro des variables
            valSum = 0;
            sampleCount = 0;
        }
    }

    return val;
}

// Tâche d'envoi des données dans le traceur série
void serialPrintTask() {
    static unsigned long serialPrintPrevious = 0;
    int serialPrintInterval = 100;

    // Si ce n'est pas le moment, on sort de la fonction immédiatement
    if (currentTime - serialPrintPrevious < serialPrintInterval) return;

    serialPrintPrevious = currentTime;

    if (msg != "") {
        Serial.println(msg);
        msg = "";
    }
}

```
---

## Exercice
- Ajouter une photoresistance sur votre platine et tester le code ci-dessus en visualisant les données dans le traceur série.
- Si ce n'est déjà fait, ajouter un potentiomètre sur votre platine et tester le code ci-dessus en visualisant les données de la photoresistance et du potentiomètre dans le traceur série.
- Modifier le code pour avoir une courbe de valeur moyenne de la valeur mesurée par la photoresistance.

---

## Références
- https://arduinogetstarted.com/tutorials/arduino-light-sensor

