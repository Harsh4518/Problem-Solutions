n=[-1,-2,-3,-4]

n.sort()

for i in n:

    if i>0:

        temp=i
        break

else:

    print("1")

try:

    temp2=max(n)

    for i in range(temp-1,temp2+2):

        if i not in n and i!=0:

            print(i)
            break

except:

    pass
