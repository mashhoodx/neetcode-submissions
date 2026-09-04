class Solution:
    def isPalindrome(self, s: str) -> bool:
        org=[]
        for i in s:
            if i.isalnum():
                j=i.lower()
                org.append(j)
            else:
                continue
        rev=org[::-1]
        if rev==org:
            return True
        else:
            return False