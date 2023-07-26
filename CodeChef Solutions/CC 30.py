for i in range(int(input("Enter the No of test Cases:"))):

    n=int(input("\nEnter the Number:"))
    d=int(input("Enter times repeated:"))

    s=n

    for i in range(d):

        for i in range(s):
            s=s+i

    print("Sum is:{}".format(s))
                
