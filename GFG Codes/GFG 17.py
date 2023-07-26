l=[2,3,2,3,5]

res=[0]*(max(l)+1)

for i in l:

    res[i]+=1

res.remove(res[0])
print(res)
