N=12
m=10**9+7

n=list(str(N))
n=n[::-1]
n="".join(n)
n=int(n)

res=N**n
print(res%m)
