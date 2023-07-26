t=int(input("Enter the number of test Cases:"))

for i in range(t):

    a,b,c=map(int, input("\nEnter the Three Angles:").split())

    if a+b+c==180:

        res="YES"

    elif a+b+c<180 or a+b+c>180:

        res="NO"

    print("Valid Triangle:",res)
