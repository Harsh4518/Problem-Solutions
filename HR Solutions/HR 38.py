ranked=[100,90,90,80]
player=[70,80,105]

r=sorted(list(set(ranked)))

r.reverse()

p=sorted(player)

p.reverse()

l=len(r)
j=0
res=[]

for i in range(len(p)):

    while j<l and p[i]<r[j]:
        j=j+1

    res.append(j+1)

res.reverse()

print(res)

    
