s="iiii"
k=1

l=""

for i in s:

    l+=str(ord(i)-ord('a')+1)


while k>0:

    s=0

    for i in l:

        s+=int(i)

    k-=1

    l=str(s)
    print(l)

print(s)

    



