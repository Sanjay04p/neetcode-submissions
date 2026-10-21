class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Optimised
        is_inc=True
        is_dec=True
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                is_inc=False
            if nums[i-1]<nums[i]:
                is_dec=False
        return is_inc or is_dec