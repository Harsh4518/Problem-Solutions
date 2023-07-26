from collections import Counter
nums = [2,2,1,1,1,2,2]

d=Counter(nums)

print(d)
res=0

for i in d.keys():

    res=max(d[i],res)

for i in d.keys():

    if d[i]==res:

        print(i)


