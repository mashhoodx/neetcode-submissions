class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        for i in range(1,len(nums)):
            ans[i]=ans[i-1]*nums[i-1]
        right=1
        for j in range(len(nums)-1,-1,-1):
            ans[j]=ans[j]*right
            right=right*nums[j]
        return ans
