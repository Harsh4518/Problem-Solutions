a=[5,2,3,4,1]

a.sort()

m=10000

for i in range(len(a)-1):

    m=min(a[i+1]-a[i],m)

res=[]

for i in range(len(a)-1):

    if a[i+1]-a[i]==m:

        res.append(a[i])
        res.append(a[i+1])

print(res)
