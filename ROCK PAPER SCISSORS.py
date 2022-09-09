#STONE PAPER SCISSOR

import random
while(True):
    i=input("Enter your choice 'r' for rock 'p' for paper 's' for scissors")
    if i not in ["r","p","s"]:
        print("Enter correct choice")
        continue
    u=random.choice(["r","p","s"])
    print("Computer's choice:",u)
    if(i==u):
        print("TIE")
    elif(i=="r" and u=="p" or i=="p" and u=="s" or i=="s" and u=="r"):
        print("You LOST")
    else:
        print("You WON")
