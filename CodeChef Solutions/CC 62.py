import math

def isdivisible(x,y):
    
    if y==1:
        
        return 1 
        
    z=math.gcd(x,y)
    
    if z==1:
        
        return 0
        
    return isdivisible(x,y//z)
    
for i in range(int(input())):
    
    x,y=map(int,input().split())
    
    if isdivisible(x,y):
        
        print("YES")
        
    else:
        
        print("NO")
