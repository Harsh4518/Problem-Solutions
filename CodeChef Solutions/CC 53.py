t=int(input("Enter testcases:"))

for i in range(t):

    X=list(input("\nEnter First String:"))
    Y=list(input("Enter Second String:"))

    A,B=[],[]


    if len(X)==len(Y):

        for i in range(len(X)):

            if X[i]!='?' and Y[i]!='?':

                A.append(X[i])
                B.append(Y[i])

        if A==B:

            print("YES")

        else:

            print("NO")
    else:

        print("NO")

    
