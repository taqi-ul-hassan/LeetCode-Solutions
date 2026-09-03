class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_num = ""
        old = x
        if x == 0:
            return True
        while x > 0:
            last_digit = x % 10
            new_num+=str(last_digit)
            x = x//10
        return new_num == str(old)
