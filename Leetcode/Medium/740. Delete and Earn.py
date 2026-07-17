

from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        if not nums:
            return 0
        c = Counter(nums)
        t = [0] * (max(nums) + 1)
        for x, f in c.items():
            t[x] = x * f
        a = b = 0
        for x in t:
            a, b = b, max(a, b + x)
        return a


