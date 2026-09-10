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
#infos enthält mehrere einzelne Argumente, beim Funktionsaufruf packt * die zu einem Tupel
def find_info(what_country,*infos):
    if what_country in all_countries:
        print(f'Country: {what_country}')
        for info in infos:
            print(f'{info}: {all_countries[what_country].get(info)} ')
    else:
        print(f'Country {what_country} not found')
    

def generate_country_dict(lst_country_data):
    gen_dictionary={}   #Dict erstellen...
    #Aus der Liste mit Dictionaries aller Länder ein Dictionary machen da schneller durchsuchbar
    for land in lst_country_data:#Liste aller Dicts iterieren land ist dict
  #namen aus Länderdict holen, dann unter diesem Namen (Schlüssel) das ganze Dict im äusseren Dict speichern      
        gen_dictionary[land['name']] = land #Dict füllen...mit Dicts
    return gen_dictionary #...und zurückgeben

if __name__ == '__main__': #guard
    all_countries = generate_country_dict(countries_data)#Funktionsaufruf, Liste übergeben, Dict zurück

    country=input ('country ? ') #welches Land ?
    if country not in all_countries:
        print(f'No country named {country}')
        sys.exit()
    lst_infos=[]#Liste erzeugen, nimmt Parameter auf
    while(True):
        what_info=input('info ? (done for exit)')
        if what_info.lower()=='done':
            break
        lst_infos.append(what_info)#infos in Liste sammeln
    find_info(country,*lst_infos)

