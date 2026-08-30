myDict={'Firstname':'Manfred','Lastname':'Kuehne','Age':59,'Profession':'Mechanic','IsSingle':True}
print('len: ',len(myDict))#Schlüssel-Wert-Paare zählen
print('First name: ',myDict['Firstname'])#Zugriff über Schlüssel, String
print('Single ? ',myDict['IsSingle'])#Zugriff über Schlüssel, Boolean
print('Alter',myDict['Age'])#Zugriff über Schlüssel, Fehler wenn nicht vorhanden
if 'Age' in myDict:#Vorher abfragen....
   print('Alter',myDict['Age'])
else:
    print('Ageless')
print('Alter',myDict.get('Lastname'))#...oder kein Fehler sondern None bei .get()
myDict['Adress']={'Street':'Habsburgerstr','Number':4,'Zip':10115}#Hinzufügen, kann Dict. enthalten
print(myDict.get('Adress'))#ganzes Dict auslesen
print(myDict.get('Adress')['Street'],myDict.get('Adress')['Number'])#Dict_in_Dict zugriff über Schlüssel in innerem Dict
print('Lenght adress:',len(myDict['Adress']))
myDict['Vehicles']=['Yamaha','Bicycle','Skates']#Kann Liste enthalten
print(myDict.get('Vehicles')[1])#Listenzugriff über index
myDict['Vehicles'].append('Legs')#Liste über Schlüssel auswählen und Eintrag hinzufügen
print(myDict.get('Vehicles')[3])#Zugriff auf Liste über Schlüssel, dann Index
myDict['IsSingle']=False #Wert direkt überschreiben
print('Single ? ',myDict['IsSingle'])#Zugriff über Schlüssel
myDict['Haircolour']='grey'
gepoppt=myDict.pop('Haircolour')#Eintrag entfernen mit pop, nur entfernter Wert wird übergeben
print('gepoppt: ',gepoppt)
if 'Haircolour' in myDict:
        print('Grey wolf!')
else:
        print('unknown!')
myDict['Height']=175
gepoppt=myDict.popitem()#entfernt und übergibt letztes Schlüssel-Wertepaar als Tupel
print('Type: ', type(gepoppt), 'gepoppt: ',gepoppt)
myDict['Drink']='Beer'
del myDict['Drink'] #Eintrag durch del entfernen
print(myDict)
lstConverted=myDict.items() #convertiert Dictionary in einen View Typ
print('Type: ',type(lstConverted),'Items: ',lstConverted)
myDict['FunnySkill']='juggling'
print('Type: ',type(lstConverted),'Items: ',lstConverted)#Änderungen werden automatisch übernommen
cpimyDict=myDict.copy()
myDict.clear()#alle Werte löschen
print(myDict)
del myDict  #Dictionary komplett löschen
print('Kopie: ',cpimyDict)
lstKeys=cpimyDict.keys()
print('Type: ',type(lstKeys), 'Keys: ',lstKeys) #Gibt alle Schlüssel zurück mit vorangestelltem dict_keys als eigenen type
cpimyDict['PrefColour']='DCM2'
print('Type: ',type(lstKeys), 'Keys: ',lstKeys) #Änderungen im Dict werden automatisch übernommen
lstValues=cpimyDict.values()#gleiches für Werte
print('Type: ',type(lstValues), 'Values: ',lstValues) #Gibt alle Werte zurück mit vorangestelltem dict_values als eigenen type
cpimyDict['Animal']='Spider'
print('Type: ',type(lstValues), 'Values: ',lstValues)  #Änderungen im Dict werden automatisch übernommen
lstInnerValues=cpimyDict['Adress'].values()#gleiches für Werte im inneren Dictionary
print(lstInnerValues)