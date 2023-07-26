s="acxz"  ##ord() function is used to ascess ASCII value of a character.
list1=[]
list2=[]

for i in range(len(s)-1):
    
    element=abs(ord(s[i])-ord(s[i+1]))
    list1.append(element)

s2=s[::-1]

for i in range(len(s2)-1):

    element=abs(ord(s2[i])-ord(s2[i+1]))
    list2.append(element)

print(list1)
print(list2)

if list1==list2:
    print("funny")
else:
    print("Not funny")
