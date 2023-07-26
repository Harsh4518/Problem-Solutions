n=6
c=[0,1,2,3,4,5]

c.sort()

t,ans=0,0

for i in range(1,len(c)):

    t=(c[i]-c[i-1])//2

    ans=max(ans,t)

ans=max(ans,c[0],(n-1)-c[len(c)-1])

print(ans)
