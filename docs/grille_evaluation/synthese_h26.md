# Grille de correction pour l'évaluation synthèse H26
---

| No | Nom court | Catégorie | Pts | Description détaillée |
| --- | --- | --- | --- | --- |
| **T01** | Enum + switch 4 états | Infrastructure | 6 | Les 4 états (REPOS, TRAVAIL, SUCCES, AVERTISSEMENT) sont déclarés dans l'enum `AppState` ET le `stateManager` les route tous les 4 dans son switch/case. (baud rate, callbacks OneButton et `btn.tick` déjà fournis dans le projet de base) |
| **T02** | commandeTache dans loop | Infrastructure | 4 | `commandeTache(currentTime)` est appelée dans `loop()` selon le patron tâche vu en classe (pas dans un état, pas dans `serialEvent`). Permet le traitement asynchrone des commandes série. |
| **T03** | clickEvent → clicFlag | Bouton | 3 | `clickEvent()` lève uniquement le drapeau `clicFlag = true` (patron événement). La logique métier (incrémentation, affichage) doit être dans `reposState`, pas dans le callback. |
| **T04** | longPressEvent → flag | Bouton | 2 | `longPressEvent()` lève uniquement `longPressFlag = true` (patron événement). |
| **T05** | nbSecondes++ sur clic | Bouton | 5 | Dans `reposState()`, sur détection de `clicFlag` : `clicFlag` remis à false et `nbSecondes` incrémentée de 1. |
| **T06** | Affichage 'Secondes : X' | Bouton | 3 | À chaque clic, le port série affiche 'Secondes : X' (valeur courante de `nbSecondes`). S'affiche une seule fois par clic, non spammé. |
| **T07** | Cmd 'go' fonctionne | Série | 5 | La commande 'go' (sans paramètre) démarre le minuteur si `nbSecondes > 0` (transition TRAVAIL via `goFlag`). Si `nbSecondes == 0`, déclenche AVERTISSEMENT. |
| **T08** | Cmd 'go:n' fonctionne | Série | 9 | La commande 'go:n' (ex: go:10) extrait correctement le paramètre n avec `substring`/`indexOf`, fixe `nbSecondes = n` et démarre immédiatement le décompte. |
| **T09** | Cmd inconnue → message | Série | 5 | Toute commande ne commençant pas par 'go' affiche sur le port série : 'CMD inconnu : <numéro_DA_étudiant>'. |
| **T10** | REPOS : DEL verte | État REPOS | 3 | À chaque clic allume la del pendant 100 ms. |
| **T11** | REPOS → AVERTISSEMENT | État REPOS | 6 | Si `nbSecondes == 0` ET (`longPressFlag` OU `goFlag`), transition vers AVERTISSEMENT. DEL jaune éteinte, drapeaux réinitialisés. |
| **T12** | REPOS → TRAVAIL | État REPOS | 5 | Si `nbSecondes > 0` ET (`longPressFlag` OU `goFlag`), transition vers TRAVAIL. DEL jaune éteinte, drapeaux réinitialisés. |
| **T13** | REPOS : msgs Entrée/Sortie | État REPOS | 3 | Le port série affiche 'Entrée : REPOS' à l'entrée (une seule fois, bloc `firstTime`) et 'Sortie : REPOS' à la sortie. Messages non spammés. |
| **T14** | TRAVAIL : DEL verte 1 Hz | État TRAVAIL | 6 | La DEL verte (broche 10) clignote à exactement 1 Hz : change d'état toutes les 500 ms (rate = 500). Géré de façon asynchrone avec `millis()`. |
| **T15** | TRAVAIL : décompte série | État TRAVAIL | 5 | Toutes les secondes, affiche 'Décompte : X' sur le port série et décrémente `nbSecondes`. S'affiche une seule fois par seconde. |
| **T16** | TRAVAIL → SUCCES | État TRAVAIL | 5 | Lorsque le temps alloué est écoulé (`exitTime = ct + nbSecondes * 1000`), la DEL verte s'éteint et le système bascule vers SUCCES. |
| **T17** | TRAVAIL : msgs Entrée/Sortie | État TRAVAIL | 3 | Le port série affiche 'Entrée : TRAVAIL' (dans `firstTime`) et 'Sortie : TRAVAIL'. Messages non spammés (pas hors du bloc `firstTime`). |
| **T18** | SUCCES : alternance 4 Hz | État SUCCES | 5 | Les DELs verte et rouge clignotent EN ALTERNANCE à 4 Hz (rate = 125 ms). Quand l'une est allumée, l'autre est éteinte. |
| **T19** | SUCCES : durée 3 s | État SUCCES | 5 | L'état SUCCES dure exactement 3 secondes (`exitTime = ct + 3000`). Géré de façon asynchrone. |
| **T20** | SUCCES → REPOS | État SUCCES | 3 | Après 3 secondes, les deux DELs s'éteignent et le système retourne à l'état REPOS. |
| **T21** | SUCCES : msgs Entrée/Sortie | État SUCCES | 2 | Le port série affiche 'Entrée : SUCCES' et 'Sortie : SUCCES' (une seule fois chacun). |
| **T22** | Qualité générale | Qualité | 5 | Qualité générale du code. |
| **T23** | Patron respecté | Qualité | 2 | Les fonctions d'état utilisent le patron 'firstTime' (variable static locale bool) pour exécuter le code d'initialisation une seule fois à l'entrée de l'état. |
| **TOTAL** |  |  | **100** |  |