nums=[4,3,2,1]

l=[]

for i in range(len(nums)):

    if i%10==nums[i]:

        l.append(i)

else:

    print("-1")

print(min(l))
