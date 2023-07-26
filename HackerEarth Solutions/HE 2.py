data=[85,25,65,21,84]
N=5

strs=""

for i in data:

    temp=str(i%10)

    strs=strs+temp

res=int(strs)

print("No. through last digits:",res)

if res%10==0:

    print("Yes")

else:

    print("No")
    


