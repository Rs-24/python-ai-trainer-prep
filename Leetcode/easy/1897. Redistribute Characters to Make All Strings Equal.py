

from collections import Counter

class Solution:
    def makeEqual(self, words: list) -> bool:
        # Time: O(n), n = total number of characters in words
        # Space: O(n)
        c = Counter()
        for w in words:
            c.update(w)
        return all(freq % len(words) == 0 for freq in c.values())


