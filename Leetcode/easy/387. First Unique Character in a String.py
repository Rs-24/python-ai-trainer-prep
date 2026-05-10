

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(n)
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i
        return -1


