nums=[6,5,4,8]

l=[]

for i in range(len(nums)):

    s=0

    for j in range(len(nums)):

        if nums[j]<nums[i]:

            s+=1

    l.append(s)

print(l)

    
    
