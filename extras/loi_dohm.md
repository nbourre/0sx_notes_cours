# Loi d'Ohm

La loi d'Ohm est une loi physique qui établit la relation entre la tension, l'intensité et la résistance d'un circuit électrique. Elle est exprimée par la formule suivante :
$$U = RI$$
où :
- `U` est la tension (`V`);
- `R` la résistance (`Ohm`);
- `I` l'intensité (`A`).

Cette loi est importante car elle permet de comprendre comment les différents composants d'un circuit électrique interagissent les uns avec les autres et comment ils peuvent être utilisés pour contrôler et mesurer le courant électrique. Elle est utilisée pour toutes les applications électriques, allant de la conception de circuits électroniques à la résolution de problèmes électriques dans les bâtiments et les véhicules.

# Calculer la résistance nécessaire pour une DEL

Avec la loi d'Ohm, on peut calculer la résistance nécessaire pour faire allumer une DEL. On utilisera la formle suivante pour calculer la résistance nécessaire pour une DEL :
$$R = \frac{U_{max} - U_{DEL}}{I_{DEL}}$$

où :
- $U_{max}$ est la tension maximale du circuit (`V`).
  - Par exemple `5V` pour un Arduino;
- $U_{DEL}$ la tension de la DEL (`V`);
  - Par exemple `2V` pour une DEL rouge;
  - Note : Il faudra lire la fiche signalétique de la DEL pour connaître sa tension;
- $I_{DEL}$ l'intensité de la DEL (`A`);
  - Par exemple `20mA` pour une DEL rouge.
  - Note : Il faudra lire la fiche signalétique de la DEL pour connaître l'intensité;

## Exemple
Dans nos kits, nous avons des DEL rouge de 2V et 20mA. Nous allons donc calculer la résistance nécessaire pour une DEL rouge de 2V et 20mA avec une tension maximale de 5V.

$$R = \frac{5V - 2V}{20mA} = 150\Omega$$

> **Note spécifique aux DEL** : La résistance calculée est une valeur idéale. Il est possible de mettre une valeur de résistance plus élevé si l'on veut réduire la consommation de courant de la DEL. Par exemple, si on met une résistance de 1k$\Omega$, 3mA circuleront dans la DEL au lieu de 20mA.
> 
> Prenez note qu'en contrepartie, celle-ci aura une puissance plus faible.

# Références
- [Calcul de résistance pour une led](http://fantaisyland.fr/calcul-resistance-led/)
- [LED resistance in the kit](https://forum.arduino.cc/t/led-resistences-in-the-kit/482081)
  - [DEL bleue](https://www.arduino.cc/documents/datasheets/LED(blue).pdf)
  - [DEL rouge](https://www.arduino.cc/documents/datasheets/LED(red).pdf)
  - [DEL verte](https://www.arduino.cc/documents/datasheets/Leds(Green).pdf)
  - [DEL jaune](https://www.arduino.cc/documents/datasheets/LEDY-L-7113YT.pdf)