pattern="abba"
s="dog cat cat dog"

S=s.split()

if len(pattern)!=len(S):

    print("False")

d={}

for i in range(len(pattern)):

    if pattern[i] not in d:

        if S[i] in d.values():

            print("False")
            break

        d[pattern[i]]=S[i]

    else:

        if d[pattern[i]]!=S[i]:

            print("False")
            break
        

else:

    print("True")







