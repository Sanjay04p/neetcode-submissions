class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        for i in range(len(s)):
            res=set()
            for j in range(i,len(s)):
                if s[j] in res:
                    break
                else:
                    res.add(s[j])
                longest=max(longest,len(res))
                
        return longest