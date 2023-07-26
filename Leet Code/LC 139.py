firstWord="acb"
secondWord="cba"
targetWord="cdb"

s1=""
s2=""
s3=""

for i in firstWord:

    s1+=str(ord(i)-ord('a'))

for i in secondWord:

    s2+=str(ord(i)-ord('a'))

for i in targetWord:

    s3+=str(ord(i)-ord('a'))

if int(s1)+int(s2)==int(s3):

    print("True")

else:

    print("False")
    
