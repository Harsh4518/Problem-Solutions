#finding triplet o(n^2) logic through high low.

a=[0,-1,2,-3,1]

for i in range(len(a)):

    l=i+1
    h=len(a)-1
    s=0

    while h<l:

        s=a[i]+a[l]+a[h]

    if s==0:

        print(1)
        break

    if sum<0:

        l+=1

    else:
        h-=1

print(0)
        

