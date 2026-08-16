class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        m=0
        for i in nums:
            if i-1 not in s:
                c=i
                l=1
                while c+1 in s:
                    c+=1
                    l+=1
                if l>m:
                    m=l
        return m

        