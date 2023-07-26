s="abcabcabcabc"

l=len(s)
i=1
sub=s[0]

while sub*(l//len(sub))!=s and i<len(s):

    sub+=s[i]

    i+=1

if sub*(l//len(sub))==s:

    print("True")

else:

    print("False")


    
    

