arr = [1,0,2,3,0,4,5,0]
i=0
t=len(arr)

while i<len(arr):

    if arr[i]==0:

        arr.insert(i,0)
        i+=2

        if len(arr)>t:

            arr.pop()

    else:

        i+=1

print(arr)
