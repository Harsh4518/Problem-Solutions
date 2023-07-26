t=int(input("Enter the No of test Cases:"))

for i in range(t):

    a,b,c,d=map(int,input("\nEnter Four Sides:").split())

    """ list1=[a,b,c,d]
    flag=0

    for i in list1:

        if list1.count(i)==2:

            flag=1

        else:

            flag=0

    if flag==1:
        print("YES")
    else:
        print("NO") """

    if a==b and c==d:

        print("YES")

    elif a==c and b==d:

        print("YES")
        
    elif a==d and b==c:

        print("YES")

    else:

        print("NO")





              

