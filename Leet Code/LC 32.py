words=["a","b","c","ab","bc","abc"]
s="abc"

c=0

for i in words:

    if s.startswith(i):

        c+=1

print(c)
