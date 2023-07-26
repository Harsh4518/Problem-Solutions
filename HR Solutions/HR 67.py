s="99100"

a=s[:1]
f=n=int(a)

for i in range(len(s)):

    while len(a)<len(s):

        n=n+1
        a=a+str(n)

    if a==s:

        print("YES",f)
        break

    else:

        a=s[:i+1]
        f=n=int(a)

else:

    print("NO")



    
