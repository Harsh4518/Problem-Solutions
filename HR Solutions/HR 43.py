from collections import Counter

s1="absdjkvuahdakejfnfauhdsaavasdlkj"
s2="djfladfhiawasdkjvalskufhafablsdkashlahdfa"

a=Counter(s1)
b=Counter(s2)

r1=a-b
r2=b-a

res=(r1+r2).values()

ans=sum(list(res))

print(ans)
