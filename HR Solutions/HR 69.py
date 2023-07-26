s="aabaa"

r=s[0:2+1]

l=list(r)
res=[]

for i in range(len(l)):

    for j in range(i,len(l)):

        res.append("".join(l[i:j+1]))
        
print(list(set(res)))
