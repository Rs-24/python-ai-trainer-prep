

from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        c = Counter(s)
        for i in range(1, len(s)):
            if s[i - 1] != s[i] and c[s[i - 1]] == int(s[i - 1]) and c[s[i]] == int(s[i]):
                return s[i - 1:i + 1]
        return ""


