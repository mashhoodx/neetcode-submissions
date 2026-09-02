class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a=list(zip(position,speed))
        a.sort(reverse=True)
        f=0
        ft=0
        for i,j in a:
            c=(target-i)/j
            if c>ft:
                f+=1
                ft=c
        return f