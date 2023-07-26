s="a"

x=s.find('b')

l1=s[:x]
l2=s[x:]

if 'b' not in l1 and 'a' not in l2:

    print("True")

else:

    print("False")

