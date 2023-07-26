nums=[1,2,1,4,5]
k,count=0,0
waste=[]

for i in range(len(nums)):

    for j in range(len(nums)):

        if abs(nums[i]-nums[j])==k and i!=j:
            
                var=(nums[i],nums[j])

                waste.append(var)

res=list(set(waste))
result=[]

for i in range(len(res)):

    temp=res[i]

    v=(temp[0],temp[1])

    if (temp[1],temp[0]) not in result:

        result.append(v)

print(len(result))


    

            

                

                





            


        

            

            

    
