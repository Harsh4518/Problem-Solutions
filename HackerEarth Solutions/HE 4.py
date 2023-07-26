tag="04v246-68"

vowel=['A','E','I','O','U']

tag=tag.upper()

num=[]
temp=0
flag=0

if '0' in tag:

    print("invalid")

else:

    for i in range(len(tag)):

        if tag[i].isdigit():

            num.append(tag[i])

        if tag[i].isalpha():

            temp=tag[i]

if temp not in vowel:

    for i in range(len(num)-1):

        res=int(num[i])+int(num[i+1])

        if res%2==1:

            print("invalid")
            break

        else:

            flag=1

    if flag==1:

        print("valid")
else:

    print("invalid")

        

        

        
