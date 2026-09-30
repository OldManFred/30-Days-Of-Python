#Eine Funktion kann auch eine Funktion als Parameter bekommen
def addTwo(firstNumber,secondNumber):
        return firstNumber+secondNumber
    

def subTwo(firstNumber,secondNumber):
        return firstNumber-secondNumber
    
def divTwo(firstNumber,secondNumber):
        return firstNumber/secondNumber
    
def mulTwo(firstNumber,secondNumber):
        return firstNumber*secondNumber


def call_function(function,firstNumber,secondNumber):#bekommnt Funktion und Parameter
    return function(firstNumber,secondNumber)# ruft die übergebene Funktion auf.


if __name__ == '__main__':
    while(True):
        firstNumber = int(input('Nummer 1 ?'))
        secondNumber = int(input('Nummer 2 ?'))
        func=input('Funktion ?')
        if func=='+':
            result = call_function(addTwo,firstNumber,secondNumber)
        elif func=='-':
            result = call_function(subTwo,firstNumber,secondNumber)
        elif func=='/':
            result = call_function(divTwo,firstNumber,secondNumber)
        elif func=='*':
            result = call_function(mulTwo,firstNumber,secondNumber)
        else:
            print(f'No Function {func}')
        print(f'Result: {result}')