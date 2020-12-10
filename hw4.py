def check_int(a):
    while True:
        try:
            x = int(input(a))
        except ValueError:
            print("Error! Plz enter again!")
            continue
        else:
            return x

def check_float(a):
    while True:
        x = input(a)
        try:
            if "." in x:
                y = float(x)
            else:
                y = int(x)        
        except ValueError :
            print("Error! Plz enter again!")
            continue
        else: 
            return y

def check_pint(a):
    while True:
        x = check_int(a)
        if (x >= 0):
            return x
        else:
            print("Error! Plz enter again!")
            continue

def check_b(a):
    while True:
        x = check_int(a)
        if (x == 1 or x ==0 ):
            return x
        else:
            print("Error! Plz enter again!")
            continue
    
def dtob(x):
    if(x > 1):
        dtob(x//2)
    print(x%2, end = " ")        

def btod():
    print("\nplz enter the binary number from right to left!!!")
    c = 1
    total = 0
    print("Plz enter digital ", c, end = " ")
    a = (check_b(" : "))
    b = (check_b("Do you want to include another number? 0-No and 1-Yes: ")) 
    total += a 
    while b == 1:
        c += 1
        print("Plz enter digital ", c, end = " ")
        a = int(input(" : "))
        if (a == 1):
            total += pow(2, c-1)
        b = (check_b("Do you want to include another number? 0-No and 1-Yes: "))
    print(total)

def programmer():
    a = (check_b("(0:binary to decimal and 1:decimal to binary)\nPlz choose a mode: "))
    if (a == 0):
        btod()
    elif (a == 1):
        x = (check_pint("Plz enter the decimal number: ")) 
        dtob(x)

def operate(a,b,x):
    if (x == 1):
        print(a+b)
    elif(x == 2):
        print(a-b)
    elif(x == 3):
        print(a*b)
    elif(x == 4):
        print(a/b)
    elif(x == 5):
        print(pow(a,b))

def enter1():
    x =  (check_float("Plz enter the first number you want: "))
    return x

def enter2():
    x =  (check_float("Plz enter the second number you want: "))
    return x
def scientific():
    while True:
        x = (check_pint("Plz choose a mathematical operations:\n1 for +, 2 for -, 3 for *, 4 for /, and 5 for **: "))
        if(x != 1 and x != 2 and x != 3 and x != 4 and x != 5):
            print("Error! Plz enter again!")
            continue
        else:
            a = enter1()
            b = enter2()
            operate(a,b,x)
            return x

def play():
    while True:
        x = (check_b("(Plz choose your mode~ Programmer mode-0 and Scientific mode-1 )\nPlz choose a mode: "))
        if (x == 0):
            programmer()
        elif (x == 1):
            scientific()
        a = (check_b("\nDo you want to press1 for switch mode/play again or press0 for exit : "))
        if (a == 0):
            return a
        elif(a == 1):
            continue

play()

