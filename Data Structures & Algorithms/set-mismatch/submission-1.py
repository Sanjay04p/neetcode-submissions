class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        count=Counter(nums)
        for i,j in count.items():
            if j>1:
                res.append(i)
        if count:
            res.append((n*(n+1)//2)-sum(list(count.keys())))
        return res