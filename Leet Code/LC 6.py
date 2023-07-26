nums=[0,1,2,2,3,0,4,2]

index=len(nums)-1

var=2

for i in range(len(nums)//2):

    if nums[i]==var:

        while nums[index]==2:
            index-=1

        temp=nums[i]
        nums[i]=nums[index]
        nums[index]=temp

print("Modified Array:{}".format(nums))
