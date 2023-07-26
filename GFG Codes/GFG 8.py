a=[10, 11, 1, 2, 3]

res=[]

for i in range(len(a)-1):

    n=a[i]^a[i+1]
    res.append(n)

if len(a)%2==1:

    res.append(a[-1])

print(res)
