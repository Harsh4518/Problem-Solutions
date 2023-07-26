t=int(input("Enter the Number of test cases:"))

for i in range(t):

    N,X,P=list(map(int,input().split()))

    X2=N-X

    incorrect=-1*X2
    correct=3*X

    if (correct+incorrect)>=P:

        print("Pass")

    elif (correct+incorrect)<P:

        print("Fail")
