from collections import Counter

b="RBY_YBR"

B=Counter(b)

for x,y in B.items():

    if x!='_' and y==1:

        Print("NO")
        break

if B['_']>0:

    print("YES")

else:

    p=0

    for i in range(len(b)-1):

        if b[i]==b[i+1]:
            p=p+1

        elif p>0:

            p=0

        else:

            print("NO")

    print("YES")



            
