nums=[1,1,0,1,1,1]

r,l=[],[]

for i in range(len(nums)):

    if nums[i]==1:

        l.append(i)

    if nums[i]==0 or i==len(nums)-1:

        r.append(l)
        l=[]

res=0
for i in r:

    m=len(i)
    res=max(m,res)

print(res)

    

        
