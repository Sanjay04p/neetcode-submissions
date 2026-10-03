class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        l=0
        r=(row*col)-1
        while l<=r:
            mid_idx=l+(r-l)//2
            mid_val=matrix[mid_idx//col][mid_idx%col]
            if mid_val==target:
                return True
            elif mid_val<target:
                l=mid_idx+1
            else:
                r=mid_idx-1
        return False
