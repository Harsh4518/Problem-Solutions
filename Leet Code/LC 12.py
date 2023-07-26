n=24

list1=[]

for i in range((n//2)+1):

    if i*i<=n:

        list1.append(i)

res=max(list1)

print(res)
