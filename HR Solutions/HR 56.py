gems=["Emerald","Ivory","Jasper","Ruby","Garnet"]

price=[1760,2119,1599,3920,3999]

rgems=["Ivory","Emerald","Garnet"]

quantity=[3,10,12]

p=0

for i in range(len(rgems)):

    if rgems[i] in gems and quantity[i]>0:

        t=gems.index(rgems[i])

        p=p+price[t]*quantity[i]

    else:
        p=-1
        break

if p>30000:

    p=p-(p*0.05)

print(p)
