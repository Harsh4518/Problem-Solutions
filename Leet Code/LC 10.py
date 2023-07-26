s="Hello World"

list1=[]

for i in s.split():

    list1.append(i)

print("Length of last word:{}".format(len(list1[len(list1)-1])))
