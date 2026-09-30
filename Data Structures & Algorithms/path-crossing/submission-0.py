class Solution:
    def isPathCrossing(self, path: str) -> bool:
        k=[[0,0]]
        p=[0,0]
        for i in path:
            if i=="N":
                p[1]=p[1]+1
            elif i=="S":
                p[1]=p[1]-1
            elif i=="E":
                p[0]=p[0]+1
            elif i=="W":
                p[0]=p[0]-1
            if p in k:
                return True
            k.append(p.copy())
        return False