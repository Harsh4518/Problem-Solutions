items=[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey="color"
ruleValue="silver"

l=["type","color","name"]
index=l.index(ruleKey)

c=0
for i in items:

    if i[index]==ruleValue:

        c+=1

print(c)
        

    
