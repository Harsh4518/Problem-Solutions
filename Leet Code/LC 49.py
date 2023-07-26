from collections import Counter
nums=[3,1,3,4,2]

d=Counter(nums)

for i in d.keys():

    if d[i]>1:

        print(i)
        break







