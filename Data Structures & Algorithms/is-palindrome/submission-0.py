class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        arr=[]
        for i in s:
            if i.isalnum():
                arr.append(i)
        s="".join(arr).lower()
        return s==s[::-1]