

class Solution:
    def subarraySum(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        p = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            p[i + 1] = p[i] + nums[i]
        t = 0
        for i, n in enumerate(nums):
            s = max(0, i - n)
            t += p[i + 1] - p[s]
        return t


