print("WELCOME TO X-O GAME PYTHON")
print("---------------------------------------------------------------------------------")
print("ROW COLUMN CHOICE ORDER")
for i in range(3):
    for j in range(3):
        print("{}{}".format(i+1,j+1),"         ",end=" ")
    print("\n")
def check(a):
    u1=0
    u2=0
    for x in range(0,len(mat)):
        for y in range(0,len(mat[x])):
            colc=x
            cold=y
            if(a!=0):
                colc=y
                cold=x
            if(mat[colc][cold]==xo1):
                u1+=1
            elif(mat[colc][cold]==xo2):
                u2+=1
        if(u2==3):
            return "u2"
        elif(u1==3):
            return "u1"
        u1=0
        u2=0
    return "none"
def dia1():
    u1=0
    u2=0
    for x in range(0,len(mat)):
        for y in range(0,len(mat[x])):
            if(x==y):
                if(mat[x][y]==xo1):
                    u1+=1
                elif(mat[x][y]==xo2):
                    u2+=1
    if(u2==3):
        return "u2"
    elif(u1==3):
        return "u1"
    else:
        u1=0
        u2=0
        return "none"
def dia2():
    u1=0
    u2=0
    m=len(mat)
    for x in range(0,len(mat)):
        for y in range(0,len(mat[x])):
            if(y==m-1):
                m-=1
                if(mat[x][y]==xo1):
                    u1+=1
                elif(mat[x][y]==xo2):
                    u2+=1
    if(u2==3):
        return "u2"
    elif(u1==3):
        return "u1"
    else:
        u1=0
        u2=0
        return "none"
mat=[['-','-','-'],['-','-','-'],['-','-','-']]
c=0
def choice():
    global xo2
    xo2=0
    global xo1
    xo1=input("User 1 \nDo You want X or O?? ")
    if(xo1=='X'):
        xo2='O'
    elif(xo1=="O"):
        xo2='X'
    else:
        print("\r")
        print("Only X or O is allowed")
        print("\r")
        choice()
choice()
print("User 1 plays with ",xo1)
print("User 2 plays with ",xo2)
print("---------------------------------------------------------------------------------")
tie=0
while(True):
    print("User 1 Turn")
    print("\r")
    row=int(input("Enter the row number : "))
    col=int(input("Enter the column number : "))
    if(mat[row-1][col-1]=='-'):
        mat[row-1][col-1]=xo1
        tie+=1
    else:
        while(True):
            print("\r")
            print("This choice is already filled,Please enter a new choice")
            print("\r")
            row=int(input("Enter the row number : "))
            col=int(input("Enter the column number : "))
            if(mat[row-1][col-1]=='-'):
                mat[row-1][col-1]=xo1
                tie+=1
                break
            else:
                continue
    for i in range(0,len(mat)):
        for j in range(0,len(mat[i])):
            print(mat[i][j],"         ",end=" ")
        print("\n")
    if(check(0)=="u2" or check(1)=="u2" or dia1()=="u2" or dia2()=="u2"):
        print("HURRAY !!! USER 2 WINS")
        c+=1
        break
    elif(check(0)=="u1" or check(1)=="u1" or dia1()=="u1" or dia2()=="u1"):
        print("HURRAY !!! USER 1 WINS")
        c+=1
        break
    if(tie==9):
        print("IT'S AN TIE")
        c+=1
        break
    print("User 2 turn")
    row=int(input("Enter the row number : "))
    col=int(input("Enter the column number : "))
    if(mat[row-1][col-1]=='-'):
        mat[row-1][col-1]=xo2
        tie+=1
    else:
        while(True):
            print("\r")
            print("This choice is already filled,please enter a new choice")
            print("\r")
            row=int(input("Enter the row number : "))
            col=int(input("Enter the column number : "))
            if(mat[row-1][col-1]=='-'):
                mat[row-1][col-1]=xo2
                tie+=1
                break
            else:
                continue
    for i in range(0,len(mat)):
        for j in range(0,len(mat[i])):
            print(mat[i][j],"         ",end=" ")
        print("\n")
    if(check(0)=="u2" or check(1)=="u2" or dia1()=="u2" or dia2()=="u2"):
        print("HURRAY !!! USER 2 WINS")
        c+=1
        break
    elif(check(0)=="u1" or check(1)=="u1" or dia1()=="u1" or dia2()=="u1"):
        print("HURRAY !!! USER 1 WINS")
        c+=1
        break
