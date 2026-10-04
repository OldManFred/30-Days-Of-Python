#List comprehensions
from pathlib import Path
import sys
#Variante mit pathlib
pfad=Path(__file__).resolve()#objekt erstellen und auf __file__ setzen
#3 Ebenen rauf
parent_pfad=pfad.parents[1] #Listenähnliche Sammlung von Elternordnern, parents[0] wäre direkter Elternordner
print(type(parent_pfad))#achtung, ist noch kein string
print(f'Pfad to add: {str(parent_pfad)}')
sys.path.append(str(parent_pfad))   #sys.path.append erwartet String
from my_modules import generateFibonacci as Fibos, is_prime
'''
import my_modules                                   # Variante A, aufruf my_modules.generateFibonacci(10)
from my_modules import C_to_F, F_to_C, is_unique, generateFibonacci  # Variante B, aufruf mit generateFibonacci(10)
    oder from my_modules import generateFibonacci as Fibos, aufruf mit Fibos(10)
from my_modules import *                            # Variante C aufruf mit  generateFibonacci(10)'''

if __name__ == '__main__':
   
    
    str_Message = 'Hello fool!'
    lst_Chars= [i for i in str_Message]#ganze Schleife zusammengefasst
    print(type(lst_Chars),' ',lst_Chars)
    
    lst_numbers=[i for i in range(20)]#Liste erzeugen alle Zahlen
    print(f'Summe: {lst_numbers}')
    
    lst_fibos=Fibos(30) #funktion in my_modules nutzen um Fibonaccizahlen zu bilden
    lst_fibos_prime=[i for i in lst_fibos if is_prime(i)]#liste mit primzahlenfibonaccis bilden
    print(lst_fibos_prime)
     
    print([i for i in Fibos(30) if is_prime(i)])# Alles zusammengefasst