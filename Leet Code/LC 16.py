a=[8,1,5,2,6]

list1=[]

for i in range(len(a)):

    for j in range(i+1,len(a)):

        element=a[i]+a[j]+i-j

        list1.append(element)

print(max(list1))
