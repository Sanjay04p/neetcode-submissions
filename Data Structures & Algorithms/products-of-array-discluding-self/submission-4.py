class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #sol3: two pointers
        pref=1
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=pref
            pref=pref*nums[i]
        suff=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=suff
            suff*=nums[i]
        return res