from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ct = Counter(nums)
        for i in ct.values():
            if i!=1:
                return True
        return False

        