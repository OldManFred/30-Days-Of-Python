#Funktion mit variabler Anzahl Argumente
def add_all_nums(*nummern):
    a=0
    for nummer in nummern:# durch alle übergebenen Argumente iterieren
        a = a + nummer# zusammenaddieren
    return a
    
    
if __name__ == '__main__':# guard
    lst_nummern=[]# Liste erzeugen
    while(True):
        z=input('Nummer: ')
        if z.lower()== 'done' :
            break# while beenden
    print(f'Summe: {add_all_nums(*lst_nummern)}')# * entpackt Liste in einzelne Werte, die als Argumente übergeben werden

        