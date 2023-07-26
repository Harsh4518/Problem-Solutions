t=int(input("Enter the Testcases:"))

for i in range(t):

    n=input("\nEnter the Number:")

    count_1=0
    count_0=0

    for i in n:

        if i=='1':

            count_1+=1

        elif i=='0':

            count_0+=1

    if count_0==1 or count_1==1:

        print("YES")

    else:

        print("NO")
