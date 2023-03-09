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