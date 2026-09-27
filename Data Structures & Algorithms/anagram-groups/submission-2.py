class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        for i in strs:
            n=tuple(sorted(i))
            if n in s:
                s[n].append(i)
            else:
                s[n]=[i]
        return [x for x in s.values()]
            


            