from collections import Counter
arr=[1,2,2,1,1,3]

c=Counter(arr)

l=list(c.values())

for i in l:

    if l.count(i)>1:

        print("False")
        break

else:

    print("True")




