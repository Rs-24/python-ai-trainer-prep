

class Solution:
    def productExceptSelf(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        n = len(nums)
        out = [1] * n
        t = 1
        for i in range(n):
            out[i] = t
            t *= nums[i]
        t = 1
        for i in range(n - 1, -1, -1):
            out[i] *= t
            t *= nums[i]
        return out


