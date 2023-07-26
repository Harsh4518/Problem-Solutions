t=int(input("Enter the No of test cases:"))

operator=''

for i in range(t):

    a,b=map(int, input("\nEnter two Numbers:").split())

    if a>b:

        operator=">"

    elif a<b:

        operator="<"

    elif a==b:

        operator="="

    print("Operator between the Numbers is:",operator)
        
        

    
