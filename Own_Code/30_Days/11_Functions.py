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


def generate_country_dict(lst_country_data):
    gen_dictionary={}   #Dict erstellen...
    #Aus der Liste mit Dictionaries aller Länder ein Dictionary machen da schneller durchsuchbar
    for land in lst_country_data:#Liste aller Dicts iterieren land ist dict
  #namen aus Länderdict holen, dann unter diesem Namen (Schlüssel) das ganze Dict im äusseren Dict speichern      
        gen_dictionary[land['name']] = land #Dict füllen...mit Dicts
    return gen_dictionary #...und zurückgeben


def is_there_such_country(country):
    if country in countries:
        print(country)
    else:
        print('no such country!')
        
def find_capital(country):
    if country in all_countries:
        return all_countries[country]['capital']
    return 'No result'

def find_info(what_country,what_info='capital'):#capital ist default value
    if what_country in all_countries:#äusseres Dict durchsuchen
        if what_info in all_countries[what_country]:#inneres Dict durchsuchen
            return what_country,all_countries[what_country][what_info] #zwei Werte zurückgeben
        else:
            return 'No_info ', (f'for {what_country}')#zwei Werte zurückgeben
    else:
        return 'country', 'not found' #zwei Werte zurückgeben


if __name__ == "__main__": #guard
    all_countries = generate_country_dict(countries_data)#Funktionsaufruf, Liste übergeben, Dict zurück

    while True:
        country=input('Enter country: ')
        print(f'Input: {country}')
        if country.lower() == 'exit':
            print('Break!')
            break
        info=input('Enter info: ')
        
        #is_there_such_country(cap_country) #Funktionsaufruf
       
        '''result=find_capital(cap_country)#Funktionsaufruf
        print(f'result: {result}')
         if result != 'No result':
                    print(f'Country: {cap_country} capital: {result}')
                else:
                    print(result)'''
        #print(find_info(country,info))#Funktionsaufruf einfach
        
        #Funktionsaufruf mit Rückgabe, bei Angabe der Parameternamen ist Reihenfolge egal
        if info!='':
            result_country,result_info=find_info(what_info=info,what_country=country)
        else:
            result_country,result_info=find_info(what_country=country)#what_info wird durch default ersetzt
        if result_country=='country' and result_info=='not found':
            print((f'Country: {result_country} {result_info}'))
        else:
            print(f'Country: {result_country} {info}: {result_info}')
        
       
