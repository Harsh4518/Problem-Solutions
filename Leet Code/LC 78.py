image=[[1,1,0],[1,0,1],[0,0,0]]

l=[]

for i in image:

    t=i[::-1]
    l.append(t)
    
l2=[]

for i in l:

    t=[]

    for j in range(len(i)):

        if i[j]==0:

            t.append(1)

        else:

            t.append(0)

    l2.append(t)

print(l2)

            

        

        
