a=[[8,1],[4,2],[5,6],[3,1],[4,3]]

d={}

for i in range(len(a)):

    d[i+1]=sum(a[i])

print(d)

d=sorted(d.items(),key=lambda i:(i[1],i[0]))

print(d)

list1=[]


for i in d:

    t=i[0]

    list1.append(t)

print(list1)




