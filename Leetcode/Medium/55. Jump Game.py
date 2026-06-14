

class Solution:
    def canJump(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(1)
        f = 0
        for i, n in enumerate(nums):
            if i > f:
                return False
            f = max(f, i + n)
        return f >= len(nums) - 1


