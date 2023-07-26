n=5
c=[0,4]

dist=[]

for i in range(n):

    for j in c:
        
        if j!=i:
            d=i-j
            if abs(d)!=n-1:
                dist.append(d)

print(dist)
