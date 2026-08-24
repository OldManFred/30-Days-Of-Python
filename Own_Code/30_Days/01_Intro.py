print(20//7)
print(2**10)
print('4 mal type:')
print(type([2,3,5,7]))
print(type('FU'))
print(type({'Summe':1000}))
print(type({2,4,7}))
listtest=[13,17,19,23]
print(f"listtest: {listtest}")
print(*listtest,sep=' <-> ')# * ist deconstructor
settest={2,3,7,3} #duplikate werden automatisch entfernt
print(type(settest))
print(f"Settest: {settest}")
a,b,c=settest
print(a)
print(b)
print(c)
settest.add(11)
print(f"Settest: add {settest}")
print('mit sorted in list wandeln')
settestlist=sorted(settest)
print('nach sorted: ',type(settestlist))
print(settestlist[1])# jetzt indizierbar
#Sets verknüpfen
setA={'a','b','c','d'}
setB={'c','d','e','f'}

print('SetA',setA)
print('SetB',setB)
print(f'Sets verknüpft &:{setA & setB}')
print(f'Sets verknüpft |:{setA | setB}')
print(f'Sets verknüpft - differenz :{setA - setB}')
setA={'a','b','c','d'}
setB={'b','c'}
print(f'issubset {setB.issubset(setA)}') #Ist setB komplett in setA enthalten ?
setB.add('x')#ein Element hinzufügen
print(f'issubset {setB.issubset(setA)}') #Ist setB komplett in setA enthalten ?
setB.remove('x')
print(f'SetA: {setA}')
print(f'SetB: {setB}')
print(f'issuperset {setA.issuperset(setB)}') #enthält setA alles von setB  ?
setB.add('x')#ein Element hinzufügen
print(f'issubset {setA.issuperset(setB)}') #enthält setA alles von setB  ?
setA.update('otto')#mehrere Elemente aus Liste, Set,String hinzufügen
print(setA)
setA.remove('o')#ein Element weg, Fehler wenn nicht vorhanden
print(setA)
setA.discard('l')#ein Element weg, kein Fehler wenn nicht vorhanden
print(setA)
tupeltest=(2,3,7,3)
print(type(tupeltest))
print('Tupel in Variablen zerlegt')
a,b,c,d=tupeltest
print(a)
print(b)
print(c)
print(d)
print(f"Tupeltest: {tupeltest}")
#Elemente zählen
z=tupeltest.count(3)
print(f"count 3: {z}")
#1. Index eines Elements ermitteln
z=tupeltest.index(7)
print(f"index 7: {z}")
tplMetalle=('Gold','Silber','Mercury','Eisen')
tplOrdnungsz=(79,47,80,26)
#zip gibt zip Object zurück
Zwischenergebnis=(zip(tplMetalle,tplOrdnungsz))
print('Typ: Zip ',type(Zwischenergebnis))
#in list casten
Periodens=list(Zwischenergebnis)
print(Periodens)


'''Merksatz
                Liste [...]	                Set {...}	                     Dictionary {k: v}
Duplikate?	    erlaubt	                    nicht möglich	                 Schlüssel eindeutig, Werte beliebig
Reihenfolge?	fest, per Index	            Python 3.7 Einfügereihenfolge
Zugriff	        liste[i]	                kein Index-Zugriff	             dict[schlüssel]

WICHTIGE FALLEN
----------------
{}			ist ein leeres DICT, NICHT ein leeres Set!
set()			ist der richtige Weg für ein leeres Set

menge[0]			FUNKTIONIERT NICHT -- Sets haben keine Indizes/Reihenfolge

{[1,2]}			FEHLER -- Listen können NICHT in ein Set (nicht "hashbar")
			nur unveränderliche Typen erlaubt: int, float, str, tuple, bool
'''