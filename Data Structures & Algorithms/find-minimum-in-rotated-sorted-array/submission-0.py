class Solution:
    def findMin(self, nums: List[int]) ->int:
        left=0
        right=len(nums)-1
        while(left!=right):
            if nums[left]<nums[right]:
                return nums[left]
            else:
                m=(left+right)//2
                if nums[m]<nums[right]:
                    right=m
                elif nums[m]>nums[right]:
                    left=m+1
        return nums[left]
                
            
