class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        small = min(nums)
        large = max(nums)
        for i in range(small,large):
            if i not in nums:
                nums.append(i)
                result.append(i)
        return result