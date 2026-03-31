
## Nouvelle structure
Dans plusieurs situations, il est nécessaire de préparer un état avant de l'exécuter ou encore de faire des actions pour sortir d'un état. Par exemple, si nous avons un état qui doit allumer une DEL avant de s'exécuter, nous allons utiliser l'entrée pour allumer la DEL. De plus, si nous avons un état qui doit éteindre une DEL lorsque nous sortons de l'état, nous allons utiliser la sortie pour éteindre la DEL.

Ainsi, on se retrouve avec trois blocs de code pour chaque état:

- **L'entrée**: code qui est exécuté lorsque l'état est activé. Il est utilisé pour préparer l'état avant son exécution.
- **L'exécution**: code qui est exécuté tant que l'état est actif.
- **La sortie**: code qui est exécuté lorsque l'état est désactivé. Il est utilisé pour terminer l'état. Souvent, on réinitialise les variables utilisées dans l'état.

À notre niveau, une sortie est souvent initialisée par une **transition**. Une transition est un événement qui fait que l'on sort d'un état. Par exemple, un bouton qui est appuyé, un délai qui est écoulé, etc.

## Exemple de code

Voici un modèle d'état simple en utilisant une fonction.

```cpp

void xState(unsigned long cT) {
  static unsigned long lastTime = 0;
  const int rate = 500;

  static bool firstTime = true; // Drapeau pour l'entrée

  // Code d'ENTRÉE
  if (firstTime) {
    // Code d'initialisation de l'état
    // Reset tes trucs
    // Exemples : 
    //   Angle de référence, initialiser le lastTime,
    //   Chronomètre, etc.

    firstTime = false;
    return;
  }

  // Ligne nécessaire si l'on doit temporiser
  // les appels de cet état
  if (cT - lastTime < rate) return;

  lastTime = cT;

  // Code d'EXÉCUTION de l'état
  // Code de la job à faire

  // Code de TRANSITION
  // Il s'agit de la transition qui permet de sortir de l'état
  // Qu'est-ce qui fait que l'on sort de l'état?
  bool transition = false;

  // Il est possible d'avoir plusieurs transitions

  if (transition) {
    // Code de SORTIE
    // Code pour terminer l'état
   
    // Remettre le drapeau d'entrée à true pour la prochaine fois que l'on entre dans cet état
    firstTime = true;
    
    // appState = PROCHAIN_ETAT;   
  }
}

```
