s=[2,2,1,3,2]
d=4
m=2

list1=[]

for i in range(len(s)):

    for j in range(i+1,len(s)+1):

        e=s[i:j]

        list1.append(e)

c=0

for i in list1:

    e=sum(i)
    l=len(i)

    if l==m and e==d:
        c+=1

print(c)

        
