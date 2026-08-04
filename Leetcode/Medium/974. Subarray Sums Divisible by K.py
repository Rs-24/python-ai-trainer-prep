

from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        d = defaultdict(int)
        d[0] = 1
        a = t = 0
        for x in nums:
            t += x
            a += d[t % k]
            d[t % k] += 1
        return a


        