s="AbCdEfGhIjK"
l=set()

for i in s:

    if i.isupper():

        t=ord(i)
        x=chr(t+32)

        if x in s:

            l.add(i)

    if i.islower():

        t=ord(i)
        x=chr(t-32)

        if x in s:

            l.add(x)

if l==set():

    print("")
    
else:
    print(max(l))

        
