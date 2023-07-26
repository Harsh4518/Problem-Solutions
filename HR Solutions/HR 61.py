from math import floor

n,s,t=5,5,1

l=[]

while t<=n:

    r=floor(s/2)
    l.append(r)
    s=r*3

    t+=1

print(l)

for i in range(1,len(l)):

    l[i]=l[i]+l[i-1]

print(l)

print("ans:",l[len(l)-1])

    
