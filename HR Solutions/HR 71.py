s="www.abc.xy"
k=87
k=k%26
S=""

for i in s:

    if i.isalpha():

        t=ord(i)
        t=t+k

        if t>90 and i.isupper():

            t=t-90
            t=t+64

        if t>122 and i.islower():

            t=t-122
            t=t+96
            
        r=chr(t)
        S+=r

    else:

        S+=i

print(S)

        
