class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Brute Force
        count=0
        curr_sum=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                curr_sum+=nums[j]
                if curr_sum%k==0:
                    count+=1
            curr_sum=0
        return count