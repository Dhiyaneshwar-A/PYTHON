import random
print("Let's play a BINGO game with 5*5 matrix with computer")
print("\r")
B=list('BINGO')
M=[]
L=list("_"*5)
L1=list("_"*5)
for i in range(1,26):
    M.append(i)
random.shuffle(M)
print("USER MATRIX")
print("\r")
for i in range(0,25,5):
    for j in range(i,i+5):
        print(M[j],end=" "*(6-(len(str(M[j])))))
    print("\n")
Mc=[]
for i in range(1,26):
    Mc.append(i)
random.shuffle(Mc)
print(Mc)
while(True):
    def uchoice():
        print("\r")
        uch=int(input("USER's Choice"))
        return uch
    x=uchoice()
    if x not in M:
        continue
    def cchoice():
        while(True):
            cch=random.randint(1,26)
            if cch not in M:
                continue
            else:
                return(cch)
    y=cchoice()    
    if x==y:
        print("COMPUTER's choice ",y)
        print("No same value. Try again")
        continue
    print("COMPUTER's choice ",y)
    if x in M and x in Mc and x!=y:
        M[M.index(x)]='-'
        Mc[Mc.index(x)]='-'
    if y in Mc and y in M and x!=y:
        M[M.index(y)]='-'
        Mc[Mc.index(y)]='-'
    print("\r")
    print("USER MATRIX - UPDATED")
    print("\r")
    for i in range(0,25,5):
        for j in range(i,i+5):
            print(M[j],end=" "*(6-(len(str(M[j])))))
        print("\n")
    print(Mc)
    def bingo(M,L):
        global B
        n=0
        for i in range(0,25,5):
            r=0
            for j in range(i,i+5):
                if M[j]=='-':
                    r+=1
                    if r==5:
                        if n<5:
                            L[n]=B[n]
                            n+=1
        for i in range(0,5):
            c=0
            for j in range(i,25,5):
                if M[j]=='-':
                    c+=1
                    if c==5:
                        if n<5:
                            L[n]=B[n]
                            n+=1
        d1=0
        if n>5:
            n=0
        for j in range(0,25,6):
            if M[j]=='-':
                d1+=1
                if d1==5:
                    if n<5:
                        L[n]=B[n]
                        n+=1
        d2=0
        for j in range(4,24,4):
            if M[j]=='-':
                d2+=1
                if d2==5:
                    if n<5:
                        L[n]=B[n]
                        n+=1
        return L
    x=bingo(M,L)
    y=bingo(Mc,L1)
    print("\r")
    for i in x:
        print(i,end="   ")
    print("\r")
    for i in y:
        print(i,end="   ")
    print("\r")
    if L==B:
        print("\r")
        print("YOU WON!!!!")
        break
    elif L1==B:
        print("\r")
        print("YOU LOST!!!!")
        break
    
    

    
