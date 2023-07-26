n='9875'
n=int(n)

"""while n!=0:

    t=n%10
    s=s+t
    n=n//10

print(s)"""

def Sum(n):

    if n==0:

        return 0

    else:

        return (n%10+Sum(n//10))

res=Sum(n)
print(res)   
