arr=[2,3,4,7,11]
k=5
c=0

for i in range(max(arr)+k+1):

    if i not in arr:

        c+=1

        if c>k:

            print(i)
            break
