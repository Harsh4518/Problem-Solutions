from collections import Counter
words=["az","azz"]

res=[]

for i in range(len(words)):

    if res==[] or Counter(res[-1])!=Counter(words[i]):

        res.append(words[i])

print(res)

    
