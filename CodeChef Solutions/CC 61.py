import math
for i in range(int(input())):
    
    n=int(input())
    l=list(map(int,input().split()))
    
    max_gcd=0
    
    for i in l:
        
        max_gcd=math.gcd(max_gcd,i)
        
    ans=0
    
    for i in l:
        
        if i/max_gcd>1:
            
            ans+=1
            
    print(ans)
