import math

a=24
b=49

A=math.sqrt(a)
B=math.sqrt(b)

res=int(B)-int(A)

if int(A)*int(A)==a:

    res=res+1

print("No of perfect Squares:{}".format(res))
