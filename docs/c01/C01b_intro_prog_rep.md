# Réponses aux exercices
## Recherches
1. Les variables écrit tout en majuscules s'agissent généralement de constante. Les constantes sont des valeurs qui ne changent pas pendant l'exécution du programme. Utiliser des noms de variables en majuscule pour les constantes permet de les identifier facilement dans le code et de les différencier des autres variables. Cela peut également aider à éviter les erreurs en empêchant la modification accidentelle de la valeur d'une constante.
2. `HIGH` = 1, `LOW` = 0, `LED_BUILTIN` = 13
3. `delay()` est une fonction qui permet de mettre en pause le programme pendant un certain temps. Elle prend en paramètre un nombre entier qui représente le temps en millisecondes pendant lequel le programme est mis en pause.
4. `pinMode()` est une fonction qui permet de définir le mode d'un port. Elle prend en paramètre le numéro du port et le mode du port. Les modes possibles sont `INPUT`, `OUTPUT` et `INPUT_PULLUP`.
5. Le Arduino Mega possède 8 KO de mémoire SRAM alors que l'Arduino Uno n'en possède que 2 KO. Il possède également 256 KO de mémoire flash contre 32 KO pour l'Arduino Uno.

## Questions
1. Une variable locale n'est disponible que dans la fonction dans laquelle est déclarée. Une variable globale est disponible dans toutes les fonctions du programme.
2. Pour stocker du temps en millisecondes, il est préférable d'utiliser un type `unsigned long`.
