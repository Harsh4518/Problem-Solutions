g=[1,2,3]
s=[1,1]

c=0

for i in g:

    if i in s and g.count(i)>=s.count(i):
        c+=1

print(c)
