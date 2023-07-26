n=int(input("Enter the Number:"))

count=0

while n!=0:

    r=n%10
    count+=1
    n=n//10

print("No of digits:{}".format(count))
