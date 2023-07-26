strs=["eat","tea","tan","ate","nat","bat"]

d=defaultdict(list)

for i in strs:

    c=[0]*26

    for j in i:

        c[ord(j)-ord('a')]+=1

    d[tuple(c)].append(i)

print(d.values())
