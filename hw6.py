def check_int(a):
    while True:
        try:
            x = int(input(a))
        except ValueError:
            print("Error! Plz enter again: ")
            continue
        else:
            return x

def check_p_int(a):
    while True:
        x = check_int(a)
        if (x > 0):
            return x
        else:
            print("Error! Plz enter again!")
            continue

def check_choose3(a):
    while True:
        x = check_int(a)
        if (x == 1 or x == 2 or x == 3):
            return x
        else:
            print("Error! Plz enter again: ")
            continue

def check_choose2(a):
    while True:
        x = check_int(a)
        if (x == 1 or x == 2):
            return x
        else:
            print("Error! Plz enter again: ")
            continue

def sum_f1():
    while True:
        a = (check_int("Please enter the starting point (should be an integerl number): ")) 
        b = (check_int("Please enter the ending point (should be an integerl number, and equal or greater than a): "))
        if (b < a):
            print("Error! Plz enter again: ")
            continue
        elif(b >= a):
            x = a
            y = 0
            for x in range(a,b+1):
                y += 10*x**2
                x += 1
            print("The result is: ", y)
            return a

def sum_f2():
    while True:
        a = (check_int("Please enter the starting point (should be an integerl number): ")) 
        b = (check_int("Please enter the ending point (should be an integerl number, and equal or greater than a): "))
        if (b < a):
            print("Error! Plz enter again: ")
            continue
        elif(b >= a):
            x = a
            y = 0
            for x in range(a,b+1):
                y += ((2*x**2)-5)
                x += 1
            print("The result is: ", y)
            return a

def sum_f3():
    while True:
        a = (check_int("Please enter the starting point (should be an integerl number): ")) 
        b = (check_int("Please enter the ending point (should be an integerl number, and equal or greater than a): "))
        if (b < a):
            print("Error! Plz enter again: ")
            continue
        elif(b >= a):
            x = a
            y = 0
            for x in range(a,b+1):
                y += (x+20)
                x += 1
            print("The result is: ", y)
            return a

def count_sum():
    a = (check_choose3("1: f(x)=10x^2\n2: f(x)=2x^2-5\n3: f(x)=x+20\nWhich function would you like: "))
    if(a == 1):
        sum_f1()
    elif(a == 2):
        sum_f2()
    elif(a == 3):
        sum_f3()
    return a

def r_integral_f1():
    while True:
        a = (check_int("Please enter the starting point (should be an integerl number): ")) 
        b = (check_int("Please enter the ending point (should be an integerl number, and equal or greater than a): "))
        if (b < a):
            print("Error! Plz enter again: ")
            continue
        elif(b >= a):
            n = (check_p_int("Please enter the number of rectangle(should be a positive integral): "))
            area = 0
            w = ((b-a)/n)
            for x in range(1,n+1):
                area += (10*(a+x*w)**2)*w
                x += 1
            print("The result is: ", area)
            return a

def r_integral_f2():
    while True:
        a = (check_int("Please enter the starting point (should be an integerl number): ")) 
        b = (check_int("Please enter the ending point (should be an integerl number, and equal or greater than a): "))
        if (b < a):
            print("Error! Plz enter again: ")
            continue
        elif(b >= a):
            n = (check_p_int("Please enter the number of rectangle(should be a positive integral): "))
            area = 0
            w = ((b-a)/n)
            for x in range(1,n+1):
                area += ((2*(a+x*w)**2)-5)*w
                x += 1
            print("The result is: ", area)
            return a

def r_integral_f3():
    while True:
        a = (check_int("Please enter the starting point (should be an integerl number): ")) 
        b = (check_int("Please enter the ending point (should be an integerl number, and equal or greater than a): "))
        if (b < a):
            print("Error! Plz enter again: ")
            continue
        elif(b >= a):
            n = (check_p_int("Please enter the number of rectangle(should be a positive integral): "))
            area = 0
            w = ((b-a)/n)
            for x in range(1,n+1):
                area += ((a+x*w)+20)*w
                x += 1
            print("The result is: ", area)
            return a

def r_integral():
    a = (check_choose3("1: f(x)=10x^2\n2: f(x)=2x^2-5\n3: f(x)=x+20\nWhich function would you like: "))
    if(a == 1):
        r_integral_f1()
    elif(a == 2):
        r_integral_f2()
    elif(a == 3):
        r_integral_f3()
    return a

def t_integral_f1():
    while True:
        a = (check_int("Please enter the starting point (should be an integerl number): ")) 
        b = (check_int("Please enter the ending point (should be an integerl number, and equal or greater than a): "))
        if (b < a):
            print("Error! Plz enter again: ")
            continue
        elif(b >= a):
            n = (check_p_int("Please enter the number of rectangle(should be a positive integral): "))
            area = 0
            w = ((b-a)/n)
            for x in range(1,n+1):
                area += (((10*(a+x*w)**2)+(10*(a+(x-1)*w)**2))/2)*w
                x += 1
            print("The result is: ", area)
            return a

def t_integral_f2():
    while True:
        a = (check_int("Please enter the starting point (should be an integerl number): ")) 
        b = (check_int("Please enter the ending point (should be an integerl number, and equal or greater than a): "))
        if (b < a):
            print("Error! Plz enter again: ")
            continue
        elif(b >= a):
            n = (check_p_int("Please enter the number of rectangle(should be a positive integral): "))
            area = 0
            w = ((b-a)/n)
            for x in range(1,n+1):
                area += (((2*(a+x*w)**2-5)+(2*(a+(x-1)*w)**2-5))/2)*w
                x += 1
            print("The result is: ", area)
            return a

def t_integral_f3():
    while True:
        a = (check_int("Please enter the starting point (should be an integerl number): ")) 
        b = (check_int("Please enter the ending point (should be an integerl number, and equal or greater than a): "))
        if (b < a):
            print("Error! Plz enter again: ")
            continue
        elif(b >= a):
            n = (check_p_int("Please enter the number of rectangle(should be a positive integral): "))
            area = 0
            w = ((b-a)/n)
            for x in range(1,n+1):
                area += (((a+x*w)+20+(a+(x-1)*w)+20)/2)*w
                x += 1
            print("The result is: ", area)
            return a

def t_integral():
    a = (check_choose3("1: f(x)=10x^2\n2: f(x)=2x^2-5\n3: f(x)=x+20\nWhich function would you like: "))
    if(a == 1):
        t_integral_f1()
    elif(a == 2):
        t_integral_f2()
    elif(a == 3):
        t_integral_f3()
    return a

def main():
    while True:
        b = (check_choose2("What do you want to count? Sum-1 or integrate-2: "))
        if (b == 1):
            count_sum()
        elif(b == 2):
            c = (check_choose2("Which shape do you want to use? Rectangle-1 or trapezoid-2: "))
            if(c == 1):
                r_integral()
            elif(c == 2):
                t_integral()
        d = (check_choose2("Do you want to play again? Yes-1 or No-2: "))
        if (d == 1):
            continue
        elif(d == 2):
            return d

main()