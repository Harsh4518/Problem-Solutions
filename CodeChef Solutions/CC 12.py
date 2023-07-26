t=int(input("Enter the Number of test cases:"))

for i in range(t):

    list1=list(map(int, input("\nEnter the Elements:").split()))

    list1.remove(max(list1))

    print("Second maximum Element of list:",max(list1))

    
