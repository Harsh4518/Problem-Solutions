from collections import Counter
a=[1,5,3,4,3,5,6]

d=Counter(a)

res=[]
r=100000

for i in d.keys():

    if d[i]==2:

        res.append(i)

if res==[]:

    print("-1")

else:
    
    for i in res:

    t=a.index(i)
    r=min(r,t)

    print(a[r])

    

    
