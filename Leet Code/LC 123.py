s="y#fo##f"
t="y#f#o##f"

l1=[]
l2=[]
        
for i in s:
            
    if l1==[] or i!="#":
                
        l1.append(i)
                
    else:
                
        l1.pop()

    if l1==["#"]:

        l1.pop()
                
for i in t:
            
    if l2==[] or i!="#":
        
        l2.append(i)
        
    else:
        
        l2.pop()

    if l2==["#"]:

        l2.pop()

l1="".join(l1)
l2="".join(l2)

print(l1,l2)
