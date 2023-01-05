# Robotique

# Cours 02 – Communication série, délais et lecture de données

# Plan de leçon

* La fonction  _millis\(\)_
* Délais sans blocage
* Communication série
  * TX : Transmission de données
  * RX : Réception de données
* digitalRead\(\)
* Brancher un bouton

# La fonction millis()

* La fonction  _millis_ \(\) retourne le temps en millisecondes depuis que le programme s’exécute
* Le type retourné est un unsigned long
  * Un unsigned long a 4 octets \(32 bit\)
  * La plage de valeur est de 0 à 4 294 967 295 \(2^32 \- 1\)
* Question
  * Après environ combien de jours\, le compteur va recommencer?

Personnellement\, j’utilise principalement cette fonction une seule fois au début de la boucle pour enregistrer la valeur dans une variable

# La fonction millis() : Exemple

![](img%5C1SX%20-%20Cours%2001%20-%20UART%2C%20D%C3%A9lais0.gif)

<span style="color:#0000FF">unsigned</span>  <span style="color:#000000"> </span>  <span style="color:#0000FF">long</span>  <span style="color:#000000"> </span>  <span style="color:#000000">currentTime</span>  <span style="color:#000000">;</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">setup</span>  <span style="color:#000000">\(\) \{</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// Initialisation des ports de communication Série</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// avec une vitesse de 9600 baud</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">begin</span>  <span style="color:#000000">\(</span>  <span style="color:#098658">9600</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">loop</span>  <span style="color:#000000">\(\) \{</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#A31515">"Temps: "</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#000000">currentTime</span>  <span style="color:#000000"> = </span>  <span style="color:#E97366">millis</span>  <span style="color:#000000">\(\);</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// Afficher le temps depuis le démarrage</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">println</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">currentTime</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// Attendre une seconde pour limiter le</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// transfert de données</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">delay</span>  <span style="color:#000000">\(</span>  <span style="color:#098658">1000</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

Simulation : [https://wokwi\.com/projects/340698208724320852](https://wokwi.com/projects/340698208724320852)

# Délais sans blocage

* Dans le cours précédent\, nous avons vu la fonction « delay\( _ms_ \) » qui permet au microcontrôleur \(µC\) d’effectuer une pause
* Le problème avec cette fonction est qu’elle « gèle » le processeur
  * Ainsi\, il n’est plus possible de rien faire d’autre
* Si on voulait faire un clignoter un DEL\, mais que l’on puisse lire un bouton pendant la pause\, ça ne fonctionnerait pas

// La fonction setup s’exécute une seule fois lorsque

// l’on appuie sur « reset » ou que l’on met le courant

void setup\(\) \{

pinMode\(LED\_BUILTIN\, OUTPUT\);

\}

// La fonction loop s’exécute toujours et pour toujours

void loop\(\) \{

digitalWrite\(LED\_BUILTIN\, HIGH\);

delay\(1000\);

digitalWrite\(LED\_BUILTIN\, LOW\);

delay\(1000\);

\}

* Il y a quelques méthodes pour simuler un délai sans faire de pause
* Celle que je vous présente est simple à comprendre
* En gros\, je compare le temps actuel avec la dernière fois qu’il a été comparé
* Il faut 3 variables dont 2 par actions que l’on désire effectuer
  * currentTime  Temps actuel
  * __x__ Previous  La dernière fois que l’action a été exécutée\. x est le nom de l’action\. Par exemple « blinkPrevious »
  * __x__ Rate  Le taux d’exécution\. Exemple : blinkRate = 500;

# Délais sans blocage : Exemple

<span style="color:#0000FF">unsigned</span>  <span style="color:#000000"> </span>  <span style="color:#0000FF">long</span>  <span style="color:#000000"> </span>  <span style="color:#000000">currentTime</span>  <span style="color:#000000">;</span>

<span style="color:#0000FF">unsigned</span>  <span style="color:#000000"> </span>  <span style="color:#0000FF">long</span>  <span style="color:#000000"> </span>  <span style="color:#000000">blinkPrevious</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">;</span>

<span style="color:#0000FF">unsigned</span>  <span style="color:#000000"> </span>  <span style="color:#0000FF">long</span>  <span style="color:#000000"> </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">500</span>  <span style="color:#000000">;</span>

<span style="color:#0000FF">short</span>  <span style="color:#000000"> </span>  <span style="color:#000000">ledState</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">;  </span>  <span style="color:#727C81">// Peut être un autre type entier</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">setup</span>  <span style="color:#000000">\(\) \{</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// Configuration de la pin</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">pinMode</span>  <span style="color:#000000">\(</span>  <span style="color:#00979C">LED\_BUILTIN</span>  <span style="color:#000000">\, </span>  <span style="color:#00979C">INPUT</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">loop</span>  <span style="color:#000000">\(\) \{</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// Sauvegarde du temps actuel</span>

<span style="color:#000000">  </span>  <span style="color:#000000">currentTime</span>  <span style="color:#000000"> = </span>  <span style="color:#E97366">millis</span>  <span style="color:#000000">\(\);</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// On compare avec la dernière exécution</span>

<span style="color:#000000">  </span>  <span style="color:#0000FF">if</span>  <span style="color:#000000"> \(</span>  <span style="color:#000000">currentTime</span>  <span style="color:#000000"> \- </span>  <span style="color:#000000">blinkPrevious</span>  <span style="color:#000000"> >= </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000">\) \{</span>

<span style="color:#000000">    </span>  <span style="color:#000000">blinkPrevious</span>  <span style="color:#000000"> = </span>  <span style="color:#000000">currentTime</span>  <span style="color:#000000">;</span>

<span style="color:#000000">    </span>  <span style="color:#727C81">// On inverse l'état</span>

<span style="color:#000000">    </span>  <span style="color:#000000">ledState</span>  <span style="color:#000000"> = \!</span>  <span style="color:#000000">ledState</span>  <span style="color:#000000">;</span>

<span style="color:#000000">    </span>  <span style="color:#727C81">// On écrit la valeur dans la pin</span>

<span style="color:#000000">    </span>  <span style="color:#E97366">digitalWrite</span>  <span style="color:#000000">\(</span>  <span style="color:#00979C">LED\_BUILTIN</span>  <span style="color:#000000">\, </span>  <span style="color:#000000">ledState</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  \}</span>

<span style="color:#000000">\}</span>

# Délais sans blocage

* On peut utiliser cette méthode pour ensuite faire d’autres actions
* Exemple
  * Envoyer de l’information à l’ordinateur à toutes les X secondes
  * Lire l’état d’un bouton
  * Lire la température d’une sonde
  * Etc\.

# Communication série

* La communication série permet d’échanger facilement et de manière flexible avec l’Arduino
* Cela permet d’interagir avec l’appareil
* Lorsque l’on téléverse un programme sur l’Arduino\, on passe par le port série
* Lorsqu’il y a échange de données\, il y a 2 DEL qui clignotent soit RX et TX
  * RX lorsque l’Arduino reçoit \(réception\)
  * TX lorsqu’il envoie \(transmission\)

* Les Arduinos avec le µC Atmega328 possède un port série
* Ceux avec le Atmega2560 possède 4 ports série

| Port name | Transmit pin | Receive pin |
| :-: | :-: | :-: |
| Serial | 1 (also USB) | 0 (also USB) |
| Serial1 | 18 | 19 |
| Serial2 | 16 | 17 |
| Serial3 | 14 | 15 |

# Communication série : Initialisation et écriture

* Pour utiliser la communication série\, il faut initialiser le port avec la vitesse de transfert dans la fonction setup
* La fonction pour initialiser la communication\, on utilise la fonction « Serial\.begin\( _baudRate_ \) »
  * Exemple : Serial\.begin\(9600\);
* Pour écrire dans le port\, on utilisera pour l’instant les fonctions ci\-bas
  * Serial\.print\( _data_ \);
  * Serial\.println\( _data_ \); // Envoie un retour à la ligne

# Communication série : Exemple

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">setup</span>  <span style="color:#000000">\(\) \{</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// Initialisation du port</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// série à 9600 baud</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">begin</span>  <span style="color:#000000">\(</span>  <span style="color:#098658">9600</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

<span style="color:#0000FF">int</span>  <span style="color:#000000"> </span>  <span style="color:#000000">counter</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">;</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">loop</span>  <span style="color:#000000">\(\) \{</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#A31515">"Boucle : "</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">println</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">counter</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#000000">counter</span>  <span style="color:#000000">\+\+;</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// Délai pour ne pas ralentir le µC</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">delay</span>  <span style="color:#000000">\(</span>  <span style="color:#098658">500</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

\`3??f<ÌxÌ▯▯▯ü\`³??f<

# Communication série : Discussion

* On doit initialiser
* Pour lire et envoyer de l’information\,  __il faut que le logiciel soit à la même vitesse que l’appareil__
  * Donc si l’appareil est à 9600\, il faut que le logiciel soit aussi à la même vitesse
  * Sinon\, vous obtiendrez un résultat similaire à ceci\`3??f<ÌxÌ▯▯▯ü\`³??f<
* On met un délai à la fin de l’affichage pour ne pas surutiliser le µC

# Communication série : Formatage des données

On peut formater les données que l’on veut envoyer avec le paramètre de formatage

Ex : Serial\.print\(valeur\, HEX\);

<span style="color:#0000FF">char</span>  <span style="color:#000000"> </span>  <span style="color:#000000">chrValue</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">65</span>  <span style="color:#000000">;  </span>  <span style="color:#727C81">// Lettre A en ascii</span>

<span style="color:#0000FF">int</span>  <span style="color:#000000"> </span>  <span style="color:#000000">intValue</span>  <span style="color:#000000">  = </span>  <span style="color:#098658">65</span>  <span style="color:#000000">;</span>

<span style="color:#0000FF">float</span>  <span style="color:#000000"> </span>  <span style="color:#000000">floatValue</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">65\.0</span>  <span style="color:#000000">;</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">setup</span>  <span style="color:#000000">\(\)</span>

<span style="color:#000000">\{</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">begin</span>  <span style="color:#000000">\(</span>  <span style="color:#098658">9600</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">loop</span>  <span style="color:#000000">\(\) \{</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#A31515">"</span>  <span style="color:#A31515">chrValue</span>  <span style="color:#A31515">: "</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">chrValue</span>  <span style="color:#000000">\); </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#A31515">"\\t"</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">println</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">chrValue\,</span>  <span style="color:#00979C">DEC</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#A31515">"</span>  <span style="color:#A31515">intValue</span>  <span style="color:#A31515">: "</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">intValue</span>  <span style="color:#000000">\); </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#A31515">"\\t"</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">intValue\,</span>  <span style="color:#00979C">DEC</span>  <span style="color:#000000">\); </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#A31515">"\\t"</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">intValue\,</span>  <span style="color:#00979C">HEX</span>  <span style="color:#000000">\); </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#A31515">"\\t"</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">intValue\,</span>  <span style="color:#00979C">OCT</span>  <span style="color:#000000">\); </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#A31515">"\\t"</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">println</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">intValue\,</span>  <span style="color:#00979C">BIN</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">print</span>  <span style="color:#000000">\(</span>  <span style="color:#A31515">"</span>  <span style="color:#A31515">floatValue</span>  <span style="color:#A31515">: "</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">println</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">floatValue</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">delay</span>  <span style="color:#000000">\(</span>  <span style="color:#098658">1000</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#000000">chrValue</span>  <span style="color:#000000">\+\+;</span>

<span style="color:#000000">  </span>  <span style="color:#000000">intValue</span>  <span style="color:#000000">\+\+;</span>

<span style="color:#000000">\}</span>

# Communication série : Recevoir des données

Problème : On veut recevoir de l’information d’un ordinateur ou d’un autre appareil série\. Par exemple\, on veut faire réagir l’Arduino

Solution : Utiliser les fonctions  __Serial\.available__  __\(\)__  et  __Serial\.read__  __\(\)__

Serial\.available\(\) retourne vrai lorsqu’il y a de la données de disponible

Serial\.read\(\) lit le prochain octet de disponible

# Communication série : RX

<span style="color:#0000FF">int</span>  <span style="color:#000000">   </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000">=</span>  <span style="color:#098658">0</span>  <span style="color:#000000">; </span>  <span style="color:#727C81">// taux de rafraichissement sauvegardé</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">setup</span>  <span style="color:#000000">\(\)</span>

<span style="color:#000000">\{</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">begin</span>  <span style="color:#000000">\(</span>  <span style="color:#098658">9600</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">pinMode</span>  <span style="color:#000000">\(</span>  <span style="color:#00979C">LED\_BUILTIN</span>  <span style="color:#000000">\, </span>  <span style="color:#00979C">OUTPUT</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">loop</span>  <span style="color:#000000">\(\)</span>

<span style="color:#000000">\{</span>

<span style="color:#000000">  </span>  <span style="color:#0000FF">if</span>  <span style="color:#000000"> \( </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">available</span>  <span style="color:#000000">\(\)\) </span>  <span style="color:#727C81">// Vérifier si l'on a au moins 1 octet de dispo</span>

<span style="color:#000000">  \{</span>

<span style="color:#000000">    </span>  <span style="color:#0000FF">char</span>  <span style="color:#000000"> </span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> = </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">read</span>  <span style="color:#000000">\(\); </span>  <span style="color:#727C81">// Lire le prochain octet</span>

<span style="color:#000000">    </span>  <span style="color:#0000FF">if</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> >= </span>  <span style="color:#A31515">'0'</span>  <span style="color:#000000"> && </span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> <= </span>  <span style="color:#A31515">'9'</span>  <span style="color:#000000">\) </span>  <span style="color:#727C81">// Est\-ce que c'est une valeur entre '0' et '9'</span>

<span style="color:#000000">    \{</span>

<span style="color:#000000">       </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000"> = \(</span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> \- </span>  <span style="color:#A31515">'0'</span>  <span style="color:#000000">\);      </span>  <span style="color:#727C81">// Valeur ASCII converti en numérique</span>

<span style="color:#000000">       </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000"> = </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000"> \* </span>  <span style="color:#098658">100</span>  <span style="color:#000000">; </span>  <span style="color:#727C81">// </span>  <span style="color:#727C81">Interval</span>

<span style="color:#000000">    \}</span>

<span style="color:#000000">  \}</span>

<span style="color:#000000">  </span>  <span style="color:#000000">blink</span>  <span style="color:#000000">\(\);</span>

<span style="color:#000000">\}</span>

<span style="color:#727C81">// Faire clignoter le LED</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#000000">blink</span>  <span style="color:#000000">\(\)</span>

<span style="color:#000000">\{</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">digitalWrite</span>  <span style="color:#000000">\(</span>  <span style="color:#00979C">LED\_BUILTIN</span>  <span style="color:#000000">\,</span>  <span style="color:#00979C">HIGH</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">delay</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">digitalWrite</span>  <span style="color:#000000">\(</span>  <span style="color:#00979C">LED\_BUILTIN</span>  <span style="color:#000000">\,</span>  <span style="color:#00979C">LOW</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">delay</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

__Astuce__ Le caractère ‘0’ vaut 48 en code ASCII\. Pour convertir\, un chiffre en valeur numérique\, il suffit de lui soustraire ‘0’\.

__Rappel__  : Le type ‘char’ est un octet

<span style="color:#0000FF">int</span>  <span style="color:#000000">   </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000">=</span>  <span style="color:#098658">0</span>  <span style="color:#000000">;</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">setup</span>  <span style="color:#000000">\(\)</span>

<span style="color:#000000">\{</span>

<span style="color:#000000">  </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">begin</span>  <span style="color:#000000">\(</span>  <span style="color:#098658">9600</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">pinMode</span>  <span style="color:#000000">\(</span>  <span style="color:#00979C">LED\_BUILTIN</span>  <span style="color:#000000">\, </span>  <span style="color:#00979C">OUTPUT</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">loop</span>  <span style="color:#000000">\(\)</span>

<span style="color:#000000">\{</span>

<span style="color:#000000">  </span>  <span style="color:#0000FF">if</span>  <span style="color:#000000"> \( </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">available</span>  <span style="color:#000000">\(\)\)</span>

<span style="color:#000000">  \{</span>

<span style="color:#000000">    </span>  <span style="color:#0000FF">char</span>  <span style="color:#000000"> </span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> = </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">read</span>  <span style="color:#000000">\(\); </span>

<span style="color:#000000">    </span>  <span style="color:#0000FF">if</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> >= </span>  <span style="color:#A31515">'0'</span>  <span style="color:#000000"> && </span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> <= </span>  <span style="color:#A31515">'9'</span>  <span style="color:#000000">\)</span>

<span style="color:#000000">    \{</span>

<span style="color:#000000">       </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000"> = \(</span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> \- </span>  <span style="color:#A31515">'0'</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">       </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000"> = </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000"> \* </span>  <span style="color:#098658">100</span>  <span style="color:#000000">;</span>

<span style="color:#000000">    \}</span>

<span style="color:#000000">  \}</span>

<span style="color:#000000">  </span>  <span style="color:#000000">blink</span>  <span style="color:#000000">\(\);</span>

<span style="color:#000000">\}</span>

<span style="color:#727C81">// Faire clignoter le LED</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#000000">blink</span>  <span style="color:#000000">\(\)</span>

<span style="color:#000000">\{</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">digitalWrite</span>  <span style="color:#000000">\(</span>  <span style="color:#00979C">LED\_BUILTIN</span>  <span style="color:#000000">\,</span>  <span style="color:#00979C">HIGH</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">delay</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">digitalWrite</span>  <span style="color:#000000">\(</span>  <span style="color:#00979C">LED\_BUILTIN</span>  <span style="color:#000000">\,</span>  <span style="color:#00979C">LOW</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">delay</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

# Communication série : Grand nombre

Si l’on veut lire un nombre plus grand que 9\, il faudra faire une conversion de valeur ainsi qu’une manipulation de tableau

La fonction  __atoi__  __\(string\)__  permet de convertir une string en entier

<span style="color:#0000FF">const</span>  <span style="color:#000000"> </span>  <span style="color:#0000FF">int</span>  <span style="color:#000000"> </span>  <span style="color:#000000">MaxChars</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">5</span>  <span style="color:#000000">; </span>  <span style="color:#727C81">// un </span>  <span style="color:#727C81">int</span>  <span style="color:#727C81"> c'est max 5 car</span>

<span style="color:#0000FF">char</span>  <span style="color:#000000"> </span>  <span style="color:#000000">strValue</span>  <span style="color:#000000">\[MaxChars\+</span>  <span style="color:#098658">1</span>  <span style="color:#000000">\]; </span>  <span style="color:#727C81">// doit être assez gros \+ char </span>  <span style="color:#727C81">null</span>

<span style="color:#0000FF">int</span>  <span style="color:#000000"> index = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">;         </span>  <span style="color:#727C81">// Index sauvegarder les chiffres</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">loop</span>  <span style="color:#000000">\(\)</span>

<span style="color:#000000">\{</span>

<span style="color:#000000">  </span>  <span style="color:#0000FF">if</span>  <span style="color:#000000">\( </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">available</span>  <span style="color:#000000">\(\)\)</span>

<span style="color:#000000">  \{</span>

<span style="color:#000000">    </span>  <span style="color:#0000FF">char</span>  <span style="color:#000000"> </span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> = </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">read</span>  <span style="color:#000000">\(\);</span>

<span style="color:#000000">    </span>  <span style="color:#0000FF">if</span>  <span style="color:#000000">\(index <  </span>  <span style="color:#000000">MaxChars</span>  <span style="color:#000000"> && </span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> >= </span>  <span style="color:#A31515">'0'</span>  <span style="color:#000000"> && </span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> <= </span>  <span style="color:#A31515">'9'</span>  <span style="color:#000000">\)\{</span>

<span style="color:#000000">      </span>  <span style="color:#000000">strValue</span>  <span style="color:#000000">\[index\+\+\] = </span>  <span style="color:#000000">ch</span>  <span style="color:#000000">; </span>  <span style="color:#727C81">// ajouter le ASCII au tableau</span>

<span style="color:#000000">    \}</span>

<span style="color:#000000">    </span>  <span style="color:#0000FF">else</span>

<span style="color:#000000">    \{</span>

<span style="color:#000000">      </span>  <span style="color:#727C81">// Premier car non reconnu ou buffer full</span>

<span style="color:#000000">      </span>  <span style="color:#000000">strValue</span>  <span style="color:#000000">\[index\] = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">; </span>  <span style="color:#727C81">// Terminer le string avec 0 \(</span>  <span style="color:#727C81">null</span>  <span style="color:#727C81">\)</span>

<span style="color:#000000">      </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000"> = </span>  <span style="color:#000000">atoi</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">strValue</span>  <span style="color:#000000">\);  </span>  <span style="color:#727C81">// Utiliser </span>  <span style="color:#727C81">atoi</span>  <span style="color:#727C81"> pour convertir</span>

<span style="color:#000000">      index = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">;</span>

<span style="color:#000000">    \}</span>

<span style="color:#000000">  \}</span>

<span style="color:#000000">  </span>  <span style="color:#000000">blink</span>  <span style="color:#000000">\(\);</span>

<span style="color:#000000">\}</span>

<span style="color:#0000FF">const</span>  <span style="color:#000000"> </span>  <span style="color:#0000FF">int</span>  <span style="color:#000000"> </span>  <span style="color:#000000">MaxChars</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">5</span>  <span style="color:#000000">; </span>  <span style="color:#727C81">// un </span>  <span style="color:#727C81">int</span>  <span style="color:#727C81"> c'est max 5 car</span>

<span style="color:#0000FF">char</span>  <span style="color:#000000"> </span>  <span style="color:#000000">strValue</span>  <span style="color:#000000">\[MaxChars\+</span>  <span style="color:#098658">1</span>  <span style="color:#000000">\]; </span>  <span style="color:#727C81">// doit être assez gros \+ char </span>  <span style="color:#727C81">null</span>

<span style="color:#0000FF">int</span>  <span style="color:#000000"> index = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">;         </span>  <span style="color:#727C81">// Index sauvegarder les chiffres</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">loop</span>  <span style="color:#000000">\(\)</span>

<span style="color:#000000">\{</span>

<span style="color:#000000">  </span>  <span style="color:#0000FF">if</span>  <span style="color:#000000">\( </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">available</span>  <span style="color:#000000">\(\)\)</span>

<span style="color:#000000">  \{</span>

<span style="color:#000000">    </span>  <span style="color:#0000FF">char</span>  <span style="color:#000000"> </span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> = </span>  <span style="color:#E97366"> __Serial__ </span>  <span style="color:#000000">\.</span>  <span style="color:#E97366">read</span>  <span style="color:#000000">\(\);</span>

<span style="color:#000000">    </span>  <span style="color:#0000FF">if</span>  <span style="color:#000000">\(index <  </span>  <span style="color:#000000">MaxChars</span>  <span style="color:#000000"> && </span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> >= </span>  <span style="color:#A31515">'0'</span>  <span style="color:#000000"> && </span>  <span style="color:#000000">ch</span>  <span style="color:#000000"> <= </span>  <span style="color:#A31515">'9'</span>  <span style="color:#000000">\)\{</span>

<span style="color:#000000">      </span>  <span style="color:#000000">strValue</span>  <span style="color:#000000">\[index\+\+\] = </span>  <span style="color:#000000">ch</span>  <span style="color:#000000">; </span>  <span style="color:#727C81">// ajouter le ASCII au tableau</span>

<span style="color:#000000">    \}</span>

<span style="color:#000000">    </span>  <span style="color:#0000FF">else</span>

<span style="color:#000000">    \{</span>

<span style="color:#000000">      </span>  <span style="color:#727C81">// Premier car non reconnu ou buffer full</span>

<span style="color:#000000">      </span>  <span style="color:#000000">strValue</span>  <span style="color:#000000">\[index\] = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">; </span>  <span style="color:#727C81">// Terminer le string avec 0 \(</span>  <span style="color:#727C81">null</span>  <span style="color:#727C81">\)</span>

<span style="color:#000000">      </span>  <span style="color:#000000">blinkRate</span>  <span style="color:#000000"> = </span>  <span style="color:#000000">atoi</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">strValue</span>  <span style="color:#000000">\);  </span>  <span style="color:#727C81">// Utiliser </span>  <span style="color:#727C81">atoi</span>  <span style="color:#727C81"> pour convertir</span>

<span style="color:#000000">      index = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">;</span>

<span style="color:#000000">    \}</span>

<span style="color:#000000">  \}</span>

<span style="color:#000000">  </span>  <span style="color:#000000">blink</span>  <span style="color:#000000">\(\);</span>

<span style="color:#000000">\}</span>

<span style="color:#727C81">// ATTENTION\! J’ai omis les fonctions setup et </span>  <span style="color:#727C81">blink</span>

# digitalRead()

Lire de l’information d’un bouton

Nous avons vu digitalWrite\(\) pour activer/désactiver une broche sur l’Arduino

Il y a aussi la fonction complémentaire  __digitalRead__  __\(\)__  qui permet de lire l’état d’une broche

Par exemple\, si l’on veut lire l’état d’un bouton s’il est appuyé ou non

Dans les exemples qui suivront\, il faudra faire un branchement sur la plaquette d’expérimentation

# Brancher un bouton

* Reproduire le branchement ci\-contre
* Matériel
  * Bouton poussoir
  * Résistance de 4\.7k ohm
  * 5 fils

# Lire un bouton : Code

<span style="color:#0000FF">const</span>  <span style="color:#000000"> </span>  <span style="color:#0000FF">int</span>  <span style="color:#000000"> </span>  <span style="color:#000000">buttonPin</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">10</span>  <span style="color:#000000">;</span>  <span style="color:#0000FF">int</span>  <span style="color:#000000"> </span>  <span style="color:#000000">buttonState</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">; </span>  <span style="color:#727C81">// Variable pour l'état du bouton</span>

<span style="color:#0000FF">int</span>  <span style="color:#000000"> </span>  <span style="color:#000000">ledState</span>  <span style="color:#000000"> = </span>  <span style="color:#098658">0</span>  <span style="color:#000000">;</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">setup</span>  <span style="color:#000000">\(\) \{</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">pinMode</span>  <span style="color:#000000">\(</span>  <span style="color:#00979C">LED\_BUILTIN</span>  <span style="color:#000000">\, </span>  <span style="color:#00979C">OUTPUT</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">pinMode</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">buttonPin</span>  <span style="color:#000000">\, </span>  <span style="color:#00979C">INPUT</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

<span style="color:#0000FF">void</span>  <span style="color:#000000"> </span>  <span style="color:#5E6D03">loop</span>  <span style="color:#000000">\(\) \{</span>

<span style="color:#000000">  </span>  <span style="color:#727C81">// Lire l'état du bouton</span>

<span style="color:#000000">  </span>  <span style="color:#000000">buttonState</span>  <span style="color:#000000"> = </span>  <span style="color:#E97366">digitalRead</span>  <span style="color:#000000">\(</span>  <span style="color:#000000">buttonPin</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">  </span>  <span style="color:#000000">ledState</span>  <span style="color:#000000"> = </span>  <span style="color:#000000">buttonState</span>  <span style="color:#000000">;</span>

<span style="color:#000000">  </span>  <span style="color:#E97366">digitalWrite</span>  <span style="color:#000000">\(</span>  <span style="color:#00979C">LED\_BUILTIN</span>  <span style="color:#000000">\, </span>  <span style="color:#000000">ledState</span>  <span style="color:#000000">\);</span>

<span style="color:#000000">\}</span>

# Utiliser la platine d’expérimentation

Une platine d’expérimentation  _\(_  _breadboard_  _\) _ est une plaque qui possèdent plusieurs trous reliés entre eux

On utilise cette plaque pour faire des montages temporaires

Elle est généralement composée de deux \(2\) sections de cinq \(5\) points linéaires chacune

Chaque section peut être alimentée de manière indépendante

Généralement\, on retrouve deux rails pour l’alimentation de chaque côté

![](img%5C1SX%20-%20Cours%2001%20-%20UART%2C%20D%C3%A9lais1.png)

![](img%5C1SX%20-%20Cours%2001%20-%20UART%2C%20D%C3%A9lais2.png)

![](img%5C1SX%20-%20Cours%2001%20-%20UART%2C%20D%C3%A9lais3.png)

![](img%5C1SX%20-%20Cours%2001%20-%20UART%2C%20D%C3%A9lais4.jpg)

![](img%5C1SX%20-%20Cours%2001%20-%20UART%2C%20D%C3%A9lais5.png)

On utilise le  _breadboard_  en branchant des connecteurs mâles

Généralement\, on branche les rails d’alimentation avec l’Arduino

On alimente les éléments directement à partir du rail

__Attention\!\! Il ne faut pas inverser les polarités\, car il y a de forte chance que l’on endommage définitivement l’appareil__

# Composants dans le kit

Veuillez accéder ce document [Guide introduction Arduino\.docx](https://cshawi-my.sharepoint.com/:w:/g/personal/nbourre_cshawi_ca/EaBev8wOPa1PssVnkKl8PHIBLa77wqiA_3q_qOZYlsCGPw?e=bp4uy5)

# Références

[Dépôt de code du cours](https://github.com/nbourre/1SX_robotique)

[Labo](https://www.cs.uregina.ca/Links/class-info/207/Online/Lab3/)

[Livre ](https://www.oreilly.com/library/view/arduino-cookbook/9781449399368/ch04.html)[O’Reilly](https://www.oreilly.com/library/view/arduino-cookbook/9781449399368/ch04.html)[ : Chapitre 4](https://www.oreilly.com/library/view/arduino-cookbook/9781449399368/ch04.html)

