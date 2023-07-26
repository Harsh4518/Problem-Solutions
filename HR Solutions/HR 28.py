B=[4,5,6,7]
count=0

if sum(B)%2==1:

    print("NO")

for i in range(len(B)-1):

    if B[i]%2==1:

        B[i]+=1
        B[i+1]+=1
        count+=2

print(count)
        
