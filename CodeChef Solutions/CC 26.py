t=int(input("Enter the Number of test Cases:"))

list1=[100,50,10,5,2,1]


for x in range(t):

    rs=int(input("\nEnter the amount:"))
    notes=0

    for i in list1:
        
        if rs!=0:
            
            notes=notes+(rs//i)
            rs=rs%i

    print("Minimum Number of notes:{}".format(notes))           
           

