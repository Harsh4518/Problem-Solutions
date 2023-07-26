import math
s="feed the dog"
S=""

for i in s:

    if i!=" ":

        S+=i

l=len(S)
n=math.sqrt(l)
r=math.floor(n)
c=math.ceil(n)

l=[]
i=0

while i<len(S):

    t=[S[i:c+i]]
    l.append(t)
    i=i+c

print(l)





