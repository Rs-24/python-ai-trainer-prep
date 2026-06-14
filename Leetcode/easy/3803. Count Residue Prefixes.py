

class Solution:
    def residuePrefixes(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        v = set()
        c = 0
        for i, ch in enumerate(s):
            v.add(ch)
            c += len(v) == (i + 1) % 3
        return c


