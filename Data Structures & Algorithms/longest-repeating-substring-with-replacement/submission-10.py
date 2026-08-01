class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window approach
        l=0
        res=0
        c={}
        maxf=0
        for r in range(len(s)):
            if s[r] in c:
                c[s[r]]+=1
            else:
                c[s[r]]=1
            maxf=max(maxf,c[s[r]])
            while (r-l+1)-maxf>k:
                c[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            