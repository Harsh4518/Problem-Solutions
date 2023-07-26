tag=list(input("Enter the tag:"))

vowel=['A','E','I','O','U']

tag.remove('-')

letter=tag[2]

tag.remove(letter)
flag=0

if letter not in vowel:

     for i in range(len(tag)-1):

         res=int(tag[i])+int(tag[i+1])

         if res%2==1:

             print("invalid")
             break

         else:

             flag=1

     if flag==1:

         print("valid")
    
else:

     print("invalid")

         
