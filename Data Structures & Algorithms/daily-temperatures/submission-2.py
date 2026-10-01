class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # using stack
        res=[0]*len(temp)
        stk=[]
        for i in range(len(temp)):
            while stk and temp[i]>temp[stk[-1]]:
                prev_idx=stk.pop()
                res[prev_idx]=i-prev_idx
            stk.append(i)
        return res