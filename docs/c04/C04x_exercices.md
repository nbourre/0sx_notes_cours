# Exercices
## Exercices - `analogRead()`
1. Réalisez l'[Exemple de code de base](#exemple-de-code-de-base)
2. Ajoutez une DEL branché sur la broche de votre choix. En utilisant la fonction map, faites en sorte que la DEL clignote à une fréquence proportionnelle à la valeur analogique lue par le potentiomètre, c'est-à-dire que si la valeur analogique est de 0, la DEL ne clignote pas. Si la valeur analogique est de 1023, la DEL clignote à toutes les millisecondes.
3. Réalisez le montage de l'exemple [Sélection de DEL](#sélection-de-del) avec le code de l'exemple [Exemple de code avec la fonction `map()`](#exemple-de-code-avec-la-fonction-map).

## Exercices - avec `analogWrite()`
- Avec le montage de l'[exercices](#exercices) #4 des notes sur `analogRead`, faire varier des DEL en utilisant la fonction `analogWrite()`.

### Défi
- Avec le montage précédent, réalisez un programme qui allume l'ensemble des DEL en échelle et graduellement.
  - Lorsque la valeur du potentiomètre est en déça de 255, la DEL 1 s'allume graduellement de 0 à 100% donc si le potentiomètre est à 0, la DEL 1 doit être éteinte et si le potentiomètre est à 127, la DEL 1 doit être à 50% de luminosité.
  - Si le potentiomètre est entre 255 et 511, la DEL 2 s'allume graduellement de 0 à 100% et la DEL 1 doit être allumée à 100%.
  - Ansi de suite

![Alt text](assets/pot_challenge.gif)