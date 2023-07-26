a=[1,2,3,1,2,3,3,3]
list1=[]

for i in range(len(a)):
    res=a.count(a[i])
    list1.append(res)

res=max(list1)

##for i in range(len(a)):
##    if a.count(a[i])<res:
##        a[i]=0
##
##print(a)
##
##print(a.count(0))

result=len(a)-res

print(result)
