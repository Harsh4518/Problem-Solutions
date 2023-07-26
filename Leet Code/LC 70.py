from collections import Counter

s1="apple apple"
s2="banana"

s1=s1.split()
s2=s2.split()

w1=Counter(s1)
w2=Counter(s2)

res=(w1-w2)|(w2-w1)
print(res)
