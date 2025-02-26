"""
In Python ist es auch möglich, Datein zu öffnen, diese Auszulesen, zu Erweitern und zu Überschreiben.
Hierbei gibt es verschiedene "Modi", mit welchen man die Datei öffnen kann:
r -> nur Auslesen der Datei
a -> Erweitern der Datei
w -> Überschreiben der Datei

Anmerkung:
Bei manchen Modi kann neben dem jeweiligen Buchstaben noch ein '+' hinzufügen wie zum Beispiel bei w.
Der Modus w+ sorgt dafür, dass die im Pfad angegebene Datei zusätzlich neben dem Beschreiben noch erstellt wird, 
falls sie noch nicht existiert.


#Auslesen
with open("0_Basics/3.txt", "r") as file:
    text = file.read()
    print(text)


#Erweitern
with open("0_Basics/3.txt", "a") as file:
    file.write("Test")


#Überschreiben
with open("0_Basics/3.txt", "w") as file:
    file.write("neuer Text")

"""
#############################################Übungsaufgaben##############################################
"""
Aufgabe 1:
Schreiben einen Code, der eine neue Datei (neu.txt) im Ordner Basics erstellt (vgl. Pfadangaben oben).
Beschreibe diese Datei mit einem Inhalt deiner Wahl!
"""



"""
Aufgabe 2:
Der Inhalt aus neu.txt soll ausgelesen werden und in 3.txt hinzugefügt werden.
Öffne hierzu erst neu.txt im richtigen Modus, lese die Daten aus, speicher sie in einer Variable ab
und öffne dann (während neu.txt noch geöffnet ist) 3.txt und füge den Inhalt hinzu!
"""
