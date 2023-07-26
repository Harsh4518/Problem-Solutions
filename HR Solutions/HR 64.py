prices=[1,2,3,4]
k=7

prices.sort()

s,count=0,0

for i in range(len(prices)):
    
    if s<=k:
        s=s+prices[i]
        count+=1

    if s>k:
        break

print("total toys purchased:",count-1)

