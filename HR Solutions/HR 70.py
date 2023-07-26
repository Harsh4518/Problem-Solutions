s="aabaa"
queries=[[1,1],[1,4],[1,1],[1,4],[0,2]]

for i in queries:

    left=i[0]
    right=i[1]

    t=s[left:right+1]

    l=[]

    for i in range(len(t)):

        for j in range(i,len(t)):

            r=t[i:j+1]

            l.append(r)

    print(len(list(set(l))))

            
