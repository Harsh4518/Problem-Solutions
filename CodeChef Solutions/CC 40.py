t=int(input("Enter the Number of testcases:"))

for i in range(t):
    
    n,k=map(int,input("\nEnter No of Coins and Peoples:").split())
    c=0
    
    for i in range(1,k+1):

        r=n%i

        if r>c:

            c=r

    print("Remaining coins:{}".format(c))

        

        
