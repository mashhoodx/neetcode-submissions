class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=[]
        for i in range(len(nums)):
            res=[]
            t=0
            while(t!=i):
                if(nums[i]+s[t]==target):
                    res.append(t)
                    res.append(i)
                    return res
                t=t+1
            s.append(nums[i])
                    