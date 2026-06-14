

class Solution:
    def minimumSumSubarray(self, nums: list, l: int, r: int) -> int:
        # Time: O(n^2)
        # Space: O(1)
        b = float("inf")
        for i in range(len(nums)):
            t = 0
            for j in range(i, len(nums)):
                t += nums[j]
                if l <= j - i + 1 <= r:
                    b = min(b, t)
        return b if b != float("inf") else -1


