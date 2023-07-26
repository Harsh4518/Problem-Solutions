import math

##n=20
##
##print(str(n)[::-1])
##
##b=int(str(n)[::-1])
##
##print(b)
##
##print(n-b)
##
##c=n-b
##
##res=isinstance(c,int)
##
##print(res)

##a="HARSH"

##b="NILESH"

##c=set(a)
##d=set(b)
##
##print(c.intersection(d))

i=23
j=20
k=6

c=0
a=int(str(i)[::-1])
b=int(str(j)[::-1])

print(a,b)
    
r1=(abs(i-a))%k
r2=(abs(j-b))%k

print(r1,r2)

if isinstance(r1,int):
    c=c+1
if isinstance(r2,int):
    c=c+1

print(c)

