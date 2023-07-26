##s='aba'
##n=10
##
##l=len(s)
##
##for i in range(len(s)):
##    if l<n:
##        s=s+s[i]
##        l=l+1
##
##print(s)
##print(s.count('a')

##s='abcac'
##n=10
##i=0
##l=len(s)
##
##while l<n:
##    if i<len(s):
##        s=s+s[i]
##        i=i+1
##        if i==len(s)-1:
##            i=0
##    l=l+1
##
##print(s)
##print(s.count('a'))

s='aba'
n=10

c=s.count('a')
l=len(s)
r=n//l

res=r*c
m=n%l

str1=s[:m]
res1=str1.count('a')

print(res+res1)


