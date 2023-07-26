t=['10101','11100','11010','00101']
n=3
waste,list1=[],[]
count=0

for i in range(len(t)):

    for j in range(len(t)):

        if i!=j:

            var=(i,j)

            if (j,i) not in waste:

                waste.append(var)

                t1=t[i]
                t2=t[j]

                index=0

                sub=0

                while index<len(t1):

                    if (t1[index]=='0' and t2[index]=='1') or (t1[index]=='1' and t2[index]=='0') or (t1[index]=='1' and t2[index]=='1'):


                        sub=sub+1
                        list1.append(sub)

                    index+=1

                if sub==len(t1):

                    count+=1

print(max(list1),count)
                        

                
