from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        m=len(s)
        n=[]
        d=defaultdict(list)
        d["["]="]"
        d["("]=")"
        d["{"]="}"
        if m<=1:
            return False

        for i,j in enumerate(s):
            if j in d.keys():
                n.append(j)
            elif not n:
                return False
            elif d[n[-1]]==j:
                n.pop()
            else:
                return False
                
        return len(n)==0
