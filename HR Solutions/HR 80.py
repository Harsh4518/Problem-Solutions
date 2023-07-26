n=9
N=str(bin(9))[2:]

l="0"*(32-len(N))

res=l+N
print(res)
s=""
for i in res:

    if i=='0':

        s+='1'

    else:

        s+='0'

print(s)
print(int(s,2))
