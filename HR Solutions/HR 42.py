from collections import Counter

s="xaxbbbxx"

s=list(s)

l=len(s)

s1=s[:l//2]
s2=s[l//2:]

a=Counter(s1)
b=Counter(s2)

res=(a&b).values()

res=sum(res)

ans=len(s1)-res

print(ans)

