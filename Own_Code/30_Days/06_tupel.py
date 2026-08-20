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
#tupel zu Liste
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





