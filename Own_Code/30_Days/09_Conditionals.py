print('And now for something compleatly differnt....Conditionals')
fibo=[0,1,1,2,3,5,8,13,21,34,55,89]

if fibo[0]+fibo[1]  == fibo[2] and fibo[1]+fibo[2] == fibo[3]:
    print('could be Fibonacci')
else:
     print('can\'t be Fibonacci')
#names = ['Linda','Claudia','Eva','Zoe']
#names = ['Walter','Horst','Karl','Dieter']
names = ['Rufus','Hasso','K9']
if 'Claudia' in names:
    print('It\'s a girl!')
elif 'Horst' in names:
    print('It\'s a boy!')
else:
    print('You got a doggy!')
print('It\'s a girl!') if 'Claudia' in names else print('its something else')#shorthand code for true if condition else code for false
if fibo[0]+fibo[1]  == fibo[2]:
    if fibo[1]+fibo[2]  == fibo[3]: #nested
        print('Fibonacci possible')
    else:
        print('sorry no Fibonacci')
if 'Claudia' in names and 'Zoe' in names: #bool
    print('Twin girls')
if 'Claudia' in names or 'Horst' in names:
    print('At least it\'s human.')
else:
    print('A dog is mans best friend!')
a = input('Enter a number 0...100:  ')
a = int(a)
if a >= 0 and a <= 100:
    if a in fibo:
        print('part of Fibonacci sequence!')
    else:
        print('sorry no Fibonacci number.')
else:
    print('Follow the instructions!')
a = int(input('How many pull-ups can you do ? '))
if a == 0:
    print('Go work out!!')
elif a < 5 :
    print('at least something!')
elif a < 10:
    print('not bad!')
elif a < 15:
    print('way above average!')
elif a < 20:
    print('outstanding!!')
else: #Alle anderen Fälle
    print('Excellent!!!')
    
colours=['blue','red','green']
col = input('your favorite color: ')
if col in colours:
    print(f'Colour {col} is already known!')
else:
    colours.append(col)
    print('appended: ',col)
    print(colours)
myDict={'Firstname':'Manfred','Lastname':'Kuehne','Age':59,'Profession':'Mechanic','IsSingle':False}
if 'Firstname' in myDict.keys():
    print('Hello ',myDict['Firstname'])
else:
    print('Hello stranger')
if myDict['Age'] < 20:
    print('Youth has the right to be foolish!')
else:
    print(f"At {myDict['Age']}  you are still not old.")
print(f"{myDict['Firstname']} is not married") if myDict['IsSingle'] else print(f"{myDict['Firstname']} is  married") 
        

