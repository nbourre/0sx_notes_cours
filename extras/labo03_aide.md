# Laboratoire 03 : Aide

Dans le laboratoire 03, votre système doit effectuer différentes tâches. 

# Retour sur l'énoncé
Regardons l'énoncé du laboratoire 03.

- Démarrage : Les DEL s’allument un à la suite de l’autre pendant 250 ms chaque et ensuite s’éteignent;
  - Si ton dernier chiffre est pair, les DEL s’allument dans le sens horaire et vice versa.
- L’intensité des DEL de gauche et droite varient selon l’axe des X;
- L’intensité des DEL de haut et bas varient selon l’axe des Y;
- 1 clic : Tout le monde s’allume graduellement sur 500 ms;
- 1 clic : Tout le monde s’éteint graduellement sur 500 ms.
- À toutes les 100 ms, le programme devra envoyer sur le port série les valeurs de X, Y, l’état du bouton et le niveau de luminosité dans un format compatible avec le traceur série.
  - Les valeurs de X et Y devront être en -50.0 et 50.0 soit en float;
  - La valeur du bouton peut être 0 ou 50;
  - La valeur du niveau de luminosité doit être entre 0 et 100.
    - 0 étant noir et 100 plein éclairage

# Identification des tâches
Regardons les différentes tâches que nous devons effectuer.
- Gestion du démarrage : Tâches de démarrage du système.
- Gestion des axes : Tâches de gestion des intensités des DEL selon les axes X et Y.
- Gestion du clic : Tâches de gestion du clic sur le bouton.
- Sortie vers le traceur série
- Valeur de la luminosité

Implicement, on observe que certaines tâches ont priorité sur d'autres. En effet, tout semble indiquer que le clic a priorité la gestion des intensités.
Vous devez donc gérer les priorités des tâches. Pour ce faire, vous pouvez utiliser des drapeaux (ou sémaphores) pour indiquer si une tâche est en cours d'exécution ou non.

# Gestion du démarrage
Le démarrage est une tâche qui doit être effectuée au démarrage du système et on n'y revient jamais. On peut donc mettre cette tâche dans le démarrage.

```pseudocode
démarrage
{
    executer la tâche de démarrage;
}

```

# Gestion du clic
Le clic est une tâche qui doit être effectuée à chaque fois qu'on appuie sur le bouton. À la lecture de l'énoncé, on constate que ce code doit être exécuté peu importe l'état du système. On peut donc mettre cette tâche dans la boucle principale.

On se souvent que l'on a vu en classe que l'on peut lire le moment où le bouton est relâché.

```pseudocode
boucle principale
{
    lire le bouton;
    Est-ce que le bouton est relâché?
    {
        lever le drapeau du clic;
    }
}

```

Ce que le systeme doit faire lorsque le clic est détecté dépendra de chacune des tâches. Par exemple, si le système est en mode normal, le clic doit faire passer le système en mode "pause". On doit réappuyer sur le bouton pour revenir au mode normal.

On fera donc un mode pause. Lorsqu'il entre dans le mode pause, on allume graduellement les DEL. Lorsqu'il sort du mode pause, on éteint graduellement les DEL et ensuite il devient en mode normal.

```pseudocode
boucle principale
{
    lire le bouton;
    Est-ce que le bouton est relâché?
    {
        //lever le drapeau du clic;
        drapeauClic = 1;
    }
    Est-ce que le système est en mode normal?
    {
        Est-ce que le drapeau du clic est levé?
        {
            passer le système en mode allumage graduel;
            baisser le drapeau du clic;
        } sinon {
            executer la tâche de gestion des axes;
        }
    } Sinon est-ce que le systeme est en mode allumage graduel? {
        Est-ce qu'on a atteint le niveau de luminosité 100?
        {
            passer le système en mode pause;
        }
    } Est-ce que le système est en mode pause? {
        Est-ce que le drapeau du clic est levé?
        {
            passer le système en mode éteint des DEL;
            baisser le drapeau du clic;            
        }
    } Sinon est-ce que le système est en mode éteint des DEL?
    {
        Est-ce qu'on a atteint le niveau de luminosité 0?
        {
            passer le système en mode normal;
        }
    }

    luminositeTache();
}

```


# Gestion des axes - mode normal
La gestion des axes se fait lorsque le système est en mode normal.

```pseudocode
gestionDesAxes{
    Lire les axes
    Faire la conversion des valeurs
    Allumer les DEL selon les valeurs

    Est-ce que 100 ms se sont écoulées?
    {
        Envoyer les valeurs sur le port série
    }
}

```

# Luminositée
À toutes les 100 ms, le niveau de luminosité doit être envoyé peu importe le mode du système. On peut donc appeler cette tâche dans la boucle principale.

Le pseudocode de celle-ci est le suivant.

```pseudocode
luminositeTache{
    Est-ce que 100 ms se sont écoulées?
    {
        lire la luminosité;
        convertir la valeur;
        Envoyer la valeur sur le port série
    }
}

```

# État du bouton
À toutes les 100 ms, l'état du bouton doit être envoyé peu importe le mode du système. On peut donc appeler cette tâche dans la boucle principale.

```pseudocode
boutonTache{
    Est-ce que 100 ms se sont écoulées?
    {
        lire l'état du drapeau du clic;
        convertir la valeur;
        Envoyer la valeur sur le port série
    }
}

```

Cependant, il faudra l'afficher avant la gestion de celui-ci, car les différentes tâches peuvent modifier la valeur du drapeau du clic.