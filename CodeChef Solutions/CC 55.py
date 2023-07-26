t=int(input("Enter testcases:"))

for i in range(t):

    n=int(input("\nEnter No of elements:"))
    l=list(map(int,input("Enter Elements:").split()))

    x=min(l)*(n-1)

    print("Minimum Cost:{}".format(x))
