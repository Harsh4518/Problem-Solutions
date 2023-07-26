t=int(input("Enter the No of test cases:"))

for i in range(t):

    r=int(input("\nEnter the Range:"))

    s=r*r

    x1,y1=map(int,input("\nEnter Chef's Location:").split())

    x2,y2=map(int,input("Enter head server's Location:").split())

    x3,y3=map(int,input("Enter Sous Chef's Location:").split())

    d1=((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
    d2=((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    d3=((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))

    if s>=d1 or (s>=d2 and s>=d3):

        print("YES")

    else:

        print("NO")

    
