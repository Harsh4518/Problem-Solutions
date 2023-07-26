n=int(input("Enter the No Soldiers:"))
print()

list1=[]

for i in range(n):

    element=int(input("No of weapons with Soldier:"))

    list1.append(element)


even,odd=0,0

for i in list1:

    if i%2==0:
        even+=1
    else:
        odd+=1

if(even>odd):
    print("\nREADY!")
else:
    print("\nNOT READY!")
         
