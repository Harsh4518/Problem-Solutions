num=2032

if num==0:

    print("True")

else:

    num=list(str(num))
    num=num[::-1]

    if num[0]=='0':
        
        print("False")

    else:

        print("True")
