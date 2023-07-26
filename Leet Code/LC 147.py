a=[7,10,4,3,20,15]
k=3

heap=[]

for i in range(len(a)):

    if heap==[]:

        heap.append(a[i])

    if a[i]>heap[-1]:

        heap.append(a[i])

    if a[i]<heap[-1]:

        heap.insert(0,a[i])

    if len(heap)>k:

        heap.pop()

print(heap[-1])
