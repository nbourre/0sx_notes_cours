# Le concept des pointeurs en C++ <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Qu'est-ce qu'un pointeur?](#quest-ce-quun-pointeur)
- [Déclaration et initialisation des pointeurs](#declaration-et-initialisation-des-pointeurs)
- [Accéder à la valeur pointée](#acceder-a-la-valeur-pointee)
- [Exemples de programmation](#exemples-de-programmation)
- [Exercices](#exercices)
- [Références](#references)


# Introduction
Les pointeurs sont l'une des caractéristiques les plus puissantes et distinctives du langage C++. Ils permettent aux programmeurs de manipuler directement la mémoire de l'ordinateur, ce qui peut améliorer considérablement les performances des programmes et faciliter la gestion de structures de données complexes. Cependant, les pointeurs peuvent également être source d'erreurs et de bogues difficiles à détecter, il est donc important de bien comprendre comment ils fonctionnent et de les utiliser avec prudence.

# Qu'est-ce qu'un pointeur?

Un pointeur est une variable qui stocke l'adresse mémoire d'une autre variable. En d'autres termes, un pointeur "pointe" vers l'emplacement où une autre variable est stockée en mémoire. Les pointeurs sont souvent utilisés pour accéder à des variables et des objets de manière indirecte, ce qui peut faciliter le passage d'informations entre les fonctions et la manipulation de structures de données.

<table width="300" align="center">
<tr>
<td>

![Tableau de pointeurs](https://upload.wikimedia.org/wikipedia/commons/8/8b/Pointers.png)

</td>
</tr>
<tr>
<td>Le pointeur <b>a</b> pointe sur la variable <b>b</b>. On peut noter que b contient un nombre (en hexadécimal 00000011 = en décimal 17), et que <b>a</b> contient l'adresse de <b>b</b> en mémoire (en hexadécimal 1008). Dans ce cas précis, l'adresse et la donnée sont contenues dans 32 bits. </td>
</tr>

</table>


# Déclaration et initialisation des pointeurs

En C++, un pointeur est déclaré en utilisant le symbole `*` après le type de la variable pointée. Par exemple, pour déclarer un pointeur vers un entier, on utiliserait la syntaxe suivante :

```cpp
int* myPointer;
```

Lorsqu'un pointeur est déclaré, il est important de l'initialiser avant de l'utiliser. Un pointeur non initialisé peut provoquer des comportements indéterminés et des erreurs difficiles à détecter. Pour initialiser un pointeur, on peut lui attribuer l'adresse d'une autre variable en utilisant l'opérateur `&` :


```cpp
int myVariable = 42;
int* myPointer = &myVariable;
```

# Accéder à la valeur pointée

Pour accéder à la valeur de la variable pointée par un pointeur, on utilise l'opérateur de déréférencement `*`. Cela permet de lire ou de modifier la valeur de la variable pointée:

```cpp
int myVariable = 42;
int* myPointer = &myVariable;

int value = *myPointer; // value contient maintenant 42
*myPointer = 13; // myVariable contient maintenant 13
```

# Exemples de programmation

Voici quelques exemples de code utilisant des pointeurs:

1. Échange de valeurs entre deux variables en utilisant un pointeur:

```cpp
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5;
    int y = 10;
    swap(&x, &y); // x = 10, y = 5
}
```

2. Manipulation d'un tableau en utilisant des pointeurs:

```cpp
int sum(int* arr, int size) {
    int total = 0;
    for (int i = 0; i < size; ++i) {
        // On peut accéder à l'élément d'indice i du tableau en utilisant
        // l'opérateur de déréférencement * et en ajoutant i à l'adresse
        // du premier élément du tableau
        total += *(arr + i);
    }
    return total;
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int result = sum(numbers, 5); // result = 15
}
```	

> **Note :** Dans un système de 64 bits, les pointeurs ont une taille de 64 bits, soit 8 octets. Lorsque vous travaillez avec un tableau d'entiers, chaque élément occupe généralement 4 octets. Ainsi, lorsque vous ajoutez 1 à un pointeur vers un tableau d'entiers, il pointe vers l'élément suivant du tableau, qui se trouve 4 octets plus loin en mémoire.
> 
> Si l'adresse du tableau `arr` est `0x7ffddc0c0a10`, alors `arr + 1` vaudra `0x7ffddc0c0a10 + 4 = 0x7ffddc0c0a14`. Pour accéder à la valeur de cet élément, il faut déréférencer le pointeur en utilisant l'opérateur `*` : `*(arr + 1)`.
> 
> Donc, `*(arr + 1)` représente la valeur de l'élément à l'adresse mémoire `0x7ffddc0c0a14`.

---

# Exercices
- Vous pouvez faire les exercices en lien avec les pointeurs sur cette [page](../exercices/pointeurs.md).


---

# Références

- [Wikipédia - Pointeur](https://fr.wikipedia.org/wiki/Pointeur_(programmation)#C_et_C++)
- [C++ References](https://www.w3schools.com/cpp/cpp_references.asp)
- [C++ Memory address](https://www.w3schools.com/cpp/cpp_references_memory.asp)
- [C++ Pointers](https://www.w3schools.com/cpp/cpp_pointers.asp)
