a=[1,1,3,2,1]

m=max(a)
f=[0]*(m+1)

for i in a:

    f[i]+=1

print(f)

for i in range(1,m+1):

    f[i]=f[i]+f[i-1]

o=[0]*len(a)

for i in range(len(a)-1,-1,-1):

    o[f[a[i]]-1]=a[i]
    f[a[i]]=f[a[i]]-1

print(o)


