temperatures=[73,74,75,71,69,72,76,73]

l=[]

for i in range(len(temperatures)):

    for j in range(i+1,len(temperatures)):

        if temperatures[j]>temperatures[i]:

            l.append(j-i)
            break

    else:

        l.append(0)

print(l)


            
