from collections import Counter

for i in range(int(input())):
    
    list1=list(map(int,input().split()))

    r=Counter(list1)

    if r[0]>r[1]:

        print("Poor")

    else:

        print("Good")
