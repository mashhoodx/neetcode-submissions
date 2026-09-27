class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while(l<r):
                s=nums[l]+nums[r]+nums[i]
                if s==0:
                    res.add(tuple(sorted([nums[i],nums[l],nums[r]])))
                    l=l+1
                    r=r-1
                elif s<0:
                    l=l+1
                elif s>0:
                    r=r-1
        return [list(x) for x in res]