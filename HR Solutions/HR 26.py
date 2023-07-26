s="HackerRank.com presents Pythonist 2"

str=''

for i in s:

    if i.islower():

        str=str+i.upper()

    elif i.isupper():

        str=str+i.lower()

    else:
        str=str+i

print(str)
