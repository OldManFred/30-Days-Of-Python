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
    
    
if __name__ == '__main__':# guard
    '''lst_nummern=[]# Liste erzeugen
    while(True):
        z=input('Nummer: ')
        if z.lower()== 'done' :
            break# while beenden
    print(f'Summe: {add_all_nums(*lst_nummern)}')# * entpackt Liste in einzelne Werte, die als Argumente übergeben werden

'''
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