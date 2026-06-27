

class Solution:
    def maxRotateFunction(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        s = sum(nums)
        t = sum(i * x for i, x in enumerate(nums))
        a = t
        for i in range(1, len(nums)):
            t += s - n * nums[n - i]
            a = max(a, t)
        return a


