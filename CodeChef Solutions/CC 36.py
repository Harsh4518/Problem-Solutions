for i in range(int(input("Enter No of Strings:"))):

    s=input("\nEnter a String:")
    
    l=len(s)

    mid=0

    if l%2!=0:

        mid=l//2

        a=sorted(s[0:mid])   #length of string is odd then s[0:mid]
        b=sorted(s[mid+1:l]) #and s[mid+1:len(s)] compare in sorted form
                             #leaving the mid character if len(s) is odd
        if a==b:
            print("{} is Lapindrome.".format(s))
        else:
            print("{} is Not Lapindrome.".format(s))


    if l%2==0:

        mid=l//2

        a=sorted(s[0:mid]) #length of string is even then s[0:mid]
        b=sorted(s[mid:l]) #and s[mid:len(s)] compare in sorted form

        if a==b:
            print("{} is Lapindrome.".format(s))
        else:
            print("{} is Not Lapindrome.".format(s))



    



    
