test_cases=int(input("Enter the Number of test cases:"))

while test_cases>0:

    n=int(input("\nEnter the Number:"))
    temp=n
    reverse=0

    while n>0:

        r=n%10
        reverse=reverse*10+r
        n=n//10

    print("Reverse of the Number {} is: {}.".format(temp,reverse))

    test_cases-=1
