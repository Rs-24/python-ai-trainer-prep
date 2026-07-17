

class Solution:
    def minMoves(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        t = min(nums)
        return sum(x - t for x in nums)


