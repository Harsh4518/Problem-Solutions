arr=[1,2,4,5,7,8,10]
d=3

c=0
    
for i in range(0,len(arr)):
    temp=arr[i]
    for j in range(i+1,len(arr)):
        temp2=arr[j]
        for k in range(j+1,len(arr)):
            if (temp2-temp)==(arr[k]-temp2)==d:
                c=c+1

print(c)
