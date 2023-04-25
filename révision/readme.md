# Révision pour l'évaluation finale

---

# Volet pratique
- La programmation orientée objet
- Les tâches
  - Savoir comment créer et utiliser une tâche
- Les états avec des énumérations
- Les switch-case
- Le contrôle des broches
  - Lire des boutons
  - Allumer ou éteindre des DEL
- Le PWM
  - Allumer graduellement une DEL
- La programmation sans la fonction `delay()`
- Le moniteur série

## Exemples de question
Voici quelques exemples de questions qui pourraient être posées lors de l'évaluation finale. Ces questions ne sont pas nécessairement représentatives de ce qui sera demandé lors de l'évaluation finale. Elles sont là pour vous donner une idée du genre de question qui pourrait être posée. La meilleure façon de vous préparer est de faire les exercices de révision et de vous pratiquer à faire des programmes qui utilisent les concepts mentionnés ci-dessus.

Il n'y aura qu'une seule question pratique à l'évaluation finale.

- Faites un programme qui allume et éteint graduellement une DEL à l'aide du PWM. La DEL doit prendre 5 secondes pour s'allumer et 5 secondes pour s'éteindre. La DEL doit rester allumée pendant 5 secondes avant de s'éteindre. Affichez la valeur du PWM sur le moniteur série à toutes les 100 ms.
- Faites un programme qui fait clignoter une DEL à l'aide d'un bouton. Si l'utilisateur clique une fois sur le bouton, la DEL clignote 1 fois par seconde, s'il clique 2 fois, la DEL clignotera 2 fois ainsi de suite jusqu'à 5 fois. Après la 5e fois, la DEL s'éteint. À chaque clic, le nombre de clignotement s'affiche dans le moniteur série.
- Faites un programme qui accepte un chiffre de 0 à 9 entrée par le port série. Le chiffre indique le nombre de clignotement par seconde que doit faire une DEL. Si l'utilisateur entre 0, la DEL s'éteint. Si l'utilisateur entre 1, la DEL clignote 1 fois par seconde. Si l'utilisateur entre 2, la DEL clignote 2 fois par seconde ainsi de suite jusqu'à 9. Si l'utilisateur entre une valeur non valide, la DEL clignote 20 fois par seconde et le programme affiche un message d'erreur dans le moniteur série.

## Critères d'évaluation
Voici les principaux critères d'évaluation qui seront utilisés pour évaluer votre programme. Il est possible que d'autres critères soient utilisés.
- Le programme compile sans erreur
- Le programme fonctionne comme demandé
- L'utilisation des variables est adéquate
  - Par exemple, je ne retrouve pas de valeur arbitraire dans le code, mais des variables avec des noms explicites
- La mise en pratique des concepts est adéquate
  - Par exemple, je ne retrouve pas de `delay()` dans le code. Le code est en tâche.

---

# Volet théorique
En plus des connaissances du volet pratique, vous devez être en mesure de répondre aux questions qui pourraient être en lien avec les notions suivantes:
- Les concepts derrière la programmation orientée objet
- Les concepts derrière le MQTT
- La refactorisation

## Exemples de question
Voici des exemples de questions qui pourraient être posées lors de l'évaluation finale. Ces questions ne sont pas nécessairement représentatives de ce qui sera demandé lors de l'évaluation finale. Elles sont là pour vous donner une idée du genre de question qui pourrait être posée. La meilleure façon de vous préparer est de faire les exercices de révision et de vous pratiquer à faire des programmes qui utilisent les concepts mentionnés ci-dessus.

- Expliquez-vous en vos mots ce qu'est un sujet dans le contexte du MQTT.
  - Donnez 5 exemples de sujets avec une description de ce qu'ils représentent.
- Qu'est-ce que le payload dans le contexte du MQTT?
  - Donnez 3 exemples de payload avec une description de ce qu'ils représentent.
- Nommez 3 avantages de la programmation orientée objet.
- À quoi sert une librairie et nommez 3 librairies que l'on a utilisées dans le cours.
- Pourquoi il est proscrit d'utiliser la fonction `delay()` dans un programme?
- Pourquoi dans nos classes développées durant le cours, nous avons une fonction `update()`?
- Quelles sont les broches permettant la communication i2c sur l'Arduino Mega?
- Que représentent les couleurs sur une résistance?
- Quel est l'avantage d'utiliser une librairie pour gérer un bouton?
- Pourquoi met-on une résistance de tirage vers le haut ou vers le bas sur un bouton?