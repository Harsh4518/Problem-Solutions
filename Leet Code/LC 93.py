from collections import Counter
arr=[2,2,3,4]

c=Counter(arr)
res=-1

for i in c.keys():

    if i==c[i]:

        t=i
        res=max(res,t)

print(res)
                
