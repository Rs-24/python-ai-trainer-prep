

class Solution:
    def getMinDistance(self, nums: list, target: int, start: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        best = float("inf")
        for i, num in enumerate(nums):
            if num == target:
                best = min(best, abs(i - start))
        return best


