calorie=[5,10,7]

calorie.sort()

print(calorie)

n=len(calorie)-1

s=0

for i in range(len(calorie)):

    s=s+(2**(n-i)*calorie[i])

print(s)

    
