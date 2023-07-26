s="Let's take LeetCode contest"
s=s.split()
l=[]

for i in s:
    
    l.append(i[::-1])

l=" ".join(l)

print(l)
