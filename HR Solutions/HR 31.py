s='abcac'
n=7

l=len(s)

n1=n//l

a_count=s.count('a')

res1=n1*a_count

m=n%l

str1=s[:m]

res=str1.count('a')

total=res+res1

print("Total No of a:",total)

