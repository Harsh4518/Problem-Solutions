nums=[1,2,3,4,0]
index=[0,1,2,3,0]

l=[]*len(nums)

for i in range(len(nums)):

    l.insert(index[i],nums[i])

print(l)
