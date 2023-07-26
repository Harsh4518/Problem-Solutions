"""s="SOSSPSSQSSOR"

l=len(s)

S_count=s.count('S')
O_count=s.count('O')

total=S_count+O_count

res=l-total

print("No of letters changed during transmission: {}".format(res)) """

"""ALTERNATE LOGIC"""

#sliced the given string to margins of 3-3 and append each string to list1
#here substring message is "SOS"
#which needs to be checked with each element of list1
#initialize the to count=0    
#iterate through each element of list1
#take one element of list1 at a time in i
#compare each character of sub_str with each character of i
#if letters differ increment the count through 1
#repeat the same procedure with each element of list1
#return the final result

s="SOSOOSOSOSOSOSSOSOSOSOSOSOS"

print("Original Message:",s,"\n")

k=0
list1=[]

for i in range(len(s)):

    element=s[k:k+3]
    
    if element:
        
        list1.append(element)
        k+=3

print("List after slicing:",list1,"\n")

sub_str="SOS"

print("SOS Message:",sub_str,"\n")

count=0

for i in list1:

    index=0
    while index<3:
        
        if i[index]!=sub_str[index]:
            count+=1
        index+=1
            
print("Total no of letters changed during transmission: {}".format(count))

    



    


