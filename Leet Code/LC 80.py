from collections import Counter 
words=["cool","lock","cook"]

t=Counter(words[0])

for i in range(1,len(words)):

    t=t&(Counter(words[i]))

l=[]

print(t)

for i in t.keys():

    for j in range(t[i]):

        l.append(i)

print(l)

        

    

    

    
