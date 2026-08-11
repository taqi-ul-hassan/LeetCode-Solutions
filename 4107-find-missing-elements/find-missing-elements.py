class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        target = []
        for i in range(small,large):
            if i not in nums:
                target.append(i)
                nums.append(i)
        nums.sort()
        target.sort()
        return target
        
