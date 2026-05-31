

class Solution:
    def sumOfSquares(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(n**2 for i, n in enumerate(nums) if len(nums) % (i + 1) == 0)


