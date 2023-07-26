from itertools import permutations
nums=[1,2,3]

res=list(permutations(nums))

for i in range(len(res)):

    res[i]=list(res[i])

print(res)
