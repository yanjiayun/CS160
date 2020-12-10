import turtle
from random import randint

def check_int(a):
  while True:
    try:
      x = int(input(a))
    except ValueError:
      print("Error! Plz enter an integer number!")
      continue
    else:
      return x

def check_choose(a):
  while True:
    x = check_int(a)
    if (x==1 or x==2 or x==3 or x==4 or x==5):
      return x
    else:
      print("Error! Plz enter again! You can only choose from 1 to 5!")
      continue

def draw_J(myTurtle):
  turtle.down()
  turtle.fd(60)
  turtle.bk(30)
  turtle.right(90)
  turtle.fd(120)
  turtle.right(90)
  turtle.fd(30)
  turtle.pu()
  turtle.right(180)
  turtle.fd(80)
  turtle.left(90)
  turtle.fd(120)
  turtle.right(90)

def draw_Y(myTurtle):
  turtle.down()
  turtle.right(45)
  turtle.fd(45)
  turtle.left(90)
  turtle.fd(45)
  turtle.bk(45)
  turtle.right(135)
  turtle.fd(90)
  turtle.pu()
  turtle.left(90)
  turtle.fd(110)
  turtle.left(90)
  turtle.fd(120)
  turtle.right(90)

def initial(myTurtle):
  draw_J(myTurtle)
  draw_Y(myTurtle)

def draw_E(myTurtle):
  turtle.down()
  turtle.right(90)
  turtle.fd(120)
  turtle.bk(120)
  turtle.left(90)
  turtle.fd(60)
  turtle.bk(60)
  turtle.right(90)
  turtle.fd(60)
  turtle.left(90)
  turtle.fd(60)
  turtle.bk(60)
  turtle.right(90)
  turtle.fd(60)
  turtle.left(90)
  turtle.fd(60)
  turtle.pu()
  turtle.fd(20)
  turtle.left(90)
  turtle.fd(120)
  turtle.right(90)

def draw_G(myTurtle):
  turtle.down()
  turtle.fd(60)
  turtle.bk(60)
  turtle.right(90)
  turtle.fd(120)
  turtle.left(90)
  turtle.fd(60)
  turtle.left(90)
  turtle.fd(60)
  turtle.left(90)
  turtle.fd(30)
  turtle.bk(30)
  turtle.pu()
  turtle.right(90)
  turtle.fd(60)
  turtle.right(90)
  turtle.fd(20)

def draw_L(myTurtle):
  turtle.down()
  turtle.right(90)
  turtle.fd(120)
  turtle.left(90)
  turtle.fd(60)
  turtle.pu()
  turtle.fd(80)
  turtle.left(90)
  turtle.fd(120)
  turtle.right(90)

def gel(myTurtle):
  draw_G(myTurtle)
  draw_E(myTurtle)
  draw_L(myTurtle)

def draw_O(myTurtle):
  turtle.down()
  turtle.fd(60)
  turtle.right(90)
  turtle.fd(120)
  turtle.right(90)
  turtle.fd(60)
  turtle.right(90)
  turtle.fd(120)
  turtle.right(90)
  turtle.pu()
  turtle.fd(80)

def joy(myTurtle):
  draw_J(myTurtle)
  draw_O(myTurtle)
  draw_Y(myTurtle)

def draw_B(myTurtle):
  turtle.down()
  turtle.right(90)
  turtle.fd(120)
  turtle.bk(120)
  turtle.right(90)
  turtle.circle(25,-180)
  turtle.right(180)
  turtle.circle(35,-180)
  turtle.pu()
  turtle.fd(55)
  turtle.left(90)
  turtle.fd(120)
  turtle.right(90)

def boy(myTurtle):
  draw_B(myTurtle)
  draw_O(myTurtle)
  draw_Y(myTurtle)

def smile(myTurtle):
  turtle.down()
  turtle.right(90)
  turtle.fd(40)
  turtle.left(90)
  turtle.pu()
  turtle.fd(60)
  turtle.left(90)
  turtle.down()
  turtle.fd(40)
  turtle.pu()
  turtle.bk(40)
  turtle.left(90)
  turtle.fd(60)
  turtle.left(90)
  turtle.fd(40)
  turtle.down()
  turtle.circle(30,180)
  turtle.pu()
  turtle.right(90)
  turtle.fd(80)
  turtle.left(90)
  turtle.fd(80)
  turtle.right(90)

def see1(myTurtle):
  a = randint(1,5)
  if (a == 1):
    initial(myTurtle)
  elif(a == 2):
    gel(myTurtle)
  elif(a == 3):
    joy(myTurtle)
  elif(a == 4):
    boy(myTurtle)
  elif(a == 5):
    smile(myTurtle)

def see2(myTurtle):
  a = randint(1,5)
  b = randint(1,5)
  while (a == b):
    b = randint(1,5)
  
  if (a == 1):
    initial(myTurtle)
  elif(a == 2):
    gel(myTurtle)
  elif(a == 3):
    joy(myTurtle)
  elif(a == 4):
    boy(myTurtle)
  elif(a == 5):
    smile(myTurtle)

  if (b == 1):
    initial(myTurtle)
  elif(b == 2):
    gel(myTurtle)
  elif(b == 3):
    joy(myTurtle)
  elif(b == 4):
    boy(myTurtle)
  elif(b == 5):
    smile(myTurtle)

def see3(myTurtle):
  a = randint(1,5)
  b = randint(1,5)
  c = randint(1,5)
  while (a == b):
    b = randint(1,5)
  while (a == c or b == c):
    c = randint(1,5)

  if (a == 1):
    initial(myTurtle)
  elif(a == 2):
    gel(myTurtle)
  elif(a == 3):
    joy(myTurtle)
  elif(a == 4):
    boy(myTurtle)
  elif(a == 5):
    smile(myTurtle)

  if (b == 1):
    initial(myTurtle)
  elif(b == 2):
    gel(myTurtle)
  elif(b == 3):
    joy(myTurtle)
  elif(b == 4):
    boy(myTurtle)
  elif(b == 5):
    smile(myTurtle)

  if (c == 1):
    initial(myTurtle)
  elif(c == 2):
    gel(myTurtle)
  elif(c == 3):
    joy(myTurtle)
  elif(c == 4):
    boy(myTurtle)
  elif(c == 5):
    smile(myTurtle)

def see4(myTurtle):
  a = randint(1,5)
  b = randint(1,5)
  c = randint(1,5)
  d = randint(1,5)
  while (a == b):
    b = randint(1,5)
  while (a == c or b == c):
    c = randint(1,5)
  while (a == d or b == d or c ==d):
    d = randint(1,5)

  if (a == 1):
    initial(myTurtle)
  elif(a == 2):
    gel(myTurtle)
  elif(a == 3):
    joy(myTurtle)
  elif(a == 4):
    boy(myTurtle)
  elif(a == 5):
    smile(myTurtle)

  if (b == 1):
    initial(myTurtle)
  elif(b == 2):
    gel(myTurtle)
  elif(b == 3):
    joy(myTurtle)
  elif(b == 4):
    boy(myTurtle)
  elif(b == 5):
    smile(myTurtle)

  if (c == 1):
    initial(myTurtle)
  elif(c == 2):
    gel(myTurtle)
  elif(c == 3):
    joy(myTurtle)
  elif(c == 4):
    boy(myTurtle)
  elif(c == 5):
    smile(myTurtle)

  if (d == 1):
    initial(myTurtle)
  elif(d == 2):
    gel(myTurtle)
  elif(d == 3):
    joy(myTurtle)
  elif(d == 4):
    boy(myTurtle)
  elif(d == 5):
    smile(myTurtle)

def see5(myTurtle):
  a = randint(1,5)
  b = randint(1,5)
  c = randint(1,5)
  d = randint(1,5)
  e = randint(1,5)
  while (a == b):
    b = randint(1,5)
  while (a == c or b == c):
    c = randint(1,5)
  while (a == d or b == d or c ==d):
    d = randint(1,5)
  while (a == e or b == e or c == e or d == e):
    e = randint(1,5)

  if (a == 1):
    initial(myTurtle)
  elif(a == 2):
    gel(myTurtle)
  elif(a == 3):
    joy(myTurtle)
  elif(a == 4):
    boy(myTurtle)
  elif(a == 5):
    smile(myTurtle)

  if (b == 1):
    initial(myTurtle)
  elif(b == 2):
    gel(myTurtle)
  elif(b == 3):
    joy(myTurtle)
  elif(b == 4):
    boy(myTurtle)
  elif(b == 5):
    smile(myTurtle)

  if (c == 1):
    initial(myTurtle)
  elif(c == 2):
    gel(myTurtle)
  elif(c == 3):
    joy(myTurtle)
  elif(c == 4):
    boy(myTurtle)
  elif(c == 5):
    smile(myTurtle)

  if (d == 1):
    initial(myTurtle)
  elif(d == 2):
    gel(myTurtle)
  elif(d == 3):
    joy(myTurtle)
  elif(d == 4):
    boy(myTurtle)
  elif(d == 5):
    smile(myTurtle) 

  if (e == 1):
    initial(myTurtle)
  elif(e == 2):
    gel(myTurtle)
  elif(e == 3):
    joy(myTurtle)
  elif(e == 4):
    boy(myTurtle)
  elif(e == 5):
    smile(myTurtle) 

def main():
  myTurtle = turtle.Turtle()
  turtle.pu()
  turtle.goto(-800, 0)
  turtle.down()
  print("I include 5 words and one of them is a smiling face!")
  x = (check_choose("Plz enter how many word(s) you would like to see(1-5): "))
  if (x == 1):
    see1(myTurtle)
  elif(x == 2):
    see2(myTurtle)
  elif(x == 3):
    see3(myTurtle)
  elif(x == 4):
    see4(myTurtle)
  elif(x == 5):
    see5(myTurtle)

main()