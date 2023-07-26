allowed="ab"
words=["ad","bd","aaab","baa","badab"]

t=set(allowed)
c=0

for i in words:

    x=set(i)

    res=x.difference(t)

    if res==set():

        c+=1

print(c)

