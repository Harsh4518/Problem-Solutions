s="codeleet"
indices=[4,5,6,7,0,2,1,3]

l=[0]*len(s)

for i in range(len(s)):

    l[indices[i]]=s[i]

l="".join(l)
print(l)

    
