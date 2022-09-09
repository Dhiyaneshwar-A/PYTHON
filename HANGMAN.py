print("HANGMAN - Game Description")
print("1.To guess Vijay's movie using Hangman")
print("2.There are 7 chances till the man hang")
print("3.If you made a man to hang after 5 chances YOU LOST!!")
print("4.If you find the movie YOU WON!!")
print("\r")

import random
ch=random.choice(['bigil','mersal','master','sarkar','nanban','beast','pokkiri','ghilli','sivakasi','thirupaachi','theri'])
s=''+ch
print("Guess the {} letter Vijay's movie : ".format(len(ch)))
turn=0
L=[]
for i in range(len(ch)):
    L.append("_")
for i in range(100):
    for i in L:
        print(i,end=" ")
    print("\n")
    inp=input("Enter Your Guess : ")
    if inp in ch:
        t=ch.count(inp)
        while t>=1:
            L[ch.index(inp)]=inp
            ch=ch.replace(inp,"-",1)
            t-=1
            continue
        if L==list(s):
            print("\r")
            print("You Got it!!!!")
            print("\r")
            print("ANS IS ")
            for i in L:
                print(i,end=" ")
            print("\r")
            break
    else:
        turn+=1
        if turn==1:
            print("-----")
            print("|   |")
            print("|")
            print("|")
            print("|")
            print("| ")
        elif turn==2:
            print("-----")
            print("|   |")
            print("|   O")
            print("|")
            print("|")
            print("|")
        elif turn==3:
            print("-----")
            print("|   |")
            print("|  O")
            print("|   |")
            print("|")
            print("|")
        elif turn==4:
            print("-----")
            print("|   |")
            print("|  O")
            print("|  /|")
            print("|")
            print("|")
        elif turn==5:
            print("-----")
            print("|   |")
            print("|  O")
            print("|  /|\\")
            print("|")
            print("|")
        elif turn==6:
            print("-----")
            print("|   |")
            print("|  O")
            print("|  /|\\")
            print("|  /")
            print("| ")
            print("Only one chance left!!")
        elif turn==7:
            print("-----")
            print("|   |")
            print("|  O")
            print("|  /|\\")
            print("|  / \\")
            print("| ")
            print("GAME OVER!!!")
            print("ANS IS ",s)
            break
