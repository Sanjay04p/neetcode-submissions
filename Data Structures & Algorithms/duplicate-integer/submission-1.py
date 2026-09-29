class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        for i,j in c.items():
            if j>1:
                return True
        return False