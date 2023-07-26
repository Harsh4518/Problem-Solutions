s="leetcode"
s=list(s)
l=['a','e','i','o','u']

i=0
j=len(s)-1

while i<=j:

    if s[i] in l and s[j] in l:

        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1

    elif s[i] in l and s[j] not in l:

        j-=1

    elif s[i] not in l and s[j] in l:

        i+=1

    else:

        i+=1
        j-=1

s="".join(s)
print(s)

        

