""" s="aaab" ##aaab baa aaa
s1=s[::-1]

l=len(s)
i=0
flag=0

while i<len(s):

    if s[i]==s1[i]:
        flag=1
    else:
        flag=0
        res=i
        break4

    i+=1
    
if flag==0:
    print(res)
else:
    print("-1") """


""" ALTERNATE LOGIC """

##Divide the string to half of its length
##and then compare the first and last characters respectively
##through iteration if characters did'nt match
##check for palindrome string from
##i:l-i-1 and i+1:l-i-i for first return (l-1-i)ith
##and for second return i th index respectively
##if string is palindrome return -1. 

s="aaab" ## aabCbcaa ##aaab baa aaa 

l=len(s)
res=0

if s==s[::-1]:
    res=-1

for i in range(l//2):

    if s[i]!=s[l-i-1]:

        if s[i:l-i-1]==s[i:l-i-1][::-1]:
            res=l-i-1
            break
        elif s[i+1:l-i]==s[i+1:l-1][::-1]:
            res=i
            break
    else:
        res=-1

print(res)

        

        

