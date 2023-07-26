t=int(input("Enter the Number of test cases:"))

for i in range(t):

    n=int(input("\nEnter the Number:"))
    fact=1

    for i in range(n,1,-1):

        fact=fact*i

    print("Factorial of number {} is {}.".format(n,fact))
