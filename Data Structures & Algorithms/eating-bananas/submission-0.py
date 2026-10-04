class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            mid=(l+r)//2
            total_hours=sum(math.ceil(p/mid) for p in piles)
            if total_hours<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans