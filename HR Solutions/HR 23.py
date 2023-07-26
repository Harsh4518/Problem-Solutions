s="AABAAB"
s=list(s)
list2=[]

set1=sorted(list(set(s)))

index=0

while index<len(set1):

    count=0
    for i in range(len(s)-1):

        if s[i]==set1[index]:
            count+=1

            if count%2==0:
                s[i]=0

    index+=1

for i in s:

    if i:
        list2.append(i)

res="".join(list2)

print(res)


