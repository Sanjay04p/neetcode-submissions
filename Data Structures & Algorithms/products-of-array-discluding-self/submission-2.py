class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pro=1
        # cnt=0
        # for i in nums:
        #     if i!=0:
        #         pro*=i
        #     else:
        #         cnt+=1
        # if cnt>1:
        #     return [0]*len(nums)
        # else:
        #     res=[0]*len(nums)
        #     for i in range(len(nums)):
        #         if cnt==1:
        #             if nums[i]!=0:
        #                 res[i]=0
        #             else:
        #                 res[i]=pro
        #         else:
        #             res[i]=pro//nums[i]
        # return res   
        # pref=[0]*len(nums)
        # suff=[0]*len(nums)
        # res=[1]*len(nums)
        # pref[0]=1
        # suff[len(nums)-1]=1
        # for i in range(1,len(nums)):
        #     pref[i]=pref[i-1]*nums[i-1]
        # for i in range(len(nums)-2,-1,-1):
        #     suff[i]=suff[i+1]*nums[i+1]
        # for i in range(len(nums)):
        #     res[i]=pref[i]*suff[i]
        # return res
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




