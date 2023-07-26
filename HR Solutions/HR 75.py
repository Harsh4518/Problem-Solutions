a=[1,2,4,5,3]

for i in range(1,len(a)):
    
    key=a[i]
    j=i-1

    while j>=0 and key<a[j]:

        a[j+1]=a[j]

        print(a)

        j-=1

    a[j+1]=key

print(a)
