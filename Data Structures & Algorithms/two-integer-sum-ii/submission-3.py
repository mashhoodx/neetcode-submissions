class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        r=len(numbers)-1
        l=0
        while(l!=r):
            m=numbers[r]+numbers[l]
            if m==target:
                res.append(l+1)
                res.append(r+1)
                return res
            elif m<target:
                l=l+1
            elif m>target:
                r=r-1
