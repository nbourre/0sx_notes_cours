ARDUINO

Guide d’introduction

<img src="media/image1.png"
style="width:2.59406in;height:1.7663in" alt="Arduino — Wikipédia" />

<img src="media/image2.png"
style="width:1.76521in;height:0.51485in" />

Jean-Philippe Boulard (Mars 2022)

Rév. Nicolas Bourré (A22)

# Table des matières

[Introduction [3](#introduction)](#introduction)

[Qu’est-ce que Arduino?
[4](#quest-ce-que-arduino)](#quest-ce-que-arduino)

[Arduino NANO [4](#arduino-nano)](#arduino-nano)

[Arduino UNO R3 [4](#arduino-uno-r3)](#arduino-uno-r3)

[Arduino MEGA 2560 (rev3)
[4](#arduino-mega-2560-rev3)](#arduino-mega-2560-rev3)

[Comparaison entre les tailles
[5](#comparaison-entre-les-tailles)](#comparaison-entre-les-tailles)

[Références [5](#références)](#références)

[Composantes de base [6](#composantes-de-base)](#composantes-de-base)

[Câble USB type USB-B [6](#câble-usb-type-usb-b)](#câble-usb-type-usb-b)

[Platine d'expérimentation sans soudure (*Breadboard*)
[6](#platine-dexpérimentation-sans-soudure-breadboard)](#platine-dexpérimentation-sans-soudure-breadboard)

[Fil de raccordement M/M (*Jumper wires*)
[7](#fil-de-raccordement-mm-jumper-wires)](#fil-de-raccordement-mm-jumper-wires)

[Fil de raccordement M/F (*Jumper wires)*
[7](#fil-de-raccordement-mf-jumper-wires)](#fil-de-raccordement-mf-jumper-wires)

[Attache batterie 9V (*9V battery snap*)
[8](#attache-batterie-9v-9v-battery-snap)](#attache-batterie-9v-9v-battery-snap)

[DEL (*LED*) [8](#del-led)](#del-led)

[Intensité [8](#intensité)](#intensité)

[Résistance (*Resistor*)
[9](#résistance-resistor)](#résistance-resistor)

[Autres composantes [10](#autres-composantes)](#autres-composantes)

[DEL RVB (*LED RGB*) [10](#del-rvb-led-rgb)](#del-rvb-led-rgb)

[Ressources et références
[11](#ressources-et-références)](#ressources-et-références)

# Introduction

# Qu’est-ce que Arduino?

Arduino est une plateforme de prototypage de type « *Open-Source* »
utilisant un circuit électronique et un microcontrôleur. Le
fonctionnement simple de ces cartes avec microcontrôleurs, réside dans
la possibilité à LIRE une information ENTRANTE (*INPUT*) puis après
analyse, de poser une ACTION (*OUTPUT*).

Il existe plusieurs types de cartes Arduino sur le marché. Chacune ayant
des caractéristiques propres malgré leurs très grands nombres de
similitudes. Voici les trois (3) modèles les plus communément utilisés :

## Arduino NANO

Il s’agit du modèle de base de petite dimension (45mm x 18mm). Le
contrôleur **ATMega328** fonctionne à 16MHz et il possède une mémoire de
32KB. Son connecteur USB est de type « Mini-B ».

<img src="media/image3.png"
style="width:1.47927in;height:1.18152in"
alt="Une image contenant équipement électronique, circuit Description générée automatiquement" />

(Référence complète : <https://docs.arduino.cc/hardware/nano> )

## Arduino UNO R3

Il s’agit du modèle le plus commun. Il dispose du même nombre de
connecteurs analogue (*pins*) que le modèle NANO. De dimension moyenne
(54mm x 69mm), il utilise le contrôleur **ATMega328P** à 16 MHz avec un
mémoire de 32KB. Son connecteur USB est de type « USB-B ».

<img src="media/image4.png"
style="width:2.26071in;height:1.45598in"
alt="Une image contenant équipement électronique, circuit Description générée automatiquement" />

(Référence complète : <https://docs.arduino.cc/hardware/uno-rev3> )

## Arduino MEGA 2560 (rev3)

Il s’agit du modèle plus *costaud*. De plus grande dimension (54mm x
102mm), il dispose de 54 connecteurs (*pins*) entrée et sortie. Il est
équipé du contrôleur **ATM2560** à 16MHz et d’une mémoire de 256KB. Son
connecteur USB est de type « USB-B ».

<img src="media/image5.png"
style="width:2.44331in;height:1.89513in"
alt="Une image contenant équipement électronique, circuit Description générée automatiquement" />

(Référence complète : <https://docs.arduino.cc/hardware/mega-2560> )

## Comparaison entre les tailles

<img src="media/image6.png"
style="width:5.29861in;height:1.28472in"
alt="Une image contenant texte, équipement électronique, circuit Description générée automatiquement" />

(Source :
<https://www.arrow.com/en/research-and-events/articles/arduino-uno-vs-mega-vs-micro>
)

### Tableau résumé

Tableau résumé des caractéristiques de base des trois principaux
modèles :

| **Modèle**       | **Dimension** | **Processeur** | **Mémoire** | **Connecteurs (*Pins*)** | **USB** |
|------------------|---------------|----------------|-------------|--------------------------|---------|
| NANO             | 45mm x 18mm   | ATMega328      | 32KB        | 14                       | Mini-B  |
| UNO R3           | 54mm x 69mm   | ATMega328P     | 32KB        | 14                       | USB-B   |
| MEGA 2560 (rev3) | 54mm x 102mm  | ATM2560        | 256KB       | 54                       | USB-B   |

## Références

Site officiel d’Arduino :

<https://www.arduino.cc/en/Guide/Introduction>

<https://www.arduino.cc/en/Main/Products>

# Composantes de base

Voici une liste de composantes de base qui sont utilisées pour la
conception de projets simples. Vous trouverez des photos, schémas et
informations de base pour chaque composante. Notez que vos projets
peuvent être aussi bonifiés avec les éléments de la liste « **Autres
composantes** » à la suite de cette section.

## Câble USB type USB-B

<img src="media/image7.jpeg"
style="width:1.42627in;height:1.0692in" />

Le câble USB permet de relier la carte ARDUINO à un ordinateur afin d’y
transférer les applications (codes) que vous avez créées. Il permet
aussi d’alimenter la carte.

Après le transfert, le câble peut être retiré. Vous devez cependant,
alimenter votre carte avec une autre source d’énergie si vous désirez
qu’elle puisse fonctionner de manière autonome (batteries ou bloc
d’alimentation).

<img src="media/image8.png"
style="width:3.46087in;height:1.74485in" />

## Platine d'expérimentation sans soudure (*Breadboard*)

<img src="media/image9.jpeg"
style="width:2.24167in;height:1.47986in" />La platine d’expérimentation
permet de réaliser un montage avec des composantes électroniques sans
avoir à les souder.

- Elle est généralement composée de deux (2) sections de cinq (5) points
  linéaires chacune. Le nombre de points peut varier entre 400 et 800
  sur les platines standards. Chaque section peut être alimentée de
  manière indépendante.

<img src="media/image10.png"
style="width:2.33795in;height:0.74976in"
alt="Une image contenant texte Description générée automatiquement" />

- Chaque colonne est identifiée par les lettres de l’alphabet. La
  première section de **A** à **E** et la seconde de **F** à **J**.

- Tous les points d’une ligne sont rattachés ensemble, i.e. ils agissent
  comme si c’était un seul fil.

<img src="media/image11.png"
style="width:0.92368in;height:0.36552in"
alt="Une image contenant équipement électronique, fermer Description générée automatiquement" />

- Une ligne s’arrête avec l’encoche qui délimite les deux sections.

<img src="media/image12.png"
style="width:2.33156in;height:0.38586in"
alt="Une image contenant texte, fermer, trouble Description générée automatiquement" />

<img src="media/image13.png"
style="width:3.30422in;height:2.41429in" alt="breadboard" />

Figure : Branchement interne d'une platine d’expérimentation

## Fil de raccordement M/M (*Jumper wires*)

<img src="media/image14.png"
style="width:1.36111in;height:1.36111in" />

Les fils de raccordement M/M (pour Mâle/Mâle) sont utilisés pour lier
des composantes entre elles sur la platine de montage ainsi que vers la
carte Arduino. Ils existent dans différentes longueurs et couleurs.

- Évitez d’utiliser des fils de trop grandes longueurs lors de la
  création de vos montages. Cela rend plus difficile la lecture visuelle
  de votre circuit.

- Essayez de respecter, autant que possible, les conventions de couleur
  > afin de faciliter la lecture de vos circuits et ainsi vous permettre
  > de relever rapidement les erreurs potentielles.

> <img src="media/image15.jpeg"
> style="width:2.48611in;height:1.86458in" />  
> (source :<https://www.hackster.io/super-kid/windows-remote-arduino-windows-remote-arduino-experience-a5ea4d>)

## Fil de raccordement M/F (*Jumper wires)*

<img src="media/image17.png"
style="width:1.40278in;height:1.37472in" />

Les fils de raccordement M/F (pour Mâle/Femelle) sont utilisés pour lier
des modules de capteurs sur la platine de montage ainsi que vers la
carte Arduino. Ils existent dans différentes longueurs et couleurs.

- Évitez d’utiliser des fils de trop grandes longueurs lors de la
  création de vos montages.

- Essayez de respecter, autant que possible, les conventions de couleur
  > afin de faciliter la lecture de vos circuits et ainsi vous permettre
  > de relever rapidement les erreurs potentielles.

> <img src="media/image18.jpeg"
> style="width:2.59722in;height:1.83333in" />
>
> (Source :
> <http://electroniqueamateur.blogspot.com/2020/09/capteur-de-son-ky-038-et-arduino.html>
> )

## <img src="media/image20.png"
style="width:1.03125in;height:1.5in" />Attache batterie 9V (*9V battery snap*)

L’attache de batterie 9V permet à la carte Arduino d’avoir une
alimentation électrique sans être rattachée au port USB de l’ordinateur.

## DEL (*LED*)

(Blanche, rouge, verte, bleue, jaune)

<img src="media/image21.png"
style="width:0.84236in;height:1.49792in" />

Une DEL (*led*) ou **d**iodes **é**lectro**l**uminescentes est un
dispositif capable d’émettre de la lumière. La DEL est composée d’une
Anode (**+**) et d’une Cathode (**-**).

La DEL est « polarisée ». C’est-à-dire qu’elle laisse circuler
l’électricité en respectant la polarité positive et négative. Il existe
des différences physiques qui vous permettent de différencier le côté
positif et le côté négatif. Le tableau ci-dessous vous permettra de les
repérer facilement.

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 22%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Anode (+)</strong></th>
<th rowspan="2"><img src="media/image22.png"
style="width:0.75in;height:1.64713in" />(1)</th>
<th><strong>Cathode (-)</strong></th>
</tr>
<tr class="odd">
<th><ul>
<li><p>C’est la broche la plus <strong>longue</strong>;</p></li>
<li><p>À l‘intérieur de la DEL, c’est la portion la plus
<strong>petite</strong>;</p></li>
<li><p>La bordure externe est présente et est
<strong>arrondie</strong>.</p></li>
</ul></th>
<th><ul>
<li><p>C’est la broche la plus <strong>courte</strong>;</p></li>
<li><p>À l’intérieur de la DEL, c’est la portion la plus
<strong>grosse</strong>;</p></li>
<li><p>La bordure externe est absente et est <strong>droite.</strong>
Truc : Ça fait un « - » comme négatif</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> \(1\) Source :
> <https://fr.wikipedia.org/wiki/Diode_%C3%A9lectroluminescente>

### Intensité

Il est important de ne pas dépasser l’intensité admissible d’une DEL
pour ne pas la faire griller. Dans le kit, ***<u>l’ajout d’une
résistance de 220 ohms en série est fortement recommandé.</u>***

DEL RVB (LED RGB)

Voir la section « **Autres composantes** » pour plus de détails sur les
DEL RVB.

## Résistance (*Resistor*)

<img src="media/image24.jpeg"
style="width:1.29583in;height:0.9in" />

La résistance permet de contrôler l’intensité dans un circuit
électrique. Elle se calcule en « **ohms** ». Plus la valeur d’une
résistance est élevée, moins elle laissera circuler l’électricité.

Dans le cadre de vos projets Arduino, elles devraient toujours être
présentes sur le circuit d’une DEL.

Pour connaitre la valeur d’une résistance, vous pouvez :

- **Utiliser un multimètre :**

<img src="media/image25.png"
style="width:3.18448in;height:2.11382in"
alt="Une image contenant horloge, périphérique, main, jauge Description générée automatiquement" />

- **Utiliser le tableau suivant :**

<img src="media/image26.png"
style="width:3.30726in;height:4.68018in" />

# Autres composantes

## DEL RVB (*LED RGB*)

<img src="media/image27.png"
style="width:1.22495in;height:0.77556in" />

Les DEL RVB combinent trois DEL : une Rouge, une Verte et une Bleu. Cela
permet de produire une combinaison de 16 millions de nuances de lumière.

Elles existent en deux versions : Anode commune ou Cathode commune.

- Dans la version **Anode commune**, nous utilisons le **5V**.

- Dans la version **Cathode commune**, nous utilisons la **mise à terre
  > (*ground*)**.  
  > (Il s’agit de la version présentée ici et disponible dans votre
  > kit.)

*<span class="mark">\* \* \* Comme pour les autres LED, l’ajout d’une
résistance de 220ohms en série est fortement recommandé (i.e une pour
chaque tige qui contrôle la couleur).</span>*

Utiliser la Cathode (tige la plus grande) comme point de référence. Les
autres « Anodes » servent pour chacune des couleurs.

<img src="media/image28.png"
style="width:2.9167in;height:1.09463in" />

Source :
<https://www.lighting.philips.be/fr/assistance/assistance-produit/faqs/white-light-and-colour/what-does-rgb-led-mean>

## Bouton poussoir

Dans les kits fournit, il y a quelques boutons poussoir.

| <img src="media/image29.png"                                                                                              
 style="width:1.91218in;height:0.98591in" /> Le bouton poussoir permet à un utilisateur d’activer des fonctions dans le microcontrôleur.  | <img src="media/image30.png"                                                                                                            
                                                                                                                                           style="width:1.31667in;height:1.04236in" />À l’intérieur, il y a 2 côtés. Une connexion entre les deux côtés s’effectue lorsque le bouton est activé.  |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|

On retrouve ces boutons dans plusieurs types d’objet électronique. Ils
sont généralement recouverts d’un plastique pour le design. Pouvez-vous
en nommer quelques objets du quotidien qui possèderaient des boutons
similaires?

### Référence

- <https://arduinogetstarted.com/tutorials/arduino-button>

- [https://www.cs.uregina.ca](https://www.cs.uregina.ca/Links/class-info/207/Online/Lab3/)

# Ressources et références

Site officiel ARDUINO

<https://www.arduino.cc/>

Guide du « *MEGA2560 Starter Kit* »

<https://cdn.shopify.com/s/files/1/0069/6513/3376/files/the_most_complete_starter_kit_for_mega_v1.0.17.7.9.pdf?5732344175148787081>

Matériels complets du « *MEGA2560 Starter Kit*»

<https://drive.google.com/drive/folders/1xATtuchoAMSYJ-8C5U0dIHVlOGRsg2fC>

Tout sur les DEL (*All About LED’s*)

<https://learn.adafruit.com/all-about-leds>

Chaine de formations sur ARDUINO (en français)

<https://www.youtube.com/channel/UC1f3yfI3YFzhuoScarGSKwA>
