import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        res=0
        while(left!=right):
            m=(left+right)//2
            temp=0
            for i in piles:
                temp=temp+(math.ceil(i/m))
            if temp>h:
                left=m+1
                res=left
            elif temp<=h:
                right=m
        return left

