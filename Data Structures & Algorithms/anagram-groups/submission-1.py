class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c={}
        for i in range(len(strs)):
            word="".join(sorted(strs[i]))
            if word in c:
                c[word].append(strs[i])
            else:
                c[word]=[strs[i]]
        return list(c.values())