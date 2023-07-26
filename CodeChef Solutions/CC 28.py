t=int(input("Enter the Number of test cases:"))

list1=[2048,1024,512,256,128,64,32,16,8,4,2,1]

for i in range(t):

    n=int(input("\nEnter total Price:"))
    r=0

    for i in list1:

        if n!=0:

            r=r+(n//i)
            n=n%i

    print("Minimum Number of Menus:{}".format(r))

    
            
