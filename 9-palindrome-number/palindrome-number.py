class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = ""
        original = x
        while x > 0:
            last = x%10
            r+=str(last)
            x=x//10
        if original == 0 or original == 1:
            return True
        return r == str(original)