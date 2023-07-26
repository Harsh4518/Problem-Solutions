tag=list(input("Enter the tag:"))

vowels=['A','E','I','O','U','Y']

t=tag[2]

if t in vowels:

    print("invalid")

elif (((int(tag[0])+int(tag[1]))%2!=0) or
     ((int(tag[3])+int(tag[4]))%2!=0) or
     ((int(tag[4])+int(tag[5]))%2!=0) or
     ((int(tag[7])+int(tag[8]))%2!=0)):

    print("invalid")

else:

    print("valid")
