s="abcdefg"
k=2

ans=""

if len(s)<k:

    ans=s[::-1]

x=s[0:k]
y=s[k:]
x=x[::-1]
ans=x+y

print(ans)


