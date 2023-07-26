l=[-7,1,5,2,-4,3,0]

flag=0
index=1
   
while flag==0:
    
    s1=sum(l[:index])
    s2=sum(l[index+1:])

    if s1==s2:

        flag=1

    else:
        index+=1

if flag==1:

    print("Equillibrium Index:{}".format(index))

    
