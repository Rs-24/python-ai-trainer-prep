

from collections import Counter

class Solution:
    def removeAnagrams(self, words: list) -> list:
        # Time: O(n)
        # Space: O(n)
        out = []
        prev = None
        for word in words:
            c = Counter(word)
            if prev != c:
                out.append(word)
                prev = c
        return out


