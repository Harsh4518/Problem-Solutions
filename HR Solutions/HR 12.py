grid=['1112','1912','1892','1234']

##index=-1
##for i in grid:
##    index=index+1
##    if '9' not in i[0] and i[len(i)-1] and index!=0 and index!=len(grid)-1:
##        i=i.replace('9','X')
##        grid[index]=i
##
##print(grid)
        
grid=[list(x) for x in grid]

for i in range(1,len(grid)-1):
    for j in range(1,len(grid)-1):

        if grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i][j+1]:

            grid[i][j]="X"
            

grid=["".join(x) for x in grid]

print(grid)
            



