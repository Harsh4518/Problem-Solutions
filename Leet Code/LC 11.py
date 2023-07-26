D=[4,3,2,9]

l=len(D)

if D[l-1]!=9:

    res=1+D[l-1]
    D.pop()
    D.append(res)

    print(D)

elif D[l-1]==9:

    list1=[]

    for i in D:

        res=str(i)

        list1.append(res)

    list1=int("".join(list1))

    res=list1+1

    list1=[]

    while res!=0:

        r=res%10
        list1.append(r)
        res=res//10

    list1.reverse()

    print(list1)

            

    
    

    
