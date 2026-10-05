from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        res=""
        l=0
        r=len(self.d[key])-1
        while(l<=r):
            m=(l+r)//2
            k=self.d[key][m][0]
            if k==timestamp:
                return self.d[key][m][1]
            elif k>timestamp:
                r=m-1
            elif k<timestamp:
                l=m+1
                res=self.d[key][m][1]
        return res


        
