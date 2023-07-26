t=int(input("Enter the No of testcases:"))

for i in range(t):

    n=int(input("\nEnter the Number:"))

    if n%4==0:

        res=n+1

    else:

        res=n-1

    print("RESULT:{}".format(res))
