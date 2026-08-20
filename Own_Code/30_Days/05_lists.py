#listen erzeugen
mylist=list()# mit eingebauter list Funktion
print('Type: ',type(mylist))
mylist = ['otto','hubert']
print(mylist,'len:',len(mylist))#len zählt einträge bei Listen
mylist.append('karl')#anhängen
print(mylist,'len:',len(mylist))
#mixed,
myotherlist=['Manfred',59,{'profession':'electrician'}]
for thing in myotherlist:
    print(f"{thing},{type(thing)}")
#dict direkt über index auslesen
print(myotherlist[2].get('profession'))
#Wert über index verändern
mylist[0]='olga'
print(mylist)
#Tupel erzeugen...
pers1=('helmut',33)
pers2=('jorge',44)
pers3=('egon',102)
print(type(pers3))
#...und in Liste packen
suspects=[pers1,pers2,pers3]
for name,age in suspects:
    print(f'{name} is {age} years old')
#gleich Tupel in Liste packen. Jeder Tupel hat 2 Werte
suspects=[('peter',25),('steve',19),('claude',3)]
#beide Werte des Tupel in Schleife auslesen
for name,age in suspects:
    print(f'{name} is {age} years old')
#Liste erzeugen und gleich mit Werten füllen
origin =['Berlin','London','Paris']
print('Orginal: ',origin)
#Das erzeugt nur ein alias, KEINE Kopie!#
#beide Namen greifen auf die gleiche Liste zu
kopie=origin
print('Copy: ',kopie)
kopie.append('Bergen')
#Nur die eine vorhandene Liste mit zwei Namen wird verändert
print('Orginal: ',origin)
print('Copy: ',kopie)
kopie2=kopie.copy() #Das erzeugt wirklich eine Kopie
kopie2.append('Tokyo')
print(kopie)
print(kopie2)
#unpacking rest, * sammelt alle in der Reihenfolge nicht zugewiesene Elemente in Liste
city1,city2,*other_cities=kopie2 #ende sammeln
print('*Ende')
print(city1)
print(city2)
print(other_cities)
city1, *other_cities, city2=kopie2 #Mitte sammeln
print('*Mitte')
print(city1)
print(city2)
print(other_cities)
print('*Anfang')
*other_cities,city1,  city2=kopie2 #Anfang sammeln
print(city1)
print(city2)
print(other_cities)
#slicing
print('Liste: ',kopie2)
print('slicing:',kopie2[1:3:1])#Stop exclusive!
print('slicing:',kopie2[2:])#2 bis Ende Liste
print('slicing:',kopie2[:2])#2 bis exclusive Stop
print('slicing:',kopie2[1:len(kopie2):1])#Stop exclusive, deshalb geht len!
print('slicing:',kopie2[1::2])#Schrittweite 2
#negativ, letztes Element ist -1
#Rückwärts
print('Liste: ',kopie2)
print('slicing negativ reverse:',kopie2[-1::-1])#liste Umkehren
print('slicing negativ reverse:',kopie2[::-1])#oder so, default start bei negative Schrittweite Ende Liste
#liste kann man auch mit reverse umkehren
print(kopie2)
kopie2.reverse()
print('reverse() ',kopie2)
print('slicing negativ reverse:',kopie2[-1:-4:-1])#Stop exclusive
#geht auch vorwärts
print('slicing negativ forward:',kopie2[-5:-3:])
#slicing erzeugt keinen Index Error
print('slicing out of range:',kopie2[17:39:])
#Wert abfragen
if 'Bergen' in kopie2:
    print('Rügen calling!')
#einfügen
kopie2.insert(2,'Madrid')#index,item
print(kopie2)
#entfernen
kopie2.remove('Paris')#über item
print(kopie2)
kopie2.pop(3)#über index
print(kopie2)
#oder über keyword del
del kopie2[1:3]
print(kopie2)
#Liste leeren
kopie2.clear()
print('leer' ,kopie2)
kopie.clear()
kopie2=['Bier','Cola','Wein']
kopie=['Limo','Diesel']
print(kopie2)
print(kopie)
#joining mit +
beverages=kopie + kopie2
print(beverages)
beverages.clear()
#mit extend
kopie2.extend(kopie)
print(kopie2)
#zählen
kopie2.append('Wein')
print('Anzahl Wein: ',kopie2.count('Wein'))#nur 1 Argument
#index anzeigen, nur erstes Auftreten
kopie2.append('Bier')
print('Wo ist Bier? ',kopie2.index('Bier'))
#sortieren aufsteigend, Liste wird modifiziert
kopie2.sort()
print('sort: ',kopie2)
#sortieren absteigend
kopie2.sort(reverse=True)
print('sort reverse: ',kopie2)
#sortieren aufsteigend, Liste wird nicht modifiziert
numbers=[23,55,17,24,42,]
print('Liste: ',numbers)
print('sorted: ',sorted(numbers))
print('Liste: ',numbers)
#sortieren absteigend
print('sorted reverse: ',sorted(numbers,reverse=True))
print('Liste: ',numbers)
while len(kopie2)>0:
    drink=kopie2.pop(0)
    print('Lets have a glass of ',drink)
'''Methoden mit .methode() direkt auf der Liste verändern meist die Liste
selbst und geben oft None zurück (.sort(), .reverse(), .append(), .extend(), .clear()).
Eingebaute Funktionen wie sorted(), oder Ausdrücke wie liste[::-1] bzw. a + b,
erzeugen dagegen eine neue Liste und lassen das Original unangetastet.'''