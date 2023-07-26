address="1.1.1.1"

res=""

for i in address:

    if i==".":

        res+="[.]"

    else:

        res+=i

print(res)



