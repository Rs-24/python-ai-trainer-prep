

class Solution:
    def minimumDifference(self, nums: list, k: int) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(1)
        nums.sort()
        best = float("inf")
        for i in range(len(nums) - k + 1):
            best = min(best, nums[i + k - 1] - nums[i])
        return best


