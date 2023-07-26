p=20
d=3
m=6
s=70

c=0

while p<=s:

    s=s-p
    p=max(p-d,m)

    c+=1

print(c)
