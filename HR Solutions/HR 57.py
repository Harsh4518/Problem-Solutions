s="AABAAB"
s=list(s)
i=0

if 'A' in s and 'B' not in s:

    res=len(s)-1

else:

    while i<len(s)-1:

        if s[i]==s[i+1]:

            s.remove(s[i])

        i+=1

print()
            
