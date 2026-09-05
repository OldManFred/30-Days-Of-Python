import sys
import os

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
print()
#Dreieck
for a in range(1,8,):
    print('#'*a)
print()
#8Zeilen mit 8 Zeichen
for b in range(1,9):
    print()
    for a in range(1,9):
        print('#',end='')
print()
for a in range(2,100):
    prime=True
    for b in range(2,a):
        if a!=b and b<a:
            if a%b==0:
                prime=False
    if prime :
        print(f'{a} is prime!')
b=1
c=10
for a in range(1,c):
    b+=b*a
print(f'{c}! = {b}')
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Deutschland',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
for countr in countries:
    if 'land' in countr:
        print(countr,end = '-')
print()
#Liste reverse mit for
fruits=['banana', 'orange', 'mango', 'lemon']
for fruit in range(len(fruits)-1,-1,-1):#Wert Ende ist exclusive!
    print(fruits[fruit])

#Liste aus Datei importieren, Ordner data ist zwei Ebenen über script
Pfad=__file__ #relativer oder absoluter Pfad zum Script
Pfad=os.path.abspath(Pfad) #in absoluten Pfad wandeln
DirPfad=os.path.dirname(Pfad)#Filenamen abtrennen
ParentDirPfad=os.path.join(DirPfad,'..','..')#Zwei Verzeichnisebenen nach oben anhängen
ParentDirPath=os.path.normpath(ParentDirPfad)#evtl in Normpfad wandeln, nicht unb. nötig
print(f'Pfad: {ParentDirPath}')
sys.path.append(ParentDirPath)# Pfad nun in Path aufnehmen
from data.countries_working_file import countries_data#Liste aus Modul (Datei) importieren
print(f'Einträge in countries_data: {len(countries_data)}')
#Zählen wie oft jede Sprache vorkommt, in dict ablegen
dictLanguages={'English':0}#Dictionary erzeugen
for nDict in countries_data:#durch alle Dicts in Liste iterieren
    for lang in nDict['languages']:#durch Liste der Sprachen im dict iterieren
        print(lang)
        if lang in dictLanguages:   #wenn Sprache schon in dict
            y=dictLanguages[lang]   #aktuelle Anzahl auslesen
            y+=1    #erhöhen
            dictLanguages[lang]=y   #wieder speichern
        else:#Sprache noch nicht in dict
            dictLanguages[lang]=1   #Eintrag anlegen und auf 1 setzen
print(f'Anzahl Sprachen: {len(dictLanguages)}')
for i in range(10):#10 Durchläufe, 10 häufigste Sprachen anzeigen
    count_langu=1#Zähler zurücksetzen
    name_langu=''
    for lang in dictLanguages:# Sprachen iterieren
        if dictLanguages[lang] > count_langu:#Anzahl höher ?
            count_langu = dictLanguages[lang]#neue Höchstzahl speichern
            name_langu=lang#Name dazu speichern
    print(f'Sprache: {name_langu} Anzahl: {count_langu}')#Aktuelle Höchstzahl anzeigen
    dictLanguages.pop(name_langu) #Sprache entfernen vor neuem Durchlauf 

dict_popu={} #neues Dictionary anlegen mit Land:Bevölkerung
for nDict in countries_data: #durch alle dicts in Liste iterieren
    #neues Dictionary mit Werten aus Dictionaries in Liste füllen, Name und Einwohner
    dict_popu[nDict.get('name')] = nDict.get('population')#Dictionaryeintrag anlegen
#10 Bevölkerungsreichste Länder anzeigen
for i in range(10): #10 Durchläufe
    max_popu=1
    for country in dict_popu: #Durch alle Einträge in neuem Dict iterieren
        if dict_popu.get(country) > max_popu:
            max_popu= dict_popu.get(country)
            max_popu_country=country
    print(f'Land: {max_popu_country} Einwohner: {max_popu}')
    dict_popu.pop(max_popu_country)
    