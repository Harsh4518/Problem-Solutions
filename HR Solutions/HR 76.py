a=[2,1,3,1,2]

c=0
for i in range(1,len(a)):

    key=a[i]
    j=i-1

    while j>=0 and key<a[j]:

        a[j+1]=a[j]
        c+=1
        j-=1

    a[j+1]=key

print(a,c)
