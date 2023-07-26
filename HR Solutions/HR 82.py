s="abcd"

i=0
j=len(s)-1
c=0

while i<=j:

    if s[i]<s[j]:

        c+=ord(s[j])-ord(s[i])
        i+=1
        j-=1

    elif s[i]>s[j]:

        c+=ord(s[i])-ord(s[j])
        i+=1
        j-=1

    else:
        i+=1
        j-=1

print(c)

    
