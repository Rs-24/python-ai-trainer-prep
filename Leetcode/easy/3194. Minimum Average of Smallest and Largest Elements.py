

class Solution:
    def minimumAverage(self, nums: list) -> float:
        # Time: O(n log n)
        # Space: O(1)
        b = float("inf")
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            b = min(b, (nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return b


