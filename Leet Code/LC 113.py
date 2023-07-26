from collections import Counter
nums1=[1,1,3,2]
nums2=[2,3]
nums3=[3]

n1=Counter(nums1)
n2=Counter(nums2)
n3=Counter(nums3)

l=list((n1&n2).keys())
m=list((n2&n3).keys())
n=list((n1&n3).keys())
print(list(set(l+m+n)))
