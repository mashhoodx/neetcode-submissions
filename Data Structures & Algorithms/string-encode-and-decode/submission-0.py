class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=[]
        for i in strs:
            ans.append(str(len(i))+"#"+i)
        k=""
        for j in ans:
            k=k+j
        return k

    def decode(self, s: str) -> List[str]:
        final=[]
        i=0
        k=""
        while i<len(s):
            if s[i]!="#":
                k=k+s[i]
                i=i+1
            elif s[i]=="#":
                final.append(s[i+1:i+int(k)+1])
                i=i+int(k)+1
                k=""

        return final


