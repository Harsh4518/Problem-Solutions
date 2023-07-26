n=4
width=[2,3,2,1]
cases=[[1,2],[2,4]]

res=[]

for i in cases:
    t1=i[0]
    t2=i[1]
    res.append(min(width[t1:t2+1]))   

for x in res:
    print(x)
