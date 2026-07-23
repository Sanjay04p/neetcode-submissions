class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        c1={}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i in t:
            if i in c1:
                c1[i]+=1
            else:
                c1[i]=1
        if count==c1:
            return True
        return False