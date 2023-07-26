from itertools import combinations

n=4
k=2

l=[]

for i in range(1,n+1):

    l.append(i)

res=list(combinations(l,k))

for i in range(len(res)):

    res[i]=list(res[i])

print(res)

