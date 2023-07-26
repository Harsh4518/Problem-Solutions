arr=[3,3,6,5,-2,2,5,1,-9,4]

s=sum(arr)//3
l=[]
res=0

for i in range(len(arr)):

    res+=arr[i]

    if res==s:

        l.append(i)
        res=0

if len(l)==3:

    print("YES")

else:

    print("False")

