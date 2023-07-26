l=11
r=100

x=[]

for i in range(l,r+1):

    for j in range(i,r+1):

        t=(i,j)
        x.append(t)

res=[]

for x,y in x:

    res.append(x^y)

print(max(res))
        
