from collections import Counter
candyType=[1,1,2,2,3,3]

l=len(candyType)
c=l//2

C=Counter(candyType)
print(C)

if len(C)<=c:

    res=len(C)

elif len(C)>c:

    res=c

print(res)


