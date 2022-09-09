print("#Guess the number selected by Computer which is b/w 0-20 IN '5' CHANCES")
import random
u=random.randint(0,20)
for chances in range(0,5):
    i=int(input("Your choice/Guess"))
    if i>20:
        print("Enter number between 0 to 20")
    if i!=u:
        if i>u+5 or i==u+5:
            print("Your Guess is high")
        elif(i<u-5 or i==u-5):
            print("Your Guess is low")
        elif(i<u+5 and i>u+3 or i>u-3 and i<u-3):
            print("You came closer")
        elif(i==u+3 or i==u-3):
            print("You came more closer")
        elif(i==u+2 or i==u-2 or i==u+1  or i==u-1):
            print("You came even more closer")
    else:
        print("HURRAY!! YOU GUESSED THE RIGHT NUMBER")
        break
    chances+=1
else:
    print("BUT YOU FAILED TO GUESS IT IN 5 GUESSES")
    print("THE NUMBER IS ",u)
        
