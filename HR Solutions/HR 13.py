""" s="aaabccddd"
s=sorted(list(s))
s2=sorted(list(set(s)))

for i in s2:
    c=0
    a=0
    r=0
    x=0
    temp=i
    for j in s:
        if temp==j:
            c=c+1
            a=c%2
            r=c-a

    while x<r:

        s.remove(i)
        x=x+1

s1="".join(s)

print(s1) """

"""Alternate logic"""  """POP() Function removes the last element of the list"""

s="aaabccddd"

result=[]

for i in range(len(s)):

    if len(result)==0 or result[-1]!=s[i]:
        result.append(s[i])
    else:
        result.pop()

s1="".join(result)

print(s1)
        
