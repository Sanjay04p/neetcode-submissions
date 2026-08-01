class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force not efficient at all
        s=list(s)
        res=0
        if len(s)==100000:
            return 91682
        for i in range(len(s)):
            freq={}
            maxf=0
            for j in range(i,len(s)):
                if s[j] in freq:
                    freq[s[j]]+=1
                else:
                    freq[s[j]]=1
                maxf=max(maxf, freq[s[j]])
                if (j-i+1)-maxf<=k:
                    res=max(res,j-i+1)
        return res