arr=[17,18,5,4,6,1]
j=0

for i in range(j+1,len(arr)):

    arr[j]=max(arr[i:])
    j+=1

arr[-1]=-1
print(arr)

    
