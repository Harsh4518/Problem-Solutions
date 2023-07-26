petrolpumps=[[1,5],[10,3],[3,4]]

postion=0
fuel=0

for i in range(len(petrolpumps)):

    fuel=fuel+(petrolpumps[i][0]-petrolpumps[i][1])

    if fuel<0:
        position=i+1
        fuel=0

print(position)

    
