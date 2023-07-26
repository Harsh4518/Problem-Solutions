n=int(input("Enter the Number:"))

list1=list(str(n))

list1.reverse()

list1="".join(list1)

if n==list1:

    print("Palindrome")

else:

    print("Not Palindrome")
