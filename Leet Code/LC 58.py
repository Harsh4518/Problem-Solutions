from collections import Counter
list1=["Shogun","Tapioca Express","Burger King","KFC"]
list2=["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

a=Counter(list1)
b=Counter(list2)

res=list((a&b).keys())
t=res[0]
print([t])
