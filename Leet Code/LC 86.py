nums=[1,2,3,4]
l=[]

for i in range(0,len(nums)-1,2):

    x=nums[i]
    y=nums[i+1]

    for j in range(x):

        l.append(y)

print(l)

    
    
