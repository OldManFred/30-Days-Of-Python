a,b,c,d=0,1,0,0
fibo=[0,1]#  Liste erzeugen
while c<500:
	c=a+b# nächste Fibonacci-Nummer berechnen
	fibo.append(c)#an Liste anhängen
	a=b#für nächste Berechnung schieben
	b=c
print('done')
print(f'Fibonacci-sequence: {fibo}')
while d<10:
    print(d,end=' ')
    d+=1
    if d==7:
        break # beendet Schleife
print()
d=0
while d<10:
    d+=1
    if d==5:
        continue #zurück zu while
    print(d,end=' ')
print()
print('Nummern in fibo:',end=' ')
for nummer in fibo: #Liste iterieren
    
    print(nummer,end=';')
print('\n String')
myName='Manfred'
for letter in myName: #String iterieren
    print(f'{ord(letter)}:{letter} ' ,end='')
print('\n \r range')
for i in range(len(myName)):# oder mit range-Funktion range(stop) range(start,stop(excl),step)
	print(myName[i],end=' ')
print('\n Range')
for i in range(4,12,2):
    print(i,end=' ')
print('\n Tupel')
tplFibo=(0,1,1,2,3,5,8) #Tupel iterieren
for nummer in tplFibo:
    print(nummer,end=' ')
print('\n Dictionary')
myDict={'Firstname':'Manfred','Lastname':'Kuehne','Age':59,'Profession':'Mechanic','IsSingle':True}
for schluessel in myDict:
    print(schluessel,end=':')#durch Schlüssel iterieren
    print(myDict[schluessel],end=' ')#durch Werte iterieren
for schluessel,wert in myDict.items(): #Schlüssel und Wert gleichzeitig abfragen mit .items() (view-type)
    print(f'{schluessel}:{wert} ;',end=' ')
print('\n Set')
stVeggies={'banana','ananas','apple','kiwi','grapes'}
for veg in stVeggies:#durch set iterieren (unordered)
    print(veg,end=';')
for veg in stVeggies:#durch set iterieren
    print(veg,end=';')
    if veg=='apple':
        break #beendet Schleife irgendwo da unordered
print('\n ',end=' ' )
for veg in stVeggies:#durch set iterieren
    if veg=='apple':
        continue #gleich zurück zu nächstem for
    print(veg,end=';')
print('\n range \n',end=' ' )
tpRange=range(2,20,2) #Start,Stop (excl),Step - Typ Range von Zahlen erzeugen
print(f'Type: {type(tpRange)}, {tpRange}')
lstRange=list(tpRange)#in Liste der Zahlen konvertieren
print(lstRange)
for a in range(3,7):#Teil aus String extrahieren in Schleife
    print(myName[a],end='')
print()
for a in range(6,2,-1):#rückwärts Teil aus String extrahieren in Schleife
    print(myName[a],end='')
print()
myDict['Hobbies']=['Diving','Hamradio','Skating','Tinkering','Languages','Motobiking','Geocaching']
for Schluessel in myDict:#alle Schlüssel iterieren
    if Schluessel=='Hobbies':
        for Hobby in myDict[Schluessel]: #Werte in Liste in Dictionary iterieren
            print(Hobby, end = '-')
        break