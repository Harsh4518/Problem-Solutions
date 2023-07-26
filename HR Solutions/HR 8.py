a=[1,1,2,2,4,4,5,5,5]
list1=[]

for i in range(len(a)-1):
    if a[i+1]-a[i]==0 or a[i+1]-a[i]==1:
        t=i+1
    else:
        break

print(a[:t+1])
        
