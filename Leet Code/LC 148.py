class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        l=[]

        for i in range(len(nums)+1):

            for element in combinations(nums,i):

                l.append(list(element))

        return l
