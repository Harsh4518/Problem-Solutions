rounds=int(input("Enter the Number of rounds:"))
print()

P1=0
P2=0

player1,player2=[],[]

for i in range(rounds):

    P1,P2=map(int, input("Enter the scores of player 1 And Player 2:").split())

    player1.append(P1)
    player2.append(P2)

print("\nPlayer 1 Scores:",player1)
print("Player 2 Scores:",player2)

CS=[]

for i in range(rounds):

    element=player1[i]-player2[i]

    CS.append(element)

print("\nCumulative Score:",CS)

res=max(CS)

if res>0:

    print("\nPlayer 1 wins with lead:",res)

elif res<0:

    res=min(CS)

    print("\nPlayer 2 wins with lead",abs(res))


    




    
    
