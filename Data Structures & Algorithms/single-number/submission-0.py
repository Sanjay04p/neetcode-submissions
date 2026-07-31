class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        res={k:v for k,v in c.items() if v==1}
        return list(res.keys())[0]