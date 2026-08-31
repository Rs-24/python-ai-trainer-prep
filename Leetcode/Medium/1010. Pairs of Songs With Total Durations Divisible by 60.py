

from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: list) -> int:
        # Time: O(n)
        # Space: O(1)
        d = defaultdict(int)
        a = 0
        for t in time:
            a += d[(60 - (t % 60)) % 60]
            d[(60 - (t % 60)) % 60] += 1
        return a


