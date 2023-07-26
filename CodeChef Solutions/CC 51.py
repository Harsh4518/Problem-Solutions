t=int(input("Enter testcases:"))

for i in range(t):

    s=input("\nEnter the String:")

    list1=list(s)

    ca,cb=0,0

    ca=list1.count('a')
    cb=list1.count('b')

    res=min(ca,cb)

    print("Minimum Ballons:{}".format(res))
    

