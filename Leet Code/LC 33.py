nums=[-4,-2,1,4,8]

d={}

for i in nums:

    d[i]=abs(i-0)

print(d)

res=1000000

for i in d.keys():

    m=d[i]
    res=min(m,res)

l=[]

for i in d.keys():

    if d[i]==res:

        l.append(i)

print(max(l))
