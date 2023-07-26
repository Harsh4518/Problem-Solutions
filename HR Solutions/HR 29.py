arr=[3,4,5]

res=0

l=len(arr)

if l%2==0:

    print("XOR is Zero.")

for i in range(0,l,2):

    res^=arr[i]

print("XOR:",res)

    
