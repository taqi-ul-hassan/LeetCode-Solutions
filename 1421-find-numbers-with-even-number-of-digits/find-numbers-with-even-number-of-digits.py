class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = []
        count = 0
        for i in nums:
            original = i
            while i > 0:
                i = i//10
                count+=1
            if count%2 == 0:
                result.append(original)
            count = 0
        return len(result)