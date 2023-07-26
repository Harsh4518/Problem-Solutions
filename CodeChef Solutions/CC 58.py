t=int(input("Enter testcases:"))

for i in range(t):

    n=int(input("\nEnter No of dolls:"))

    list1=[]
            
    for i in range(n):

        element=int(input("Enter element:"))

        list1.append(element)

    for i in list1:

        if list1.count(i)%2!=0:

            print("Unpaired Doll:{}".format(i))
            break
        
