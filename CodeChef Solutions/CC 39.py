t=int(input("Enter the No of test Cases:"))

for i in range(t):

    x=int(input("\nEnter the Number:"))

    """if x==0 or x==1:
        print("Not Possible.")

    count=0

    while x%10!=0:

        x=x*2
        count+=1

    print("Minimum No is:{}".format(count))"""

    #if Numbers are 5,15,25,35,45...they require only 1 time multiply by 2.

    if x%10==0:

        print("Minimum Multiply by 2 is 0")

    elif x%10==5: #for no like 5,15,25,35...

        print("Minimum Multiply by 2 is 1")

    else:

        print("Not Possible")

        

        
