nums=list(map(int,input("Enter Elements:").split()))

target=int(input("Enter target element:"))

list1=[]


for i in range(len(nums)):

    temp=nums[i]

    for j in range(len(nums)):

        if temp+nums[j]==target and i!=j:

            list1.append(i)
            list1.append(j)
            break

list1=sorted(set(list1))

print("List:",list(list1))
        

            

        
            
            
