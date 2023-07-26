l=[1,3,5,2,2]
i=1

res=[i for i in range(1,len(l)-1) if sum(l[i+1:])==sum(l[i-1::-1])]

print(res)


    
