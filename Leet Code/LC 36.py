sentences=["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

space=0

for i in sentences:

    r=i.count(" ")
    space=max(r,space)

print(space+1)
