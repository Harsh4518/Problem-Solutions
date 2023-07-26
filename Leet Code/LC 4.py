dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

s=input("Enter the Roman Number:")

l=len(s)

n=dict1[s[l-1]]

for i in range(l-2,-1,-1):

    if dict1[s[i]]>=dict1[s[i+1]]:

        n=n+dict1[s[i]]

    else:

        n=n-dict1[s[i]]

print("Roman Number:{}".format(n))

