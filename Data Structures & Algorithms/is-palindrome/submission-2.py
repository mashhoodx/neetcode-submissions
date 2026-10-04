class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev=""
        for i in s:
            if i.isalpha():
                rev=i.lower()+rev
            elif i.isdigit():
                rev=i+rev
        if rev==rev[::-1]:
            return True   
        return False