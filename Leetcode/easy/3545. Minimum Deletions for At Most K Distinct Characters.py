

from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        # Time: O(n log n)
        # Space: O(n)
        c = Counter(s)
        if len(c) <= k:
            return 0
        s = sorted(c.values())
        return sum(s[:len(s) - k])


