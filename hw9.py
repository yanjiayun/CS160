from wire_plotter import Wire_Plotter
def check_int(a):
    while True:
        try:
            x = int(input(a))
        except ValueError:
            print("Error! Plz enter again: ")
            continue
        else:
            return x

def check_number(a):
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

def check_pfloat(a):
    while True:
        x = check_number(a)
        if (x >= 0):
            return x
        else:
            print("Error! Plz enter again!")
            continue

def check_b(a):
    while True:
        x = check_int(a)
        if (x == 0 or x == 1):
            return x
        else:
            print("Error! Plz enter again: ")
            continue

def main():
    a = 0
    wire = []
    temp = []
    while a == 0:
        k = (check_number("Please enter the thermal conductivity(k):"))
        p = (check_pfloat("Please enter the density(ρ): "))
        c = (check_pfloat("Please enter the specific heat(c): "))
        it = (check_number("Please enter the initial temperature: "))
        lt = (check_number("Please enter the left boundary condition: "))
        rt = (check_number("Please enter the right boundary condition: "))
        l = (check_number("Please enter the length of wire: "))
        s = (check_pfloat("Please enter the sections of wire: "))
        t = (check_pfloat("Please enter the time intervals: "))
        ct = (check_pfloat("Please enter the change in time: "))
        if abs((k*ct)/(s**2*c*p)) >= 0.5:
            print("It's not stable, please enter all the values again!")
        else:
            a = 1
    dx = l/s
    coefficient = (ct*k)/(dx**2*c*p)
    wire.append(lt)
    for i in range (1,s-1):
        wire.append(it)
    wire.append(rt)
    temp = [it]*s
    temp[0] = lt
    temp[s-1] = rt
    plotter = Wire_Plotter(l, s, lt, rt, True)
    for b in range (0,t):
        print(b)
        for d in range (1,s-1):
            wire[d] = (coefficient*(temp[d+1]-2*temp[d]+temp[d-1])+temp[d])
        print(wire)
        temp = wire [:]
        plotter.add_interval(wire)
    plotter.animate()
main()