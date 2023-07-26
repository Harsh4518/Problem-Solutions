class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()

        l=len(citations)

        for i in range(len(citations)):

            res=l-i 

            if res<=citations[i]:

                return res 

        return 0
