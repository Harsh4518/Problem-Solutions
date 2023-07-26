nums=[1,2,5,2,3]
target = 2

nums.sort()

res=[]

for i in range(len(nums)):

    if nums[i]==target:

        res.append(i)

print(res)
