# garten-bewaesserung
System für den Raspberry Pi für eine Bewässerungsanlage des Gartenhauses.

## Aufbau

### Frontend
Webbasierte Anwendung (vermutlich Angular)
- geschützt über Passwort (htaccess)
- übersichtliche Darstellung von aktuellem Status
- manuelles schalten der Anlage, durch erstellen einer neuen Konfigurationsdatei (Menge und Dauer manuell festlegen)
- Notfall-Aus Button
- schlankes Design mobil-optimiert
- Benachrichtigung von Statusänderungen und wenn z.B. Regentonne leer sein könnte (nach x Tagen)

### Backend
Flask Server
- läuft auf Raspberry PI
- liest Konfigurationsdaten aus einer JSON aus
- nimmt aktuelle Wetterdaten aus einer API um Bewässerungsmenge in der Konfigurationsdatei anzupassen

  optional:
  - dokumentiert Werte in einer NoDB für eine Auswertung
