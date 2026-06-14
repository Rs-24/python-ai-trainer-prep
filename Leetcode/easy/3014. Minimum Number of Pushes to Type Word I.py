

from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Time: O(n log n)
        # Space: O(n)
        f = sorted(Counter(word).values(), reverse=True)    
        return sum(f * ((i // 8) + 1) for i, f in enumerate(f))


