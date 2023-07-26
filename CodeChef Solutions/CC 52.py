t=int(input("Enter the testcases:"))

for i in range(t):

    X=input("\nEnter first String:")
    Y=input("Enter Second String:")

    X=X.lower()
    Y=Y.lower()

    if len(X)==len(Y):

        for i in range(len(X)):

            if X[i]==Y[i] or (X[i]=='?' or Y[i]=='?'):

                flag=1

            else:

                flag=0
                break


        if flag==1:

            print("YES")

        else:

            print("NO")

    else:

        print("NO")

    





        
