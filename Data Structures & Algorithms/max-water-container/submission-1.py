class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxi=0
        for i in range(len(h)):
            for j in range(i+1,len(h)):
                res=min(h[i],h[j])*(j-i)
                maxi=max(res,maxi)
        return maxi