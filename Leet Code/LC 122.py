s="abBAcC"

l=[]

for i in range(len(s)):

    if l==[] or abs(ord(l[-1])-ord(s[i]))!=32:

        l.append(s[i])

    else:

        l.pop()

l="".join(l)
print(l)

    
