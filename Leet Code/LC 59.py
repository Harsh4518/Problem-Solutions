jewels="aA"
stones="aAAbbbb"

l=[]
s=list(stones)
j=list(jewels)

for i in j:

    t=s.count(i)
    l.append(t)

print(sum(l))
