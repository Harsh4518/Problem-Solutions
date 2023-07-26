from collections import Counter

a=[1,1,2,2,4,4,5,5,5]

d=Counter(a)

print(d)

res=0

for i in range(100):

    res=max(res,d[i]+d[i+1])

print(res)




