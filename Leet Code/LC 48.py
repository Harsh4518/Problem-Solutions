nums=[1,2,2,4]

a=set(nums)
repeated=sum(nums)-sum(a)

for i in range(1,len(nums)+1):

    if i not in a:

        missing=i
        break

print(repeated,missing)
