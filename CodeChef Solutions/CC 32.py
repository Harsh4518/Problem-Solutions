for i in range(int(input("Enter no of test Cases:"))):

    a,b=map(int, input("\nEnter Two Numbers:").split())

    GCD,LCM=0,0

    n1,n2=a,b

    """for i in range(1,n2+1):

        if a%i==0 and b%i==0:

             GCD=i"""

    while n2:

        n1,n2=n2,n1%n2

    GCD=n1

    """for i in range(n2,(n1*n2+1)):

        if i%a==0 and i%b==0:

            list1.append(i)

            LCM=min(list1)"""

    LCM=(a*b)//GCD
    
    print("GCD of Numbers {} and {} is:{}".format(a,b,GCD))

    print("LCM of Numbers {} and {} is:{}".format(a,b,LCM))

    

            
