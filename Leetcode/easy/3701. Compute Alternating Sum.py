

class Solution:
    def alternatingSum(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(n for i, n in enumerate(nums) if i % 2 == 0) - sum(n for i, n in enumerate(nums) if i % 2 != 0)


