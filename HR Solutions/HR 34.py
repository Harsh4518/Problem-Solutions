a=[5,4,4,2,2,8]

list1=[]

while a!=[]:

    m=min(a)
    count,i=0,0
    l=len(a)

    while i<l:

        a[i]=a[i]-m
        count+=1

        if a[i]==0:

            a.remove(a[i])
            l=l-1
            i=i-1    

        i=i+1

    list1.append(count)
    
print("Final list:{}\nSticks Cut at each turn:{}".format(a,list1))








    
