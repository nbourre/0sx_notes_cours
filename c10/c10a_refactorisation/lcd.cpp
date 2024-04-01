void lcdTask() {
  static unsigned long lastUpdate = 0;
  static unsigned long lastMsgChange = 0;

  const int lcdRefreshRate = 250; // Temps entre chaque rafraîchissement de l'affichage
  const int nextStateRate = 3000; // Temps entre chaque changement d'état

  if (currentTime - lastUpdate < lcdRefreshRate){
    return; // On sort si le temps n'est pas écoulé
  }

  lastUpdate = currentTime;

  switch (lcdState) {
    case ECLAIRAGE:
      lcdEclairage();
      // On passe au prochain état
      if (changeState) {
        lcdState = ALARME;
        changeState = false;
      }
      break;
    case ALARME:
      lcdAlarme();
      // On passe au prochain état
      if (changeState) {
        lcdState = GARAGE;
        changeState = false;
      }
      break;
    case GARAGE:
      lcdGarage();
      // TODO
      break;
    case AC:
      lcdAC();
      // TODO
      break;
    case DATA_RECEIVED:
      lcdDataReceived();
      // TODO
      break;
    default:
      break;
  }

  if (currentTime - lastMsgChange > nextStateRate) {
    changeState = true;
    lastMsgChange = currentTime;
  }
}

void lcdEclairage() {
  static int luminosity = 0;
  static int threshold = 0;

  luminosity = eclairage.getLuminosity();
  threshold = eclairage.getThreshold();

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Luminosite: ");
  lcd.print(luminosity);
  lcd.print("%");
  lcd.setCursor(0, 1);
  lcd.print("Etat: ");
  if (luminosity < threshold) {
    lcd.print("Allume");
  } else {
    lcd.print("Eteint");
  }
}

void lcdAlarme() {
  // Ligne 1 : Afficher la distance
  // Ligne 2 : Afficher l'état de l'alarme
}

void lcdGarage() {
  // Ligne 1 : Afficher l'état de la porte de garage
}

void lcdAC() {
  // Ligne 1 : Afficher l'état de la climatisation
}

void lcdDataReceived() {
  // Ligne 1 : Afficher "To be defined"
}