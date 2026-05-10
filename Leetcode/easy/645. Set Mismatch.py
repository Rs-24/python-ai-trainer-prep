

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        duplicate = None
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = num
            else:
                nums[abs(num) - 1] *= -1
        for i, num in enumerate(nums):
            if num > 0:
                return [duplicate, i + 1]


