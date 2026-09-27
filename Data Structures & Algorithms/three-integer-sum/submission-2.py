class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=sorted(nums)
        res=set()
        for i in range(len(s)):
            l=i+1
            r=len(s)-1
            while(l<r):
                if s[i]+s[l]+s[r]==0:
                    res.add(tuple(sorted([s[i],s[l],s[r]])))
                    l=l+1
                    r=r-1
                elif s[l]+s[r]<-s[i]:
                    l=l+1
                elif s[l]+s[r]>-s[i]:
                    r=r-1
        return [list(x) for x in res]