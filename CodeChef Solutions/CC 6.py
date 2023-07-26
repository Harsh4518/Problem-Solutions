test_cases=int(input("Enter the Number of test cases:"))

while test_cases>0:

    n=int(input("\nEnter a Number:"))
    temp=n

    list1=[]

    while n>0:

        r=n%10
        n=n//10

        list1.append(r)

    l=len(list1)

    s=list1[0]+list1[l-1]

    print("SUM of first and last digit of Number {} is:{}".format(temp,s))

    test_cases-=1


        
