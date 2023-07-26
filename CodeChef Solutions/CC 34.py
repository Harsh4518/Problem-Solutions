t=int(input("Enter the No of Testcases:"))

for i in range(t):

    l=int(input("\nEnter the Base of Isosceles Triangle:"))

    res=0

    while l>2:

        r=(l-2)//2 

        res+=r

        l=l-2

    print("Minimum Number of squares:{}".format(res))

        

        
        
