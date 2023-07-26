s='abbcccdddd'

d={'a':1,'c':3,'b':2,'e':5,'d':4,'g':7,'f':6,'i':9,'h':8,'k':11,'j':10,'m':13,'l':12,'o':15,'n':14,'q':17,'p':16,'s':19,'r':18,'u':21,'t':20,'w':23,'v':22,'y':25,'x':24,'z':26}


list1=[]

s1=list(set(s))

for i in s1:

    temp=i

    strs=""

    for j in range(len(s)):

        if temp==s[j]:

            strs+=s[j]

    
    list1.append(strs)

list1.sort()

print(list1)



    
        

    
