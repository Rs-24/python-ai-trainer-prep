# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description/

from collections import defaultdict

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        l = 0
        res = 0
        d = defaultdict(int)
        for r in range(len(s)):
            d[s[r]] += 1
            while any(freq > k for freq in d.values()):
                d[s[l]] -= 1
                l += 1
            res += (r - l + 1)
        return res


