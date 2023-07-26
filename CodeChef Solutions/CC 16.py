rounds=int(input("Enter the No of rounds:"))
print()

lead=0

player1,player2=0,0

for i in range(rounds):

    P1,P2=map(int, input("Enter the Scores:").split())

    player1=player1+P1
    player2=player2+P2

    d=player1-player2

    if d>0 and d>lead:
        leader=1
        lead=d
        
    elif d<0 and lead<abs(d):
        leader=2
        lead=abs(d)

print("\nLeader {} wins by lead: {}".format(leader,lead))
