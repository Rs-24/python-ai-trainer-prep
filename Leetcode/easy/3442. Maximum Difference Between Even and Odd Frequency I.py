

from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        c = Counter(s)
        odd = float("-inf")
        even = float("inf")
        for v in c.values():
            if v % 2 != 0:
                odd = max(odd, v)
            else:
                even = min(even, v)
        return odd - even


