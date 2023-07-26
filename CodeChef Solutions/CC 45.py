t=int(input("Enter the Number of testcases:"))

for i in range(t):

    a,o,c=map(int ,input("\nEnter Parameters:").split())

    m=max(a,o)
    n=min(a,o)
    temp=n
    list1=[]
    i=0

    while i<=c:

        temp=temp+i
        d=abs(m-temp)
        list1.append(d)

        i=i+1
        temp=n

    res=min(list1)
    
    print("Minimum Difference:{}".format(res))

   

    
