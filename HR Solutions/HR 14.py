s="OneTwoThree"
c=0
for i in range(len(s)):
    if s[i].isupper():
        c=c+1

if s[0].islower():
    print("Total Words:{}".format(c+1))
else:
    print("Total Words:{}".format(c))
