arr=[1,1,2,2,3]

l=[0]*(max(arr)+1)

for i in arr:

    l[i]+=1

t=max(l)

print(l.index(t))
