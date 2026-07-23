class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        cnt=0
        for i in nums:
            if i!=0:
                pro*=i
            else:
                cnt+=1
        if cnt>1:
            return [0]*len(nums)
        else:
            res=[0]*len(nums)
            for i in range(len(nums)):
                if cnt==1:
                    if nums[i]!=0:
                        res[i]=0
                    else:
                        res[i]=pro
                else:
                    res[i]=pro//nums[i]
        return res       


