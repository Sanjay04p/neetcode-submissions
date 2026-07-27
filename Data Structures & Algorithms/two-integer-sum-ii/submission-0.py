class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        while i<j:
            res=nums[i]+nums[j]
            if res==target:
                break
                # return [i+1,j+1]
            elif res>target:
                j-=1
            else:
                i+=1
        
        return [i+1,j+1]   