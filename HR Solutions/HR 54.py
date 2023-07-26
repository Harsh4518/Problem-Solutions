path="UDDDUDUU"
steps=len(path)

valleys,level=0,0

for i in range(steps):

    if level==0 and path[i]=='D':

        valleys+=1

    if path[i]=='U':

        level+=1

    if path[i]=='D':

        level-=1

print(valleys)
