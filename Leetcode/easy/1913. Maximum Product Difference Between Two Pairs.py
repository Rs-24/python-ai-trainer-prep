

class Solution:
    def maxProductDifference(self, nums: list) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(1)
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


