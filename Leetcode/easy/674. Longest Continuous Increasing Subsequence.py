

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l = 0
        best = 0
        prev = None
        for r, num in enumerate(nums):
            if prev is not None and prev >= num:
                l = r
            best = max(best, r - l + 1)
            prev = num
        return best


