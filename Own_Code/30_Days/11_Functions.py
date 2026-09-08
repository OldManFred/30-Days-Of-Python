import sys
import os
pfad = __file__ #aktuellen pfad/filename
pfad = os.path.abspath(pfad)    #in absoluten Pfad wandeln
print(f'Pfad to file: {pfad}')
parent_pfad = os.path.join(pfad,'..','..','..')#zwei Ebenen hochgehen, da ist der Ordner
parent_pfad=os.path.normpath(parent_pfad)
print(f'Pfad to add: {parent_pfad}')
sys.path.append(parent_pfad)#Damit Python hier sucht bei import
from data.countries import countries
from data.countries_working_file import countries_data

def is_there_such_country(country):
    if country in countries:
        print(country)
    else:
        print('no such country!')
        
def find_capital(country):
    if country in all_countries:
        return all_countries[country]['capital']
    return 'No result'

def generate_country_dict(lst_country_data):
    gen_dictionary={}   #Dict erstellen...
    #Aus der Liste mit Dictionaries aller Länder ein Dictionary machen da schneller durchsuchbar
    for land in lst_country_data:#Liste aller Dicts iterieren
  #namen aus Länderdict holen, dann unter diesem Namen das ganze Dict im äusseren Dict speichern      
        gen_dictionary[land['name']] = land #Dict füllen...
    return gen_dictionary #...und zurückgeben

if __name__ == "__main__": #guard
    {}  #neues Dict erstellen
    all_countries = generate_country_dict(countries_data)#Funktionsaufruf, Liste übergeben, Dict zurück

    while True:
        cap_country=input('Enter country: ')
        print(f'Input: {cap_country}')
        if cap_country.lower() == 'exit':
            print('Break!')
            break
        is_there_such_country(cap_country) #Funktionsaufruf
       
        result=find_capital(cap_country)#Funktionsaufruf
        print(f'result: {result}')
        if result != 'No result':
            print(f'Country: {cap_country} capital: {result}')
        else:
            print(result)
