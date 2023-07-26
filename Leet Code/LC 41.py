a=[1,2,3,4]

i=0
res=-10000000

while i<len(a)-2:

    m=a[i]*a[i+1]*a[i+2]
    res=max(m,res)

    i+=1

print(res)

    
