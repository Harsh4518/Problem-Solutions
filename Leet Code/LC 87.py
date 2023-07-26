heights=[1,1,4,2,1,3]

h=sorted(heights)
s=0

for i in range(len(heights)):

    if heights[i]!=h[i]:

        s+=1

print(s)
