nums=[1,3,5,6]

target=2

if target not in nums:

    nums.append(target)

    nums.sort()

    res=nums.index(target)

    print("Index of {} is:{}".format(target,res))

else:

    res=nums.index(target)

    print("Index of {} is:{}".format(target,res))
