class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        left=0
        right=r*c-1

        while(left<=right):
            mid=(left+right)//2
            row=mid//c
            col=mid%c
            m=matrix[row][col]
            if target==m:
                return True
            elif target>m:
                left=mid+1
            elif target<m:
                right=mid-1
        return False
