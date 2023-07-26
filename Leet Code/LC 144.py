nums=[4,3,2,7,8,2,3,1]

l=len(nums)
s=sum(set(nums))
      
S=0

for i in nums:

    S+=i

print(S,s)
