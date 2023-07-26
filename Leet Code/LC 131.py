text="loonbalxballpoon"

d={"b":0,"a":0,"l":0,"o":0,"n":0}

for i in text:

    try:

        d[i]+=1

    except:

        pass

d["l"]=d["l"]//2
d["o"]=d["o"]//2

l=list(d.values())
res=min(l)

print(res)



    
