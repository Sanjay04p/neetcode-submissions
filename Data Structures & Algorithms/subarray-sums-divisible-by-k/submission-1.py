class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # using prefix_sum and hashmap
        count=0
        curr_sum=0
        # c=defaultdict(int)
        # c[0]=1
        c={0:1}
        for i in nums:
            curr_sum+=i
            rem=curr_sum%k
            if rem in c:
                count+=c[rem]
                c[rem]+=1
            else:
                c[rem]=1
        return count