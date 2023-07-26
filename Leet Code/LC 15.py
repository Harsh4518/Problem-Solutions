strs=["cir","car"]
l=[]

if len(strs)==1:

    t=strs[0]
    print(str(t))

for i in strs:

    l.append(len(i))

m=min(l)

for i in strs:

    if len(i)==m:

        temp=i
        strs.remove(i)
        break

index,flag=0,0
res=""

while index<len(temp):

    for j in range(len(strs)):

        t1=strs[j]
        
        if temp[index]==t1[index]:

            flag=1

        elif temp[index]!=t1[index]:

            flag=0
            break

    if flag==1:

        res=res+temp[index]

    if flag==0:

        break

    index+=1    

print("Longest Common Substring:{}".format(res))
    



