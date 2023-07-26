from collections import Counter
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

p=paragraph.lower()
p=list(p)

l=[]

for i in p:

    if i.isalpha():

        l.append(i)

l="".join(l)
print(l)

