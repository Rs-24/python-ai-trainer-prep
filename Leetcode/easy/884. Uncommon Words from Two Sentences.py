

from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        # Time: O(m + n), m = len(s1), n = len(s2)
        # Space: O(m + n)
        c = Counter((s1 + " " + s2).split())
        return [word for word, freq in c.items() if freq == 1]


