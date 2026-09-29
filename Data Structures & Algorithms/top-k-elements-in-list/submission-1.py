from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(list)
        m=defaultdict(int)
        res=[]

        for i in nums:
            m[i]=m[i]+1
        for j,n in m.items():
            d[n].append(j)

        for freq in range(len(nums),0,-1):
            for num in d[freq]:
                res.append(num)
                if len(res)==k:
                    return res



        
