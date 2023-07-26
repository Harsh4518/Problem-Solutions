s=input("Enter the Roman No.:")

s=s.upper()

list1,ans=[],[]
index=1

for i in range(len(s)):

    element=s[i:index]
    index+=1

    if element=='I':

        element=1

    elif element=='V':

        element=5

    elif element=='X':

        element=10

    elif element=='L':

        element=50

    elif element=='C':

        element=100

    elif element=='D':

        element=500

    elif element=='M':

        element=1000

    list1.append(element)

print("Roman Number:{}".format(sum(list1)))

