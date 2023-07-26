from collections import Counter

n=11
b=bin(n)
b=str(b)[2:]

x="0"*(32-len(b))
B=x+b

B=list(B)
c=Counter(B)

res=c['1']
print(res)







