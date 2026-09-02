class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = ""
        number = x
        while x > 0:
            last_digit = x%10
            new_x+=(str(last_digit))
            x = x//10
        if number == 0:
            return True
        if new_x == str(number):
            return True
        return False