

class Solution:
    def movesToMakeZigzag(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        def f(s: int) -> int:
            a = 0
            for i in range(s, len(nums), 2):
                l = nums[i - 1] if i > 0 else float("inf")
                r = nums[i + 1] if i < len(nums) - 1 else float("inf")
                a += nums[i] - min(l, r) + 1 if nums[i] > min(l, r) - 1 else 0
            return a
        return min(f(0), f(1))


