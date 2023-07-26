nums=[1,2,3]

i=1

while True:

    if sum(nums[0:i])==sum(nums[i+1:]):

        print(nums[i],i)
        break


    else:

        if i==len(nums)-1:

            print("-1")
            break
        
        i+=1



        
