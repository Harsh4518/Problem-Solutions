x=23

while x!=1:

    if x%2!=0:

        res=0
        break

    else:

        res=1

    x=x//2

if res==1:

    print("YES")

else:

    print("NO")
