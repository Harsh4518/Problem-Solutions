test_cases=int(input("Enter the Number of test cases:"))

while test_cases>0:

    list1=[]                
    list1=list(map(int, input("\nEnter the list elements:").split()))

    list1.sort()

    print("LIST after sorting",list1)

    test_cases-=1

    

    
