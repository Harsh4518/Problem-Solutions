n=32

if n<0:

    print("NO")

else:
    
    b=bin(n)
    B=str(b)[2:]
    print(B)

    B=list(B)

    if B.count('1')==1:

        print("Yes")

    else:

        print("NO")
