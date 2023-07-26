#initialize i1 and i2 to -1 initially as indexing start from 1 of arr
#consider list1 and temp=0
#iterate through each element of arr
#pick one element of arr at a time store it in temp
#again iterate through arr with different index j
#check whether sum(ith element,jth element) is equal to m or not
#even if sum is equal to m,ith index must not be equal to jth index
#store satisfying indices in i1 and i2 respectively
#append them in list1
#remove repeatitions and sort the list
#return final result

a=[2,2,4,3]
m=4

i1,i2=-1,-1

list1=[]

for i in range(len(a)):

    temp=a[i]
    for j in range(len(a)):
        if temp+a[j]==m and i!=j:
            i1,i2=i+1,j+1
            list1.append(i1)
            list1.append(i2)
                
res=sorted(list(set(list1)))
print("Required index for sum m={}: {}".format(m,res))
            

