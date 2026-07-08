class Solution(object):
    def isPalindrome(self, x):
        to_str = str(x)
        reversed_x = to_str[::-1]
        if to_str == reversed_x:
            return True
        else:
            return False
        return x
        