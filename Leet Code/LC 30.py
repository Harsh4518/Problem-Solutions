from collections import Counter
nums=[1,2,3,2]

d=Counter(nums)

s=0

for i in d.keys():

    if d[i]==1:

        s=s+i

print(s)
