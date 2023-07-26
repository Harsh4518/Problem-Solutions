s="aabbccdd"

list1=[]

strs=list(set(s))

for i in strs:

    element=s.count(i)

    list1.append(element)

odd=0

for i in list1:

    if i%2!=0:

        odd+=1

if odd>1:

    print("Not Possible")

else:

    print("Possible")
