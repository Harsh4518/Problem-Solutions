l=[1,7,4,3,4,8,7]
k=2

res=[0]*(max(l)+1)

for i in l:

    res[i]+=1

    if res[i]==k:

        print(i)
        break
else:

    print("-1")
