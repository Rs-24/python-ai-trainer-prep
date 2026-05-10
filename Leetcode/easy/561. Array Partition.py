

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(1)
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total


