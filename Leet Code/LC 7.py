nums=[0,1,2,2,3,0,4,2]

var=2
count=0

for i in range(len(nums)):

    if nums[i]!=var:

        nums[count]=nums[i]
        count+=1

print("Non-target:{}".format(count))
