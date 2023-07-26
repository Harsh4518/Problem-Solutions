t=int(input("Enter the No of testcases:"))

for i in range(t):

    BS=int(input("\nEnter the Salary:"))

    GS,DA,HRA=0,0,0

    if BS<1500:

        HRA=0.1*BS
        DA=0.9*BS

    if BS>=1500:

        HRA=500
        DA=0.98*BS

    GS=BS+HRA+DA

    print("Gross Salary:%.2f"%GS)

    
