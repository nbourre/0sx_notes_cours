# Retour sur le port série <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [ESP8266](#esp8266)
  - [Les commandes AT](#les-commandes-at)
- [Le shield ESP8266](#le-shield-esp8266)
  - [Branchement](#branchement)
  - [Exemple de code - Serveur Web](#exemple-de-code---serveur-web)
  - [Exemple - Allumer une DEL](#exemple---allumer-une-del)
- [Références](#références)


# Introduction
Nous avons vu les notions de lecture pour le port série dans le cours suivant : [Lecture de données à partir du port série](../c07/c07b_serial_read/C07b_lecture_serie.md).

Dans ce cours, nous allons voir comment communiquer avec un Arduino Mega via le port série en utilisant un shield qui possède un microontrôleur ESP8266.

![Alt text](esp8266-wifi-shield-desc2.jpg)

# ESP8266
Avant de débuter avec le shield, nous devons en connaître un peu plus sur l'ESP8266.

L'ESP8266 est un microcontrôleur qui peut être programmé en langage Arduino. Si vous êtes un apprenant qui commence à programmer en C, vous pourriez être intéressé par cette petite puce car elle est facile à utiliser et offre une grande variété de fonctionnalités.

![Différents models d'ESP](ModelosESP.avif)

Cette image montre la variété de modèles d'ESP disponibles sur le marché. Vous pouvez trouver des modèles avec des caractéristiques différentes, mais tous sont basés sur le même microcontrôleur ESP8266.

L'ESP8266 est un module peu coûteux d'où sa popularité. Il est également très facile à utiliser et à programmer. Il est également puissant et peut être utilisé pour créer des projets complexes.

L'ESP8266 est principalement utilisé pour se connecter à Internet et interagir avec des services en ligne. Vous pouvez créer des projets tels que des capteurs connectés, des systèmes d'automatisation domestique ou même des robots qui communiquent avec un serveur distant. Il peut également être utilisé pour contrôler des appareils électroniques tels que des lumières, des ventilateurs et des moteurs.

L'ESP8266 est équipé d'un processeur 32 bits à faible consommation d'énergie et dispose de 80 à 160 Ko de mémoire flash pour le stockage de programmes. Il prend en charge le Wi-Fi et peut être connecté à un réseau local ou à un point d'accès Wi-Fi pour se connecter à Internet. Il est également compatible avec de nombreuses bibliothèques et outils de développement, ce qui facilite la création de projets complexes.

Pour commencer à programmer l'ESP8266, vous devez disposer d'un module ESP8266 et d'un câble USB pour le connecter à votre ordinateur. Vous devez également télécharger et installer l'environnement Arduino. Une fois cela fait, vous pouvez ouvrir l'interface Arduino, sélectionner votre carte ESP8266 et commencer à écrire votre code.

En résumé, l'ESP8266 est un microcontrôleur puissant et facile à utiliser qui peut être programmé, entre autres, en langage C/C++. Il est équipé d'un processeur 32 bits, de Wi-Fi et d'une grande quantité de mémoire flash pour stocker des programmes. En utilisant l'environnement Arduino, vous pouvez facilement commencer à programmer l'ESP8266 et créer des projets connectés à Internet passionnants.

---

## Les commandes AT
Si le module ESP8266 est programmé avec le firmware AT, il peut être contrôlé par des commandes AT. Ainsi, il ne sera pas nécessaire de programmer directement le module ESP8266 pour l'utiliser. Il suffit de lui envoyer des commandes AT via le port série.

Les commandes AT sont des commandes qui permettent de contrôler le module ESP8266. Ces commandes sont envoyées au module ESP8266 via le port série. Le module ESP8266 répondra à ces commandes avec des données ou des informations.

Elles permettent, entre autres, de configurer les informations de connexion.

Dans notre cas, nous utilisons un librairie qui cachera ces commandes AT. Ce qui nous permettra de nous concentrer sur le code de notre application.

---

# Le shield ESP8266
Le module ESP8266 WiFi Shield est un module UART-WiFi ultra-basse consommation. Il a des dimensions excellentes et une technologie ULP par rapport à d'autres modules similaires. Le module est spécialement conçu pour les appareils mobiles et l'Internet des objets (IoT).

Ce Shield WiFi est basé sur ESP-12F, qui est la nouvelle version de l'ESP-12 avec la puce Wifi ESP8266. Avec ce Shield, vous pouvez facilement connecter votre Arduino au réseau et contrôler votre appareil de n'importe où. La communication se fait via une interface UART et le contrôle se fait par commande AT.

- Supporte la norme sans fil 802.11 b/g/n
- Supporte les trois modes de travail STA/AP/STA + AP
- Pile de protocoles TCP/IP intégrée, et supporte plusieurs connexions TCP Client
- Supporte une riche série de commandes AT pour Socket

## Branchement
La documentation en ligne montre un branchement du shield sur un Arduino Uno. Pour le branchement sur un Arduino Mega, il faut désactiver les cavaliers commen montré sur l'image ci-dessous.

Ensuite, il faut brancher une des broches ESP_RX sur la broche TX1 du Mega et la broche ESP_TX sur la broche RX1 du Mega.

![Branchement](https://raw.githubusercontent.com/nbourre/documentations_generiques/cb843f0d7438001efba129667d5b35b14bcb41a5/embedded/esp8266/makerfabs_wifi_mega.jpg)

Dans le code, il faudra alors utiliser les fonctions `Serial1` pour échanger avec le module.

## Exemple de code - Serveur Web

Ce code est un exemple d'utilisation de la bibliothèque `WiFiEsp` pour créer un serveur web à l'aide d'un module Wifi ESP8266 branché sur le port série.

```cpp
/*
Exemple WiFiEsp : Serveur Web

Un simple serveur web qui affiche la valeur des broches d'entrée analogiques
via une page web en utilisant un module ESP8266.
Ce croquis imprimera l'adresse IP de votre module ESP8266 (une fois connecté)
sur le moniteur série. À partir de là, vous pouvez ouvrir cette adresse dans un navigateur Web
pour afficher la page Web.
La page Web sera automatiquement actualisée toutes les 20 secondes.

Pour plus de détails, voir: http://yaab-arduino.blogspot.com/p/wifiesp.html
*/

/****************************************/
// Créer un fichier "arduino_secrets.h"
// Ajouter les lignes suivantes
// #define SSID_NAME "nomReseau"
// #define PASS "motDePasse"
#include "arduino_secrets.h"
/****************************************/

#include "WiFiEsp.h"

char ssid[] = SSID_NAME;            // votre nom de réseau SSID
char pass[] = PASS;        // votre mot de passe de réseau
int status = WL_IDLE_STATUS;     // statut de la radio Wifi
int reqCount = 0;                // nombre de requêtes reçues

WiFiEspServer server(80);

void setup() {
  // initialise le port série pour le débogage
  Serial.begin(115200);
  // initialise le port série pour le module ESP
  Serial1.begin(115200); // Dépend de la configuration du module
  // initialise le module ESP
  WiFi.init(&Serial1);

  // vérifie la présence du module
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("Shield WiFi non présent");
    // ne pas continuer
    while (true)
      ;
  }

  // tentative de connexion au réseau WiFi
  while (status != WL_CONNECTED) {
    Serial.print("Tentative de connexion à WPA SSID : ");
    Serial.println(ssid);
    // connexion au réseau WPA/WPA2
    status = WiFi.begin(ssid, pass);
  }

  Serial.println("Vous êtes connecté au réseau");
  printWifiStatus();

  // démarre le serveur web sur le port 80
  server.begin();
}

void loop() {
  // attend les clients entrants
  WiFiEspClient client = server.available();
  if (client) {
    Serial.println("Nouveau client");
    // une requête http se termine par une ligne vide
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        // si vous avez atteint la fin de la ligne (reçu un caractère de nouvelle ligne)
        // et la ligne est vide, la requête http est terminée,
        // donc vous pouvez envoyer une réponse
        if (c == '\n' && currentLineIsBlank) {
          Serial.println("Envoi de la réponse");

          // envoie un en-tête de réponse http standard
          // utilisez \r\n au lieu de nombreuses instructions println pour accélérer l'envoi de données
          client.print(
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Connection: close\r\n"  // la connexion sera fermée après l'achèvement de la réponse
            "Refresh: 20\r\n"        // actualiser la page automatiquement toutes les 20 secondes
            "\r\n");
          client.print("<!DOCTYPE HTML>\r\n");
          client.print("<html>\r\n");
          client.print("<h1>Bonjour le monde !</h1>\r\n");
          client.print("Requêtes reçues : ");
          client.print(++reqCount);
          client.print("<br>\r\n");
          client.print("Entrée analogique A0 : ");
          client.print(analogRead(0));
          client.print("<br>\r\n");
          client.print("</html>\r\n");
          break;
        }
        if (c == '\n') {
          // vous commencez une nouvelle ligne
          currentLineIsBlank = true;
        } else if (c != '\r') {
          // vous avez reçu un caractère sur la ligne actuelle
          currentLineIsBlank = false;
        }
      }
      // donne au navigateur Web le temps de recevoir les données
      delay(10);

      // ferme la connexion :
      client.stop();
      Serial.println("Client déconnecté");
    }
  }
}

void printWifiStatus()
{
    // affiche le SSID du réseau auquel vous êtes connecté
    Serial.print("SSID : ");
    Serial.println(WiFi.SSID());

    // affiche l'adresse IP de votre module WiFi
    IPAddress ip = WiFi.localIP();
    Serial.print("Adresse IP : ");
    Serial.println(ip);

    // affiche où aller dans le navigateur
    Serial.println();
    Serial.print("Pour voir cette page en action, ouvrez un navigateur à l'adresse http://");
    Serial.println(ip);
    Serial.println();
}

```

## Exemple - Allumer une DEL

---

# Références
- [Site officiel : ESP8266](https://www.espressif.com/en/products/socs/esp8266)
- [Documentation libraire WiFiEsp](https://github.com/bportaluri/WiFiEsp)