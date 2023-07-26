t=int(input("Enter the Number of testcases:"))

for i in range(t):

    n=int(input("\nEnter total numbers:"))

    list1=list(map(int,input("Enter the Elements:").split()))

    min1=min(list1)
    list1.remove(min(list1))
    min2=min(list1)

    print("Minimum Sum possible:{}".format(min1+min2))
