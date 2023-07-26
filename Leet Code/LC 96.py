nums=[0,1,1]

s=""
l=[]

for i in nums:

    s+=str(i)
    t=int(s,2)

    if t%5==0:

        l.append(True)

    else:

        l.append(False)

print(l)
