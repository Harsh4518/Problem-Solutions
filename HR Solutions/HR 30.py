price=[20,15,8,2,12]

d={}

for i in range(len(price)):

    d[price[i]]=i

price.sort()

diff=10**20

for i in range(len(price)-1):

    if d[price[i+1]]<d[price[i]]:

        diff=min(diff,price[i+1]-price[i])

print("Minimum Difference:{}".format(diff))

        
