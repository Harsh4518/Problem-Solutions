arr=['abcdde','baccd','eeabg']
list1=[]
l=len(arr)

for i in arr:

    element=sorted(set(i))
    element="".join(element)
    list1.append(element)

print(list1)

index=0
temp=list1[0]
list2=[]


while index<len(temp):
    
    count=0
    for i in list1:

        if temp[index] in i:
           count+=1

    list2.append(count)

    index+=1

print(list2)

print("Total No of Gemstones:{}".format(list2.count(l)))

#first here I converted each element of arr to set to remove repeatitions
#then joined returned set and stored it in list2
#then I stored first element of list1 in temp
#now taking one letter at a time of temp
#checking whether it is in other list1 elements or not
#if found increment count
#and then so on for remaining character of temp
#if count==len(arr) for a particular character of temp
#means it is present in all elements of list1 and hence its a gemstone 
    
    
    

