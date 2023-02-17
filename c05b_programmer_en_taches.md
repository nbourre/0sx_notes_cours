# Programmer en tâches <!-- omit in toc -->


# Introduction
La programmation multitâches est une technique qui permet d'exécuter plusieurs tâches en même temps. C'est relativement simple sur un PC, car ils ont plusieurs processeurs. Sur un Arduino, il n'y a qu'un seul processeur. Donc, il n'y a pas vraiment de programmation multitâches. Cependant, il est possible de simuler l'effet multitâche en exécutant des parties de tâche en séquence très rapide.

La programmation multitâches est utilisée dans les systèmes embarqués pour exécuter plusieurs tâches en même temps. Par exemple, un système embarqué peut exécuter une tâche pour lire les données d'un capteur, une autre tâche pour traiter les données, et une autre tâche pour afficher les données sur un écran.

# Exemple disfonctionnel
Disons que je désire faire clignoter 2 DEL à des fréquences différentes. Disons que la DEL 1 doit clignoter à 1 Hz et que la DEL 2 doit clignoter à 2 Hz. Voici un exemple de code qui pourrait faire ça:

```cpp
int led1 = 13;
int led2 = 12;

int rate1 = 500;
int rate2 = 250;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  digitalWrite(led1, HIGH);
  delay(rate1);
  digitalWrite(led1, LOW);
  delay(rate1);
  digitalWrite(led2, HIGH);
  delay(rate2);
  digitalWrite(led2, LOW);
  delay(rate2);
}
```

Le problème avec ce code est qu'il ne peut pas faire les deux DEL en même temps. La DEL 1 clignote à 1 Hz, mais la DEL 2 ne clignote pas du tout. Pourquoi? Parce que le code est exécuté en séquence. Le code exécute la première ligne, puis la deuxième, puis la troisième, etc. Il ne peut pas faire les deux DEL en même temps. De plus, le code est bloquant. Il ne peut pas faire autre chose pendant qu'il exécute les lignes 1 à 4.

On pourrait modifier le code en calculant le délai à utiliser pour chaque DEL. Par exemple, on pourrait utiliser une variable pour stocker le délai à utiliser pour la DEL 1 et une autre variable pour stocker le délai à utiliser pour la DEL 2. On pourrait ensuite utiliser ces variables pour déterminer le délai à utiliser pour chaque DEL. Voici un exemple de code qui pourrait faire ça:

```cpp
int led1 = 13;
int led2 = 12;

int rate1 = 500;
int rate2 = 250;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  digitalWrite(led1, HIGH);
  digitalWrite(led2, HIGH);
  delay(rate2);
  digitalWrite(led2, LOW);
  delay(rate2);
  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  delay(rate2);
  digitalWrite(led2, LOW);
  delay(rate2);
}

```

Ça fonctionne, mais c'est un peu compliqué. On est chanceux car 500ms est une multiplicateur de 250ms. De plus, le code est toujours bloquant.

Si je veux ajouter une DEL qui clignote à 3Hz. Ça va être une défi!!

# Améliorer l'exemple en utilisant millis()
On peut améliorer l'exemple en utilisant la fonction `millis()`. La fonction `millis()` retourne le nombre de millisecondes depuis que le programme a commencé à s'exécuter. On peut utiliser cette fonction pour déterminer quand allumer et éteindre les DEL. Voici un exemple de code qui pourrait faire ça:

```cpp
int led1 = 13;
int led2 = 12;

int rate1 = 500;
int rate2 = 250;

unsigned long previousMillis1 = 0;
unsigned long previousMillis2 = 0;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  // DEL 1
  if (currentMillis - previousMillis1 >= rate1) {
    previousMillis1 = currentMillis;
    digitalWrite(led1, !digitalRead(led1));
  }

  // DEL 2
  if (currentMillis - previousMillis2 >= rate2) {
    previousMillis2 = currentMillis;
    digitalWrite(led2, !digitalRead(led2));
  }
}
```

C'est déjà une nette amélioration, car maintenant le code n'est plus blocant et est plus clair.

En effet, on peut voir les blocs de code qui s'exécutent pour la DEL 1 et les blocs de code qui s'exécutent pour la DEL 2. On peut aussi voir que le code est plus court.

# Améliorer l'exemple en utilisant des fonctions
On peut encore améliorer l'exemple en utilisant des fonctions en tant que tâche.

Pour ce faire, **il faut identifier les tâches à exécuter**. Dans notre exemple, on a deux tâches:
- Clignoter la DEL 1
- Clignoter la DEL 2

Ainsi on peut créer **une fonction pour chaque tâche**.

Comme vue dans les cours précédents, **on peut utiliser des variables statiques pour stocker les données d'une tâche**. Par exemple, on peut utiliser une variable statique pour stocker la dernière exécution de la fonction pour la DEL 1 et une autre variable statique pour stocker la dernière exécution de la DEL 2.

Voici un exemple de code qui pourrait faire ça:

```cpp
int led1 = 13;
int led2 = 12;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  blinkLed1();
  blinkLed2();
}

void blinkLed1() {
  static unsigned long previousMillis = 0;
  unsigned long currentMillis = millis();
  unsigned int rate = 500;

  if (currentMillis - previousMillis >= rate) {
    previousMillis = currentMillis;
    digitalWrite(led1, !digitalRead(led1));
  }
}

void blinkLed2() {
  static unsigned long previousMillis = 0;
  unsigned long currentMillis = millis();
  unsigned rate = 250;

  if (currentMillis - previousMillis >= rate) {
    previousMillis = currentMillis;
    digitalWrite(led2, !digitalRead(led2));
  }
}
```

Voici un comparatif de l'exemple initiale et de l'exemple final:

<table>
    <tr  style="vertical-align:top">
        <th>Exemple initial</th>
        <th>Exemple final</th>
    </tr>
    <tr>
        <td>
        
```cpp
int led1 = 13;
int led2 = 12;

int rate1 = 500;
int rate2 = 250;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  digitalWrite(led1, HIGH);
  digitalWrite(led2, HIGH);
  delay(rate2);
  digitalWrite(led2, LOW);
  delay(rate2);
  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  delay(rate2);
  digitalWrite(led2, LOW);
  delay(rate2);
}

```

</td>
<td style="vertical-align:top">
        
```cpp
int led1 = 13;
int led2 = 12;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  blinkLed1();
  blinkLed2();
}

void blinkLed1() {
  static unsigned long previousMillis = 0;
  unsigned long currentMillis = millis();
  unsigned int rate = 500;

  if (currentMillis - previousMillis >= rate) {
    previousMillis = currentMillis;
    digitalWrite(led1, !digitalRead(led1));
  }
}

void blinkLed2() {
  static unsigned long previousMillis = 0;
  unsigned long currentMillis = millis();
  unsigned rate = 250;

  if (currentMillis - previousMillis >= rate) {
    previousMillis = currentMillis;
    digitalWrite(led2, !digitalRead(led2));
  }
}
```

Malgré un code plus long, il est beaucoup plus facile à comprendre et à modifier.

**Il est important de favoriser la lecture du code par les autres ainsi que la maintenance du code.** C'est pourquoi il est important de bien structurer le code.

TODO : Ajouter d'autres éléments tel que la lecture d'un capteur qui ne nécessite pas d'avoir un délai.