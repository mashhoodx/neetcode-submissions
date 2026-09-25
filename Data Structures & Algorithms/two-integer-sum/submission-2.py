class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        s={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in s:
                res.append(s[diff])
                res.append(i)
                return res
            s[nums[i]]=i
