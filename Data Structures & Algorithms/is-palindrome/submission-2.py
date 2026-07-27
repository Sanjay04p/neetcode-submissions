class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        arr=[]
        for i in s:
            if i.isalnum():
                arr.append(i)
        s="".join(arr).lower()
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True