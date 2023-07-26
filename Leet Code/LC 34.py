nums1=[1,2,3]
nums2=[2,4,6]

a=list(set(nums1).difference(set(nums2)))
b=list(set(nums2).difference(set(nums1)))

print([a,b])
