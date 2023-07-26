d=[1,2,9]

l=len(d)

if d[l-1]!=9:

    x=d.pop()
    x=x+1
    d.append(x)
    print(d)

if d[l-1]==9:

    res=[]

    for i in d:

        res.append(str(i))

    res="".join(res)

    res=int(res)+1

    res=list(str(res))

    print(res)
