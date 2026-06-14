

from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        d = defaultdict(list)
        b = float("inf")
        for i, n in enumerate(nums):
            d[n].append(i)
            if len(d[n]) >= 3:
                x, y, z = d[n][-3], d[n][-2], d[n][-1]
                b = min(b, abs(x - y) + abs(y - z) + abs(x - z))
                d[n].pop(0)
        return b if b != float("inf") else -1


