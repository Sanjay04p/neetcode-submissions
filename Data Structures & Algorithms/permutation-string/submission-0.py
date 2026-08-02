class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c={}
        for i in s1:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        for i in range(len(s2)-len(s1)+1):
            c2={}
            for j in range(i,i+len(s1)):
                if s2[j] in c2:
                    c2[s2[j]]+=1
                else:
                    c2[s2[j]]=1
            if c==c2:
                return True
        return False