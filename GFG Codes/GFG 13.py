from collections import Counter 
l=[2,3,1,2,3]

d=Counter(l)
res=[]


for i in d.items():

    if i[1]>1:

        res.append(i[0])

print(res)

    
