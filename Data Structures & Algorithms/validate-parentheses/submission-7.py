from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        n=[]
        d=defaultdict(list)
        d["["]="]"
        d["("]=")"
        d["{"]="}"

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
