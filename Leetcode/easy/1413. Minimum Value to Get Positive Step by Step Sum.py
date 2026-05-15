

class Solution:
    def minStartValue(self, nums: list) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        lowest = float("inf")
        cur = 0
        for num in nums:
            cur += num
            lowest = min(lowest, cur)
        return 1 - lowest


