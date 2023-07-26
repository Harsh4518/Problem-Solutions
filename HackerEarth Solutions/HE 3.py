A=[15478,8452,8232,874,985,4512]

l=len(A)

first,sec=[],[]

for i in range(l//2):

    first.append(A[i])

for i in range(l//2,l):

    sec.append(A[i])

strs=""

for i in first:

    while i!=0:

        r=str(i%10)
        i=i//10

    strs=strs+r

for i in sec:

    r=str(i%10)

    strs=strs+r

res=int(strs)

if res%11==0:

    print("OUI")

else:

    print("NON")


