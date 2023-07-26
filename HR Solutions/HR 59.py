n=4
a=10
b=100

if a>b:

    a,b=b,a

"""t=(n-1)*b

res=[]

res.append(t)

while (t-b)>=0:

    t=(t-b)+a
    res.append(t)

print(sorted(res))"""

res=[]

for i in range(1,n+1):

    t=((i-1)*a+(n-i)*b)

    res.append(t)

res=list(set(res))

print(sorted(res))
    

    

