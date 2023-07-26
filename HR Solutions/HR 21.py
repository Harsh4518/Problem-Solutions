s1="hi"
s2="world"

l1=len(s1)
l2=len(s2)

flag=0


#if s1 is greater than s2 consider s2 as sub-string

if l1>=l2:

    #iterate through each character of s2 to check any of it is in s1
    #if even any one character of s2 is in s1 than s2 is substring of s1
    for i in s2:

        if i in s1:
            flag=1
            break
        else:
            flag=0



#if s2 is greater than s1 consider s1 as sub-string
            
elif l1<=l2:

    #iterate through each character of s1 to check any of it is in s2
    #if even any one character of s1 is in s2 than s1 is substring of s2
    for i in s1:

        if i in s2:
            flag=1
            break
        else:
            flag=0

if flag==1:
    print("TRUE")
else:
    print("FALSE")

    

    
