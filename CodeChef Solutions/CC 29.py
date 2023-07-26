for i in range(int(input("Enter the Number of testCases:"))):

    n=int(input("\nEnter the Number:"))
    flag=0

    for i in range(2,n):

        if n%i==0:

            flag=1
            
          
    if flag==1 or n==1:
        print("Not a prime Number:")
    else:
        print("Prime Number")
          
