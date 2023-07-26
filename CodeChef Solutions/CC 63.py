# cook your dish here
for i in range(int(input())):
    
    c=int(input())
    l=list(map(int,input().split()))
    
    d={}
    
    for i in l:
        
        d[i]=d.get(i,0)+1 
        
    m=max(d.values())
    
    if m>=3:
        
        print("NO")
        
    else:
        
        print("YES")
