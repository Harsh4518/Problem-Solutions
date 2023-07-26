a=[1,2,3,4,5]

#anti-clockwise array rotation.
"""t=a[0]

for i in range(len(a)-1):

    a[i]=a[i+1]

a[len(a)-1]=t

print(a)"""

#through slicing array rotation.
"""a[:]=a[1:5]+a[0:1]

print(a)"""

#clockwise array rotation.

t=a[len(a)-1]

for i in range(len(a)-1,0,-1):

    a[i]=a[i-1]

a[0]=t

print(a)

a=[1,2,3,4,5]

#after r=2 rotations.
r=2
n=len(a)

l1=a[0:r]
l2=a[r:n]

print(l2+l1)














 
