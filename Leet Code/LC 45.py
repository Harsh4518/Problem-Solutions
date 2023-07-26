nums=[1,-1,4]

for i in range(len(nums)):

    if sum(nums[0:i])==sum(nums[i+1:]):

        print(nums[i])
        break
