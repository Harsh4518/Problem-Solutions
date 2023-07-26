from collections import Counter

a=[203,204,205,206,207,208,203,204,205,206]
b=[203,204,204,205,206,207,205,208,203,206,205,206,204]

A=Counter(a)
B=Counter(b)

print(A)
print(B)

r=B-A

print(list(r.keys()))



