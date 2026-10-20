class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c={}
        res=[]
        for i in arr:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        for i,j in c.items():
            if j==1:
                res.append(i)
        if len(res)>=k:
            return res[k-1]
        return ""