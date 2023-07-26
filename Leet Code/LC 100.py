nums=[2,5,1,3,4,7]
n=3

l=[]
for i in range(len(nums)//2):

    l.append(nums[i])
    l.append(nums[i+n])

print(l)
