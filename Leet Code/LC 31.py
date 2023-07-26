from itertools import permutations
n=4
l=[]

o=1

twos=n//2
rones=n-twos*2

print(twos,rones)

for i in range(twos):

    l.append(2)

for i in range(rones):

    l.append(1)

c=list(set(permutations(l)))

x=len(c)

ways=x+o

print(ways)




