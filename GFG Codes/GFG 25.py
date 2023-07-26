s1="gkfg"
s2="set"

l1=set(s1)
l2=set(s2)

l3=l1.intersection(l2)

if len(l3)==0:

    print(-1)

else:
    print(l3)

    res=[s1.index(i) for i in l3]

    print(min(res))
