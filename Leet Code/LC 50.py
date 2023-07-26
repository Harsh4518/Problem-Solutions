prices=[7,1,5,3,6,4]

d={}

for i in range(len(prices)):

    d[prices[i]]=i

prices.sort()

diff=100000000

l=[]

for i in range(len(prices)-1):

    if d[prices[i]]>d[prices[i+1]]:

        diff=min(diff,prices[i+1]-prices[i])

print(diff)

