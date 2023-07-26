s="abc"
t="ahbgdc"

d={}

for i in range(len(t)):

    d[t[i]]=i
    
l=[]
for i in s:

    try:

        l.append(d[i])

    except:

        pass

for i in range(len(l)-1):

    if l[i+1]>l[i]:

        continue

    else:

        print("False")
        break

else:

    print("True")

