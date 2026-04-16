# Time to write all of below including tests, explanation and time and aux
# and total space: 2 min

# Problem: https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/description/

from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # Time: O(n), n = len(word1) = len(word2)
        # Space: O(1)
        c1 = Counter(word1)
        c2 = Counter(word2)
        for i in range(26):
            ch = chr(ord("a") + i)
            if abs(c1.get(ch, 0) - c2.get(ch, 0)) > 3:
                return False
        return True


