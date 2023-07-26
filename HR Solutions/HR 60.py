p=[5,2,1,3,4]

m1=min(p)
m2=max(p)

res=[]

for i in range(m1,m2+1):

    t=(p.index(i))+1

    r=p.index(t)

    res.append(r+1)

print(res)
