# Les fonctions de base et la communication <!-- omit in toc -->
# Exercices <!-- omit in toc -->

## Plusieurs états
1. Programmez une DEL pour qu'elle clignote 2 fois dans une seconde et ensuite 5 fois dans une seconde.
   <details><summary>Astuces</summary>
   
   - Vous pouvez utiliser une variable pour simuler un "etat" pour la del.
   - Par exemple, si la variable est à 0, la DEL est clignote 2 fois, si la variable est à 1, la DEL clignote 5 fois. À chaque fin d'état, vous changez la valeur de la variable.

   </details>  
2. Modifiez le programme précédent qui envoit à l'ordinateur l'état du LED à chaque changement d'état.
  - Exemple de sortie : `LED allumée` ou `LED éteinte`

## Amélioration de code
Ci-bas il y a [l'exemple](C02_fonctions_comm.md#état-de-lapplication) que l'on retrouve dans le cours. Il permet de faire clignoter une DEL à 1 Hz et à 4 Hz.

```cpp
//définir la broche de la DEL
const int ledPin = 13;
//définir l'état de la DEL
bool ledState = LOW;

//définir l'état de l'application
int appState = 0; // 0 = 1 fois par seconde, 1 = 4 fois par seconde
int counter = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (appState == 0) {
    //inverser l'état de la DEL
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
    delay(500);
    counter++;
    if (counter == 2) {
      counter = 0;
      appState = 1;
    }
  } else if (appState == 1) {
    //inverser l'état de la DEL
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
    delay(125);
    counter++;
    if (counter == 8) {
      counter = 0;
      appState = 0;
    }
  }
}

```

1. Il y a beaucoup de code en double. Modifiez le code pour qu'il n'y ait moins de code en double.
2. Modifiez le code pour remplacer les `if` par un `switch-case`.
3. Affichez à l'ordinateur l'état de l'application à chaque changement d'état.
   - **Précision :** On ne veut pas afficher l'état de l'application à chaque fois que la DEL change d'état. On veut afficher l'état de l'application seulement quand l'état de l'application change.

## Défi
4. Modifiez le code en programmant une fonction pour chaque état de l'application et appelez la fonction correspondante à l'état de l'application.
   - Donc 2 fonctions par exemple `void un_hertz()` et `void quatre_hertz()`.

