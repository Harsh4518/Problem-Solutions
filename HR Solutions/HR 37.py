topic=['10101','11110','00010']

count=0
max_sub=0

for i in range(len(topic)):

    for j in range(len(topic)):

        sub=0

        for x,y in zip(topic[i],topic[j]):

            if x=='1' or y=='1':

                sub+=1

            if sub>max_sub:
                max_sub=sub
                count=1

            elif sub==max_sub:
                count+=1

print(max_sub,count)
