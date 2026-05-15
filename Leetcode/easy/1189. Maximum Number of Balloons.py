

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Time: O(n), n = len(text)
        # Space: O(1)
        c = Counter(text)
        best = float("inf")
        for ch in "balloon":
            if ch not in c:
                return 0
            if ch == "l" or ch == "o":
                best = min(best, c[ch] // 2)
            else:
                best = min(best, c[ch])
        return best


