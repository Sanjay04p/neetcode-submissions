class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #brute force
        return nums.index(target) if target in nums else -1
                