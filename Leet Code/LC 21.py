nums=[1,0,1,1]
k=1

for i in nums:

    t1=nums.index(i)
    t2=(len(nums)-1)-nums[::-1].index(i)

    print(t1,t2)

    if t1!=t2 and abs(t1-t2)<=k:

        print("True")

    else:

        print("false")
    

    


       
