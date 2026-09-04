class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        my_list = []
        original = nums
        for i in nums:
            while i > 0:
                i = i // 10
                count+=1
            if count % 2 == 0:
                my_list.append(original)
            count = 0
        return len(my_list)