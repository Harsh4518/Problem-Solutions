n=43261596

b=bin(n)
b=str(b)[2:]

x="0"*(32-len(b))
B=x+b
B=B[::-1]
res=int(B,2)

print(res)
