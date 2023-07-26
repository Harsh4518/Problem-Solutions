topic=['10101','11110','00010']

result=[]

for i in range(len(topic)):

    for j in range(len(topic)):

        sub=0
        for x,y in zip(topic[i],topic[j]):

            if x=='1' or y=='1':

                sub+=1

            result.append(sub)

max_sub=max(result)

total_teams=result.count(max_sub)

print("Maximum Subject:{}\nTotal teams:{}".format(max_sub,total_teams))


    
