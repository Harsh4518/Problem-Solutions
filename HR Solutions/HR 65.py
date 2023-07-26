sticks=[1,2,3,4,5,10]

"""sticks.sort()

sticks=sticks[::-1]

res,s=0,0

for i in range(len(sticks)-2):

    a=sticks[i]
    b=sticks[i+1]
    c=sticks[i+2]

    if a<(b+c) and b<(a+c) and c<(a+b):

        s=a+b+c
        res=max(s,res)

    else:
        continue

print(res)"""

sticks.sort()

i=len(sticks)-3

while i>=0 and sticks[i]+sticks[i+1]<=sticks[i+2]:

    i-=1

if i>=0:

    print([sticks[i],sticks[i+1],sticks[i+2]])

else:

    print(-1)
