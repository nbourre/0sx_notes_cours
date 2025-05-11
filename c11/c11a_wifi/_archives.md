

### Code pour configurer le wifi
Pour utiliser le ESP-01, il faudra utiliser la librairie "WifiEsp.h" qui permet de communiquer avec le module.

### Initialisation du module
```cpp

#include <WiFiEsp.h>

// Mettre à 1 si le fichier arduino_secrets.h est présent
#define HAS_SECRETS 0

#if HAS_SECRETS
#include "arduino_secrets.h"
/////// SVP par soucis de sécurité, mettez vos informations dans le fichier arduino_secrets.h

// Nom et mot de passe du réseau wifi
const char ssid[] = SECRET_SSID;
const char pass[] = SECRET_PASS;

#else
const char ssid[] = "TechniquesInformatique-Etudiant";  // your network SSID (name)
const char pass[] = "shawi123";                         // your network password (use for WPA, or use as key for WEP)
#endif

#define AT_BAUD_RATE 115200

int blinkRate = 500;

int status = WL_IDLE_STATUS;     // Status du module wifi

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(AT_BAUD_RATE);
  while (!Serial)
    ;

  
  // Démarre la communication série avec le module ESP (connecté à Serial1)
  Serial1.begin(AT_BAUD_RATE);

  // Initialise la bibliothèque WiFiEspAT avec ce port série
  WiFi.init(&Serial1);           

  // Cela peut prendre un certain temps pour que le module wifi soit prêt
  // Voir 1 minute dans la documentation
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println();
    Serial.println("La communication avec le module WiFi a échoué!");

    // Clignote 2.1 pour indiquer cette erreur
    errorState(2, 1);
  }

  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);

  // Tentative de connexion au Wifi
  while (status != WL_CONNECTED) {
    Serial.print(".");

    // Connecter au ssid
    status = WiFi.begin(ssid, pass);
  }

  Serial.println("Vous êtes connecté au réseau");
  printWifiStatus();
  Serial.println();


}

void loop() {
  static unsigned long lastBlink = 0;
  if (millis() - lastBlink >= blinkRate) {
    lastBlink = millis();
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
  }
}
```

#### Fonctions d'aide
Code pour les fonctions supplémentaires `printWifiStatus` et `errorState`.

<details><summary>Ouvrir pour voir le code</summary>

```cpp
void printWifiStatus() {

  // imprime le SSID du réseau auquel vous êtes connecté:
  char ssid[33];
  WiFi.SSID(ssid);
  Serial.print("SSID: ");
  Serial.println(ssid);

  // imprime le BSSID du réseau auquel vous êtes connecté:
  uint8_t bssid[6];
  WiFi.BSSID(bssid);
  Serial.print("BSSID: ");
  printMacAddress(bssid);

  uint8_t mac[6];
  WiFi.macAddress(mac);
  Serial.print("MAC: ");
  printMacAddress(mac);

  // imprime l'adresse IP de votre carte:
  IPAddress ip = WiFi.localIP();
  Serial.print("Adresse IP: ");
  Serial.println(ip);

  // imprime la force du signal reçu:
  long rssi = WiFi.RSSI();
  Serial.print("force du signal (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}

// Imprime l'adresse MAC
void printMacAddress(byte mac[]) {
  for (int i = 5; i >= 0; i--) {
    if (mac[i] < 16) {
      Serial.print("0");
    }
    Serial.print(mac[i], HEX);
    if (i > 0) {
      Serial.print(":");
    }
  }
  Serial.println();
}

// Fonction affichant un état d'erreur avec 2 paramètres pour code d'erreur
// Cela permet de clignoter la DEL avec un code pour faciliter le débogage pour
// l'utilisateur. On ne sort jamais de cette fonction.
// Le programmeur doit définir la signification des codes d'erreur.
//
// Exemple de code d'erreur:
//   errorState (2, 3) <-- (clignote 2 fois, pause, clignote 3 fois)
void errorState(int codeA, int codeB) {
  const int rate = 100;
  const int pauseBetween = 500;
  const int pauseAfter = 1000;

  // On ne sort jamais de cette fonction
  while (true) {
    for (int i = 0; i < codeA; i++) {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(rate);
      digitalWrite(LED_BUILTIN, LOW);
      delay(rate);
    }
    delay(pauseBetween);
    for (int i = 0; i < codeB; i++) {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(rate);
      digitalWrite(LED_BUILTIN, LOW);
      delay(rate);
    }
    delay(pauseAfter);

    Serial.print("Erreur : ");
    Serial.print(codeA);
    Serial.print(".");
    Serial.println(codeB);
  }
}
```
</details>

---

### Exemple de code pour le ESP-01

```cpp
/*
 Exemple WiFiEsp : Serveur Web

 Un serveur Web simple qui affiche la valeur des entrées analogiques
 via une page web en utilisant un module ESP8266.
 Ce sketch affichera l'adresse IP de votre module ESP8266 (une fois connecté)
 dans le moniteur série. Vous pourrez ensuite ouvrir cette adresse dans un navigateur
 pour afficher la page web.
 La page web sera automatiquement actualisée toutes les 20 secondes.

 Pour plus de détails, voir : http://yaab-arduino.blogspot.com/p/wifiesp.html
*/

#include "WiFiEsp.h"

#define AT_BAUD_RATE 115200

const char ssid[] = "TechniquesInformatique-Etudiant";  // SSID (nom) de votre réseau
const char pass[] = "shawi123";                         // Mot de passe de votre réseau (WPA ou clé WEP)
int status = WL_IDLE_STATUS;     // État de la connexion WiFi
int reqCount = 0;                // Nombre de requêtes reçues

WiFiEspServer server(80);

void setup()
{
  // Initialiser la liaison série pour le débogage
  Serial.begin(AT_BAUD_RATE);
  // Initialiser la liaison série pour le module ESP
  Serial1.begin(AT_BAUD_RATE);
  // Initialiser le module ESP
  WiFi.init(&Serial1);

  // Vérifier la présence du shield
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("Module WiFi non détecté");
    while (true);
  }

  // Tentative de connexion au réseau WiFi
  while (status != WL_CONNECTED) {
    Serial.print("Tentative de connexion au réseau WPA : ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
  }

  Serial.println("Connecté au réseau");
  printWifiStatus();

  // Démarrer le serveur web sur le port 80
  server.begin();
}

void loop()
{
  // Écouter les clients entrants
  WiFiEspClient client = server.available();
  if (client) {
    Serial.println("Nouveau client");
    bool currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);

        if (c == '\n' && currentLineIsBlank) {
          Serial.println("Envoi de la réponse");

          client.print(
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Connection: close\r\n"
            "\r\n");
          client.print("<!DOCTYPE HTML>\r\n");
          client.print("<html>\r\n");
          client.println("<head>");
          // actualisez la page automatiquement toutes les 5 secondes
          client.println("<meta http-equiv=\"refresh\" content=\"5\">");
          client.println("<meta charset=\"UTF-8\">");
          client.println("</head>");
          client.println("<body>");
          client.print("<h1>Bonjour le monde !</h1>\r\n");
          client.print("Requêtes reçues : ");
          client.print(++reqCount);
          client.print("<br>\r\n");
          
          // afficher la valeur des broches d'entrée analogique
          for (int analogChannel = 0; analogChannel < 4; analogChannel++) {
            int sensorReading = analogRead(analogChannel);
            client.print("Entree analogique ");
            client.print(analogChannel);
            client.print(" est ");
            client.print(sensorReading);
            client.println("<br />");
          }
          client.println("</body>");
          client.print("</html>\r\n");
          break;
        }
        if (c == '\n') {
          currentLineIsBlank = true;
        }
        else if (c != '\r') {
          currentLineIsBlank = false;
        }
      }
    }
    delay(10);
    client.stop();
    Serial.println("Client déconnecté");
  }
}

void printWifiStatus()
{
  Serial.print("SSID : ");
  Serial.println(WiFi.SSID());

  IPAddress ip = WiFi.localIP();
  Serial.print("Adresse IP : ");
  Serial.println(ip);

  Serial.println();
  Serial.print("Pour voir cette page en action, ouvrez un navigateur à l'adresse http://");
  Serial.println(ip);
  Serial.println();
}

```
