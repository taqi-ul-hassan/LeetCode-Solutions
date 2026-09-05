class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = []
        count = 0
        original = nums
        for i in nums:
            while i > 0:
                last = i%10
                count+=1
                i = i//10
            if count % 2 == 0:
                result.append(nums[i])
            count = 0
        return len(result)