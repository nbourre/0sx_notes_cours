## Questions de révision pour les cours 01 à 06

---

### Cours 01 : Introduction, Programmation de base

1. Quelle est la différence entre un microcontrôleur et un microprocesseur?  
2. Quelle fonction est exécutée une seule fois au démarrage d’un programme Arduino?  
3. À quoi sert la fonction `loop()`?  
4. Donnez un exemple de type de variable adapté pour une minuterie en millisecondes.  
5. Quelle est la différence entre une variable statique et une variable globale?

<details>
<summary>Réponses</summary>

1. **Différence microcontrôleur vs microprocesseur** :  
   - Microcontrôleur : intègre mémoire, processeur et E/S sur une seule puce, pour tâches spécifiques.  
   - Microprocesseur : plus puissant, utilisé dans les ordinateurs, nécessite mémoire et E/S externes.
2. **Fonction exécutée une seule fois** : `setup()`
3. **Fonction exécutée en boucle infinie** : `loop()` — exécute le code en continu après `setup()`.
4. **Type pour minuterie** : `unsigned long` (pour éviter le débordement négatif).
5. **Différence variable statique vs globale** :  
   - Statique : garde sa valeur entre les appels dans la même fonction, visibilité locale.  
   - Globale : accessible dans tout le programme, initialisée une seule fois.

</details>

---

### Cours 02 : Fonctions, Communication série

1. Quelle fonction permet de définir le mode d'une broche (entrée ou sortie)?  
2. Quelle est la différence entre `Serial.print()` et `Serial.println()`?  
3. Quelle fonction permet d’écrire un signal numérique sur une broche?  
4. Pourquoi est-il déconseillé d’utiliser `delay()` dans un programme Arduino complexe?  
5. Que fait la fonction `millis()`?

<details>
<summary>Réponses</summary>

1. `pinMode()`
2. `print()` écrit sans saut de ligne, `println()` ajoute un retour à la ligne.
3. `digitalWrite(pin, HIGH/LOW)`
4. `delay()` bloque le programme — aucune autre tâche ne peut s'exécuter pendant ce temps.
5. `millis()` retourne le nombre de millisecondes écoulées depuis le démarrage du programme.

</details>

---

### Cours 03 : Branchement, Anti-rebond, sans délai

1. À quoi sert une résistance de rappel (pull-down) ou de tirage (pull-up)?  
2. Quelle broche est utilisée par défaut pour la LED intégrée sur l’Arduino?  
3. Pourquoi faut-il éviter d’utiliser `delay()` pour temporiser dans une machine à états?  
4. Quelle est l’utilité d’un anti-rebond logiciel?  
5. Expliquez en quelques mots le fonctionnement du code de détection d'anti-rebond avec `millis()`.

<details>
<summary>Réponses</summary>

1. Elle garantit un état logique connu lorsque l'entrée n'est pas activée. Par exemple, une résistance de tirage (pull-up) maintient la broche à HIGH lorsqu'elle n'est pas connectée à la masse (GND).
2. `LED_BUILTIN`, souvent broche 13.
3. Parce que `delay()` bloque l'exécution du programme, ce qui empêche les transitions rapides.
4. Pour éviter plusieurs lectures fausses d’un bouton lors d’un seul appui.
5. On compare `millis()` avec un moment précédent pour exécuter une tâche après un certain délai, sans bloquer le code.

</details>

---

### Cours 04 : Lecture et écriture analogique

1. Quelle est la plage de valeurs retournée par la fonction `analogRead()`?
2. À quoi sert la fonction `map()`?  
3. Quelle différence y a-t-il entre `analogRead()` et `analogWrite()`?  
4. Comment simule-t-on une tension analogique avec une sortie numérique?  
5. Donnez un exemple de composant qui pourrait utiliser `analogWrite()`.

<details>
<summary>Réponses</summary>

1. De 0 à 1023.
2. `map()` convertit une valeur d'une plage donnée vers une autre.
3. `analogRead()` lit une valeur analogique (entrée), `analogWrite()` écrit une valeur PWM (sortie).
4. Par PWM : modulation de largeur d’impulsion.
5. Une LED (pour varier l’intensité), un moteur, etc.

</details>

---

### Cours 05 : Composants analogiques, Tâches

1. Qu’est-ce qu’un diviseur de tension? Donnez un exemple concret.  
2. Quelle est la principale différence entre un programme utilisant `delay()` et un utilisant `millis()`?  
3. Pourquoi est-il avantageux de structurer son programme en tâches?  
4. Quelle portée de variable permet de conserver sa valeur entre les appels à une fonction?

<details>
<summary>Réponses</summary>

1. Un circuit qui réduit une tension d’entrée. Exemple : potentiomètre ou 2 résistances en série avec un point de mesure entre elles.
2. `delay()` bloque tout, `millis()` permet de continuer à exécuter d’autres tâches.
3. On évite les blocages, le programme devient plus clair, réactif et modulaire.
4. `static`

</details>

---

### Cours 06 : Librairies, Capteurs, LCD

1. Donnez un avantage à utiliser une librairie Arduino.  
2. Quelle librairie a-t-on utilisée pour l'écran LCD I2C?
3. Dans le cadre du cours, quelle librairie est utilisée pour lire un capteur DHT11?
4. Quelle fonction permet d’afficher du texte sur un écran LCD?  
5. Quelle est la fonction utilisée pour défiler le texte sur un écran LCD?

<details>
<summary>Réponses</summary>

1. Gain de temps, abstraction de la complexité, réutilisation facile.
2. `LiquidCrystal_I2C` ou `LCD_I2C` selon la version.
3. `DHT.h`
4. `lcd.print("texte")`
5. `lcd.scrollDisplayLeft()` ou `lcd.scrollDisplayRight()`

</details>
