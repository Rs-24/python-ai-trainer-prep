

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        c = defaultdict(int)
        b = m = l = 0
        for r in range(len(s)):
            c[s[r]] += 1
            m = max(m, c[s[r]])
            while r - l + 1 > m + k:
                c[s[l]] -= 1
                l += 1
            b = max(b, r - l + 1)
        return b


