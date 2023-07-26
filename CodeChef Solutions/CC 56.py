t=int(input("Enter the testcases:"))

for i in range(t):

    n=int(input("\nEnter the Number:"))
    
    count_0=0
    count_1=0

    while n>0:

        r=n%10

        if r==1:

            count_1+=1

        elif r==0:

            count_0+=1

        n=n//10

    if count_1==1 or count_0==1:

        print("YES")

    else:

        print("NO")
