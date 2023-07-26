num=19
s=0

while True:

    t=num%10
    s+=(t*t)
    num=num//10

    if len(str(s))>1:

        num=int(s)
        s=0
        continue

    else:

        print(s)
        break

        
    
    
