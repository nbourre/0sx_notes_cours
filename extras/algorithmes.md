# Algorithme pour trouver la valeur minimal

Voici un algorithme pour trouver la valeur minimal et maximal d'un capteur sur A0.
    
```cpp
// Déclaration des variables
int valeur = 0;
int valeurMax = 0; // Initialisation à 0 pour la valeur maximale
int valeurMin = 1023; // Initialisation à 1023 pour la valeur minimale

void setup() {
  Serial.begin(9600);
}

// Boucle infinie
void loop() {
  // Lecture de la valeur du capteur
  valeur = analogRead(A0);
  // Si la valeur est plus grande que la valeur maximale
  if (valeur > valeurMax) {
    // La valeur maximale devient la valeur
    valeurMax = valeur;
  }
  // Si la valeur est plus petite que la valeur minimale
  if (valeur < valeurMin) {
    // La valeur minimale devient la valeur
    valeurMin = valeur;
  }
  // Affichage des valeurs
  Serial.print("Valeur: ");
  Serial.print(valeur);
  Serial.print(" Valeur maximale: ");
  Serial.print(valeurMax);
  Serial.print(" Valeur minimale: ");
  Serial.println(valeurMin);
  // Attendre 100ms
  delay(100);
}
```

# Utiliser un tableau de caractères pour écrire sur le LCD
Voici un exemple de bout de code pour écrire sur le LCD avec un tableau de caractères.

```cpp
// Tampon pour écrire les strings
char lcdBuff[2][16] = {
  "                ",
  "                "
};

// Tampon pour écrire un float
char szFloat[6];
float valeur = 0.0;

void loop() {
  // …  
  // Convertir un float en char[]
  dtostrf(valeur, 4, 1, szFloat);

  // Écriture à la ligne 1
  // Utilisation de snprintf pour éviter un dépassement de buffer
  snprintf(lcdBuff[0], sizeof(lcdBuff[0]), "valeur=%s", szFloat);

  // Écriture à la ligne 2
  // now est une variable de type DateTime
  snprintf(lcdBuff[1], sizeof(lcdBuff[1]), "%02d:%02d:%02d",
           now.hour(), now.minute(), now.second());

  lcd.setCursor(0, 0);
  lcd.print(lcdBuff[0]);
  lcd.setCursor(0, 1);
  lcd.print(lcdBuff[1]);

  // Attendre 100ms
  delay(100);
  // Effacer le texte
  lcd.clear();
  // …
}
```

La fonction `snprintf` permet d'écrire dans un tableau de caractères.
- Elle prend 4 paramètres:
  - Le tableau de caractères à remplir
  - La taille du tableau
  - Le format de la string
  - Les valeurs à écrire. Optionnelles si le format ne contient pas de `%`.

La fonction `dtostrf` permet de convertir un float en char[].
- Elle prend 4 paramètres:
  - Le float à convertir
  - Le nombre de caractères à écrire
  - Le nombre de décimales
  - Le tableau de caractères à remplir

Le format de la string est le suivant:
- `%` indique que l'on va écrire une valeur
- Les valeurs peuvent être:
  - `d` pour un entier
  - `s` pour une string
- Pour les entiers, on peut ajouter un nombre pour indiquer le nombre de caractères à écrire. Dans l'exemple, on utilise `%02d` pour écrire un entier sur 2 caractères. Si le nombre est plus petit, on ajoute des zéros devant.

**Les `float` ne sont pas supportés** par la fonction `sprintf` avec Arduino. Il faut donc convertir le float en char[] avec la fonction `dtostrf` avant de l'écrire.