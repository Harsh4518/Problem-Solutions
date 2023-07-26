from collections import Counter

s="a"
t="aa"

a=Counter(s)
b=Counter(t)

r=(b-a).keys()
r=list(r)
r="".join(r)
print(r)


