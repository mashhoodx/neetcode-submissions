class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r=[]
        left=0
        right=len(numbers)-1
        while right>left:
            c=numbers[right]+numbers[left]
            if c==target:
                r.append(left+1)
                r.append(right+1)
                break
            elif c<target:
                left+=1
            elif c>target:
                right-=1

        return r