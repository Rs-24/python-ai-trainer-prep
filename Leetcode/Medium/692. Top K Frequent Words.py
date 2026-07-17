

from collections import Counter

class Solution:
    def topKFrequent(self, words: list, k: int) -> list:#
        # Time: O(n log n)
        # Space: O(n)
        c = Counter(words)
        t = sorted(c.keys(), key=lambda x: (-c[x], x))
        return t[:k] 


