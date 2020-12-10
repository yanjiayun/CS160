from random import randint
def check_int(a):
    while True:
        try:
            x = int(input(a))
        except ValueError:
            print("Error! Plz enter again!")
            continue
        else:
            return x

def check_b(a):
    while True:
        x = check_int(a)
        if (x == 1 or x == 2):
            return x
        else:
            print("Error! Plz enter again!")
            continue

def check_3(a):
    while True:
        x = check_int(a)
        if (x == 1 or x == 2 or x == 3):
            return x
        else:
            print("Error! Plz enter again: ")
            continue

def check_string(a):
    while True:
        x = input(a)
        try:
            if x.isalpha() and (x == 'O' or x == 'X'):   
                y = str(x)
            else:
                print("Error! Plz enter again!")
                continue
        except ValueError :
            print("Error! Plz enter again!")
            continue
        else: 
            return y

def play1():
    arr1 = [[0 for i in range (3)]for j in range (3)]
    a = (check_string("Please enter the character you would like to choose, X or O: "))
    if (a == 'X'):
        print("The computer will use O.")
        p = 'O'
    elif(a == 'O'):
        print("The computer will use X.")
        p = 'X'
    d = 1
    e = 1
    for q in range(0,4):
        for r in range(0,4):
            if (r != 3):
                print("+----", end = '')
            elif (r == 3):
                print("+", end = '')
        print(" ")
        if(q != 3):
            for t in range (0,4):
                    print("|    ", end = '')
        print(" ")
    for o in range (0,5):
        while(d == 1):
            b = (check_3("Please enter the x-axis(horizontal) position you would like to put(1-3): "))
            c = (check_3("Please enter the y-axis(vertical) position you would like to put(1-3): "))
            if (arr1[b-1][c-1] == 0):
                arr1[b-1][c-1] = 1
                d = 0
            elif(arr1[b-1][c-1] == 1 or arr1[b-1][c-1] == 2):
                print("This cell is not empty! Please enter again!")                      
        for q in range(0,4):
            for r in range(0,4):
                if (r != 3):
                    print("+----", end = '')
                elif (r == 3):
                    print("+", end = '')
            print(" ")
            if(q != 3):
                for t in range (0,4):
                    if (t<=2):
                        if(arr1[t][q] == 1):
                            print("|", a , " ", end = '')
                        elif(arr1[t][q] == 2):
                            print("|", p , " ", end = '')
                        elif(arr1[t][q] == 0):
                            print("|    " , end = '')
                    if(t == 3):
                        print("|    " , end = '')
            print(" ")
        while(e == 1):
            f = randint(1,3)
            k = randint(1,3)
            if (arr1[f-1][k-1] == 0):
                arr1[f-1][k-1] = 2
                e = 0
        print("After computer: ")
        for q in range(0,4):
            for r in range(0,4):
                if (r != 3):
                    print("+----", end = '')
                elif (r == 3):
                    print("+", end = '')
            print(" ")
            if(q != 3):
                for t in range (0,4):
                    if (t<=2):
                        if(arr1[t][q] == 1):
                            print("|", a , " ", end = '')
                        elif(arr1[t][q] == 2):
                            print("|", p , " ", end = '')
                        elif(arr1[t][q] == 0):
                            print("|    " , end = '')
                    if(t == 3):
                        print("|    ", end = '')
            print(" ")
        d = 1
        e = 1
        if(arr1[0][0]==arr1[1][0]==arr1[2][0]==1 or arr1[0][1]==arr1[1][1]==arr1[2][1]==1 or arr1[0][2]==arr1[1][2]==arr1[2][2]==1 or arr1[0][0]==arr1[0][1]==arr1[0][2]==1 or arr1[1][0]==arr1[1][1]==arr1[1][2]==1 or arr1[2][0]==arr1[2][1]==arr1[2][2]==1 or arr1[0][0]==arr1[1][1]==arr1[2][2]==1 or arr1[0][2]==arr1[1][1]==arr1[2][0]==1):
            print("Congratulations Player 1, you are a winner!!!")
            break
        elif(arr1[0][0]==arr1[1][0]==arr1[2][0]==2 or arr1[0][1]==arr1[1][1]==arr1[2][1]==2 or arr1[0][2]==arr1[1][2]==arr1[2][2]==2 or arr1[0][0]==arr1[0][1]==arr1[0][2]==2 or arr1[1][0]==arr1[1][1]==arr1[1][2]==2 or arr1[2][0]==arr1[2][1]==arr1[2][2]==2 or arr1[0][0]==arr1[1][1]==arr1[2][2]==2 or arr1[0][2]==arr1[1][1]==arr1[2][0]==2):
            print("Computer is the winner!!!")
            break
        if(o == 3):
            print("A draw!!!")
            break

def play2():
    arr1 = [[0 for i in range (3)]for j in range (3)]
    a = (check_string("Player1, please enter the character you would like to choose, X or O: "))
    if (a == 'X'):
        print("Player2 will use O.")
        p = 'O'
    elif(a == 'O'):
        print("Player2 will use X.")
        p = 'X'
    d = 1
    e = 1
    for q in range(0,4):
        for r in range(0,4):
            if (r != 3):
                print("+----", end = '')
            elif (r == 3):
                print("+", end = '')
        print(" ")
        if(q != 3):
            for t in range (0,4):
                    print("|    ", end = '')
        print(" ")
    for o in range (0,5):
        while(d == 1):
            b = (check_3("Player1, please enter the x-axis(horizontal) position you would like to put(1-3): "))
            c = (check_3("Player1, please enter the y-axis(vertical) position you would like to put(1-3): "))
            if (arr1[b-1][c-1] == 0):
                arr1[b-1][c-1] = 1
                d = 0
            elif(arr1[b-1][c-1] == 1 or arr1[b-1][c-1] == 2):
                print("This cell is not empty! Please enter again!")                      
        for q in range(0,4):
            for r in range(0,4):
                if (r != 3):
                    print("+----", end = '')
                elif (r == 3):
                    print("+", end = '')
            print(" ")
            if(q != 3):
                for t in range (0,4):
                    if (t<=2):
                        if(arr1[t][q] == 1):
                            print("|", a , " ", end = '')
                        elif(arr1[t][q] == 2):
                            print("|", p , " ", end = '')
                        elif(arr1[t][q] == 0):
                            print("|    " , end = '')
                    if(t == 3):
                        print("|    " , end = '')
            print(" ")
        if(arr1[0][0]==arr1[1][0]==arr1[2][0]==1 or arr1[0][1]==arr1[1][1]==arr1[2][1]==1 or arr1[0][2]==arr1[1][2]==arr1[2][2]==1 or arr1[0][0]==arr1[0][1]==arr1[0][2]==1 or arr1[1][0]==arr1[1][1]==arr1[1][2]==1 or arr1[2][0]==arr1[2][1]==arr1[2][2]==1 or arr1[0][0]==arr1[1][1]==arr1[2][2]==1 or arr1[0][2]==arr1[1][1]==arr1[2][0]==1):
            print("Congratulations Player1, you are a winner!!!")
            break
        elif(arr1[0][0]==arr1[1][0]==arr1[2][0]==2 or arr1[0][1]==arr1[1][1]==arr1[2][1]==2 or arr1[0][2]==arr1[1][2]==arr1[2][2]==2 or arr1[0][0]==arr1[0][1]==arr1[0][2]==2 or arr1[1][0]==arr1[1][1]==arr1[1][2]==2 or arr1[2][0]==arr1[2][1]==arr1[2][2]==2 or arr1[0][0]==arr1[1][1]==arr1[2][2]==2 or arr1[0][2]==arr1[1][1]==arr1[2][0]==2):
            print("Congratulations Player2, you are a winner!!!")
            break
        if(o == 3):
            print("A draw!!!")
            break
        while(e == 1):
            f = (check_3("Player2, please enter the x-axis(horizontal) position you would like to put(1-3): "))
            k = (check_3("Player2, please enter the y-axis(vertical) position you would like to put(1-3): "))
            if (arr1[f-1][k-1] == 0):
                arr1[f-1][k-1] = 2
                e = 0
            elif(arr1[f-1][k-1] == 1 or arr1[f-1][k-1] == 2):
                print("This cell is not empty! Please enter again!") 
        print("After Player2: ")
        for q in range(0,4):
            for r in range(0,4):
                if (r != 3):
                    print("+----", end = '')
                elif (r == 3):
                    print("+", end = '')
            print(" ")
            if(q != 3):
                for t in range (0,4):
                    if (t<=2):
                        if(arr1[t][q] == 1):
                            print("|", a , " ", end = '')
                        elif(arr1[t][q] == 2):
                            print("|", p , " ", end = '')
                        elif(arr1[t][q] == 0):
                            print("|    " , end = '')
                    if(t == 3):
                        print("|    ", end = '')
            print(" ")
        d = 1
        e = 1
        if(arr1[0][0]==arr1[1][0]==arr1[2][0]==1 or arr1[0][1]==arr1[1][1]==arr1[2][1]==1 or arr1[0][2]==arr1[1][2]==arr1[2][2]==1 or arr1[0][0]==arr1[0][1]==arr1[0][2]==1 or arr1[1][0]==arr1[1][1]==arr1[1][2]==1 or arr1[2][0]==arr1[2][1]==arr1[2][2]==1 or arr1[0][0]==arr1[1][1]==arr1[2][2]==1 or arr1[0][2]==arr1[1][1]==arr1[2][0]==1):
            print("Congratulations Player1, you are a winner!!!")
            break
        elif(arr1[0][0]==arr1[1][0]==arr1[2][0]==2 or arr1[0][1]==arr1[1][1]==arr1[2][1]==2 or arr1[0][2]==arr1[1][2]==arr1[2][2]==2 or arr1[0][0]==arr1[0][1]==arr1[0][2]==2 or arr1[1][0]==arr1[1][1]==arr1[1][2]==2 or arr1[2][0]==arr1[2][1]==arr1[2][2]==2 or arr1[0][0]==arr1[1][1]==arr1[2][2]==2 or arr1[0][2]==arr1[1][1]==arr1[2][0]==2):
            print("Congratulations Player2, you are a winner!!!")
            break
        if(o == 3):
            print("A draw!!!")
            break

def main():
    a = (check_b("How many player you would like to include: "))
    if (a == 1):
        play1()
    elif(a == 2):
        play2()

main()