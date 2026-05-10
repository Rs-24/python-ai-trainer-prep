

class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        return max(0, max(nums) - min(nums) - 2 * k)


