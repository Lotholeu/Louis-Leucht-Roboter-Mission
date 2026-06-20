import random 
import time



def reset_game():
    global x, y, Scans, counterScan, counterDrive, sx, sy, zielx, ziely, Energie
    global weg, hindernisse, kristall, eissturm, data, gletscherspalte
    global sichtbare_felder, game_status
    global name, menu_an

    name = None
    menu_an = True
    zielx = None
    ziely = None
    weg = []
    game_status = False #Status des Spiels
    hindernisse = [] # Hindernisse
    kristall = [] #Kristalle
    eissturm = [] #Eisstürme
    data = [] #Datenpunkte
    gletscherspalte = [] #Gletscherspalten
    Energie = None #Energie von {name}
    sx = None #Größe des Spielfelds in x-Richtung
    sy = None #Größe des Spielfelds in y-Richtung
    Scans = 3 #Anzahl der Scans, die {name} durchführen kann
    counterScan = 0
    counterDrive = 0 #Zähler für die Anzahl der Fahrten
    x = 0 #Position von {name} in x
    y = 0 #Position von {name} in y
    sichtbare_felder = set()

name = None
menu_an = True
zielx = None
ziely = None
weg = []
game_status = False #Status des Spiels
hindernisse = [] # Hindernisse
kristall = [] #Kristalle
eissturm = [] #Eisstürme
data = [] #Datenpunkte
gletscherspalte = [] #Gletscherspalten
Energie = None #Energie von {name}
sx = None #Größe des Spielfelds in x-Richtung
sy = None #Größe des Spielfelds in y-Richtung
Scans = 3 #Anzahl der Scans, die {name} durchführen kanncounterScan = 0
counterDrive = 0 #Zähler für die Anzahl der Fahrten
counterScan = 0 
x = 0 #Position von {name} in x
y = 0 #Position von {name} in y
sichtbare_felder = set()
sichtbare_felder.add((x, y))


#Die Einleitung des Spiels, die die Geschichte und das Ziel der Mission erklärt
def start():
    print(f"""
==================================================
                    XERON-9
==================================================

Tiefer im Universum als jemals zuvor liegt der
unerforschte Eisplanet XERON-9.

Noch nie hat ein Mensch diesen Planeten betreten.

Die einzige Hoffnung der Mission:
Der Forschungsroboter {name} —
das am weitesten entfernte Objekt,
das die Menschheit jemals erschaffen hat.

Tief unter dem ewigen Eis soll sich ein seltenes
Energie-Erz namens AETHERIUM befinden.

Die Aufgabe von {name}:
Finde das Erz und sichere die Zukunft der Menschheit.

Doch der Planet ist gefährlich.

Eisstürme, Gletscherspalten und unbekannte Hindernisse
stellen sich dem Roboter in den Weg.

Um zu überleben, muss {name} Energie-Kristalle sammeln
und sich durch die eisige Wildnis von XERON-9 kämpfen.

==================================================
             MISSION WIRD GESTARTET
==================================================
""")
def end_fuel():
    global menu_an
    
    print(f"""
==========

```
          MISSIONSBERICHT
```

==================================================

Roboter: {name}

Startparameter:

* Schwierigkeitsgrad: {sx * 2 + 1} x {sy * 2 + 1} 
* Startenergie: {"100" if sx == 4 else "200" if sx == 10 else "300"}
* Startposition: (0, 0)

Endposition:

* ({x}, {y})

Missionsdaten:

* Durchgeführte Fahrten: {counterDrive}
* Durchgeführte Scans: {counterScan}
* Verbleibende Energie: {Energie}

Besuchte Weltelemente:

* Hindernisse, Kristalle, Datenpunkte,
  Eisstürme und Gletscherspalten konnten
  während der Expedition entdeckt werden.

Grund für Missionsende:

* Energie aufgebraucht

Endergebnis:

* Mission gescheitert

==================================================
ENDE DES MISSIONSBERICHTS
=========================

""")

    end = input("Willst du die Mission erneut versuchen? (j/n): ")
    if end.lower() == "j":
        reset_game()
        menu_an = True
    else:
        menu_an = False
        print("Vielen Dank, dass du die Mission geleitet hast.")
def ziel_erreicht():
    global menu_an
    print(f"""

```
           MISSIONSBERICHT
```

==================================================

Mission: XERON-9
Status: ERFOLGREICH

Der Forschungsroboter {name} hat das Ziel der
Expedition erreicht und das seltene AETHERIUM-Erz
auf dem Eisplaneten XERON-9 entdeckt.

------------------ STARTDATEN ------------------

Roboter: {name}
Startposition: (0, 0)
Spielfeldgröße: {sx * 2 + 1} x {sy * 2 + 1}
Startenergie: {"100" if sx == 4 else "200" if sx == 10 else "300"}

---------------- MISSIONSVERLAUF ----------------

Gefahrenreiche Eislandschaften wurden durchquert.
Mehrere Hindernisse, Eisstürme und Gletscherspalten
konnten überwunden werden.

Durchgeführte Fahrten: {counterDrive}
Durchgeführte Scans: {counterScan}

---------------- ENDERGEBNIS ----------------

Endposition: ({x}, {y})
Verbleibende Energie: {Energie}

Grund für Missionsende:
Das AETHERIUM-Erz wurde erfolgreich gefunden.

Die Expedition gilt als voller Erfolg.
Die Menschheit verfügt nun über eine neue
Energiequelle und die Mission XERON-9 wird als
historischer Meilenstein in Erinnerung bleiben.

==================================================
MISSION ERFOLGREICH
===================

""")

    end = input("Willst du die Mission erneut versuchen? (j/n): ")
    if end.lower() == "j":
        reset_game()
        menu_an = True
    else:
        menu_an = False
        print("Vielen Dank, dass du die Mission geleitet hast.")

def pos():
    kristall_pos() #überprüft wo Kristall ist und gibt Energie +40 wenn drauf
    hindernis_pos() #überprüft wo Hindernis ist und gibt Energie -10 wenn drauf
    data_pos() #überprüft wo Datenpunkt ist und gibt Energie +10 und 3 Scans wenn drauf
    eissturm_pos() #überprüft wo Eissturm ist und gibt Energie -20 wenn drauf
    gletscherspalte_pos() #überprüft wo Gletscherspalte ist und gibt Energie -50 wenn man drauf steht


def gen():
    global hindernisse, data, eissturm, kristall, zielx, ziely
    #zufallig Kristalle generieren
    for i in range(6):
        kristallx = random.randint(-sx, sx)
        kristally = random.randint(-sy, sy)
        kristall.append((kristallx, kristally))

    #zufallig Hindernisse generieren
    for i in range(5):
        hindernisx = random.randint(-sx, sx)
        hindernisy = random.randint(-sy, sy)
        hindernisse.append((hindernisx, hindernisy))

    #ziel generieren
    zielx = random.randint(-sx, sx)
    ziely = random.randint(-sy, sy)

    #zufallig eistürme generieren
    eissturm_x = random.randint(-sx, sx)
    eissturm_y = random.randint(-sy, sy)

    #zufällig data generieren
    for i in range(6):
        datax = random.randint(-sx, sx)
        datay = random.randint(-sy, sy)
        data.append((datax, datay))

    eissturm.append((eissturm_x, eissturm_y))
    eissturm.append((eissturm_x + 1, eissturm_y))
    eissturm.append((eissturm_x, eissturm_y + 1))
    eissturm.append((eissturm_x + 1, eissturm_y + 1))

    #zufällig eine Richtung und position für die Gletscherspalte wählen
    gletscherspalte_x = random.randint(-sx, sx)
    gletscherspalte_y = random.randint(-sy, sy)

    richtung = random.choice(["N", "S", "O", "W"])
    #Gletscherspalte generieren basierend auf der zufällig gewählten Richtung
    for i in range(4):
        if richtung == "N":
            gletscherspalte.append((gletscherspalte_x, gletscherspalte_y + i))
        elif richtung == "S":
            gletscherspalte.append((gletscherspalte_x, gletscherspalte_y - i))
        elif richtung == "O":
            gletscherspalte.append((gletscherspalte_x + i, gletscherspalte_y))
        elif richtung == "W":
            gletscherspalte.append((gletscherspalte_x - i, gletscherspalte_y))

def game_on() :
    if game_status == False:
        print(f"Mission abgebrochen.{name} kehrt zur Rakete zurück.")
        print(f"du hast {counterDrive} Fahrten und {Scans} Scans durchgeführt")
        print(f"energie: {Energie}")


#hindernis_near() überprüft ob ein Hindernis in der Nähe ist(scan)
def hindernis_near():
    if (x+1,y) in hindernisse:
        print("Rechts von dir befindet sich ein Hindernis!")
    if (x-1,y) in hindernisse:
        print("Links von dir befindet sich ein Hindernis!")
    if (x,y+1) in hindernisse:
        print("Vor dir befindet sich ein Hindernis!")
    if (x,y-1) in hindernisse:
        print("Hinter dir befindet sich ein Hindernis!")

#kristall_near() überprüft ob ein Kristall in der Nähe ist(scan)
def kristall_near():
    if (x+1,y) in kristall:
        print("Rechts von dir befindet sich ein Kristall!")
    if (x-1,y) in kristall:
        print("Links von dir befindet sich ein Kristall!")
    if (x,y+1) in kristall:
        print("Vor dir befindet sich ein Kristall!")
    if (x,y-1) in kristall:
        print("Hinter dir befindet sich ein Kristall!")
#überprüft ob Gletscherspalte in der Nähe ist (scan)
def gletscherspalte_near():
    if (x + 1, y) in gletscherspalte:
        print(f"Rechts von {name} befindet sich eine Gletscherspalte!")

    if (x - 1, y) in gletscherspalte:
        print(f"Links von {name} befindet sich eine Gletscherspalte!")

    if (x, y + 1) in gletscherspalte:
        print(f"Vor {name} befindet sich eine Gletscherspalte!")

    if (x, y - 1) in gletscherspalte:
        print(f"Hinter {name} befindet sich eine Gletscherspalte!")

#data_near() überprüft ob ein Datenpunkt in der Nähe ist (scan)        
def data_near():
    if (x+1,y) in data:
        print(f"Rechts von {name} befindet sich ein Datenpunkt!")
    if (x-1,y) in data:
        print(f"Links von {name} befindet sich ein Datenpunkt!")
    if (x,y+1) in data:
        print(f"Vor {name} befindet sich ein Datenpunkt!")
    if (x,y-1) in data:
        print(f"Hinter {name} befindet sich ein Datenpunkt!")

def sichtbare_felder_scannen():
    global sichtbare_felder

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            neues_feld = (x + dx, y + dy)

            if -sx <= x + dx <= sx and -sy <= y + dy <= sy:
                sichtbare_felder.add(neues_feld)

#scan() scannt die Umgebung und gibt Warnungen aus( _near Funktionen)
def scan():
    print("Scanne die Umgebung...")
    time.sleep(2)

    sichtbare_felder_scannen()

    hindernis_near()
    kristall_near()
    gletscherspalte_near()
    data_near()


#überprüft wo Gletscherspalte ist und gibt Energie -50 wenn drauf, entfernt die Gletscherspalte danach
def gletscherspalte_pos():
    global Energie, game_status
    for gletscherspalte_x, gletscherspalte_y in gletscherspalte:
        if y == gletscherspalte_y and x == gletscherspalte_x:
            print(f"{name} ist in eine Gletscherspalte gefallen! Energie -50")
            exit = random.choice(["j","n"])
            if exit == "j":
                Energie -= 50
                print(f"{name} hat einen Ausweg gefunden!")
            else:
                print(f"{name} hat keinen Ausweg gefunden")
                end_fuel()
                feld()
                game_status = False
            

#position der Eisstürme überprüfen und Energie -20 geben wenn drauf
def eissturm_pos():
    global Energie

    if (x, y) in eissturm:
        print(f"{name} gerät in einen Eissturm! Energie -20")
        Energie -= 20
#bewegt die Eisstürme zufällig auf dem Spielfeld
def eissturm_bewegen():
    global eissturm
    sturm_richtung = random.choice(["N", "S", "O", "W"])
    neue_positionen = []

    for eissturm_x, eissturm_y in eissturm:

        if sturm_richtung == "N":
            neue_positionen.append((eissturm_x, eissturm_y + 1))

        elif sturm_richtung == "S":
            neue_positionen.append((eissturm_x, eissturm_y - 1))

        elif sturm_richtung == "O":
            neue_positionen.append((eissturm_x + 1, eissturm_y))

        elif sturm_richtung == "W":
            neue_positionen.append((eissturm_x - 1, eissturm_y))

    eissturm = neue_positionen

#überprüft wo kristall ist und gibt Energie +40 wenn drauf, entfernt den Kristall danach
def kristall_pos():
    global Energie
    for kristallx, kristally in kristall:
        if y == kristally and x == kristallx:
            print(f"{name} ist auf einen Kristall gestoßen! Energie +40")
            Energie += 40
            kristall.remove((kristallx, kristally))

#überprüft wo Hindernis ist und gibt Energie -10 wenn drauf , entfernt das Hindernis danach
def hindernis_pos():
    global Energie
    for hindernisx, hindernisy in hindernisse:
        if y == hindernisy and x == hindernisx:
            print(f"{name} ist auf ein Hindernis gestoßen! Energie -10")
            Energie -= 10
            hindernisse.remove((hindernisx, hindernisy))

#überprüft wo Datenpunkt ist und gibt Energie +20 und 3 Scans wenn drauf, entfernt den Datenpunkt danach   
def data_pos():
    global Scans, Energie
    for datax, datay in data:
        if y == datay and x == datax:
            print(f"{name} hat einen Datenpunkt gefunden! Energie +20 und 3 Scans")
            Energie += 20
            Scans += 3
            data.remove((datax, datay))

def fuel_station():
        global Energie
        if x==0 and y == 0:
            print(f"Energie wird aufgeladen. Du bist an der Rakete.{name}s Energie wird bis hundert aufgeladen.")
        while x == 0 and y== 0:
            if Energie < 100:
                Energie += 10
                time.sleep(1)
            else:
                print("Energie vollständig auf 100 aufgeladen!")
                break
        
def weg_save():
    global weg
    if (x, y) not in weg:
        weg.append((x, y))

def feld_verdeckt():
    print(f"R = {name}, Z = Ziel, G = Gletscherspalte, H = Hindernis, K = Kristall, D = Datenpunkt, T = Rakete, E = Eissturm, ? = unbekannt")

    for y_pos in range(sy, -sy - 1, -1):
        for x_pos in range(-sx, sx + 1):
            position = (x_pos, y_pos)
            if position == (x, y):
                print("R", end=" ")
            elif position not in sichtbare_felder:
                print("?", end=" ")
            elif position == (zielx, ziely):
                print("Z", end=" ")
            elif position in gletscherspalte:
                print("G", end=" ")
            elif position in hindernisse:
                print("H", end=" ")
            elif position in kristall:
                print("K", end=" ")
            elif position in data:
                print("D", end=" ")
            elif position == (0, 0):
                print("T", end=" ")
            elif position in eissturm:
                print("E", end=" ")
            else:
                print(".", end=" ")

        print()


#zeichnet das Spielfeld (dev)
def feld():
    print(f"R = {name}, Z = Ziel, G = Gletscherspalte, H = Hindernis, K = Kristall, D = Datenpunkt, T = Rakete, E = Eissturm, # = Weg, den du schon gegangen bist")
    for y_pos in range(sy, -sy-1, -1):
        for x_pos in range(-sx, sx+1):
            if (x_pos, y_pos) == (x, y):
                print("R", end=" ")
            elif (x_pos, y_pos) == (zielx, ziely):
                print("Z", end=" ")
            elif (x_pos, y_pos) in gletscherspalte:
                print("G", end=" ")
            elif (x_pos, y_pos) in hindernisse:
                print("H", end=" ")
            elif (x_pos, y_pos) in kristall:
                print("K", end=" ")
            elif (x_pos, y_pos) in data:
                print("D", end=" ")
            elif (x_pos, y_pos) == (0, 0):
                print("T", end=" ")
            elif (x_pos, y_pos) in eissturm:
                print("E", end=" ")
            elif (x_pos, y_pos) in weg:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

#große des Spielfelds überprüfen
def größe():
    if y == sy or y == -sy or x == sx or x == -sx:
        print(f"{name} ist am Rand des Spielfelds!")

#Fahren Funktion um sich zu bewegen
def fahren_scannen_ende():
    eingabe = input("Gib die Richtung ein, in die du fahren willst (N, S, O, W), scan um zu scannen oder x um das spiel zu beenden: ")
    global x, y, Energie, counterDrive, Scans, game_status, counterScan
    if eingabe.lower() == "n":
        if y == sy:
            print(f"{name} ist am Rand des Spielfelds! Kann nicht weiter nach Norden fahren.")
        else:
            y += 1
            pos()
            Energie -= 5
            counterDrive += 1
            sichtbare_felder.add((x, y))
            eissturm_bewegen() #Eisstürme bewegen sich jedes Mal, wenn {name} fährt
    elif eingabe.lower() == "s":
        if y == -sy:
            print(f"{name} ist am Rand des Spielfelds! Kann nicht weiter nach Süden fahren.")
        else:
            y -= 1
            pos()
            Energie -= 5
            counterDrive += 1
            sichtbare_felder.add((x, y))
            eissturm_bewegen() #Eisstürme bewegen sich jedes Mal, wenn {name} fährt
    elif eingabe.lower() == "o":
        if x == sx:
            print(f"{name} ist am Rand des Spielfelds! Kann nicht weiter nach Osten fahren.")
        else:
            x += 1
            pos()
            Energie -= 5
            counterDrive += 1
            sichtbare_felder.add((x, y))
            eissturm_bewegen() #Eisstürme bewegen sich jedes Mal, wenn {name} fährt
    elif eingabe.lower() == "w":
        if x == -sx:
            print(f"{name} ist am Rand des Spielfelds! Kann nicht weiter nach Westen fahren.")
        else:
            x -= 1
            pos()
            Energie -= 5
            counterDrive += 1
            sichtbare_felder.add((x, y))
            eissturm_bewegen() #Eisstürme bewegen sich jedes Mal, wenn {name} fährt
    elif eingabe.lower() == "scan":
        if Scans > 0:
            scan()
            Scans -= 1
            counterScan += 1
        else:
            print("Keine Scans mehr verfügbar!")
    elif eingabe.lower() == "x":
        print(f"Mission abgebrochen. {name} kehrt zur Rakete zurück.")
        print(f"du hast {counterDrive} Fahrten und {Scans} Scans durchgeführt")
        print(f"energie: {Energie}")
        game_status = False
    
    else:
        print("Ungültige Eingabe. Bitte geben Sie N, S, O oder W ein.")

# Hauptspielschleife
def main():
    global game_status, menu_an
    menu_an = False
    while game_status == True:
        if Energie <= 0:
            feld()
            end_fuel()
            game_status = False
            break
        elif (x, y) == (zielx, ziely):
            feld()
            ziel_erreicht()
            game_status = False
            break
        feld_verdeckt() #zeichnet das Spielfeld
        fuel_station()
        fahren_scannen_ende() #fragt den Spieler nach der Richtung, in die er fahren möchte, oder ob er scannen möchte
        
        größe() #überprüft die Größe des Spielfelds und gibt eine Warnung aus

        print(f"Aktuelle Position: ({x}, {y}), Energie: {Energie}, Scans: {Scans}")#gibt die aktuelle Position und Energie von {name} aus
        print("--------------------------------------------------")#trennt die Runden optisch voneinander
        time.sleep(1) #fügt eine kurze Pause hinzu, damit das Spiel nicht zu schnell abläuft
def menu():
    global name, sx,sy,Energie, game_status

    eingabe = input("willst du das Spiel starten oder die Steuerung sehen? (start/steuerung): ")
    if eingabe.lower() == "start":
        name = input("gib ein wie du Deinen Roboter nennen möchtest: ")
        while True:
            modi = input("Du kannst dich entscheiden, ob du ein 11x11 Spielfeld haben möchtest und mit 100 Energie startest (leicht),"
                         "ein 21x21 Spielfeld mit 200 Energie (mittel),"
                         "oder ein 31x31 Spielfeld mit 300 Startenergie (schwer):")
            if modi.lower() == "leicht":
                sx = 5 #immer -1 weil das Startfeld mit zählt also 4 in jede richtung
                sy = 5
                Energie = 100
                gen()
                print(f"Vielen Dank, dass du den Roboter {name} auf seiner Mission begleitest! Du hast dich für {modi} entschieden. Viel Erfolg bei der Suche nach dem AETHERIUM-Erz auf XERON-9!")
                print(f"du hast {Energie} Energie und {Scans} Scans")
                start()
                game_status = True
                main()
                break
            elif modi.lower() == "mittel":
                sx = 10
                sy = 10
                Energie = 200
                gen()
                print(f"Vielen Dank, dass du den Roboter {name} auf seiner Mission begleitest! Du hast dich für {modi} entschieden. Viel Erfolg bei der Suche nach dem AETHERIUM-Erz auf XERON-9!")
                print(f"du hast {Energie} Energie und {Scans} Scans")
                start()
                game_status = True
                main()
                break
            elif modi.lower() == "schwer":
                sx = 15
                sy = 15
                Energie = 300
                gen()
                print(f"Vielen Dank, dass du den Roboter {name} auf seiner Mission begleitest! Du hast dich für {modi} entschieden. Viel Erfolg bei der Suche nach dem AETHERIUM-Erz auf XERON-9!")
                print(f"du hast {Energie} Energie und {Scans} Scans")
                start()
                game_status = True
                main()
                break
            else:
                print("Ungültige Eingabe. Bitte gib 'leicht','mittel' oder 'schwer' ein")
        
        

    elif eingabe.lower() == "steuerung":
            print(f"""Steuerung:
    - N: Nach Norden fahren
    - S: Nach Süden fahren
    - O: Nach Osten fahren
    - W: Nach Westen fahren
    - scan: Umgebung scannen (zeigt Hindernisse, Kristalle, Gletscherspalten und Datenpunkte in der Nähe an)
    - x: Spiel beenden
    --------------------------------------------------------
                    Funktionen
    - fahren: Du kannst dich mit den obengenannten Befehlen bewegen (n,s,o,w).
    - scan:   Wenn du anstatt N,O,S,W 'scan' eingibst, führst du einen Scan aus. Du startest mit 3 scans, wenn du einen scan ausführst, wird dir auf der
              Karte angezeigt, welche items sich auf den umliegenden Feldern von {name} befinden.
    - Karte:  Dir wird nach jedem Zug die Karte angezeigt, mit den Feldern, die du bereits entdeckt hast. Mit einem Scan deckst du alle 8 Felder um 
              dich herum auf einmal auf.
    - Fuel: Du kannst zu deiner Rakete zurück kehren um deine Energie auf 100 aufzuladen.

    --------------------------------------------------------
                        Items
    - Kristalle: Es gibt 6 zufällig verteilte Kristalle auf der gesamten Karte. Wenn du einen Kristall findest (also drauf stehst), gibt er dir + 40 Energie.
    - Hindernisse: Auf der gesammten Karte sind 5 Hindernisse zufällig verteilt. Wenn du auf eines stößt, verlierst du 10 Energie (also -10E) .
    - Data: Es gibt insgesammt 6 data punkte auf der Karte. Wenn du einen findest, gibt er dir + 3 scans und + 10 Energie.
    - Sturm: Aufgepasst. Es gibt einen Eissturm, der sich über die Karte bewegt. Wenn du in ihn hineingerätst, zieht er dir
                  (mit jedem Zug, den du machst, während du in ihm bist) 20 Energie ab ( also -20E pro Zug).
    - Spalte: Auf der Karte befindet sich eine gefährliche Gletscherspalte, wenn du in sie hineinfällst, zieht sie dir 50 Energie ab (also -50E)
                  und es kann sein, dass es keinen Ausweg gibt(dann hast du automatisch verloren).
    - 


    """)
    else:
            print("Ungültige Eingabe. Bitte gib 'start' oder 'steuerung' ein.")

        


while menu_an:
    menu()

