n=-120

l=list(str(n))

if l[-1]=='0':

    l.remove(l[-1])
    l=l[::-1]
    l="".join(l)
    l=int(l)

elif l[0]=='-':

    l.remove(l[0])
    l=l[::-1]
    l="".join(l)
    l="-"+l
    l=int(l)

print(l)
    
    

    
