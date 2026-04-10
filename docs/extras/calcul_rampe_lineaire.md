# Rampe linéaire précise avec millis()

Une rampe linéaire consiste à faire varier une valeur progressivement entre deux bornes sur une durée donnée.

Contrairement à une approche avec `delay()`, l'utilisation de `millis()` permet :

- une meilleure précision temporelle
- un code **non bloquant**
- une meilleure intégration dans des systèmes multitâches (ex: boucle principale Arduino)

## Principe

On définit :

- `minVal` : valeur de départ
- `maxVal` : valeur d'arrivée
- `duration` : durée totale en millisecondes

Plutôt que d'incrémenter à intervalle fixe, on calcule directement la valeur en fonction du **temps écoulé**.

## Représentation visuelle

```text
Valeur
        ^
maxVal  |                         *
        |                      *
        |                   *
        |                *
        |             *
        |          *
        |       *
        |    *
minVal  | *
        +------------------------------> Temps
        0                            duration
```

## Formule

On utilise une interpolation linéaire :

```text
valeur = minVal + (maxVal - minVal) * (temps_ecoule / duration)
```

* `temps_ecoule = millis() - startTime`
* le ratio `(temps_ecoule / duration)` varie de 0 à 1

## Exemple de code

```cpp
int minVal = 40;
int maxVal = 255;

unsigned long duration = 5000; // 5 secondes
unsigned long startTime;

void setup() {
  startTime = millis();
}

void loop() {
  unsigned long currentTime = millis();
  unsigned long elapsed = currentTime - startTime;

  if (elapsed <= duration) {
    float progress = (float)elapsed / duration;
    int value = minVal + (maxVal - minVal) * progress;

    // Utiliser la valeur ici
  } else {
    // Fin de la rampe
    int value = maxVal;

    // Optionnel : redémarrer
    // startTime = millis();
  }
}
```

## Avantages de cette approche

!!! success "Précision"

    La durée totale est beaucoup plus proche de la valeur désirée (ex: 5000 ms), car elle dépend directement du temps réel.

!!! success "Non bloquant"

    Contrairement à `delay()`, cette méthode permet à la boucle `loop()` de continuer à s'exécuter.


!!! success "Flexible"

    Facile d'ajouter :

    - pause
    - inversion de la rampe
    - déclenchement conditionnel
    - plusieurs rampes simultanées

## Points importants

!!! warning "Types de données"

    Toujours utiliser `unsigned long` pour `millis()` afin d'éviter les problèmes de dépassement.


!!! info "Précision flottante"

    L'utilisation de `float` permet une interpolation fluide. On peut aussi utiliser des entiers pour optimiser, mais au prix d'une légère perte de précision.

## Variante sans float (optionnelle)

Pour éviter les nombres flottants :

```cpp
int value = minVal + ((maxVal - minVal) * elapsed) / duration;
```

Cette version est souvent suffisante et plus performante sur microcontrôleur.

## Résumé

Avec `millis()`, on ne calcule plus un délai par pas. On calcule directement la valeur en fonction du temps :

```cpp
value = minVal + (maxVal - minVal) * (elapsed / duration);
```

Cela permet une rampe :

* plus précise
* non bloquante
* plus professionnelle dans un système embarqué

## Cas d'utilisation

* interpolation de paramètres dans le temps
* animation de valeurs
* contrôle progressif d'une consigne
* génération de profils temporels
* synchronisation basée sur le temps réel
