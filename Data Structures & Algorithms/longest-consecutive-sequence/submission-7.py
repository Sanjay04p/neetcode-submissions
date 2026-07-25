class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        set_a=set(nums)
        for i in set_a:
            if i-1 not in set_a:
                curr_count=1
                while i+curr_count in set_a:
                    curr_count+=1
                longest=max(curr_count,longest) 
        return longest