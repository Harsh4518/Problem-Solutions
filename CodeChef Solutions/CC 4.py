#use "try: except:pass" to prevent NZEC (non zero existential error) in python.
#this error occurs because of exception handling being failed.

cases=int(input("Enter the No. of cases:"))

while cases>0:

    n=int(input("\nEnter the Number:"))
    s=0
    temp=n

    while n>0:

        r=n%10
        n=n//10
        s+=r

    print("Sum of digits of Number:{} is {}".format(temp,s))

    cases-=1

        

    
