

from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        c = Counter(s)
        if all(f == len(s) // 4 for _, f in c.items()):
            return 0
        ans = len(s)
        l = 0
        for r in range(len(s)):
            c[s[r]] -= 1
            while l <= r and all(c[ch] <= len(s) // 4 for ch in "QWER"):
                ans = min(ans, r - l + 1)
                c[s[l]] += 1
                l += 1
        return ans


