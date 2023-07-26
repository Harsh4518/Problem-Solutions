ops=["5","2","C","D","+"]

l=[]

for i in ops:

    try:

        t=int(i)
        l.append(t)

    except:

        pass

    if i=="C":

        l.remove(l[-1])

    if i=="D":

        l.append(2*l[-1])

    if i=="+":

        l.append(l[-1]+l[-2])

print(l)
print(sum(l))
