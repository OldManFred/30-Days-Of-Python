name = "Manfred"
print(name)
print("len:",len(name))
print("n in name:",'n' in name)
multiline_string='''My name is Manfred, I am old and still want to learn Python.
I hope I can grasp the concept and dont give up.'''
print(multiline_string)
firstname="Manfred"
lastname="Kuehne"
print(firstname + ' ' + lastname) #concatenation
fullname = firstname + ' ' + lastname
print(f"f-string Len: {len(fullname)}")
#escapes
text = "I am a legend \n \r I hope I am not going down. \n\r I rarely use \" \n I used \t Tab and \\n"
print(text)
#3 ways of formatting srings
text = "my name is %s %s. I am %d years old I have %.2f  intelligence" %('Manfred', 'Kuehne',59,99.999)
print(text)
text = "my name is {} {}. I am {} years old I have {:.2f}  intelligence".format('Manfred', 'Kuehne',59,99.999)
print(text)
IQ = 99.999
age=59
text = f"my name is {'Manfred'} {'Kuehne'}. I am {59} years old I have {99.999:.2f}  intelligence"
print(text)
#f-strings
text = f"my name is {firstname} {lastname}. I am {age} years old I have {IQ:.2f}  intelligence"
print(text)
#unpacking
#assigning to variables
a,b,c,d,e,f,g=firstname 
print(b)
#by Index
print(firstname[5]) #index
print(firstname[-1])#last index
print(firstname[-3])#last index but 2
#slicing [start:end:step]
skip=firstname[3:7] #3 bis 6 (7 exclusive)
print('sliced: ',skip)
skip=firstname[::-1] #step backwards
print('::-1 ',skip)
skip=firstname[6:-8:-1] #step backwards, counted from last position (-1) -8 (exclusive) is one left from M
print('6:-8:-1', skip)#Start Position 6, vom Ende des Strings aus -8 Positionen, Schrittweite 1
#slice-Object
slice_obj=slice(3,7)
skip=firstname[slice_obj] #auch in [] wie normales sliche
#Methods
print(skip.capitalize())
print('endswith')
print(lastname.endswith('e')) #True
print('startswith')
print(lastname.startswith('e')) #True
print('count')
print(lastname.count('e',0,6))#substring,start,end(exclusive)
text='Tab\tTab'#Tab einfügen
print(text)
print(text.expandtabs(12))#Replaces tab character with spaces, default tab size is 8.
print(firstname,'find:r ', firstname.find('r'))#position 0-indiziert
names=['Otto','Peter','Hubert','Jorge']#Liste erzeugen
print(f'Das sind alles namen: {names}')# als f-string
for name in names:# in Schleife
    print(f'Das sind alles namen: {name}')
name='Manfred'
skip=name[3:len(name):1]#slicing mit Funktion
print(skip)
name='Manfred Kuehne'
print(name.index('ue',0,12))#first index of substring,start,End, not found: value error1
print(name.find('ue',0,12))#first index of substring,Start,End, not found: -1
print(name.rindex('n',0,len(name)))# höchster index von substring
#Zeichen erkennen
text='bcd'
print('isalpha',text.isalpha())
text='1bcd'
print('isalpha',text.isalpha())
text='1bcd'
print('isalnum',text.isalnum())
text='1bcd'
print('isdecimal',text.isdecimal())
text='1984'
print('isdecimal',text.isdecimal()) #0...9
text='1984²'
print('isdigit',text.isdigit()) #0...9 und einige Charactes
phrase='Hallo ich bin Manfred'
Woerter=phrase.split(' ')#am Leerzeichen auftrennen, splitberzeugt Liste
print('Type: ',type(Woerter),(Woerter))