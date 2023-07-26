a=[1,2,3,4,5]

res=[]

k=3

t,i=[],0

while i<len(a):

    t=a[i:k+i]

    t=t[::-1]

    res.extend(t)

    i=i+k

print(res)



    

