prices=[8,4,6,2,3]
l=[]

for i in range(len(prices)):

    for j in range(i+1,len(prices)):

        if prices[j]<=prices[i]:

            l.append(prices[i]-prices[j])
            break

    else:

        l.append(prices[i])

print(l)

        
