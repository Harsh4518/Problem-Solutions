a=[0,0,0,1,0,0]

i=0
count=0

while i<len(a)-1:

    if i+2<len(a) and a[i+2]==0:

        count+=1
        i+=2

    elif i+1<len(a) and a[i+1]==0:

        count+=1
        i+=1

print(count)

        
