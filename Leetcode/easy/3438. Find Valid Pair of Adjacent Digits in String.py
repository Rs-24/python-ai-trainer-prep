# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/description/

from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(1)
        c = Counter(s)
        for i in range(1, len(s)):
            if s[i - 1] != s[i] and c[s[i - 1]] == int(s[i - 1]) and c[s[i]] == int(s[i]):
                return s[i - 1:i + 1]
        return ""


