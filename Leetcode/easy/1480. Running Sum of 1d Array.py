

class Solution:
    def runningSum(self, nums: list) -> list:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        for i, num in enumerate(nums):
            if i > 0:
                nums[i] += nums[i - 1]
        return nums


