t=int(input("Enter the No of testcases:"))

for i in range(t):

    n=int(input("\nEnter the No of coins:"))
    temp=n
    height=0

    for i in range(1,n):

        if temp>=i:
            
            temp=temp-i
            height+=1

    print("Height:{}".format(height)) 

        
