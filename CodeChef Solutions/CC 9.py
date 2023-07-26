test_cases=int(input("Enter the No of test cases:"))

while test_cases>0:

    n=int(input("\nEnter the Number:"))

    fact=1

    for i in range(n,1,-1):

        fact=fact*i

    print("Factorial of Number {} is: {}".format(n,fact))

    test_cases-=1 


    

    
