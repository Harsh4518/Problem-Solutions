arr=["d","b","c","b","c","a"]
k=2

l=[]

for i in arr:

    if arr.count(i)==1:

        l.append(i)

print(l)

"""l=[]

for i in arr:

    if l==[] or i not in l:

        l.append(i)

        if len(l)==k:

            print(l[-1])
            break
else:

    print("No String Found")"""

        
