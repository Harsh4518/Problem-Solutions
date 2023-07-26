a=[1,2,1,2,1,3,2]
set1={0}
c=0

for i in range(len(a)):

    if a[i] not in set1:
        set1.add(a[i])

    elif a[i] in set1:
          set1.remove(a[i])
          c=c+1

print(c)
