t=int(input("Enter the no of testcases:"))

for i in range(t):

    a,b=map(int, input("\nNo of times the Chef Entered:").split())

    res1=max(a,b)

    res2=a+b

    print("Minimum Time:{}\nMaximum Time:{}".format(res1,res2))
