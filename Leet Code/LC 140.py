title="First leTTeR of EACH Word"

s=title.split()
res=""

for i in s:

    if len(i)==1 or len(i)==2:

        t=i.lower()
        res+=t
        res+=" "

    else:

        x=i[0].upper()
        y=i[1:].lower()
        r=x+y

        res+=r
        res+=" "

res=res.strip()
    
print(res)

        

        
