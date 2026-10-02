class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        max_area=0
        for i,j in enumerate(heights):
            start=i
            while stk and stk[-1][1]>j:
                idx,hei=stk.pop()
                max_area=max(max_area,hei*(i-idx))
                start=idx
            stk.append((start,j))
        for i,j in stk:
            max_area=max(max_area,j*(len(heights)-i))
        return max_area