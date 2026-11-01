class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #using defaultdict builtin instead of dict for missing key default values
        count=0
        curr_sum=0
        c=defaultdict(int)
        c[0]=1
        for i in nums:
            curr_sum+=i
            rem=curr_sum%k
            count+=c[rem]
            c[rem]+=1
        return count
