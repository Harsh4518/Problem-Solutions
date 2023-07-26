s="abc"
t="ahbgdc"

i=len(s)-1
j=len(t)-1

while i>=0 and j>=0:

    if s[i]==t[j]:

        i-=1
        j-=1

    else:

        j-=1

if i>=0:

    print("False:")

else:

    print("True:")
        
