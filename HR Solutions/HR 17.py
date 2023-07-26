password="2bbbb"
special_char=['!','@','#','$','%','^','&','*','(',')','-','+']
l=len(password)

digit=0
lower_case=0
upper_case=0
special=0

list1=[]

if l>=6 or l<=6:

    for i in password:

        if i.isalpha():

            if i.isupper():
                upper_case+=1
            elif i.islower():
                lower_case+=1

        elif i.isdigit():
            digit+=1

        elif i in special_char:
            special+=1
            
list1.append(lower_case)
list1.append(upper_case)
list1.append(digit)
list1.append(special)

res=list1.count(0)

if l+res>=6:
    print("Minimum Characters required to make password strong:{}".format(res))
else:
    print("Minimum character required to make password strong:{}".format(6-l))

    

            

            

    

