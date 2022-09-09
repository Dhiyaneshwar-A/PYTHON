while("True"):
    n1=input("Enter Name 1")
    n2=input("Enter Name 2")
    for i in n1:
        if i in n2:
            n2=list(n2)
            n2.remove(i)
            n1=list(n1)
            n1.remove(i)
    n1+=n2
    print("Letters Remaining:",len(n1))
    f=["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    index=0
    while(len(f)>1):
        if len(n1)==0:
            break
        for i in range(len(n1)):
            index+=1
            if index>len(f):
                index=1
        f.remove(f[index-1])
        index=index-1
    print("Your Relation is",f[0])
