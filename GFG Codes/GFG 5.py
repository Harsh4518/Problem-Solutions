a=[1,2,3,4,2]

x,y=1,2

"""A=a.index(x)
B=a.index(y)

print(A,B,abs(A-B))"""

p,q,r=-1,-1,1000

for i in range(len(a)):

    if a[i]==x:

        p=i

    if a[i]==y:

        q=i

    if p!=-1 and q!=-1:

        r=min(abs(p-q),r)

print(r)

    
