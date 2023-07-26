a=[1,-1,3,2,-7,-5,11,6]

for i in range(len(a)):

    if a[i]<0:

        t=a[i]
        a[i]='*'
        a.append(t)

print(a)

l=[]

for i in a:

    if i!='*':

        l.append(i)

a.clear()

a=l

print(a)



    
