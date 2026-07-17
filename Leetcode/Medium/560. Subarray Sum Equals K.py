

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        d = defaultdict(int)
        d[0] = 1
        t = a = 0
        for x in nums:
            t += x
            if t - k in d:
                a += d[t - k]
            d[t] += 1
        return a


