l=[1,2,4]

for i in range(len(l)):

    l[i]=str(l[i])

l="".join(l)

l=int(l)
l=l+1
print(list(str(l)))

