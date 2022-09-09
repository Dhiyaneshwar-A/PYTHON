import random
ch=random.randint(1,6)
print("--------------------------------------------------------------------------------------")
print("WELCOME TO HANDCRICKET ONLINE PYTHON GAME !!!")
print("\r")
print("RULES :")
print("1. ENTER NUMBERS ONLY 1-6")
print("2. IF YOUR CHOICE AND COMPUTER CHOICE IS SAME IT'S AN OUT")
print("3. ONLY 6 BALLS FOR EACH")
print("--------------------------------------------------------------------------------------")
print("TOSS BEGINS!!")
print("\r")
UR=[]
CR=[]
cr=-1
ur=-1
def num():
    global cr
    global ur
    i=int(input("Enter a number for TOSS "))
    if i>6 or i<1:
        num()
    else:
        print("Computer's choice",ch)
        if (i+ch)%2==0:
            print("It's Even")
            if ts=="E":
                print("You WON the toss")
                print("\r")
                choice()
            elif ts=="O":
                print("You LOST the toss")
                print("\r")
                cbc=random.choice(["bat","bowl"])
                if cbc=="bat":
                    print("Computer chose BAT first")
                    cr=combat()
                    print("TARGET : ",cr+1)
                    ur=userbat()
                else:
                    print("Computer chose BOWL first")
                    ur=userbat()
                    print("TARGET : ",ur+1)
                    cr=combat()
        else:
            print("It's Odd")
            if ts=="O":
                print("You WON the toss")
                print("\r")
                choice()
            elif ts=="E":
                print("You LOST the toss")
                print("\r")
                cbc=random.choice(["bat","bowl"])
                if cbc=="bat":
                    print("Computer chose BAT first")
                    cr=combat()
                    print("TARGET : ",cr+1)
                    ur=userbat()
                else:
                    print("Computer chose BOWL first")
                    ur=userbat()
                    print("TARGET : ",ur+1)
                    cr=combat()
                    
def userbat():
    print("--------------------------------------------------------------------------------------")
    print("YOU ARE BATTING RIGHT NOW")
    print("\r")
    i=0
    uruns=0
    while(i<6):
        print("User RUNS : ",uruns)
        print("\r")
        if uruns>cr and cr!=-1:
            print("MATCH ENDS")
            print("\r")
            break
        i+=1
        usernum=int(input("{} ball : Enter a number :".format(i)))
        if usernum>6 or usernum<0:
            i=i-1
            continue
        comnum=random.choice([1,2,3,4,5,6])
        print("Computer's bowling selection ",comnum)
        if(usernum==comnum):
            print("\r")
            print("USER OUT")
            print("\r")
            break
        else:
            uruns=uruns+usernum
            UR.append(usernum)
    else:
        print("\r")
        print("OVER ENDS")
        print("\r")
    print("User Runs : ",uruns)
    return uruns

def combat():
    print("--------------------------------------------------------------------------------------")
    print("YOU ARE BOWLING RIGHT NOW")
    print("\r")
    j=0
    cruns=0
    while(j<6):
        print("Computer RUNS : ",cruns)
        print("\r")
        if cruns>ur and ur!=-1:
            print("MATCH ENDS")
            print("\r")
            break
        j+=1
        usernum=int(input("{} ball : Enter a number :".format(j)))
        if usernum>6 or usernum<0:
            j=j-1
            continue
        comnum=random.choice([1,2,3,4,5,6])
        print("Computer's batting selection ",comnum)
        if(usernum==comnum):
            print("\r")
            print("COMPUTER OUT")
            print("\r")
            break
        else:
            cruns=cruns+comnum
            CR.append(comnum)
    else:
        print("\r")
        print("OVER ENDS")
        print("\r")
    print("Computer Runs : ",cruns)
    return cruns

def choice():
    global cr
    global ur
    bc=int(input("Enter 1 for Batting 2 for Bowling "))
    if bc==1:
        ur=userbat()
        print("TARGET : ",ur+1)
        cr=combat()
    elif bc==2:
        cr=combat()
        print("TARGET : ",cr+1)
        ur=userbat()
    else:
        choice()

def toss():
    global ts
    ts=input("Enter O for odd E for even ")
    if ts!="O" and ts!="E":
       toss() 
    else:
        num()
toss()
print("\r")
if ur>cr:
    print("HURRAY !! YOU WON")
elif ur==cr:
    print("MATCH DRAW")
else:
    print("YOU LOST !! COMPUTER WINS")
print("\r")
def zeroadd():
    if len(CR)<6:
        CR.append(0)
        zeroadd()
    if len(UR)<6:
        UR.append(0)
        zeroadd()
zeroadd()
print("Computer : ",CR)
print("User : ",UR)
'''import matplotlib.pyplot as plt
import numpy as np
y1=np.array(CR)
y2=np.array(UR)
Y=[1,2,3,4,5,6]
plt.plot(Y,y1,marker="o")
plt.plot(Y,y2,marker="o")
plt.show()
xb=["USER","COMPUTER"]
yb=[ur,cr]
plt.bar(xb,yb)
plt.show()
plt.pie(yb,labels=xb)
plt.show()'''
print("--------------------------------------------------------------------------------------")
print("FINAL SCORECARD")
print("USER RUNS : ",ur)
print("COMPUTER RUNS : ",cr)
print("--------------------------------------------------------------------------------------")
