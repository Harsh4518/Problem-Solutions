t=int(input("Enter the testcases:"))

for i in range(t):

    n=int(input("\nEnter No of elements:"))
    l=list(map(int ,input("Enter elements of array:").split()))

    length=len(l)

    s=[]

    while length>1:

        for i in range(0,length-(length-1)):

            m=max(l[i],l[i+1])
            cost=min(l[i],l[i+1])

            l.remove(m)

            s.append(cost)

            length=len(l)
            
    print("Minimum Cost:{}".format(sum(s)))

        
