nums1=[4,1,2]
nums2=[1,3,4,2]

l=[]

for i in nums1:

    t=nums2.index(i)

    for j in range(t,len(nums2)):

        if nums2[j]>i:

            l.append(nums2[j])
            break

    else:

        l.append(-1)

print(l)

    
