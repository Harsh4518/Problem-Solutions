s="yo|uar|e**|b|e***au|tifu|l"

c=0
flag=False

for i in range(len(s)):

    if s[i]=="|":

        flag=not flag

    if s[i]=="*" and flag==False:

        c+=1

print(c)
        
