# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Time: O(n^2), n = len(s)
        # Space: O(n)
        s = list(s)
        while len(s) > 2:
            new = []
            for i in range(1, len(s)):
                new.append((int(s[i - 1]) + int(s[i])) % 10)
            s[:] = new
        return s[0] == s[1]


