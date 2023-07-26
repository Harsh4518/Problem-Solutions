words=["mass","as","hero","superhero"]

l=[]

for i in range(len(words)):

    for j in range(len(words)):

        if words[i]in words[j] and i!=j:

            l.append(words[i])

print(list(set(l)))
