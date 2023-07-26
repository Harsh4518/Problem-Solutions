candies=[2,3,5,1,3]
extracandies=3
r=max(candies)

l=[]

for i in range(len(candies)):

    t=candies[i]+extracandies

    if t>=r:

        l.append(True)

    else:

        l.append(False)

print(l)
