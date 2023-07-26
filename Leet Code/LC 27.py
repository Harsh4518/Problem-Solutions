s="LOVELY"
S=""

for i in range(len(s)):

    if s[i].isupper():

        t=s[i].lower()

        S+=t

    else:

        S+=s[i]

print(S)


