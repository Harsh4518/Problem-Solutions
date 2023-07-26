s="abbcccdddd"

queries=[1,7,5,4,15]

total=0

#list1=[]

dict1={}

for i in range(len(s)):

    if i==0 or s[i]!=s[i-1]:
        
        total=ord(s[i])-ord('a')+1

    else:

        total+=ord(s[i])-ord('a')+1

    #list1.append(total)

    dict1[total]=1

res=[]

for i in queries:

    res.append("Yes" if i in dict1 else "No")

print(res)

