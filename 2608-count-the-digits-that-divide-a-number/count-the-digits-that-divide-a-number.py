class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        number = num
        while num > 0:
            last_digit = num % 10
            if number % last_digit == 0:
                count+=1
            num = num//10
        return count