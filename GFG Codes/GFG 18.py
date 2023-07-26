from collections import Counter

l=[1,5,3,4,3,5,6]

d=Counter(l)

for i in d.keys():

    if d[i]>1:

        print(l.index(i))
        break

