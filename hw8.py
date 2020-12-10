def check_int(a):
    while True:
        try:
            x = int(input(a))
        except ValueError:
            print("Error! Plz enter again: ")
            continue
        else:
            return x

def check_string(a):
    while True:
        x = input(a)
        try:
            if x.isalpha():   
                y = str(x)
            else:
                print("Error! Plz enter again!")
                continue
        except ValueError :
            print("Error! Plz enter again!")
            continue
        else: 
            return y

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

def check_b(a):
    while True:
        x = check_int(a)
        if (x == 0 or x == 1):
            return x
        else:
            print("Error! Plz enter again: ")
            continue

def occurrences(name, name_number):
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0
    count_f = 0
    count_g = 0
    count_h = 0
    count_i = 0
    count_j = 0
    count_k = 0
    count_l = 0
    count_n = 0
    count_m = 0
    count_o = 0
    count_p = 0
    count_q = 0
    count_r = 0
    count_s = 0
    count_t = 0
    count_u = 0
    count_v = 0
    count_w = 0
    count_x = 0
    count_y = 0
    count_z = 0
    for i in range (0,name_number):
        for a in name[i]:
            if a == 'a' or a == 'A':
                count_a += 1
            elif a == 'b' or a == 'B':
                count_b += 1
            elif a == 'c' or a == 'C':
                count_c += 1
            elif a == 'd' or a == 'D':
                count_d += 1
            elif a == 'e' or a == 'E':
                count_e += 1
            elif a == 'f' or a == 'F':
                count_f += 1
            elif a == 'g' or a == 'G':
                count_g += 1
            elif a == 'h' or a == 'H':
                count_h += 1
            elif a == 'i' or a == 'I':
                count_i += 1
            elif a == 'j' or a == 'J':
                count_j += 1
            elif a == 'k' or a == 'K':
                count_k += 1
            elif a == 'l' or a == 'L':
                count_l += 1
            elif a == 'n' or a == 'N':
                count_n += 1
            elif a == 'm' or a == 'M':
                count_m += 1
            elif a == 'o' or a == 'O':
                count_o += 1
            elif a == 'p' or a == 'P':
                count_p += 1
            elif a == 'q' or a == 'Q':
                count_q += 1
            elif a == 'r' or a == 'R':
                count_r += 1
            elif a == 's' or a == 'S':
                count_s += 1
            elif a == 't' or a == 'T':
                count_t += 1
            elif a == 'u' or a == 'U':
                count_u += 1
            elif a == 'v' or a == 'V':
                count_v += 1
            elif a == 'w' or a == 'W':
                count_w += 1
            elif a == 'x' or a == 'X':
                count_x += 1
            elif a == 'y' or a == 'Y':
                count_y += 1
            elif a == 'z' or a == 'Z':
                count_z += 1
    if (count_a != 0):
        print("There are ", count_a, " a in the name list.")
    if (count_b != 0):
        print("There are ", count_b, " b in the name list.")
    if (count_c != 0):
        print("There are ", count_c, " c in the name list.")
    if (count_d != 0):
        print("There are ", count_d, " d in the name list.")
    if (count_e != 0):
        print("There are ", count_e, " e in the name list.")
    if (count_f != 0):
        print("There are ", count_f, " f in the name list.")
    if (count_g != 0):
        print("There are ", count_g, " g in the name list.")
    if (count_h != 0):
        print("There are ", count_h, " h in the name list.")
    if (count_i != 0):
        print("There are ", count_i, " i in the name list.")
    if (count_j != 0):
        print("There are ", count_j, " j in the name list.")
    if (count_k != 0):
        print("There are ", count_k, " k in the name list.")
    if (count_l != 0):
        print("There are ", count_l, " l in the name list.")
    if (count_n != 0):
        print("There are ", count_n, " n in the name list.")
    if (count_m != 0):
        print("There are ", count_m, " m in the name list.")
    if (count_o != 0):
        print("There are ", count_o, " o in the name list.")
    if (count_p != 0):
        print("There are ", count_p, " p in the name list.")
    if (count_q != 0):
        print("There are ", count_q, " q in the name list.")
    if (count_r != 0):
        print("There are ", count_r, " r in the name list.")
    if (count_s != 0):
        print("There are ", count_s, " s in the name list.")
    if (count_t != 0):
        print("There are ", count_t, " t in the name list.")
    if (count_u != 0):
        print("There are ", count_u, " u in the name list.")
    if (count_v != 0):
        print("There are ", count_v, " v in the name list.")
    if (count_w != 0):
        print("There are ", count_w, " w in the name list.")
    if (count_x != 0):
        print("There are ", count_x, " x in the name list.")
    if (count_y != 0):
        print("There are ", count_y, " y in the name list.")
    if (count_z != 0):
        print("There are ", count_z, " z in the name list.")

def enter_list1(list1):
    a = 1
    c = 0
    while a == 1:
        b = (check_number("Please enter number you want to put it in list 1: "))
        list1.append(b)
        c += 1
        a = (check_b("Do you want to enter another number? 0-No and 1-Yes: "))
    return c    

def enter_list2(list2):
    a = 1
    c = 0
    while a == 1:
        b = (check_number("Please enter number you want to put it in list 2: "))
        list2.append(b)
        c += 1
        a = (check_b("Do you want to enter another number? 0-No and 1-Yes: "))
    return c  

def same_length(a,b):
    if a == b:
        return True
    else:
        return False

def sum_list1(list1_number,list1):
    a = 0
    for i in range (0,list1_number):
        a += list1[i]
    return a

def sum_list2(list2_number,list2):
    a = 0
    for i in range (0,list2_number):
        a += list2[i]
    return a

def average_list1(list1_number,list1):
    a = 0
    for i in range (0,list1_number):
        a += list1[i]
    a = a/list1_number
    return a

def average_list2(list2_number,list2):
    a = 0
    for i in range (0,list2_number):
        a += list2[i]
    a = a/list2_number
    return a

def same_sum(a,b):
    if a == b:
        return True
    else:
        return False

def common_number(a,list1_number,list2_number,list1,list2):
    a = []
    for i in range (0,list1_number):
        for k in range (0,list2_number):
            if list1[i] == list2[k]:
                a.append(list1[i])
    return a

def enter():
    list1 = []
    list1_number = enter_list1(list1)
    list2 = []
    list2_number = enter_list2(list2)
    a = same_length(list1_number,list2_number)
    if a == True:
        print("These two list have the same length.")
    else:
        print("These two list have the different length.")
    sum1 = sum_list1(list1_number,list1)
    sum2 = sum_list2(list2_number,list2)
    print("The sum of list 1 is: ", sum1)
    print("The sum of list 2 is: ", sum2)
    average1 = average_list1(list1_number,list1)
    average2 = average_list2(list2_number,list2)
    print("The average of list 1 is: ", average1)
    print("The average of list 2 is: ", average2)
    b = same_sum(sum1,sum2)
    if b == True:
        print("These two list have the same sum.")
    else:
        print("These two list have the different sum.")
    common = []
    common = common_number(common,list1_number,list2_number,list1,list2)
    print("The common number(s): ", common)
    name = []
    c = 1
    name_number = 0
    while c == 1:
        d = (check_string("Please enter name you want to put it in name list (Enter only letters): "))
        name.append(d)
        name_number += 1
        c = (check_b("Do you want to enter another number? 0-No and 1-Yes: "))
    occurrences(name,name_number)
    
enter() 