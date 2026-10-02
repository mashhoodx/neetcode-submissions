class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left!=right):
            m=(left+right)//2
            if nums[m]<nums[right]:
                right=m
            elif nums[m]>nums[right]:
                left=m+1
        cut=left
        right=len(nums)-1
        left=cut
        while(right>=left):
            m=(right+left)//2
            if nums[m]==target:
                return m
            if target<nums[m]:
                right=m-1
            elif target>nums[m]:
                left=m+1
        if cut==0:
            return -1
        right=cut-1
        left=0
        while(right>=left):
            m=(right+left)//2
            if nums[m]==target:
                return m
            if target<nums[m]:
                right=m-1
            elif target>nums[m]:
                left=m+1
        return -1