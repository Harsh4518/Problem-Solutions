test_case=int(input("Enter the No of test cases:"))

for i in range(test_case):

    a,b=map(int,input("Enter two numbers:").split())

    s=a+b

    print("SUM:{}".format(s))
