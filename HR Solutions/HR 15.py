""" sub_str="hackerrank"
s="hhaacckkekraraannk"
flag=0
if len(s)>=len(sub_str):

    for i in sub_str:
        if s.count(i)>=sub_str.count(i):
            flag=1
        else:
            flag=0
else:
    flag=0

if flag==1:
    print("YES")
else:
    print("NO") """

"""ALTERNATE LOGIC"""

sub_str="hackerrank"
s="hhaacckkekraraannk"

l=len(sub_str)
j=0
flag=0

for i in s:
    if i==sub_str[j]:
        j=j+1
        #if j reaches end means complete "hackerrank" is found
        if j==l:
            flag=1
            break

if flag==1:
    print("YES")
else:
    print("NO")

    
