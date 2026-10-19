class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre=[0]*(len(nums)+1)
        for i in range(len(nums)):
            pre[i+1]=pre[i]+nums[i]
        for i in range(len(nums)):
            left=pre[i]
            right=pre[len(nums)]-pre[i+1]
            if left==right:
                return i
        return -1