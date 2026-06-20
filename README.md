# XERON-9 – Expedition auf dem Eisplaneten

## Beschreibung

XERON-9 ist ein textbasiertes Python-Spiel, in dem der Spieler einen Forschungsroboter über einen unbekannten Eisplaneten steuert.

Das Ziel der Mission ist es, das seltene Energie-Erz **AETHERIUM** zu finden. Dabei muss der Roboter Energie verwalten, Hindernissen ausweichen, Eisstürme überstehen und die Umgebung mit Scans erkunden.

Die gesamte Simulation läuft im Terminal ab.

## Starten des Programms

1. Stelle sicher, dass Python 3.11 oder neuer installiert ist.
2. Öffne ein Terminal im Projektordner.
3. Starte das Spiel mit:

```bash
python main.py
```

## Spielablauf

Nach dem Start kann der Spieler:

* einen Namen für den Roboter wählen,
* einen Schwierigkeitsgrad auswählen,
* den Roboter über die Karte bewegen,
* die Umgebung scannen,
* Energie sammeln und Gefahren vermeiden.

Die Position des Roboters wird mit den Koordinaten x und y verwaltet.

## Steuerung

| Befehl | Funktion           |
| ------ | ------------------ |
| N      | Nach Norden fahren |
| S      | Nach Süden fahren  |
| O      | Nach Osten fahren  |
| W      | Nach Westen fahren |
| scan   | Umgebung scannen   |
| x      | Mission abbrechen  |

## Weltelemente

* **Kristalle**: +40 Energie
* **Datenpunkte**: +20 Energie und +3 Scans
* **Hindernisse**: −10 Energie
* **Eisstürme**: −20 Energie
* **Gletscherspalten**: −50 Energie oder Missionsende

## Missionsende

Die Mission endet, wenn:

* das AETHERIUM-Erz gefunden wurde,
* die Energie auf 0 fällt,
* der Spieler die Mission abbricht.

Nach dem Ende wird ein Missionsbericht ausgegeben und die Mission kann erneut gestartet werden.

## Verwendete Module

* random
* time

Es werden ausschließlich Module aus der Python-Standardbibliothek verwendet.
