s="zvvo"

"""res=[]
i=0

while i<len(s):

    if res==[] or s[i] not in res:

        res.append(s[i])
        i+=1

    else:
        i+=1

res="".join(res)

print(res)"""

res=""

for i in s:

    if i not in res:

        res+=i

print(res)
