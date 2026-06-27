

class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        l, c, b = 0, 0, float("inf")
        for r, x in enumerate(nums):
            c += x
            while c >= target:
                b = min(b, r - l + 1)
                c -= nums[l]
                l += 1
        return 0 if b == float("inf") else b


