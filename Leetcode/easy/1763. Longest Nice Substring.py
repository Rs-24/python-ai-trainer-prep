# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/longest-nice-substring/description/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Time: O(n^2), n = len(s)
        # Space: O(n)
        chars = set(s)
        for i, ch in enumerate(s):
            if ch.swapcase() not in chars:
                l = self.longestNiceSubstring(s[:i])
                r = self.longestNiceSubstring(s[i + 1:])
                return l if len(l) >= len(r) else r
        return s


