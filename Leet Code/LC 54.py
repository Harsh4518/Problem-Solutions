s="0P"

S=""
for i in s:

    if i.isalnum():

        if i.isupper():

            S+=i.lower()

        else:

            S+=i

print(S)
if S==S[::-1]:

    print("Yes")

else:

    print("False")
