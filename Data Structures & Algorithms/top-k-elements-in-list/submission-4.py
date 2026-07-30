class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return nums
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        sorted_dict=sorted(c.items(),key=lambda x:x[1],reverse=True)
        return [item[0] for item in sorted_dict[:k]]
