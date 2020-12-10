print("You wake up in a dark cave :( \nThere are 4 rooms in your 4 directions, and there are may be danger, but there may also be treasure. How do you choose?");
a = int(input("East-1, South-2, West-3, North-4 and Stay here-5: "))
if(a==1):
    print("It's an empty room.")
    a1 = int(input("What do you want to do? 1:Shouting or 2:Knock on wall -2: "))
    if(a1==1):
        print("The villagers nearby heard your voice and rescured you.")
        print("You got result A: Escape from the cave.")
    elif(a1==2):
        print("You woke up the monster, it come and eat you.")
        print("You got result B: Got eaten.")
    elif(a1!=1 and a1!=2):
        print("Bad input!")
elif(a==2):
    print("There is a monster sleeping in the corner.")
    a2 = int(input("What do you want to do? 1:Turn around and run or 2:Go over and hit it on the head: "))
    if(a2==1):
        print("You still disturb the monster, it is very angry. You were eaten.")
        print("You got result B: Got eaten.")
    elif(a2==2):
        print("No one had ever dare to hit the monster!!! But the monster thought you are special and gave you the treasure.");
        print("You got result C: Got treasure.")
    elif(a2!=1 and a2!=2):
        print("Bad input!")
elif(a==3):
    print("The room is full of bats!")
    a3 = int(input("What do you want to do? 1:Drive the bats out or 2:Sing a song: "))
    if(a3==1):
        print("The bats got angry, and they took you to the 1000 meters' trap. You fell to your death.")
        print("You got result D: Fall to death.")
    elif(a3==2):
        print("Your voice sounds really frightening, but bats like that so they took you out of cave.")
        print("You got result A: Escape from the cave.")
    elif(a3!=1 and a3!=2):
        print("Bad input!")
elif(a==4):
    print("This is a 1000 meter's trap!")
    a4 = int(input("What do you want to do when falling? 1:Struggle or 2:Doing nothing: "))
    if(a4==1):
        print("It's didn't work, you fell to your death.")
        print("You got result D: Fall to death.")
    elif(a4==2):
        print("You fell to your death.")
        print("You got result D: Fall to death.")
    elif(a4!=1 and a4!=2):
        print("Bad input!")
elif(a==5):
    a5 = int(input("What do you want to do? 1:Close your eyes and pray or 2:Doing nothing: "))
    if(a5==1):
        print("The Bats found you! But they're in good mood today and took you out of cave.")
        print("You got result A: Escape from the cave.")
    elif(a5==2):
        print("You feel hungry, and you are starving to death.")
        print("You got result E: Starving to death.")
    elif(a5!=1 and a5!=2):
        print("Bad input!")
elif(a!=1 and a!=2 and a!=3 and a!=4 and a!=5):
    print("Bad input!")