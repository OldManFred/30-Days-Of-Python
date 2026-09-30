 #ganzes Modul importieren
import my_modules #ohne Erweiterung
import os
import sys
#from statistics import * #funktioniert dann ohne 'Prefix print('mean: ',mean(numbers)) ,vermeiden, wird unübersichtlich
import statistics #funktioniert dann nur mit Prefix so: print('median: ',statistics.median(numbers)
import math
from random import randint
 #einzelne Funktionen importieren mit Namensänderung
from my_modules import C_to_F as Fahrenheit, F_to_C as Celsius

def random_ID(num_digits=5,many=1): #Nutzer IDs random
    IDs=[]#Liste erzeugen
    zeichen = '0123456789abcdefghijklmnopqrstuvwxyz' #Zeichenvorrat für IDs
    for _ in range(many):#wie viele IDs ? Schleife von 0...many
        ID=''
        for _ in range(num_digits):
            ID+=zeichen[randint(0,len(zeichen)-1)]#zufälliges Zeichen auswählen aus Vorrat
        IDs.append(ID) 
    return IDs #ganze Liste zurückgeben

def shuffle_list(lst_originalliste):
    lst_originalliste_cpi=lst_originalliste.copy()
    lst_shuffleliste=[] #liste erstellen
    while len(lst_originalliste_cpi) > 0:
        lst_shuffleliste.append(lst_originalliste_cpi.pop(randint(0,len(lst_originalliste_cpi)-1))) #zufälliges item wegpoppen und an neue Liste hängen
        #print('Übrig:',len(lst_originalliste))  
    return lst_shuffleliste
    
if __name__ == '__main__':
   
    
   
    
    '''
    #Übung Listenitems auf Einzigartigkeit testen
    lst_to_test=[1,1,2,3,5,8]
    if my_modules.is_unique(lst_to_test):
        print('listitems are unique')
    else:
        print('listitems are not unique')
        
    #Übung auf Primzahl testen
    
    num_is_prime=my_modules.is_prime(int(input('Test what number ? ')))
    
       
    #kürzere Schreibweise
    print('Primzahl!') if num_is_prime else print('keine Primzahl!')
    
    #Ubung Umrechnung in Fahrenheit, kompakt
    print(f'Fahrenheit: {Fahrenheit(int(input("Temp in Celsius ? ")))}')
    '''
    
    pfad = os.path.abspath(__file__) #__file__ enthält Pfad zum py File
    print(f'os.path.abspath(__file__): {pfad}')
    pfad = os.path.dirname(pfad)#Pfad zum Ordner in dem File ist
    print(f'os.path.dirname: {pfad}')
    
    Ordner = pfad #Pfad zum Ordner ablegen
  
    
    testdir = os.path.join(pfad,'Testdir') #anhängen an Pfad
    print(testdir)
    if not os.path.isdir(testdir): #Ist dir vorhanden ?
        os.mkdir(testdir) #erzeugen
        print('testdir created')
        print(testdir)
    if  os.path.isdir(testdir): #Ist dir vorhanden ?
        os.rmdir(testdir) #Verzeichnis entfernen
        print('testdir removed')
    
    pfad = os.getcwd() #enthält aktuellen Terminal Pfad (von wo .py gestartet wurde)
    print(f'os.getcwd(): {pfad}')
    
    Argumente= enumerate(sys.argv)#mit laufender Nummer versehen
    print(Argumente)
    for Nummer,Argument in Argumente:
        print('Nummer: ',Nummer ,Argument  ,end=' ')
    print()
    print('Version: ', sys.version)
    print('maxsize: ',sys.maxsize)
    
    #statistics
    numbers=[1,1,2,3,5,8,13,21,34,55]   #liste
    print('mean: ',statistics.mean(numbers))
    print('median: ',statistics.median(numbers))
    
    #math
    print('Pi: ',math.pi)
    print('Kleinster gemeinsamer vielfacher: ',math.lcm(27,36,60))
    print('Sinus von arc pi/4:',math.sin(math.pi/4))#Bogenmaß
    print('Sinus von grd 72:',math.sin(math.radians(72)))#Grad erst in Bogenmaß umrechnen
    print('Sinus von grd 18:',math.sin(math.radians(18)))#Grad erst in Bogenmaß umrechnen
    print('Sinus von grd 90:',math.sin(math.radians(90)))#Grad erst in Bogenmaß umrechnen
    print('Entfernung: ',math.sin(math.radians(72.41))*123/math.sin(math.radians(17.59)))
    
    
    
    print('QWurzel:',math.sqrt(3))
    print('Sigma: ',math.fsum(numbers))
    print('Random Integer',randint(1,100))#both inclusive
    
    for next_ID in (random_ID(5,4)):
        print(next_ID)
    
    lst_original=[1,1,2,3,5,8,13,21,34]
    print('Originalliste: ',lst_original)
    print('Shuffled Liste: ',shuffle_list(lst_original) )
    
        
