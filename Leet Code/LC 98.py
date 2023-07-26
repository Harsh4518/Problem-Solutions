nums=[3,6,1,0]

m=max(nums)
res=nums.index(m)
nums.remove(m)

for i in nums:

    if m>=2*i:

        continue

    else:

        print("-1")
        break

else:

    print(res)
