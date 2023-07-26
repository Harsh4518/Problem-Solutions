p=20
d=3
m=6
s=80

list1=[]

while p>=m:

    list1.append(p)

    p=p-d

print(list1)
        
total=0
c=0

for i in list1:

    if total<s:

        total+=i
        c+=1

while (total+m)<s:

    total+=m
    c+=1

print(total,c)


        
