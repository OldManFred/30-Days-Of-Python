#30 days of Python Moduldatei
def is_unique(lst_itemlist):
    return len(set(lst_itemlist))==len(lst_itemlist) #Liste in Set kopieren und Länge vom Liste und Set vergleichen

def is_prime(what_number):
    if what_number==1:
        what_number=False
        return what_number
    is_number_prime=True
    for i in range(2,what_number,1):#Start, Stop exlusive.Step
        if what_number%i==0:
            is_number_prime=False
    return is_number_prime

def C_to_F(Temp):
    return (Temp * 9/5) + 32

def F_to_C(Temp):
    return (Temp-32)*5/9

def generateFibonacci(n):
    fibo=[1] #Liste erzeugen
    a=1
    b=1
    for i in range(n):
        c=a+b   #nächste Fibonaccinummer berechnen
        fibo.append(c) #an Liste hängen
        a=b
        b=c
    return fibo

