from collections import Counter
s1="s z z z s"
s2="s z ejt"

res=s1.split()+s2.split()

c=Counter(res)

l=[]

for i in c.keys():

    if c[i]==1:

        l.append(i)

print(l)


