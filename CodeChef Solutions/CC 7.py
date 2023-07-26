test_cases=int(input("Enter the Number of test cases:"))

for i in range(test_cases):

    n=list(map(int,input("\nEnter the Number:")))

    res=n.count(4)

    print("No of 4's is {}".format(res)) 

    
