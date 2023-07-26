from collections import Counter
a=[1,2,3,4,3,2,1]

d=Counter(a)

for i in d.keys():

    if d[i]==1:

        print(i)
        break


