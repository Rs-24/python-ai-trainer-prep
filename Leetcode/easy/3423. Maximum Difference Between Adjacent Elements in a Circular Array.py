

class Solution:
    def maxAdjacentDistance(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return max(abs(nums[i] - nums[(i + 1) % len(nums)]) for i in range(len(nums)))


