# Améliorer son code <!-- omit in toc -->

- [Introduction](#introduction)
- [Général](#général)
  - [Favoriser la lisibilité du code](#favoriser-la-lisibilité-du-code)
- [Variables](#variables)
  - [Noms de variables](#noms-de-variables)
  - [Portée des variables](#portée-des-variables)
- [Fonctions](#fonctions)
- [États et tâches](#états-et-tâches)
- [Classe](#classe)
- [Autres astuces](#autres-astuces)
  - [Utilisez des modèles de fonctions](#utilisez-des-modèles-de-fonctions)
    - [Modèle d'une fonction d'état](#modèle-dune-fonction-détat)
    - [Modèle d'une fonction de tâche](#modèle-dune-fonction-de-tâche)


# Introduction
Dans ce document, je vous présente mes astuces pour améliorer votre code. Ces astuces sont basées sur mon expérience personnelle et sur des bonnes pratiques de programmation.

# Général
## Favoriser la lisibilité du code
- Si vous revenez sur votre code dans quelques mois, vous serez content de l'avoir écrit de manière lisible
- Vous ne savez pas si votre code est lisible? Demandez à un collègue de le lire
- Vous pouvez utiliser des commentaires pour expliquer le code

# Variables
## Noms de variables
- Utilisez des noms de variables explicites. Par exemple, préférez `temperatureBasse` à `tb`.

## Portée des variables
- Utilisez des variables locales plutôt que des variables globales
- Est-ce que la variable doit être partagée entre plusieurs fonctions?
  - Oui, utilisez une variable globale
  - Non, utilisez une variable locale
- Est-ce que la variable doit être sauvegardée entre deux appels de la fonction?
  - Oui, utilisez une variable statique
  - Non, utilisez une variable locale
- Est-ce qu'il s'agit d'une valeur qui ne doit pas être modifiée?
  - Oui, utilisez une constante

# Fonctions
- Est-ce que la fonction fait plus d'une chose?
  - Oui, séparez la fonction en plusieurs fonctions
  - Non, la fonction est correcte

# États et tâches
- Est-ce que votre programme a plusieurs états?
  - Créez un diagramme d'états pour modéliser le comportement de votre programme
  - Créez une machine à états (enumération, `switch`, etc.)
- Créez une fonction pour chaque état
  - Nommez la fonction de manière explicite par exemple avec le suffixe `State`
- Est-ce que c'est une action récurrente?
  - Oui, il s'agit d'une tâche. Créez une fonction pour cette tâche
- Créez une fonction pour chaque tâche
  - Nommez la fonction de manière explicite par exemple avec le suffixe `Task`

# Classe
- Utilisez des classes pour la création de systèmes complexes
  - Par exemple, un système de ventilation peut être modélisé par une classe `Ventilation` qui possède un moteur, un capteur de température, etc.
- Une classe ne doit pas faire plus d'une chose. Elle ne gère qu'un seul aspect du système

# Autres astuces
## Utilisez des modèles de fonctions
### Modèle d'une fonction d'état

```cpp
void modeleState()
{
    static unsigned long previousTime = currentTime;
    static unsigned long rate = 1000; // 1 seconde
    static bool firstTime = true;

    unsigned long currentTime = millis();

    if (firstTime)
    {
        firstTime = false;
        // Code à exécuter une seule fois au début
        // Initialisation des variables

    }

    if (currentTime - previousTime < rate)
    {
        return;
    }

    previousTime = currentTime;

    // Code à exécuter à chaque appel de la fonction
    // Mise à jour des variables

    bool transition = false; // Mettre à vrai si on change d'état

    if (transition)
    {
        // Code à exécuter une seule fois à la fin
        // Nettoyage des variables

        firstTime = true;
    }

    // Vous pouvez ajouter d'autres transitions ici
}
```

### Modèle d'une fonction de tâche

```cpp
void modeleTask()
{
    static unsigned long previousTime = 0;
    static unsigned long rate = 1000; // 1 seconde

    unsigned long currentTime = millis();

    if (currentTime - previousTime < rate)
    {
        return;
    }

    previousTime = currentTime;

    // Code à exécuter à chaque appel de la fonction
    // Mise à jour des variables
}
```

