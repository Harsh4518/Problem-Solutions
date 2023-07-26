a=[1,2,3,4,5]

for i in range(len(a)-2):

    a[i],a[i+2]=a[i+2],a[i]

print(a)
