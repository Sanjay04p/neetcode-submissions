class Solution:
    def maxProfit(self, p: List[int]) -> int:
        max_pro=0
        for i in range(len(p)-1):
            for j in range(i+1,len(p)):
                pro=p[j]-p[i]
                max_pro=max(pro,max_pro)
        return max_pro