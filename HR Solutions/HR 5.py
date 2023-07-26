arr = [7, 1, 3, 4, 1, 7]
list1=[]

i1=0
i2=0

for i in range(len(arr)):
    temp=arr[i]
    for j in range(i+1,len(arr)):
        if temp==arr[j]:
            t1=i
            t2=j

            x=abs(t1-t2)
            list1.append(x)

if list1==[]:
    res=-1
else:
    res=min(list1)

print(res)


            
