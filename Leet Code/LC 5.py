nums=[0,0,1,1,1,2,2,3,3,4]

count=0

for i in range(len(nums)):

    if i<len(nums)-2 and nums[i]==nums[i+1]:

        continue

    nums[count]=nums[i]
    count+=1

print("Repeating elements:{}".format(count))

    




