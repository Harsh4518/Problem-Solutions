words=["pay","attention","practice","attend"]
pref="at"

c=0

for i in words:

    if i.startswith(pref):

        c+=1

print(c)
