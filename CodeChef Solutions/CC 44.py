l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))

area=l*b
perimeter=2*(l+b)

if area>perimeter:
    
    print("\nArea is greater")
    print("Area:{}".format(area))

if area<perimeter:
    
    print("\nPerimeter is greater")
    print("Perimeter:{}".format(perimeter))
