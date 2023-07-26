n=15

l=[]

for i in range(1,15+1):

    if i%15==0:

        l.append("FizzBuzz")

    elif i%5==0:

        l.append("Buzz")

    elif i%3==0:

        l.append("Fizz")

    else:

        l.append(str(i))

print(l)
