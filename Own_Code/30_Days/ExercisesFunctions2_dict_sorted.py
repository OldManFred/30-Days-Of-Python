import sys
import os
#Pfad zu 'data' zur Path Variable hinzufügen
Pfad=__file__ #__file__ enthält relativer oder absoluter Pfad zum Script
Pfad=os.path.abspath(Pfad) #in absoluten Pfad wandeln
DirPfad=os.path.dirname(Pfad)#Filenamen abtrennen
ParentDirPfad=os.path.join(DirPfad,'..','..')#Zwei Verzeichnisebenen nach oben anhängen
ParentDirPath=os.path.normpath(ParentDirPfad)#evtl in Normpfad wandeln, nicht unb. nötig
print(f'Pfad: {ParentDirPath}')
sys.path.append(ParentDirPath)# Pfad nun in Path aufnehmen
#Funktion mit variabler Anzahl Argumente
def add_all_nums(*nummern):
    a=0
    for nummer in nummern:# durch alle übergebenen Argumente iterieren
        a = a + nummer# zusammenaddieren
    return a

def C_to_F(Temp):
    return (Temp * 9/5) + 32

def F_to_C(Temp):
    return (Temp-32)*5/9

def rev_List(lst_to_reverse):
    reversed_list=[]
    for item in range(len(lst_to_reverse)-1,-1,-1):#Start, Stop-exclusive,Step
        reversed_list.append(lst_to_reverse[item])
    return reversed_list

def add_item(lst_list,what_item):
    lst_list.append(what_item)
    return(lst_list)

def remove_item(lst_whatList,what_item):
    lst_whatList.remove(what_item)
    return lst_whatList

def add_all_numbers(what_number): #Alle Zahlen addieren nach Gauss
    if what_number%2==1: #Test gerade - ungerade
        return (what_number*(what_number-1)/2)+ what_number#ungerade
    else: return (what_number+1)*(what_number/2)#gerade 
    
def add_all_even_numbers(what_number):
    z=0 #int erstellen
    for i in range(0,what_number+1):
        if i%2==0:#test even
            z=z+i
    return z

def is_prime(what_number):
    is_number_prime=True
    for i in range(2,what_number,1):#Start, Stop exlusive.Step
        if what_number%i==0:
            is_number_prime=False
    return is_number_prime

def is_unique(lst_itemlist):
    set_testset=set(lst_itemlist) #Liste in ein  Set kopieren, mehrfache Einträge verschwinden.
    return len(set_testset)==len(lst_itemlist)
    #mit Schleife wäre Overkill.
    #set_testset=set() #leeres Set erzeugen
    #for each_item in lst_itemlist: #alle Werte aus Liste in Set kopieren
    #    set_testset.add(each_item) #doppelte Elemente verschwinden im Set
    #return len(set_testset)==len(lst_itemlist)
    
        
    
        

if __name__ == '__main__':# guard
    '''
    #Übung variable Anzahl Argumente
    lst_nummern=[]# Liste erzeugen
    while(True):
        z=input('Nummer: ')
        if z.lower()== 'done' :
            break# while beenden
    print(f'Summe: {add_all_nums(*lst_nummern)}')# * entpackt Liste in einzelne Werte, die als Argumente übergeben werden


#Übung Funktion zum Berechnen Temperatur
while True:
    what_calc=input('C to F: C - F to C: F - exit to stop ')
    print(what_calc)
    if what_calc.lower()=='c':
        in_Temp=input('Temp in C ?')
        print(f'Temp in C: {in_Temp} Temp in F: {C_to_F(Temp=int(in_Temp)):.2f}')
    elif what_calc.lower()=='f':
        in_Temp=input('Temp in F ?')
        print(f'Temp in F: {in_Temp} Temp in C: {F_to_C(Temp=int(in_Temp)):.2f}')
    elif what_calc.lower()=='exit':
        break
    else:
        print(f'Wrong input, only c or f')
    
#Übung Liste übergeben zu reversieren in Loop und Drucken
#lst_Test=[1,1,2,3,5,8,13] #Liste erzeugen
lst_Test=['A','B','C']
lst_Rev=rev_List(lst_Test)
print(f'reversed {lst_Rev}')
#Übung item hinzufügen
lst_newlist=[]
while(True):
    new_item=input('add what item ?')
    if new_item=='exit':
        break
    print(add_item(lst_newlist,new_item))
    #Übung Element aus Liste entfernen
    lst_Test=[1,1,2,3,5,8,13] #Liste erzeugen
    item=input('remove what ?')
    item=int(item)
    if item in lst_Test:
        
        lst_Test=remove_item(lst_Test,item)
        print (lst_Test)
    else:
        print('No such item:', item)
        
    #Übung alle Zahlen addieren
    while True:
        number=(input('Add all numbers up to what ?'))
        if number == 'exit':
            print('terminated')
            break
        number=int(number)
        if number>1:
            print(f'Summe: {int(add_all_numbers(number))}')
        else:
            print('Number incompatible!')
            
            
    #Übung alle geraden Zahlen addieren   
    while True:
        number=(input('Add all even numbers up to what ?'))
        if number == 'exit':
            print('terminated')
            break
        number=int(number)
        if number>1:
            print(f'Sum all even numbers: {int(add_all_even_numbers(number))}')
        else:
            print('Number incompatible!')
    #Übung testen Primzahl
    while True:
        what_number=input('Number to test for prime: ')
        if what_number == 'exit':
            print('terminated')
            break
        else:
            what_number=int(what_number)
            if what_number<2:
                print(f'Number {what_number} incompatible')
            else:
                is_that_number_prime=is_prime(what_number)
                if is_that_number_prime:
                    print(f'Number {what_number} is prime')
                else:
                    print(f'Number {what_number} is not prime')
    from data.countries_working_file import countries_data#Liste aus Modul (Datei) importieren
    #
    dct_langu={}#dict erzeugen
    #jetzt das neue Dict mit 'Sprache':Häufigkeit füllen
    for land in countries_data: #durch alle Länder in Liste iterieren...
        for langua in land['languages']:    #...dann durch alle Sprachen des Landes iterieren
            #Nicht vorhandene Sprachen eintragen und auf 1 setzen, vorhandene um eins erhöhen
            dct_langu[langua]=dct_langu.get(langua,0)+1 #get gibt Wert aus, default 0 wenn Schlüssel nicht vorhanden. Danach +1
            
         
            #komplizierte Methode
            # if langua not in dct_langu:
                dct_langu[langua]=1     #Sprache das erste Mal vorhanden, Eintrag machen
            else:   #Sprache schon vorhanden, hochzählen
                dct_langu[langua]+=1
                
    
    sortiert=dct_langu.items() #.items() Ergibt eine 'Liste' vom Typ dict_items, diese enthält Tupel aus ('Schlüssel',Wert)
    #sorted() erzeugt eine sortierte Liste
    #lambda erzeugt anonyme Funktion, x ist übergebener Wert (ein Tupel), zurückgegeben wird x[1], danach wird sortiert
    sortiert = sorted(sortiert, key=lambda x: x[1], reverse=True )  #sorted(iterable, key=key, reverse=reverse)
    
    #sorted(dict) → sortiert nur Schlüssel, gibt Liste von Schlüsseln zurück
    #sorted(dict.items()) → sortiert nach Schlüsseln, gibt Liste von Tupeln zurück ('Schlüssel',Wert)
    #sorted(dict.items(), key=lambda x: x[1]) → sortiert nach Werten an Position [1], gibt Liste von Tupeln
sortiert=sortiert[:10]#slicing, Eintäge 0 bis 9

for platz, (sprache, anzahl) in enumerate(sortiert, start=1):
    print(f'Platz {platz}: Sprache: {sprache} Häufigkeit: {anzahl}')
#Achtung, enumerate wird bei Benutzung geleert!

print(f'Type: {type(sortiert)}')
'''
    
lst_to_test=[1,2,3,5,8]
if is_unique(lst_to_test):
    print('list is unique')
else:
    print('list is not unique')