#doppelte Einträge existieren nicht, werden gleich entfernt
myset={'Rolf','Jorge','Peter','Sven','Rolf'}
print(type(myset),myset,'len:',len(myset))
#'in' abfrage
if 'Rolf' in myset:
    print('Rolf ist da')
#sets sind erweiterber
myset.add('Werner')#ein Item
print(type(myset),myset,'len:',len(myset))

myset.update(['Karsten','ALfred','Sascha'])#mehrere Items, braucht Liste als Argument,so...
print(type(myset),myset,'len:',len(myset))
#oder so
mylist=['Dennis','Andre']
myset.update(mylist)
print(type(myset),myset,'len:',len(myset))
#Items entfernen
if 'Sascha' in myset:
    myset.remove('Sascha')#Erzeugt Fehler wenn nicht vorhanden
myset.discard('Karsten')#Erzeugt keinen Fehler wenn nicht vorhanden
gepoppt=myset.pop()# pop entfernt ein random Item und gibt dieses zurück
print(f"entfernt: {gepoppt}")
print(type(myset),myset,'len:',len(myset))
myset1=myset.copy()#set kopieren
myset.clear()
print('myset geleert: ',myset)
print('myset1 : ',myset1)
#typecast
mylist1=list(myset1)
mylist1[0]='Paul'#Sets sind ungeordnet, deshalb trifft es ein random Item
myset=set(mylist1)
print(type(myset),myset,'len:',len(myset))
#joining
myset1.clear()
myset1.update(['Elke','Lydia'])
print(myset1)
print(myset|myset1)#oder myset.union(myset1)
#sets noch nicht verändert
print(myset)
print(myset1)
#Einfügen eines sets in ein anderes
myset1.update(myset)
print(type(myset),myset1,'len:',len(myset1))
myset.clear()
myset={'Erde','Feuer','Luft'}
myset1.clear
myset1={'Wasser','Luft','Erde'}
#In beiden Sets vorkommende Items als Set
result=myset&myset1 #Oder myset.intersection(myset1)
print(type(result),result)
myset.clear()
myset1.clear()
myset={2,3,5,7,11,13,17}
myset1={11,13,19}
#subset und superset machen das gleiche von unterschiedlichen Standpunkten aus
if myset1.issubset(myset): #Alles von myset1 muss in myset vorkommen
    print('issubset')
if myset.issuperset(myset1): # myset muss alles von myset1 enthalten
    print('issuperset')
print(myset.difference(myset1))#Welche Items von myset sind nicht in myset1
print(myset1.difference(myset))#Welche Items von myset1 sind nicht in myset
print('symmetric_difference: ',myset1.symmetric_difference(myset))#Welche Items sind nur in jeweils einem Set vorhanden ?
#Haben die Sets gemeinsame Items ?
myset.clear()
myset1.clear()
myset={2,3,5,8}
myset1={13,21,34}#keine gleichen Items in beiden sets
print('disjoint: ',myset.isdisjoint(myset1))
myset1.add(8)#Item in beiden Sets
print('disjoint: ',myset.isdisjoint(myset1))