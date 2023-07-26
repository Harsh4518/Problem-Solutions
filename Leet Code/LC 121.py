s="a-bC-dEf-ghIj"

d={}

for i in range(len(s)):

    if s[i].isalpha():

        continue

    else:

        d[i]=s[i]

S=""

for i in s:

    if i.isalpha():

        S+=i

S=list(S)
S=S[::-1]

for i in d.keys():

    S.insert(i,d[i])

S="".join(S)
print(S)
