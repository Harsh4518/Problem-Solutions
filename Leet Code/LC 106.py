from collections import Counter
strs=["",""]

res={}
ans=[]

for i in range(len(strs)):

    res[strs[i]]=dict(Counter(strs[i]))

for i in res.keys():

    t=res[i]
    l=[]

    for j in strs:

        if len(t)==len(j) and t==Counter(j):

            l.append(j)

    if ans==[] or l not in ans:
        
        ans.append(l)

print(ans)

        

    




    
