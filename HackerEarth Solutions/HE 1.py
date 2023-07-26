word=input("Enter the word:")

word.lower()

z_c=0
o_c=0

for i in word:

    if i=='z':

        z_c+=1

    if i=='o':

        o_c+=1

if 2*z_c==o_c:

    print("Yes")

else:

    print("No")

    
