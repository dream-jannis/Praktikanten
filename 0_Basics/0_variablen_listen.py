# """
# in Variablen kann man Werte speichern
# hierbei gibt es verschiedene Datentypen, ja nachdem was die Variable speichern soll.
# Python erkennt automatisch, als was du den Wert speichern willst.
# (vgl. Java:
#     int ganzzahl = 1;
# )
# """

# ganzzahl = 1                    #Integer 
# fliesskommazahl = 3.14          #Float
# zeichenkette = "Hello World!"   #String
# wahrheitswert = False           #Boolean
# liste = ["SCALTEL AG", 2022]    #List
# dictionary = {"key": "value",   #Dict
#               "Alter": 19,
#               "Name": "Kilian",
#               "überAchzehn": True}

# print(type(wahrheitswert))
# ganzzahl = 5
# print(ganzzahl)


# ganzzahl_2 = ganzzahl
# #print(ganzzahl_2)

# ganzzahl = 10
# ergebnis = ganzzahl + ganzzahl_2
# #print(ergebnis)

# ergebnis = ganzzahl / ganzzahl_2
# print(ergebnis)


# Listen
#   liste = ["SCALTEL AG", 2022]
#   print(liste[1])
#   print(len(liste))
#   liste.append("IT-Ausbildung")
#   print(liste)
#   del liste[-1]
#   print(liste)


# Dictionarys
#   dictionary = {"key": "value", "Alter": [19, 16], "infos": {"name": "Simon"}}
#   print(dictionary["Alter"])
#   dictionary["Name"] = "Marc"
#   del dictionary["key"]
#   print(dictionary["Alter"][0])
#   print(dictionary["infos"]["name"])

#############################################Übungsaufgaben##############################################
"""
Aufgabe 1:
Schreibe einen Programm-Code, der den Benutzer nach seinem Namen, Alter und Wohnort  fragt.
Danach soll der Benutzer namentlich begrüßt werden und seine Daten ausgegeben werden.
Informiere dich hierfür über die input()- und print()-Funktion!
"""



"""
Aufgabe 2:
Schreibe einen Programm-Code, der die Daten aus Aufgabe 1 in die unten stehende Liste hinzufügt!
"""
data = []



"""
Aufgabe 3:
Schreibe einen Programm-Code, der die Daten aus Aufgabe 1 in das unten stehende
Dictionary als key-value-pair hinzufügt!
Beispiel: 
{
    "Name": "Michael"
}
"""



"""
Aufgabe 4:
unten siehts du 2 Variablen. 
Schreibe einen kurzen Code, der die Werte der beiden Variablen vertauscht und diese ausgibt.
Nach dem Tausch soll zahl_1 = 2 und zahl_2 = 1 gelten.
"""

zahl_1 = 1
zahl_2 = 2