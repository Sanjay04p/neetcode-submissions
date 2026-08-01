class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # actual solution
        res=0
        for i in nums:
            res=res^i
        return res
        