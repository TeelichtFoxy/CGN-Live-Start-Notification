# Das wichtigste zuerst:
# Python ist sehr assozial...
# Python benötigt im gegensatz zu anderen Programmiersprachen keine ";" Simikolons, um einen Befehl zu beenden.
# Dafür muss man bei Python ganz genau auf richtige Zeilenumbrüche achten
# Auch benötigt man für Schleifen in Python kein "{" zum öffnen und "}" zum schließen. Stattdessen musst du einfach die Schleife mit einem ":" öffnen uns sehr auf die Zeilenumbrüche achten

# Bibliotheken (In Python "Module" genannt) importieren
import sys # Systembibliothek (Mit Vorsicht zu verwenden)
import time # Bibliothek für Aufgaben wie "time.sleep()"
import datetime # Zeit/Datumsbibliothek
import tkinter as tk # Die Bibliothek "tkinter" wird importiert als "tk" und kann nun mit diesem Namen aufgerufen werden - Wir benutzen diese Bibliothek, um eigene Fenter zu erstellen

# Jede Bibliothek stellt im Script gewisse Funktionen zur Verfügung

# Es gibt Bibliotheken wie "time", "sys", etc, die bei der Pythoninstallation vorinstalliert werden. Andere musst du selbst installieren Z.B.:
# Du möchtest Infos einer URL/Website abrufen? - "requests" installieren
# Installation:
# Öffne ein neues Terminal auf deinem Computer
# gib ein: "pip install [Bibliotheknamen]" Z.B.:
# pip install requests
# Nach der erfolgreichen Installation kannst du die Bibliothek in deinem Script importieren und die Funktionen von der Bibliothek in deinem Script nutzen

# Funktionen aus einer Bibliothek können verwendet werden, indem man als Befehl folgendes angibt:
# Beispiel "time.sleep()" (Weiterführung vom Script eine definierte Zeit aussetzen)
# Der Befehl "time.sleep()" besteht aus der Bibliothek, aus dem der Befehl kommt (time), dem Funktionsnamen (sleep) und die Zeit, die gwartet werden soll - in Sekunden - (5)
# Der Befehl "time.sleep(5)" wartet also 5 Sekunden, bis das Script fortgesetzt wird
# Es können auch Kommazahlenverwendet werde (WICHTIG: bei einem "," nimmt das Programm 2 Zahlen an - time.sleep() nimmt keine 2 Variablen an und würde einen fehler ausgeben)
# Kommazahlen werden immer mit einem "." als komma definiert
# Z.B.:
# time.sleep(0.1) - Das Skript wartet 0,1 Sekunden, bis es fortgesetzt wird


# Variablendeklarierung
isCGNTime = False # Variable "isCGNTime" wird als "False" definiert (Falsch -> meistens als NICHT ausführen gemeint)
cGNDate = 6 # datetime.datetime -> Zahl "6" = Sonntag ("0" = Montag - "6" = Sonntag)
now = datetime.datetime.now() # Variable "now" wird auf die jetzige Uhrzeit und Datum gesetzt

# Variablen werden wie folgt deklariert:
# "variablenname (Erster Buchstabe IMMER klein)" = (Zuweisungsoperator) [Wert -> (string => in "" - Eine Zeichenkette), (boolean => True/False (groß geschrieben in Python) - Wahr/Falsch), (int => Zahl)]

# Funktionen vom Script
def closeNotificationWindow(): # Wir definieren eine eigene Funktion zum schließen vom Notification Window
    notificationWindow.destroy() # Das Fenster notificationWindow wird geschlossen

if now.weekday() == cGNDate: # Wir öffnen eine "if" Schleife - Wenn heute (Zahl) der Zahl "cGNDate" (6 = Sonntag) entspricht => Heute ist Sonntag? Wird der Code in der Schleife ausgeführt
    isCGNTime = True # Variable "isCGNTime" wird geändert auf "True" (Wahr)

if isCGNTime: # Der Code überprüft, ob "isCGNTime" True ist und setzt den Code fort
    while True: # Eine "while" Schleife führt die Schleife so lange aus, so lange die Bedingung "True" ist - In dem Fall für immer => Eine allgemeine Endlosschleife
        time.sleep(0.1) # Hier stellen wir sicher, dass die Schleife nicht ununterbrochen läuft, da das bedeuten würde, dass kein anderer Code im Script mehr ausgeführt werden kann
        nowTime = datetime.datetime.now().time() # Wir holen uns bei jeder Durchführung der Schleife die aktuelle Zeit
        if nowTime.hour >= 10 and nowTime.hour < 11: # Überprüfen, ob es 10 - 11 Uhr ist
            if nowTime.minute == 30 and nowTime.second == 0: # Errinerung um 11:30 Uhr
                notificationWindow = tk.Tk() # Neues Fenster mit tkinter erstellen
                notificationWindow.attributes('-fullscreen', True) # Fenster in Vollbild Modus setzen
                notificationWindow.attributes('-topmost', True) # Fenster über allen anderen anzeigen lassen
                notificationWindow.title("Livestream Start Notification") # Fenstertitel anpassen
                messageTitle = tk.Label(notificationWindow, text="Livestream Start Notification", font=("Arial", 50)) # Neuen Textinhalt zum Fenster hinzufügen
                messageTitle.pack(pady=100) # Textinhalt im Fenster anhand der y Achse positionieren
                message = tk.Label(notificationWindow, text="Der Stream sollte in 30 Minuten gestartet werden!", font=("Arial", 40)) # Neuen Textinhalt zum Fenster hinzufügen
                message.pack(pady=80) # Textinhalt im Fenster anhand der y Achse positionieren
                notificationWindow.after(10000, closeNotificationWindow) # Nach 10000 Millisekunden unsere Funktion "closeNotificationWindow" aufrufen
                notificationWindow.mainloop() # Fenster einblenden
            # Den obigen Script Abschnitt können wir immer wieder copy und pasten und die Uhrzeit anpassen
            if nowTime.minute == 50 and nowTime.second == 0: # Errinerung um 11:50 Uhr
                notificationWindow = tk.Tk()
                notificationWindow.attributes('-fullscreen', True)
                notificationWindow.attributes('-topmost', True)
                notificationWindow.title("Livestream Start Notification")
                messageTitle = tk.Label(notificationWindow, text="Livestream Start Notification", font=("Arial", 50))
                messageTitle.pack(pady=100)
                message = tk.Label(notificationWindow, text="Der Stream sollte in 10 Minuten gestartet werden!\nBitte bereit machen!", font=("Arial", 40))
                message.pack(pady=80)
                notificationWindow.after(10000, closeNotificationWindow)
                notificationWindow.mainloop()
            if nowTime.minute == 55 and nowTime.second == 0: # Errinerung um 11:55 Uhr
                notificationWindow = tk.Tk()
                notificationWindow.attributes('-fullscreen', True)
                notificationWindow.attributes('-topmost', True)
                notificationWindow.title("Livestream Start Notification")
                messageTitle = tk.Label(notificationWindow, text="Livestream Start Notification", font=("Arial", 50))
                messageTitle.pack(pady=100)
                message = tk.Label(notificationWindow, text="Der Stream sollte in 5 Minuten gestartet werden!\nBitte Gespräche einstellen und auf den Dienst vorbereiten!", font=("Arial", 40))
                message.pack(pady=80)
                notificationWindow.after(10000, closeNotificationWindow)
                notificationWindow.mainloop()
            if nowTime.minute == 57 and nowTime.second == 0: # Errinerung um 11:57 Uhr
                notificationWindow = tk.Tk()
                notificationWindow.attributes('-fullscreen', True)
                notificationWindow.attributes('-topmost', True)
                notificationWindow.title("Livestream Start Notification")
                messageTitle = tk.Label(notificationWindow, text="Livestream Start Notification", font=("Arial", 50))
                messageTitle.pack(pady=100)
                message = tk.Label(notificationWindow, text="Der Stream sollte nun beginnen!\nBitte Stream starten!", font=("Arial", 40))
                message.pack(pady=80)
                notificationWindow.after(10000, closeNotificationWindow)
                notificationWindow.mainloop()
        else: # Es ist früher als 10 Uhr oder später als 11 Uhr
            sys.exit(0) # Programm schließen
else: # Es ist noch nicht Sonntag
    print("Es ist noch nicht Gottesdienstzeit!\nScript wird beendet.") # Nachricht anzeigen lassen im CLI (Terminal)
    time.sleep(5) # 5 Sekunden warten, damit die Nachricht gelesen werden kann
    sys.exit(0) # Programm schließen