s="We promptly judged antique ivory buckles for the prize"

s=s.lower()

s=s.split()

s="".join(s)

set1=set(s)

print("string:{}\n".format(s))
print("No of characters in the String:{}\n".format(len(set1)))

if len(s)==26:
    print("pangram string")
else:
    print("Not pangram string") 


