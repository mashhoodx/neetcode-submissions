class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lr=set()
        for m,i in enumerate(nums):
            k={}
            for n,j in enumerate(nums):
                if n!=m:
                    diff=-i-j
                    if diff in k:
                        lr.add(tuple(sorted([i,j,diff])))
                    k[j]=n
        r=list(lr)
        return [list(x) for x in lr]