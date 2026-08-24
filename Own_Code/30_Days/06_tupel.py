#tupel
tpl1=('Brot','Kaese','Wurst','Schinken')
print(type(tpl1))
print(tpl1)
print('Items: ',len(tpl1))
for item in tpl1:
    print(item)
#index
print(tpl1[0])
#negativer Index -1 letztes Item u.s.w.
print(tpl1[-1])
#slicing
print('slicing direct: ',tpl1[0:2]) #stop exclusive
#slicing mit Schrittweite
print('slicing direct Schrittw. 2 : ',tpl1[0:4:2]) #stop exclusive
print('reverse: ',tpl1[::-1]) #rückwärts
print('reverse: ',tpl1[-2:-4:-1]) #rückwärts stop exclusive
#tupel zu Liste13
lst1=list(tpl1)
print('Liste: ',lst1)# list is mutable
lst1.append('Tomate')
print(type(lst1),lst1)
tpl2=tuple(lst1)#zurück zu tuple
print(type(tpl2),tpl2)
#Item abfragen
if 'Wurst' in tpl2:
    print(tpl2[tpl2.index('Wurst')]) #overkill, Index ermitteln und Element an Index ausgeben
#joining
tpl3=('Milch','Skyr')
tpl_all=tpl2 + tpl3
print('joined: ',tpl_all)
print('Items: ',len(tpl_all))
tupeltest=(2,7,11,2,5,3)
#Element zählen
z=tupeltest.count(3)
print(f"count 3: {z}")
#Index von Element
z=tupeltest.index(7)
print(f"index 7: {z}")
#slicing gibt immer den Type des 'gesliceten zurück
print('Slicing:',tupeltest[1:4:2])
#sorting gibt immer liste zurück
print('Sorted:',sorted(tupeltest))
#zip
tplMetalle=('Gold','Silber','Mercury','Eisen')
tplOrdnungsz=(79,47,80,26)
#zip ist iterator, wird beim auslesen verbraucht
x=(zip(tplMetalle,tplOrdnungsz))
print(type(x))
Periodens=list(x)
print('iterator zip ausgelesen',Periodens)
Periodens=list(x)
print('iterator zip verbraucht',Periodens)



