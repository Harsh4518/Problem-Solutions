a=[3,1,1]
b=[6,5,4]

a.sort()
b.sort()
b=b[::-1]

res=[]

for i in range(len(a)):

    res.append(a[i]*b[i])

print(sum(res))

    

    
