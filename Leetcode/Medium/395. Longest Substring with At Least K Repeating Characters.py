

from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Time: O(n^2)
        # Space: O(n)
        def f(l: int, r: int) -> int:
            if r - l + 1 < k:
                return 0
            c = Counter(s[l:r + 1])
            for i in range(l, r + 1):
                if c[s[i]] < k:
                    t = i + 1
                    while t <= r and c[s[t]] < k:
                        t += 1
                    return max(f(l, i - 1), f(t, r))
            return r - l + 1
        return f(0, len(s) - 1)


