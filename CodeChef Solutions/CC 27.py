t=int(input("Enter the Number of Test Cases:"))

for i in range(t):
    
    ID=input("\nEnter the Ship ID:")
    
    if ID=='B' or ID=='b':
        print("BattleShip")
    
    elif ID=='C' or ID=='c':
        print("Cruiser")
        
    elif ID=='D' or ID=='d':
        print("Destroyer")
        
    elif ID=='F' or ID=='f':
        print("Frigate")
