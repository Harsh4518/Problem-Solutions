t=int(input("Enter testcases:"))

for i in range(t):

    n,k=map(int,input("\nEnter the No of elements and K value:").split())
    
    count=0

    list1=list(map(int,input("Enter the elements:").split()))

    for i in list1:

        i=i+k

        if i%7==0:

            count+=1

    print("Wolverine Mutations:{}".format(count))
