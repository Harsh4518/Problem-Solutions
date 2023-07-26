k=int(input("Enter the target element:"))

list1=list(map(int, input("enter list elements:").split()))

print("LIST:",list1)

for i in list1:

    if i%k==0:
        print(i)








