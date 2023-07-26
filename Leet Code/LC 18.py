n1=[-1,0,0,3,3,3,0,0,0]
n2=[1,2,2]

"""n1.sort()
l2=len(n2)
del(n1[0:l2])
n1=n1+n2
n1.sort()
print(n1)"""

"""n1.sort()
l2=len(n2)

i=0

while i<l2:

    n1[i]=n2[i]

    i+=1

n1.sort()
print(n1)"""

i=0

for j in range(len(n1)):

    if n1[j]==0 and i<len(n2):

        n1[j]=n2[i]
        i+=1

n1.sort()
print(n1)

        




    

    
