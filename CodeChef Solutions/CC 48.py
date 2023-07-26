t=int(input("Enter the No of Testcases:"))

for i in range(t):

    coins=int(input("\nEnter the No of Coins:"))

    height=0
    count=1
    i=1

    while count<=coins:

        i=i+1
        count=count+i
        height+=1

    print("Height:{}",format(height))
        
    
