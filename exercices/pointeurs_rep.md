# Pointeurs - Exercices - Solutions

Voici les solutions pour les exercices sur les pointeurs :

1. Addition de deux entiers en utilisant des pointeurs :

```cpp
int add(int* a, int* b) {
    return *a + *b;
}

int main() {
    int x = 5;
    int y = 10;
    int result = add(&x, &y); // result = 15
}
```

2. Inversion d'un tableau d'entiers :

```cpp
void reverse(int* arr, int size) {
    for (int i = 0; i < size / 2; ++i) {
        int temp = *(arr + i);
        *(arr + i) = *(arr + size - 1 - i);
        *(arr + size - 1 - i) = temp;
    }
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    reverse(numbers, 5); // numbers = {5, 4, 3, 2, 1}
}
```

3. Trouver le plus grand élément d'un tableau d'entiers :

```cpp
int* findMax(int* arr, int size) {
    if (arr == nullptr || size <= 0) {
        return nullptr;
    }

    int* maxPtr = arr;

    for (int i = 1; i < size; ++i) {
        if (*(arr + i) > *maxPtr) {
            maxPtr = arr + i;
        }
    }

    return maxPtr;
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int* maxPtr = findMax(numbers, 5); // maxPtr pointe vers 5
}
```

4. Compter le nombre d'occurrences d'un entier dans un tableau d'entiers :

```cpp
int countOccurrences(int* arr, int size, int n) {
    int count = 0;

    for (int i = 0; i < size; ++i) {
        if (*(arr + i) == n) {
            count++;
        }
    }

    return count;
}

int main() {
    int numbers[] = {1, 2, 3, 2, 5};
    int count = countOccurrences(numbers, 5, 2); // count = 2
}
```

5. Créer un nouveau tableau contenant uniquement les nombres pairs d'un tableau d'entiers :
   
```cpp
int* createEvenArray(int* arr, int size, int& newSize) {
    newSize = 0;

    for (int i = 0; i < size; ++i) {
        if (*(arr + i) % 2 == 0) {
            newSize++;
        }
    }

    int* evenArray = new int[newSize];
    int evenIndex = 0;

    for (int i = 0; i < size; ++i) {
        if (*(arr + i) % 2 == 0) {
            *(evenArray + evenIndex) = *(arr + i);
            evenIndex++;
        }
    }

    return evenArray;
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int newSize;
    int* evenArray = createEvenArray(numbers, 5, newSize); // newSize = 2, evenArray = {2, 4}
    delete[] evenArray;
}
```

> **Attention!!** Code non recommendé pour des projets embarqués. Il est préférable d'utiliser des `std::vector` pour manipuler des tableaux dynamiques.

> **Note :** Pour les exercices 2 à 5, il est important de vérifier si les pointeurs passés en paramètres sont valides (non `NULL`) avant de les utiliser. Les exemples fournis ci-dessus ne montrent pas explicitement ces vérifications pour des raisons de simplicité, mais elles doivent être prises en compte lors de l'écriture de code réel.
> 
> En général, vous pouvez ajouter une vérification pour les pointeurs en utilisant une instruction `if` :
> ```cpp
> if (arr == nullptr || size <= 0) {
>    // Gérer le cas où le pointeur est NULL ou la taille est invalide
> }
> ```
> Pour les exercices où vous créez un nouveau tableau dynamiquement, il est également important de libérer la mémoire allouée avec `delete[]` après avoir fini de l'utiliser, comme montré dans l'exemple 5.
