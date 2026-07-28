class Solution:
    def maxProfit(self, p: List[int]) -> int:
        #optimised solution
        l=0
        r=1
        max_pro=0
        while r<len(p):
            if p[r]>p[l]:
                pro=p[r]-p[l]
                max_pro=max(max_pro,pro)
            else:
                l=r
            r+=1
        return max_pro
