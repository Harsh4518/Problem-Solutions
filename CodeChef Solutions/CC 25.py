t=int(input("Enter the Number of test Cases:"))

for i in range(t):

    n=int(input("\nEnter the Number:"))
    reverse=0
    temp=n
    
    while n>0:

        r=n%10
        reverse=reverse*10+r
        n=n//10

    print("REVERSE OF NUMBER {}".format(reverse))

    if reverse==temp:
        print("PALINDROME NUMBER")
    else:
        print("NOT PALINDROME")

    
