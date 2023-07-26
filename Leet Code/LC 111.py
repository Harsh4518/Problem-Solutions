arr=[1,2,34,3,4,5,7,23,12]

l=[i for i in range(len(arr)) if arr[i]%2!=0]

for i in range(len(l)-2):

    if l[i+1]-l[i]==l[i+2]-l[i+1]:

        print("True")
        break

else:

    print("False")
