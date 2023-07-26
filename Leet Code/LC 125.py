s="a0b1c2"

l1=[]
l2=[]

for i in s:

    if i.isalpha():

        l1.append(i)

    else:

        l2.append(i)

S=""
j,k=0,0

for i in range(len(s)):

    if i%2==0:

        S+=l2[j]
        j+=1

    else:

        S+=l1[k]
        k+=1

print(S)

        
