salary=[4000,3000,1000,2000]

salary.remove(max(salary))
salary.remove(min(salary))

res=sum(salary)

ans=res/len(salary)
print("%.5f"%ans)
