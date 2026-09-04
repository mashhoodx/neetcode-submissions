class Solution:
    def isPalindrome(self, s: str) -> bool:
        org=[]
        for i in s:
            if i.isalpha():
                j=i.lower()
                org.append(j)
            elif i.isdigit():
                org.append(i)
            else:
                continue
        rev=org[::-1]
        if rev==org:
            return True
        else:
            return False