topics=['10101','11110','00010']

n=3
teams,total=[],[]
count=0

for i in range(len(topics)):

    for j in range(len(topics)):

        if i!=j:

            var=(i,j)

            if (j,i) not in teams:

                teams.append(var)

            t1=topics[i]
            t2=topics[j]

            index,sub=0,0

            while index<len(t1):

                if (t1[index]=='1' and t2[index]=='0') or (t1[index]=='1' and t2[index]=='1') or (t1[index]=='0' and t2[index]=='1'):

                    sub+=1

                index+=1

            total.append(sub)


res=max(total)

count=total.count(res)

print("Maximum Subjects:{}\nTotal teams:{}".format(res,count))

            
