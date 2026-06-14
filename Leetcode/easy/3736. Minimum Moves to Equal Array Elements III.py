

class Solution:
    def minMoves(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return max(nums) * len(nums) - sum(nums)


