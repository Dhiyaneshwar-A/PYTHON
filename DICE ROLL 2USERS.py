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
        print("USER 1'S TURN")
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
                print("USER 2 OUT")
                print("USER 2 START THE GAME FROM FIRST !! ")
            if us<=10:
                if "U" in tot:
                    tot[tot.index('U')]='_'
                tot[us-1]="U"
            elif us>10 and us<=20:
                if "U" in tot2:
                    tot2[tot2.index('U')]='_'
                if "U" in tot:
                    tot[tot.index('U')]='_'
                tot2[10-us]="U"
                if us==20:
                    print('\r')
                    for i in tot2:
                        print(i,end=" ")
                    print("\n")
                    for j in tot:
                        print(j,end=" ")
                    print("\n")
                    print("USER 1 WON")
                    break
            else:
                print("USER 1 WON")
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
    while(us<20 and cs<20):
        print("USER 2'S TURN")
        i=input("If you're ready click r/R : ")
        if i.lower()=='r':
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
                userstart()
            if us==cs:
                us=0
                if 'U' in tot:
                    tot[tot.index('U')]='_'
                if 'U' in tot2:
                    tot2[tot2.index('U')]='_'
                print('\r')
                print("USER 1 OUT")
                print("USER 1 START THE GAME FROM FIRST !! ")
            if cs<=10:
                if "C" in tot:
                    tot[tot.index('C')]='_'
                tot[cs-1]="C"
            elif cs>10 and cs<=20:
                if "C" in tot2:
                    tot2[tot2.index('C')]='_'
                if "C" in tot:
                    tot[tot.index('C')]='_'
                tot2[10-cs]="C"
                if cs==20:
                    print('\r')
                    for i in tot2:
                        print(i,end=" ")
                    print("\n")
                    for j in tot:
                        print(j,end=" ")
                    print("\n")
                    print("USER 2 WON")
                    break
            else:
                print("USER 2 WON")
                break
            for i in tot2:
                print(i,end=" ")
            print("\n")
            for j in tot:
                print(j,end=" ")
            print("\n")
            userstart()
        else:
            compstart()                
print("DICE ROLL")
print("2 users can play this game")
print("The game is on who reaches the end point first")
print("If both coins meet at same place then another user starts from first")
print("\r")
toss=input("Enter t/T to start toss : ")
if toss.lower()=='t':
    print("It's a random choice of selecting players")
    print("Decide who is user 1 and who is user 2")
    print("If a random number is odd USER 1 WINS else USER 2 WINS")
print('\r')
sta=input("Enter Y/y to Start the game : ")
print("USER 1 => U")
print("USER 2 => C")
print('\r')
while(sta.lower()=='y'):
    i=random.randint(1,10)
    print(i)
    if i%2!=0:
        print("It's ODD")
        print("USER 1 WON!!!")
        print('\r')
        userstart()
        compstart()
        break
    else:
        print("It's EVEN")
        print("USER 2 WON!!!")
        print('\r')
        compstart()
        userstart()
        break
