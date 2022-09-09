print("COW BULL GAME")
print("Guess the 3 digit number within 12 turns")
print("Enter a four digit number as input")
print("If a number in it is in the final answer but not at the same position BULLS will be incremented by 1")
print("If a number in it is in the final answer at the same position too COWS will be incremented by 1")
print("\r")
import random
i=str(random.randint(100,999))
g=0
while(True):
        g+=1
        j=input("Enter the no : ")
        if len(j)!=len(i):
            break
        else:
            cows,bulls=0,0
            for m in range(0,3):
                if j[m]==i[m]:
                    cows+=1
                elif j[m] in i and i.count(j[m])==1:
                    bulls+=1
            print("Cows",cows,"Bulls",bulls)
            if cows==3:
                print("HURRAY! YOU FOUND IT")
                break
        if g>12:
            print("YOU LOST!!")
            print(i)
            break
            
