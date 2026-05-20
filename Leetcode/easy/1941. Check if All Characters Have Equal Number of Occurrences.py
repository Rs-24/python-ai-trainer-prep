

from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        c = Counter(s)
        return len(set(c.values())) == 1


