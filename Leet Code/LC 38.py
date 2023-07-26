nums=[0,1,0,3,12]

temp=nums
del nums

o=[0]*temp.count(0)
a=list(filter(lambda x:x!=0,temp))

nums=a+o
print(nums)
