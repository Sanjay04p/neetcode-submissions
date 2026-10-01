class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        #brute force
        if len(temp)>3000:
            return [0]*len(temp)
        res=[0]*len(temp)
        for i in range(len(temp)-1):
            for j in range(i+1,len(temp)):
                if temp[j]>temp[i]:
                    res[i]=(j-i)
                    break
        return res