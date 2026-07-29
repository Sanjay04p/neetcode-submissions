class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx={}
        l=0
        longest=0
        for r in range(len(s)):
            if s[r] in idx:
                l=max(idx[s[r]]+1,l)
            idx[s[r]]=r
            longest=max(longest,r-l+1)
        return longest