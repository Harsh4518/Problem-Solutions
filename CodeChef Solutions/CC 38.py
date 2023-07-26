t=int(input("Enter the TestCases:"))

for i in range(t):

    n=int(input("\nEnter the length of Gesture:"))
    s=input("Enter the Gesture:")

    list1=list(s)

    if list1.count("Y")!=0 and list1.count("I")!=0:

        print("INDIAN")

    if list1.count("Y")==0 and list1.count("I")!=0:

        print("INDIAN")

    if list1.count("Y")!=0 and list1.count("I")==0:

        print("NOT INDIAN")

    if list1.count("Y")==0 and list1.count("I")==0:

        print("NOT SURE")
