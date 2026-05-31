

class Solution:
    def maximizeSum(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        return max(nums) * k + (k * (k - 1)) // 2


