import random
us=0
cs=0
tot=list(("_"*10))
tot2=list(("_"*10))
tot2[0]='F'
def userstart():
    global us
    global cs
    while(us<20 and cs<20):
        print("USER'S TURN")
        i=input("If you're ready click s/S : ")
        if i.lower()=='s':
            uc=random.randint(1,6)
            us+=uc
            if uc==1:
                print("   ")
                print(" o ")
                print("   ")
            elif uc==2:
                print("o")
                print("    ")
                print("   o")
            elif uc==3:
                print("o")
                print("  o ")
                print("    o")
            elif uc==4:
                print("o   o")
                print("     ")
                print("o   o")
            elif uc==5:
                print("o   o")
                print("  o  ")
                print("o   o")
            elif uc==6:
                print("o   o")
                print("o   o")
                print("o   o")
            else:
                userstart()
            if us==cs:
                cs=0
                if 'C' in tot:
                    tot[tot.index('C')]='_'
                if 'C' in tot2:
                    tot2[tot2.index('C')]='_'
                print('\r')
                print("COMPUTER OUT")
                print("COMPUTER START THE GAME FROM FIRST !! ")
            if us<=10:
                if "U" in tot:
                    tot[tot.index('U')]='_'
                tot[us-1]="U"
            elif us>10 and us<=20:
                if "U" in tot2:
                    tot2[tot2.index('U')]='_'
                if "U" in tot:
                    tot[tot.index('U')]='_'
                tot2[20-us]="U"
                if us==20:
                    print('\r')
                    for i in tot2:
                        print(i,end=" ")
                    print("\n")
                    for j in tot:
                        print(j,end=" ")
                    print("\n")
                    print("USER WON")
                    break
            else:
                print("USER WON")
                break
            for i in tot2:
                print(i,end=" ")
            print("\n")
            for j in tot:
                print(j,end=" ")
            print("\n")
            compstart()
        else:
            userstart()
def compstart():
    global cs
    global us
    while(cs<20 and us<20):
        print("COMPUTER'S TURN")
        uc=random.randint(1,6)
        cs+=uc
        if uc==1:
            print("   ")
            print(" o ")
            print("   ")
        elif uc==2:
            print("o")
            print("    ")
            print("   o")
        elif uc==3:
            print("o")
            print("  o ")
            print("    o")
        elif uc==4:
            print("o   o")
            print("     ")
            print("o   o")
        elif uc==5:
            print("o   o")
            print("  o  ")
            print("o   o")
        elif uc==6:
            print("o   o")
            print("o   o")
            print("o   o")
        else:
            compstart()
        if cs==us:
            us=0
            if 'U' in tot:
                tot[tot.index('U')]='_'
            if 'U' in tot2:
                tot2[tot2.index('U')]='_'
            print('\r')
            print("USER OUT")
            print("USER START THE GAME FROM FIRST !! ")
        if cs<=10:
            if "C" in tot:
                tot[tot.index('C')]='_'
            tot[cs-1]="C"
        elif cs>10 and cs<=20:
            if "C" in tot2:
                tot2[tot2.index('C')]='_'
            if "C" in tot:
                tot[tot.index('C')]='_'
            tot2[20-cs]="C"
            if cs==20:
                print("\r")
                for i in tot2:
                    print(i,end=" ")
                print("\n")
                for j in tot:
                    print(j,end=" ")
                print("\n")
                print("COMPUTER WON")
                break
        else:
            print("COMPUTER WON")
            break
        for i in tot2:
            print(i,end=" ")
        print("\n")
        for j in tot:
            print(j,end=" ")
        print("\n")
        userstart()
   

print("DICE ROLL")
print("2 users can play this game")
print("The game is on who reaches the end point first")
print("If both coins meet at same place then another user starts from first")
print("\r")
while("True"):
    i=input("Enter your choice o/O for odd e/E for even : ")
    if i not in ["o","e","E","O"]:
        print("Enter the proper choice!!")
        continue
    i1=int(input("Enter the number : "))
    if i1==0 or i1>6:
        print("Enter number only from 1 to 10")
        continue
    u=random.randint(1,6)
    print("Computer number",u)
    if i=="o" or i=="O":
        if (i1+u)%2==0:
            print("You LOST")
            print('\r')
            compstart()
            userstart()
            break
        else:
            print("You WON!!!")
            print('\r')
            userstart()
            compstart()
            break
    else:
        if (i1+u)%2==0:
            print("You WON!!!")
            print('\r')
            userstart()
            compstart()
            break
        else:
            print("You LOST")
            print('\r')
            compstart()
            userstart()
            break
