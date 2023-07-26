num=41
s=0

while num>9:

    t=num%10
    num=num//10
    num+=t
    
print(num)
