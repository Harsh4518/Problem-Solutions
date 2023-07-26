from collections import Counter
words1=["leetcode","is","amazing","as","is"]
words2=["amazing","leetcode","is"]

w1=Counter(words1)
w2=Counter(words2)

res=list((w1&w2).keys())
print(res)

for i in res:

    if (i in words1 and i in words2) and (w1[i]==1 and w2[i]==1):

        print(i)


        
    
