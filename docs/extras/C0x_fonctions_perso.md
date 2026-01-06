
# Fonction en C++
## Syntaxe
Voici comment déclarer une fonction en Arduino :

```cpp	
type additionner(liste_parametres) {
  // Corps de la fonction
}
```

Le mot-clé `type` peut être remplacé par le type de données du résultat retourné par la fonction. Si la fonction ne retourne pas de résultat, vous pouvez utiliser le mot-clé `void`.

---

## Fonction avec retour de valeur

Voici un exemple de déclaration d'une fonction qui retourne un entier et qui prend deux entiers en paramètre :

```cpp
int additionner(int x, int y) {
  // Corps de la fonction
}
```

Pour appeler une fonction, vous pouvez utiliser son nom suivi de parenthèses contenant les arguments à passer à la fonction. Par exemple :

```cpp
int resultat = additionner(10, 20);
```

Voici un exemple complet de fonction en Arduino :

```cpp
int additionner(int x, int y) {
  int resultat = x + y;
  return resultat;
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  int res = additionner(10, 20);
  Serial.println(res);
  delay(1000);
}

```

Dans cet exemple, la fonction `additionner` prend deux entiers en paramètre et retourne leur somme. Elle est appelée dans la fonction `loop` et le résultat est affiché sur la liaison série.

---

## Fonction sans retour de valeur (procédure)
Parfois, on doit répéter des instructions sans que celles-ci n'aient à retourner une valeur. Dans ce cas, on peut déclarer une fonction sans type de retour. On parle alors de **procédure** ou de fonction `void`.

```cpp
void clignoteLED(int brocheLED, int tauxClignotement) {
  // Variable statique pour sauvegarder
  // la valeur de la dernière fois
  static unsigned long tempsPrecedent = 0; 
  
  if (millis() - tempsPrecedent > tauxClignotement) { 
    digitalWrite(brocheLED, !digitalRead(brocheLED)); 
    tempsPrecedent = millis();
  }
}
```

---