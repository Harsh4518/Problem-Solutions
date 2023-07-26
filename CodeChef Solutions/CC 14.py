rounds=int(input("Enter the Number of Rounds:"))

player1=[]
player2=[]

print("\nEnter the Scores of Player 1:")

for i in range(rounds):

    element=int(input())

    player1.append(element)

print("\nEnter the Scores of Player 2:")

for i in range(rounds):

    element=int(input())

    player2.append(element)
    
print("\nScores of player 1:",player1)

print("Scores of player 2",player2)

CS=[]

for i in range(rounds):

    element=player1[i]-player2[i]

    CS.append(element)

print("\nCumulative Score",CS)

res=max(CS)

if res>0:

    print("Player 1 Wins with lead:{}".format(res))

elif res<0:

    res=min(CS)

    print("Player 2 Wins with lead:{}".format(abs(res)))
    

    

    
