arr=[-2,2,4]

m=10000

for i in range(len(arr)-1):

    m=min(abs(arr[i+1]-arr[i]),m)

print("absolute minimum difference:",m)
