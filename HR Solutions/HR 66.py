s="aabbcca"

l=[]

for i in range(len(s)):

    if l!=[] and l[-1]==s[i]:

        l.pop()

    else:

        l.append(s[i])

print("".join(l))

    
