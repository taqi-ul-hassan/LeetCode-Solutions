class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        final_list = []
        for i in range(small,large):
            if i not in nums:
                final_list.append(i)
        return final_list