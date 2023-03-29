/*
Serveur Web WiFi

Un simple serveur web qui affiche la valeur des broches d'entrée analogique.

Créé le 13 Juillet 2010
par dlf (Metodo2 srl)
modifié le 31 mai 2012
par Tom Igoe
modifié en juillet 2019 pour la bibliothèque WiFiEspAT
par Juraj Andrassy https://github.com/jandrassy
*/

#include <WiFiEspAT.h>

// Emuler Serial1 sur les broches 6/7 si non présent
#if defined(ARDUINO_ARCH_AVR) && !defined(HAVE_HWSERIAL1)
#include <SoftwareSerial.h>
SoftwareSerial Serial1(6, 7);  // RX, TX
#define AT_BAUD_RATE 9600
#else
#define AT_BAUD_RATE 115200
#endif

WiFiServer server(80);

void setup() {

  Serial.begin(115200);
  while (!Serial)
    ;

  Serial1.begin(AT_BAUD_RATE);
  WiFi.init(Serial1);

  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("La communication avec le module WiFi a échoué !");
    // ne pas continuer
    while (true)
      ;
  }

  // En attendant la connexion au réseau Wifi configuré avec le sketch SetupWiFiConnection
  Serial.println("En attente de connexion au WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print('.');
  }
  Serial.println();

  server.begin();

  IPAddress ip = WiFi.localIP();
  Serial.println();
  Serial.println("Connecté au réseau WiFi.");
  Serial.print("Pour accéder au serveur, entrez \"http://");
  Serial.print(ip);
  Serial.println("/\" dans un navigateur web.");
}

void loop() {

  WiFiClient client = server.available();
  if (client) {
    IPAddress ip = client.remoteIP();
    Serial.print("nouveau client ");
    Serial.println(ip);

    while (client.connected()) {
      if (client.available()) {
        String line = client.readStringUntil('\n');
        line.trim();
        Serial.println(line);

        // si vous avez atteint la fin de l'en-tête HTTP (la ligne est vide),
        // la demande HTTP est terminée, vous pouvez donc envoyer une réponse
        if (line.length() == 0) {
          // envoyer un en-tête de réponse HTTP standard
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");  // la connexion sera fermée après la fin de la réponse
          client.println("Refresh: 5");         // actualisez la page automatiquement toutes les 5 secondes
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          // afficher la valeur des broches d'entrée analogique
          for (int analogChannel = 0; analogChannel < 4; analogChannel++) {
            int sensorReading = analogRead(analogChannel);
            client.print("Entrée analogique ");
            client.print(analogChannel);
            client.print(" est ");
            client.print(sensorReading);
            client.println("<br />");
          }
          client.println("</html>");
          client.flush();
          break;
        }
      }
    }

    // fermer la connexion:
    client.stop();
    Serial.println("client déconnecté");
  }
}
