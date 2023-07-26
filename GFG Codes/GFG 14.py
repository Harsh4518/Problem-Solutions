from collections import Counter
l=[3,1,3,3,2]
m=3

d=Counter(l)

for i in d.keys():

    if d[i]>len(l)//2:

        print(i)
    
print(-1)
