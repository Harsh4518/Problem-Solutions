word1="abc"
word2="pqr"

i=0
j=0
s=""

while i<len(word1) and j<len(word2):

    s+=word1[i]
    i+=1

    s+=word2[j]
    j+=1

while i<len(word1):

    s+=word1[i]
    i+=1

while j<len(word2):

    s+=word2[j]
    j+=1

print(s)

    
