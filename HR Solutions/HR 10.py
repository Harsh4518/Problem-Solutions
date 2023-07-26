a=[1,2,3]
k=2
query=[0,1,2]
l=len(a)
list1=[]

##l=len(a)
##
##print("Array Before Rotation:{}".format(a))
##
##for i in range(k):
##    temp=a[l-1]
##    for j in range(len(a)-1,-1,-1):
##        a[j]=a[j-1]
##    a[0]=temp
##
##print("Array after Rotation:{}".format(a))
##
##print("Elements:")
##
##for i in query:
##    if i<len(a):
##        print(a[i])



"""after kth rotations of an array of size n elements the new index of
   each elements becomes (n-k+i) where i is the original index of the
   element in the original array..."""

k=k%l  

for i in query:
    element=a[(l-k+i)%l]
    list1.append(element)

print(list1)
